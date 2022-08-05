# utils_pkg/constants --
from calendar import c
import datetime
from enum import Enum
from fileinput import filename
from operator import truediv
import os


class directories:
    ingestion_dir = os.path.abspath(
        "/catelas/shared/commsftp/Phase2"
    )
    output_dir = os.path.abspath(
        "/catelas/shared/test_output"
    )
    processed_dir = os.path.abspath(
        "/catelas/shared/processed"
    )
    log_dir = os.path.abspath(
        "/catelas/shared/scripts/metadata_mapper/metadata_mapper/logging"
    )
    speechmatics_dir = os.path.abspath("/home/ec2-user/transcribe/uat_input")
    transcribed_dir = os.path.abspath("/home/ec2-user/transcribe/output")


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
        "MIBG_MY": ["en", "ms", "yue", "cmn"],
        # PLAN: unsupported languages: unsupported languages , "hokkien", "tamil"],
        "MIBG_HK": ["en", "ms", "yue"],
        "MIBG_ID": ["en"],
        # PLAN: unsupported languages , "vietnamese"],
        "MIBG_IN": ["en", "hi"],
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
        "MBB_HK": ["en" "yue", "cmn"],
        "MBB_PH": ["en"],
        # PLAN: unsupported languages , "filipino/Tagalog"],
        "Zoom": ["en"],
    }


# class softwares:
#     datetime_format_ref = {
#         "HKT": (["Date", "Time"], ["%Y-%m-%d", "%H:%M:%S"]),
#         "Cisco": (["sessionStartDate"], ["", "%f"]),
#         "Paudium": (["date", "Time"], ["%Y%m%d", "%f"]),
#         "ZoomMeeting": (["recordingStartTime"], ["%Y-%m-%dT%H:%M:%S.%f%Z"]),
#         "ZoomPhone": (["recordingStartTime"], ["%Y-%m-%dT%H:%M:%S.%f%Z"]),
#     }  # TEMP: remove bracket after software typs are added
#     # PLAN: add software types
#     """  "IPC",
#         "ARC",
#         "Transonic",
#         "Voicesoft",
#     }
#     """


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
    }  # TEMP: remove bracket after XML is ready
    """  ,

        # INFO:  (XML):
        'IPC': {
            'datetime': 'LocalStartTime',
            'voice_file': 'Location',
            'to_email': 'AgentPBXID',
            'from_email': 'SID'
        },

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
