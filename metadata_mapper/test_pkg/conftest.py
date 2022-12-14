from collections import OrderedDict
from wsgiref.simple_server import software_version
import pytest
import datetime
import os
from utils_pkg import mapper_file, mapper_files, directories
from mapper_pkg import Mapper_Controller, Xml_Mapper, Filename_Mapper, Json_Mapper


@pytest.fixture(autouse=True, scope='session')
def test_info():
    date_time_format = '%Y-%m-%dT%H:%M:%S.%f%z'
    curr_date = datetime.date.strftime(datetime.date.today(), '%Y%m%d')
    y_date = datetime.date.strftime(
        datetime.date.today() - datetime.timedelta(1), '%Y%m%d'
    )
    audio = set(['.wav', '.mp3', '.M4A', '.MP4'])
    metadata = ['.xml', '.json']
    xml = set(['IPC'])
    json = set(['HKT', 'Cisco', 'Paudium'])
    filename = set(['ARC', 'Transonic', 'Voicesoft'])
    type = ['xml', 'json', 'filename']
    software = ['HKT', 'Cisco', 'Paudium', 'ZoomPhone', 'ZoomMeeting']
    out_label_ref = ['datetime', 'voice_file', 'to_email', 'from_email', 'languages']
    #  PLAN: Add other software types
    #  'IPC', 'ARC', 'Transonic', 'Voicesoft']/catelas/shared/scripts/metadata_mapper/test_pkg/sample_data
    ingestion_mapping_dir = os.path.abspath(os.path.join( 'metadata_mapper', 'test_pkg', 'sample_data'))
    speechmatics_in_dir = os.path.abspath(os.path.join('test_pkg', 'test_speechmatics', 'test_input'))
    processed_mapping_dir = os.path.abspath(os.path.join('test_pkg', 'test_processed'))
    speechmatics_out_dir = os.path.abspath(os.path.join( 'test_pkg', 'test_speechmatics', 'test_output'))
    voice_output_dir = os.path.abspath(os.path.join('test_pkg', 'test_voice_out'))
    temp_dir = os.path.abspath(os.path.join( 'test_pkg', 'sample_data_backup'))


    return {
        'date_time_format': date_time_format,
        'curr_date': curr_date,
        'y_date': y_date,
        'audio': audio,
        'metadata': metadata,
        'xml': xml,
        'json': json,
        'filename': filename,
        'type': type,
        'software': software,
        'out_label_ref':out_label_ref,
        'ingestion_mapping_dir': ingestion_mapping_dir,
        'speechmatics_in_dir': speechmatics_in_dir,
        'processed_mapping_dir': processed_mapping_dir,
        'speechmatics_out_dir': speechmatics_out_dir,
        'voice_output_dir': voice_output_dir,
        'temp_dir': temp_dir,
    }


@pytest.fixture(autouse=True, scope='module')
def test_datetime_format():
    HKT = (['2022-06-28', '16:10:50'], ['%Y-%m-%d', '%H:%M:%S'])
    Cisco = ([1640222986177], ['', '%f'])
    Paudium = (['20220623', '125102'], ['%Y%m%d', '%f'])
    ZoomMeeting = (['2022-06-08T13:18:49.0330156+08:00'], ['%Y-%m-%dT%H:%M:%S.%f+%z'])
    ZoomPhone = (['2022-06-08T13:18:42.6411264+08:00'], ['%Y-%m-%dT%H:%M:%S.%f+%z'])
    IPC = (['2022-08-04T14:26:46.5000000+0000'], ['%Y-%m-%dT%H:%M:%S.%f+%z'])
    return {
        'HKT': HKT,
        'Cisco': Cisco,
        'Paudium': Paudium,
        'ZoomMeeting': ZoomMeeting,
        'ZoomPhone': ZoomPhone,
        'IPC': IPC
    }


