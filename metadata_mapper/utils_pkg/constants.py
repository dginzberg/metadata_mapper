# utils_pkg/constants --
from calendar import c
import datetime
from enum import Enum
from fileinput import filename
from operator import truediv
import os


class directories:
    ingestion_mapping_dir = os.path.abspath(
        # "/catelas/shared/commsftp/Phase2/MIBG_ID/Cisco/20220801"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220804"
        # "/catelas/shared/commsftp/Phase2/MIBG_IN/Paudium/20220805"
        # "/catelas/shared/commsftp/Phase2/Zoom/ZoomPhone/20220722"
        # "/catelas/shared/commsftp/Phase2/Zoom/ZoomMeeting/20220719"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220607"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220609"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220610"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220612"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220613"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220614"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220615"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220616"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220617"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220620"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220621"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220622"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220623"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220624"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220625"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220626"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220627"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220606"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220608"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220628"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220629"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220630"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220701"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220704"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220705"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220706"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220707"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220708"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220711"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220712"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220713"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220714"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220715"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220716"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220717"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220718"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220719"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220720"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220721"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220722"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220724"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220725"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220726"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220727"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220728"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220729"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220730"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220731"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220801"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220802"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220803"
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220805"
        "/metadata_mapper/test_pkg/sample_data",
        # "/catelas/shared/commsftp/Phase2/MIBG_HK/HKT/20220808"
    )
    output_dir = os.path.abspath(
        # "/catelas/shared/scripts/metadata_mapper/environment/test_output"
        "C:/Users/Daniel.Ginzberg/Documents/Projects/metadata_mapper/environment/mapper_voice_out"
    )
    processed_mapping_dir = os.path.abspath(
        # "/catelas/shared/scripts/metadata_mapper/environment/test_processed"
        "C:/Users/Daniel.Ginzberg/Documents/Projects/metadata_mapper/environment/mapper_processed"
    )
    log_dir = os.path.abspath(
        # "/catelas/shared/scripts/metadata_mapper/logging"
        "C:/Users/Daniel.Ginzberg/Documents/Projects/metadata_mapper/logging"
    )
    speechmatics_in_dir = os.path.abspath(
        # "/catelas/shared/scripts/metadata_mapper/environment/speechmatics_input"
        "C:/Users/Daniel.Ginzberg/Documents/Projects/metadata_mapper/environment/mapper_speechmatics/mapper_input"
    )
    speechmatics_out_dir = os.path.abspath(
        # "/catelas/shared/scripts/metadata_mapper/environment/transcribed"
        "C:/Users/Daniel.Ginzberg/Documents/Projects/metadata_mapper/environment/mapper_speechmatics/mapper_output"
    )


class data_info:
    date_time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    curr_date = datetime.date.strftime(datetime.date.today(), "%Y%m%d")
    y_date = datetime.date.strftime(
        datetime.date.today() - datetime.timedelta(1), "%Y%m%d"
    )
    audio = set([".wav", ".mp3", ".M4A", ".MP4"])
    metadata = [".xml", ".json"]
    xml = set(["IPC"])
    json = set(["HKT", "Cisco", "Paudium", "ZoomMeeting", "ZoomPhone"])
    filename = set(["ARC", "Transonic", "Voicesoft"])
    type = ["xml", "json", "filename"]
    software = [
        "IPC",
        "HKT",
        "Cisco",
        "Paudium",
        "ARC",
        "Transonic",
        "Voicesoft",
        "ZoomMeeting",
        "ZoomPhone",
    ]


class regions:
    lang_ref = {
        # BLOCK: missing some support for languages
        # "MIBG_MY": ["en", "ms", "yue", "cmn"],
        "MIBG_MY": ["en", "ms"],
        # PLAN: unsupported languages: unsupported languages , "hokkien", "tamil"],
        # "MIBG_HK": ["en", "ms", "yue"],
        "MIBG_HK": ["en", "ms"],
        "MIBG_ID": ["en"],
        # PLAN: unsupported languages , "vietnamese"],
        # "MIBG_IN": ["en", "hi"],
        "MIBG_IN": ["en"],
        "MIBG_VN": ["en"],
        # PLAN: unsupported languages , "vietnamese"],
        "MIBG_TH": ["en"],
        # PLAN: unsupported languages , "thai"],
        "MIBG_US": ["en"],
        "MIBG_PH": ["en"],
        # PLAN: unsupported languages , "filipino/Tagalog"],
        "MIBG_SG": ["en"],
        os.path.normpath("MBB_VN/Hanoi"): ["en"],
        # PLAN: unsupported languages , "vietnamese"],
        os.path.normpath("MBB_VN/HCMC"): ["en"],
        # PLAN: unsupported languages , "vietnamese"],
        # "MBB_HK": ["en" "yue", "cmn"],
        "MBB_HK": ["en"],
        "MBB_PH": ["en"],
        # PLAN: unsupported languages , "filipino/Tagalog"],
        "Zoom": ["en"],
    }


class labels:
    out_label_ref = ["datetime", "voice_file", "to_email", "from_email", "languages"]
    label_ref = {
        # INFO: (JSON):
        "HKT": {
            "datetime": (["Date", "Time"], ["%Y-%m-%d", "%H:%M:%S"]),
            "voice_file": "Voice_File",
            "to_email": "To_Phone_Number",
            "from_email": "From_Phone_Number",
        },
        "Cisco": {
            "datetime": (["sessionStartDate"], ["", "%f"]),
            "voice_file": "sessionId",
            "to_email": 'file.data_dict.get("tracks")[1].get("participants")[0].get("deviceRef")',
            "from_email": 'file.data_dict.get("tracks")[0].get("participants")[0].get("deviceRef")',
        },
        "Paudium": {
            "datetime": (["date", "Time"], ["%Y%m%d", "%f"]),
            "voice_file": "Voice_file",
            "to_email": "to_Phone_Number",
            "from_email": "from_Phone_Number",
        },
        "ZoomMeeting": {
            "datetime": (["recordingStartTime"], ["%Y-%m-%dT%H:%M:%S.%f%Z"]),
            "voice_file": "voiceFile",
            "to_email": "MeetingID",
            "from_email": "StaffEmailAddress",
        },
        "ZoomPhone": {
            "datetime": (["recordingStartTime"], ["%Y-%m-%dT%H:%M:%S.%f%Z"]),
            "voice_file": "voiceFile",
            "to_email": "calleeNumber",
            "from_email": "callerNumber",
        },
        "IPC": {
            "datetime": (["CAudioFile.CRI.StartTime"], ["%Y-%m-%dT%H:%M:%S.%f%Z"]),
            "voice_file": "CAudioFile.File.Location",
            "to_email": "CAudioFile.CRI.AgentPBXID",
            "from_email": "CAudioFile.CRI.SID",
        },
    }  # TEMP: remove bracket after XML is ready
    """  ,

        # INFO: (Filename):
        # TODO: voice_file is name
        'ARC': {
            'datetime': 2,
            'to_email': 4,
            'from_email': 3
        },
        'Transonic': {
            'datetime': 2,
            'to_email': 4,
            'from_email': 3,
        },
        'Voicesoft': {
            'datetime': 2,
            'to_email': 4,
            'from_email': 3
        }
        
    } """
