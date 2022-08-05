from wsgiref.simple_server import software_version
import pytest
import datetime
import os
from utils_pkg import mapper_file, mapper_files, directories
from mapper_pkg.types_pkg import json_mapper, xml_mapper, filename_mapper
from mapper_pkg import Mapper_Controller, Xml_Mapper


@pytest.fixture(autouse=True, scope="session")
def test_info():
    curr_date = datetime.date.strftime(datetime.date.today(), "%Y%m%d")
    y_date = datetime.date.strftime(
        datetime.date.today() - datetime.timedelta(1), "%Y%m%d"
    )
    audio = set([".wav", ".mp3", ".M4A", ".MP4"])
    metadata = [".xml", ".json"]
    xml = set(["IPC"])
    json = set(["HKT", "Cisco", "Paudium"])
    filename = set(["ARC", "Transonic", "Voicesoft"])
    type = ["xml", "json", "filename"]
    software = ["HKT", "Cisco", "Paudium", "ZoomPhone", "ZoomMeeting"]
    out_label_ref = ["datetime", "voice_file", "to_email", "from_email", "languages"]
    #  PLAN: Add other software types
    #  'IPC', 'ARC', 'Transonic', 'Voicesoft']
    ingestion_dir = os.path.normpath("metadata_mapper\\test_pkg\\sample_data")
    speechmatics_dir = os.path.normpath(
        "metadata_mapper\\test_pkg\\speechmatics\\input"
    )
    processed_dir = os.path.normpath("metadata_mapper\\test_pkg\\processed")
    transcribed_dir = os.path.normpath("metadata_mapper\\test_pkg\\transcribed")
    output_dir = os.path.normpath("metadata_mapper\\test_pkg\\output")
    temp_dir = os.path.normpath("metadata_mapper\\test_pkg\\temp")

    return {
        "curr_date": curr_date,
        "y_date": y_date,
        "audio": audio,
        "metadata": metadata,
        "xml": xml,
        "json": json,
        "filename": filename,
        "type": type,
        "software": software,
        "ingestion_dir": ingestion_dir,
        "speechmatics_dir": speechmatics_dir,
        "processed_dir": processed_dir,
        "transcribed_dir": transcribed_dir,
        "output_dir": output_dir,
        "temp_dir": temp_dir,
    }


@pytest.fixture(autouse=True, scope="module")
def test_datetime_format():
    HKT = (["2022-06-28", "16:10:50"], ["%Y-%m-%d", "%H:%M:%S"])
    Cisco = ([1640222986177], ["", "%f"])
    Paudium = (["20220623", "125102"], ["%Y%m%d", "%f"])
    ZoomMeeting = (["2022-06-08T13:18:49.0330156+08:00"], ["%Y-%m-%dT%H:%M:%S.%f+%z"])
    ZoomPhone = (["2022-06-08T13:18:42.6411264+08:00"], ["%Y-%m-%dT%H:%M:%S.%f+%z"])
    return {
        "HKT": HKT,
        "Cisco": Cisco,
        "Paudium": Paudium,
        "ZoomMeeting": ZoomMeeting,
        "ZoomPhone": ZoomPhone,
    }