@pytest.fixture(autouse=True, scope='module')
def test_files(test_info):
    directories.ingestion_mapping_dir = test_info.get('ingestion_mapping_dir')
    mix_mapper_files = mapper_files(
        [
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_HK', 'IPC', '20220520', '815001006900078.xml'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_PH', 'IPC', '20220713', '238001003601700.xml'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'Hanoi', 'ARC', '20220713', 'IN-20220712_084848_DEV10003092_CH05.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'Hanoi', 'ARC', '20220713', 'OUT-20220711_082950_DEV10004134_CH01_L139_P114.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Transonic', '20220713', '01-106AnhTuyet-B----20220713093844.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Transonic', '20220713', '01-106AnhTuyet-B-104---20220713102138.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Transonic', '20220713', '01-106AnhTuyet-B-90904227697---20220713111155.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Voicesoft', '20220713', '01-109-M.Ha-A----20220712090132.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Voicesoft', '20220713', '03-113-T.Trang-B-101---20220607162053.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_HK', 'HKT', '20220712', '54644_20220628_1610_277_22680294_81700.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_ID', 'Cisco', '20220712', 'ddf717de4e88eda1.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '07966215700_20220623_125102_709_O_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '7966215700_20220623_132133_709_I_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '8928178129_20220623_145226_706_I_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '09323931304_20220623_125121_720_O_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_US', 'ARC', '20220714', '20220429_190018_I_6315672300_107.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'Zoom', 'ZoomMeeting', '20220713', 'recording_1632278095044.mp40.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'Zoom', 'ZoomPhone', '20220712', 'teste.json'
            )),
        ]
    )
    json_mapper_files = mapper_files(
        [
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_HK', 'HKT', '20220712', '54644_20220628_1610_277_22680294_81700.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_ID', 'Cisco', '20220712', 'ddf717de4e88eda1.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '07966215700_20220623_125102_709_O_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '7966215700_20220623_132133_709_I_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '8928178129_20220623_145226_706_I_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '8928178129_20220623_145226_706_I_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_IN', 'Paudium', '20220712', '09323931304_20220623_125121_720_O_.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'Zoom', 'ZoomMeeting', '20220713', 'recording_1632278095044.mp40.json'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'Zoom', 'ZoomPhone', '20220712', 'test.json'
            )),
        ]
    )
    xml_mapper_files = mapper_files(
        [
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_HK', 'IPC', '20220520', '815001006900078.xml'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_PH', 'IPC', '20220713', '238001003601700.xml'
            )),
        ]
    )
    filename_mapper_files = mapper_files(
        [
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'Hanoi', 'ARC', '20220713', 'IN-20220712_084848_DEV10003092_CH05.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'Hanoi', 'ARC', '20220713', 'OUT-20220711_082950_DEV10004134_CH01_L139_P114.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Transonic', '20220713', '01-106AnhTuyet-B----20220713093844.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Transonic', '20220713', '01-106AnhTuyet-B-104---20220713102138.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Transonic', '20220713', '01-106AnhTuyet-B-90904227697---20220713111155.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Voicesoft', '20220713', '01-109-M.Ha-A----20220712090132.wav'
            )),
            os.path.abspath(os.path.join(
                 'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_VN', 'HCMC', 'Voicesoft', '20220713', '03-113-T.Trang-B-101---20220607162053.wav'
            )),
            os.path.abspath(os.path.join(
                'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_US', 'ARC', '20220714', '20220429_190018_I_6315672300_107.wav'
            )),
        ]
    )
    json_output = [
        os.path.join('MIBG_HK', 'HKT', '20220712', '54644_20220628_1610_277_22680294_81700.json'),
        os.path.join('MIBG_ID', 'Cisco', '20220712', 'ddf717de4e88eda1.json'),
        os.path.join('MIBG_IN', 'Paudium', '20220712', '07966215700_20220623_125102_709_O_.json'),
        os.path.join('MIBG_IN', 'Paudium', '20220712', '7966215700_20220623_132133_709_I_.json'),
        os.path.join('MIBG_IN', 'Paudium', '20220712', '8928178129_20220623_145226_706_I_.json'),
        os.path.join('MIBG_IN', 'Paudium', '20220712', '8928178129_20220623_145226_706_I_.json'),
        os.path.join('MIBG_IN', 'Paudium', '20220712', '09323931304_20220623_125121_720_O_.json'),
        os.path.join('Zoom', 'ZoomMeeting', '20220713', 'recording_1632278095044.mp40.json'),
        os.path.join('Zoom', 'ZoomPhone', '20220712', 'test.json'),
    ]

    return {
        'mix_mapper_files': mix_mapper_files,
        'json_mapper_files': json_mapper_files,
        #TODO:
        # 'json_output': json_output,
        'xml_mapper_files': xml_mapper_files,
        'filename_mapper_files': filename_mapper_files,
    }


