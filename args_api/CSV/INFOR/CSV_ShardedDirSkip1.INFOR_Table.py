# Title:	CSV_ShardedDirSkip1 -->> INFOR_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\infor_data_dir', 'Input CSV directory.'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')})
	