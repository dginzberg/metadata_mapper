# types_pkg/mapper_interface --
from abc import ABCMeta, abstractmethod
from ast import In
from datetime import datetime
import json
import logging
import time
from black import out
import psutil
import os
import sys
from utils_pkg import directories, data_info, labels, mapper_files, regions
import re
import pytz


class Mapper(metaclass=ABCMeta):
    def __init__(self, files):
        self.start_time = time.time()
        self.logger_config()
        self.files = files
        self.successful = 0

    def logger_config(self):
        self.log_file = os.path.join(
            directories.log_dir, self.__module__.split(".")[-1] + ".log"
        )
        if not os.path.isdir(os.path.dirname(self.log_file)):
            os.mkdir(os.path.dirname(self.log_file))
        if not os.path.isfile(self.log_file):
            with open(self.log_file, "w") as outfile:
                outfile.close
        self.file_handler = logging.FileHandler(
            self.log_file, mode="a", encoding=None, delay=False
        )
        self.logger = logging.getLogger()
        self.logger.addHandler(self.file_handler)
        self.logger.setLevel(logging.DEBUG)

    def final_logging(self):
        self.finish_time = time.time() - self.start_time
        self.mem_usage = self.get_process_memory()
        self.logger.info("          files provided: %d", self.files)
        self.logger.info("   successfully produced: %d", self.successful)
        self.logger.debug("              Time took: %s", self.finish_time)
        self.logger.debug("            Memory Used: %d",
                      self.mem_usage - self.start_mem)

    def get_process_memory():
        process = psutil.Process(os.getpid())
        return process.memory_info().rss

    def datetime_formatter(self, format):
        date = format[0][0]
        # INFO: removing unnecessary microsecond digit (datetime only supports 6 microseconds)

        if len(format[1]) == 1:
            date = format[0][0]
            self.logger.debug("mapping datetime (just date):%s with format: %s", format[1], format[0][0])
            # INFO: just date
            if ("+" or "-") in date:
                if "+" in date:
                    sign = "+"
                else:
                    sign = "-"
                split_date = date.split(sign)
                date = split_date[0][:26] + sign + split_date[1]
            try:
                datetime.strptime(date, data_info.date_time_format)
                self.logger.debug("result date: %s", date)
                return date
            except ValueError:
                date = datetime.strptime(date, format[1][0]).astimezone(pytz.UTC).strftime(data_info.date_time_format)
                self.logger.debug("result date: %s", date)
                return date
        elif format[1][0] == "":
            # INFO: epoch microseconds
            self.logger.debug("mapping datetime (just time):%s with format: %s", format[1][0], format[0][0])
            s = format[0][0] / 1000.0
            date = datetime.fromtimestamp(s).astimezone(pytz.UTC).strftime(data_info.date_time_format)
            self.logger.debug("result date: %s", date)
            return date
        else:
            # INFO: date and time
            date = format[0][0]
            time = format[0][1]
            date_format = format[1][0]
            time_format = format[1][1]
            self.logger.debug("mapping datetime (Date and time) Date:%s Time:%s with format: %s (Date) %s (Time)", date, time, date_format, time_format)
            date_time = datetime.strptime(
                date + "T" + time, date_format + "T" + time_format
            ).astimezone(pytz.UTC).strftime(data_info.date_time_format)
            self.logger.debug("result date: %s", date_time)
            return date_time

    # PLAN : organize files by dir and date
    def write_json(self, file, speechmatics_dir=directories.speechmatics_dir):
        if not os.path.isdir(speechmatics_dir):
            os.makedirs(speechmatics_dir)
        out_file = os.path.join(speechmatics_dir, file.filename.split('.')[0]+'.json')

        with open(out_file, "w") as outfile:
            self.logger.debug("Writing output file: %s", out_file)
            json.dump(file.data_dict, outfile, indent=4)
        return outfile

    def get_label_data(self, file, label):
        return file.data_dict.get(labels.label_ref.get(file.software).get(label))

    def get_date_label_data(self, file, label):
        date_labels = labels.label_ref.get(file.software).get(label)
        out_data = []
        for date_label in date_labels[0]:
            out_data.append(file.data_dict[date_label])
        date_labels = (out_data, date_labels[1])
        return self.datetime_formatter(date_labels)

    def get_email_label_data(self, file, label):
        if file.software == data_info.software[2]:
            return eval(labels.label_ref.get(file.software).get(label))
        else:
            return self.get_label_data(file, label)

    def get_audio_label_data(self, file, label):
        if file.software == data_info.software[0]:
           return os.path.abspath(file.file_dir + os.sep + self.get_label_data(file, label).split('WAV')[1])
        return os.path.abspath(file.file_dir + os.sep + self.get_label_data(file, label))

    def map_data(self, file):
        out_dict = {}
        for label in labels.out_label_ref:
            # datetime
            if label == labels.out_label_ref[0]:
                out_dict[label] = self.get_date_label_data(file, label)
            # language
            elif label == labels.out_label_ref[4]:
                out_dict[label] = file.languages
            # email
            elif label == labels.out_label_ref[2] or label == labels.out_label_ref[3]:
                out_dict[label] = self.get_email_label_data(file, label)
            #audio
            elif label == labels.out_label_ref[1]:
                out_dict[label] = self.get_audio_label_data(file, label)
            else:
                out_dict[label] = self.get_label_data(file, label)
        file.data_dict = out_dict

    @abstractmethod
    def ingest_data(self, file):
        pass

    @abstractmethod
    def run_mapper(self):
        pass