@pytest.fixture(autouse=True, scope='module')
def test_json_file(test_info):
    directories.ingestion_mapping_dir = test_info.get('ingestion_mapping_dir')
    file = os.path.abspath(os.path.join(
       'metadata_mapper', 'test_pkg', 'sample_data', 'MIBG_HK', 'HKT', '20220712', '54644_20220628_1610_277_22680294_81700.json'
    ))
    map_file = mapper_file(file)
    filetype = '.json'
    filename = '54644_20220628_1610_277_22680294_81700.json'
    file_dir = os.path.abspath(os.path.join('metadata_mapper', 'test_pkg','sample_data','MIBG_HK', 'HKT', '20220712'))
    software = 'HKT'
    region = 'MIBG_HK'
    date_data = '2022-06-28T20:10:50.000000+0000'
    data_dict = {
        'From_Phone_Number': '22680294',
        'To_Phone_Number': '22680277',
        'Voice_File': '54644_20220628_1610_277_22680294_81700.wav',
        'Date': '2022-06-28',
        'Time': '16:10:50',
        'Duration': '9',
        'Direction': 'Outbound', 
    }
    out_dict = {
        'datetime': '2022-06-28T20:10:50.000000+0000',
        'voice_file': os.path.abspath(os.path.join(
            file_dir , '54644_20220628_1610_277_22680294_81700.wav'
        )),
        'to_email': '22680277',
        'from_email': '22680294',
        'languages': ['en', 'ms'],
    }
    return {
        'file': file,
        'mapper_file': map_file,
        'filetype': filetype,
        'filename': filename,
        'file_dir': file_dir,
        'software': software,
        'region': region,
        'date_data': date_data,
        'out_dict': out_dict,
        'data_dict': data_dict,
    }