@pytest.fixture(autouse=True, scope="module")
def test_files(test_info):
    directories.ingestion_dir = test_info.get("ingestion_dir")
    mix_mapper_files = mapper_files(
        [
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_HK\\IPC\\20220520\\815001006900078.xml"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_PH\\IPC\\20220713\\238001003601700.xml"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\Hanoi\\ARC\\20220713\\IN-20220712_084848_DEV10003092_CH05.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\Hanoi\\ARC\\20220713\\OUT-20220711_082950_DEV10004134_CH01_L139_P114.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Transonic\\20220713\\01-106AnhTuyet-B----20220713093844.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Transonic\\20220713\\01-106AnhTuyet-B-104---20220713102138.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Transonic\\20220713\\01-106AnhTuyet-B-90904227697---20220713111155.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Voicesoft\\20220713\\01-109-M.Ha-A----20220712090132.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Voicesoft\\20220713\\03-113-T.Trang-B-101---20220607162053.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_HK\\HKT\\20220712\\54644_20220628_1610_277_22680294_81700.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_ID\\Cisco\\20220712\\ddf717de4e88eda1.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\07966215700_20220623_125102_709_O_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\7966215700_20220623_132133_709_I_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\8928178129_20220623_145226_706_I_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\09323931304_20220623_125121_720_O_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_US\\ARC\\20220714\\20220429_190018_I_6315672300_107.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\Zoom\\ZoomMeeting\\20220713\\recording_1632278095044.mp40.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\Zoom\\ZoomPhone\\20220712\\teste.json"
            ),
        ]
    )
    json_mapper_files = mapper_files(
        [
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_HK\\HKT\\20220712\\54644_20220628_1610_277_22680294_81700.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_ID\\Cisco\\20220712\\ddf717de4e88eda1.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\07966215700_20220623_125102_709_O_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\7966215700_20220623_132133_709_I_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\8928178129_20220623_145226_706_I_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\8928178129_20220623_145226_706_I_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_IN\\Paudium\\20220712\\09323931304_20220623_125121_720_O_.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\Zoom\\ZoomMeeting\\20220713\\recording_1632278095044.mp40.json"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\Zoom\\ZoomPhone\\20220712\\test.json"
            ),
        ]
    )
    xml_mapper_files = mapper_files(
        [
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_HK\\IPC\\20220520\\815001006900078.xml"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_PH\\IPC\\20220713\\238001003601700.xml"
            ),
        ]
    )
    filename_mapper_files = mapper_files(
        [
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\Hanoi\\ARC\\20220713\\IN-20220712_084848_DEV10003092_CH05.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\Hanoi\\ARC\\20220713\\OUT-20220711_082950_DEV10004134_CH01_L139_P114.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Transonic\\20220713\\01-106AnhTuyet-B----20220713093844.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Transonic\\20220713\\01-106AnhTuyet-B-104---20220713102138.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Transonic\\20220713\\01-106AnhTuyet-B-90904227697---20220713111155.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Voicesoft\\20220713\\01-109-M.Ha-A----20220712090132.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\HCMC\\Voicesoft\\20220713\\03-113-T.Trang-B-101---20220607162053.wav"
            ),
            os.path.normpath(
                "metadata_mapper\\test_pkg\\sample_data\\MIBG_US\\ARC\\20220714\\20220429_190018_I_6315672300_107.wav"
            ),
        ]
    )
    json_output = [
        "MIBG_HK\\HKT\\20220712\\54644_20220628_1610_277_22680294_81700.json",
        "MIBG_ID\\Cisco\\20220712\\ddf717de4e88eda1.json",
        "MIBG_IN\\Paudium\\20220712\\07966215700_20220623_125102_709_O_.json",
        "MIBG_IN\\Paudium\\20220712\\7966215700_20220623_132133_709_I_.json",
        "MIBG_IN\\Paudium\\20220712\\8928178129_20220623_145226_706_I_.json",
        "MIBG_IN\\Paudium\\20220712\\8928178129_20220623_145226_706_I_.json",
        "MIBG_IN\\Paudium\\20220712\\09323931304_20220623_125121_720_O_.json",
        "Zoom\\ZoomMeeting\\20220713\\recording_1632278095044.mp40.json",
        "Zoom\\ZoomPhone\\20220712\\test.json",
    ]

    return {
        "mix_mapper_files": mix_mapper_files,
        "json_mapper_files": json_mapper_files,
        "json_output": json_output,
        "xml_mapper_files": xml_mapper_files,
        "filename_mapper_files": filename_mapper_files,
    }


@pytest.fixture(autouse=True, scope="module")
def test_json_file(test_info):
    directories.ingestion_dir = test_info.get("ingestion_dir")
    file = os.path.normpath(
        "metadata_mapper\\test_pkg\\sample_data\\MIBG_HK\\HKT\\20220712\\54644_20220628_1610_277_22680294_81700.json"
    )
    map_file = mapper_file(file)
    filetype = ".json"
    filename = "54644_20220628_1610_277_22680294_81700.json"
    file_dir = os.path.normpath("MIBG_HK\\HKT\\20220712")
    software = "HKT"
    region = "MIBG_HK"
    date_data = "2022-06-28T20:10:50.000000+0000"
    data_dict = {
        "From_Phone_Number": "22680294",
        "To_Phone_Number": "22680277",
        "Voice_File": "54644_20220628_1610_277_22680294_81700.wav",
        "Date": "2022-06-28",
        "Time": "16:10:50",
        "Duration": "9",
        "Direction": "Outbound",
    }
    out_dict = {
        "datetime": "2022-06-28T20:10:50.000000+0000",
        "voice_file": "54644_20220628_1610_277_22680294_81700.wav",
        "to_email": "22680277",
        "from_email": "22680294",
        "languages": ["en", "ms", "yue"],
    }
    return {
        "file": file,
        "mapper_file": map_file,
        "filetype": filetype,
        "filename": filename,
        "file_dir": file_dir,
        "software": software,
        "region": region,
        "date_data": date_data,
        "out_dict": out_dict,
        "data_dict": data_dict,
    }


@pytest.fixture(autouse=True, scope="module")
def test_xml_file(test_info):
    directories.ingestion_dir = test_info.get("ingestion_dir")
    file = os.path.normpath(
        "metadata_mapper\\test_pkg\\sample_data\\MBB_HK\\IPC\\20220520\\815001006900078.xml"
    )
    map_file = mapper_file(file)
    filetype = ".xml"
    filename = "815001006900078.xml"
    file_dir = os.path.normpath("MBB_HK\\IPC\\20220520")
    software = "IPC"
    region = "MBB_HK"

    data_dict = {
        "recording": {
            "segment": {
                "complete": True,
                "master": True,
                "keepcontent": True,
                "keepxml": True,
                "rollbackrequired": False,
                "rollbacktime": 15,
                "compressiontype": 4,
                "compressed": True,
                "rollbackid": "51_00E0A708E36F_1140850690",
                "contenttype": "audio/vnd.verint.wav",
                "capturetype": "IP",
                "starttime": "2022-05-20T19:41:07.336+08:00",
                "readytoarchive": True,
                "switch_id": 815000051,
                "captureversion": "15.1.0.3441",
                "tags": {
                    "tag": [
                        {"attribute": 0},
                        {"attribute": "SIP/00E0A708E36F_1140850690/1649690459065"},
                        {"attribute": 51},
                        {"attribute": "MAYBANK DATA SOURCE 1"},
                        {"attribute": -1},
                        {"attribute": "00E0A708E36F_1140850690"},
                        {"attribute": 815001006900077},
                        {
                            "attribute": [
                                "Out",
                                "00E0A708E36F",
                                51,
                                "00E0A708E36F_1140850690",
                                "00E0A708E36F_1140850690",
                                793,
                                "Phoebe Wong",
                                "Recorder",
                                "Recorder",
                                793,
                                "Phoebe Wong",
                            ]
                        },
                        {"attribute": 1},
                        {"attribute": 1},
                        {"attribute": "10.120.113.6:10092"},
                        {"attribute": "10.120.113.14:16426"},
                        {"attribute": "2022-05-20T19:41:07.336+08:00"},
                        {"attribute": [0, 0]},
                        {
                            "attribute": [
                                "Outbound",
                                "3518 8793",
                                1604739792788,
                                0,
                                93121997,
                                "793H",
                                93121997,
                                793,
                                793,
                                "00E0A708E36F_1140850690",
                                793,
                                "Phoebe Wong",
                                "00E0A708E36F",
                            ]
                        },
                        {
                            "attribute": [
                                "Outbound",
                                "3518 8793",
                                1604739792788,
                                0,
                                93121997,
                                "793H",
                                93121997,
                                793,
                                793,
                                "00E0A708E36F_1140850690",
                                793,
                                "Phoebe Wong",
                                "00E0A708E36F",
                            ]
                        },
                        {"attribute": 54375},
                        {"attribute": "2022-05-20T19:42:06.728+08:00"},
                        {"attribute": "SilenceDetection"},
                    ]
                },
                "systemtype": "trading",
                "shared_key": "audio_51_00e0a708e36f_1140850690",
                "duration": 54,
                "streams": {
                    "stream": {
                        "audiodurationinms": 53240,
                        "dstip": "10.120.113.6:10092",
                        "expectedpacketcount": 2590,
                        "firstpackettime": "2022-05-20T19:41:07.336+08:00",
                        "lastpackettime": "2022-05-20T19:42:01.723+08:00",
                        "missedrtppackets": 0,
                        "rtptype": "PCMU",
                        "silencedurationinms": 1180,
                        "srcip": "10.120.113.14:16426",
                        "ssrcid": 1318837296,
                        "totalrtppackets": 2662,
                    }
                },
            },
            "contacts": {
                "contact": {
                    "sessions": {
                        "session": {
                            "complete": True,
                            "interactiontype": "Phone",
                            "mark": True,
                            "inums": {"inum": 815001006900078},
                            "switch_id": 815000051,
                        }
                    },
                    "complete": True,
                }
            },
        }
    }
    return {
        "file": file,
        "mapper_file": map_file,
        "filetype": filetype,
        "filename": filename,
        "file_dir": file_dir,
        "software": software,
        "region": region,
        "data_dict": data_dict,
    }


@pytest.fixture(autouse=True, scope="module")
def test_audio_file(test_info):
    directories.ingestion_dir = test_info.get("ingestion_dir")
    file = os.path.normpath(
        "metadata_mapper\\test_pkg\\sample_data\\MBB_VN\\Hanoi\\ARC\\20220713\\IN-20220712_084848_DEV10003092_CH05.wav"
    )
    map_file = mapper_file(file)
    filetype = ".wav"
    filename = "IN-20220712_084848_DEV10003092_CH05.wav"
    file_dir = os.path.normpath("MBB_VN\\Hanoi\\ARC\\20220713")
    software = "ARC"
    region = "MBB_VN\\Hanoi"
    return {
        "file": file,
        "mapper_file": map_file,
        "filetype": filetype,
        "filename": filename,
        "file_dir": file_dir,
        "software": software,
        "region": region,
    }


@pytest.fixture(scope="class")
def init_controller(request, test_info):
    controller = Mapper_Controller(
        test_info.get("ingestion_dir"),
        test_info.get("processed_dir"),
        test_info.get("speechmatics_dir"),
    )
    request.cls.controller = controller


@pytest.fixture(scope="class")
def init_xml_mapper(request, test_files):
    xml_mapper = Xml_Mapper(test_files.get("xml_mapper_files"))

    request.cls.xml_mapper = xml_mapper