@pytest.fixture(autouse=True, scope='module')
def test_xml_file(test_info):
    directories.ingestion_mapping_dir = test_info.get('ingestion_mapping_dir')
    file = os.path.abspath(os.path.join(
        'metadata_mapper', 'test_pkg', 'sample_data', 'MBB_HK', 'IPC', '20220520', '815001006900078.xml'
    ))
    map_file = mapper_file(file)
    filetype = '.xml'
    filename = '815001006900078.xml'
    file_dir = os.path.abspath(os.path.join(
        'metadata_mapper', 'test_pkg', 'sample_data','MBB_HK', 'IPC', '20220520'))
    software = 'IPC'
    region = 'MBB_HK'
    date_data = '2022-08-04T14:26:46.500000+0000'

    data_dict = OrderedDict(
        [
            ('CAudioFile.@xmlns:xsd', 'http://www.w3.org/2001/XMLSchema'),
            ('CAudioFile.@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance'),
            ('CAudioFile.CRI.StartTime', '2022-08-04T14:26:46.5000000+0000'),
            ('CAudioFile.CRI.Duration', '2'),
            ('CAudioFile.CRI.Direction', '0'),
            ('CAudioFile.CRI.AgentPBXID', '33049'),
            ('CAudioFile.CRI.AgentID', '0'),
            ('CAudioFile.CRI.PrivateData.PrivateData.DictionaryEntry.Key', 'CD16'),
            ('CAudioFile.CRI.PrivateData.PrivateData.DictionaryEntry.Value',
                '8778510_318'),
            ('CAudioFile.CRI.Channel', '1913'),
            ('CAudioFile.CRI.Unit', '1000'),
            ('CAudioFile.CRI.SID', '8778510'),
            ('CAudioFile.CRI.DBS_ID', '318'),
            ('CAudioFile.CRI.ScreenUnit', '0'),
            ('CAudioFile.CRI.NumberOfHolds', '0'),
            ('CAudioFile.CRI.NumberOfConferences', '0'),
            ('CAudioFile.CRI.NumberOfTransfers', '0'),
            ('CAudioFile.CRI.TotalHoldTime', '0'),
            ('CAudioFile.CRI.LocalStartTime', '2022-08-04T22:26:46.5000000+0800'),
            ('CAudioFile.CRI.LocalEndTime', '2022-08-04T22:26:48.5000000+0800'),
            ('CAudioFile.CRI.ContactID', '9145781785270000008'),
            ('CAudioFile.CRI.WrapUpTime', '0'),
            ('CAudioFile.CRI.SwitchCallID', 'SIP/AUDIO/00E0A707F66C_3/1658591'),
            ('CAudioFile.CRI.DataSourceName', 'Zone 1'),
            ('CAudioFile.CRI.IsException', '1'),
            ('CAudioFile.CRI.ExceptionReason', '1'),
            ('CAudioFile.CRI.Extension', '33049 Channel 3'),
            ('CAudioFile.CRI.OriginalContactId', '9204604776060000012'),
            ('CAudioFile.CRI.TurretID', '33049'),
            ('CAudioFile.CRI.TurretName', '00E0A707F66C'),
            ('CAudioFile.CRI.RecordingReference', '00E0A707F66C_3'),
            ('CAudioFile.Agent.GroupsList', None),
            ('CAudioFile.Agent.Name', 'Wei Yang,KL_FICC'),
            ('CAudioFile.Agent.Organization', 'MY Traders'),
            ('CAudioFile.File.Location',
                'http://localhost/WSAAudio/Verints;15_20220805_194701/WAV/54644_20220628_1610_277_22680294_81700.wav'),
            ('CAudioFile.File.RawLocation',
                'E:\\Upload\\IPC\\Verints;15_20220805_194701\\WAV\\54644_20220628_1610_277_22680294_81700.wav'
            ),
            ('CAudioFile.File.RawLocationType', 'File'),
            ('CAudioFile.Instances.CInstance.Id', '1'),
            ('CAudioFile.Instances.CInstance.Name', 'CI-Analytics Instance 1'),
            ('CAudioFile.XmlVersion', '10.0.0.0'),
        ]
    )
    out_dict = {
        'datetime': '2022-08-04T14:26:46.500000+0000',
        'voice_file': os.path.abspath(os.path.join(
            file_dir,'54644_20220628_1610_277_22680294_81700.wav'
        )),
        'to_email': '33049',
        'from_email': '8778510',
        'languages': ['en'],
    }
    return {
        'file': file,
        'mapper_file': map_file,
        'filetype': filetype,
        'filename': filename,
        'file_dir': file_dir,
        'software': software,
        'region': region,
        'date_data': date_data,
        'out_dict': out_dict,
        'data_dict': data_dict,
    }


@pytest.fixture(autouse=True, scope='module')
def test_audio_file(test_info):
    directories.ingestion_mapping_dir = test_info.get('ingestion_mapping_dir')
    file = os.path.abspath(os.path.join('metadata_mapper', 'test_pkg','sample_data', 'MBB_VN', 'Hanoi', 'ARC', '20220713', 'IN-20220712_084848_DEV10003092_CH05.wav'
    ))
    map_file = mapper_file(file)
    filetype = '.wav'
    filename = 'IN-20220712_084848_DEV10003092_CH05.wav'
    file_dir = os.path.abspath(os.path.join('metadata_mapper', 'test_pkg','sample_data','MBB_VN', 'Hanoi', 'ARC', '20220713'))
    software = 'ARC'
    region = os.path.join('MBB_VN', 'Hanoi')
    return {
        'file': file,
        'mapper_file': map_file,
        'filetype': filetype,
        'filename': filename,
        'file_dir': file_dir,
        'software': software,
        'region': region,
    }


@pytest.fixture(scope='class')
def init_controller(request, test_info):
    controller = Mapper_Controller(
        test_info.get('ingestion_mapping_dir'),
        test_info.get('processed_mapping_dir'),
        test_info.get('speechmatics_in_dir'),
    )
    request.cls.controller = controller


@pytest.fixture(scope='class')
def init_xml_mapper(request, test_files):
    xml_mapper = Xml_Mapper(test_files.get('xml_mapper_files'))

    request.cls.xml_mapper = xml_mapper

@pytest.fixture(scope='class')
def init_filename_mapper(request, test_files):
    filename_mapper = Filename_Mapper(test_files.get('filename_mapper_files'))

    request.cls.filename_mapper = filename_mapper
