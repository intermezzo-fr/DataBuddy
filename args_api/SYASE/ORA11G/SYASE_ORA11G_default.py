# Title:	Default API.
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
# do not change below this line
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'Input file with SAP Sybase ASE query sql.'), 'from_db_name': ('-b', '--from_db_name', 'SAP Sybase ASE source database.'), 'header': ('-H', '--header', 'Include header to SAP Sybase ASE extract.'), 'from_table': ('-c', '--from_table', 'From table.'), 'source_client_home': ('-z', '--source_client_home', 'Path to SAP Sybase ASE client home.'), 'from_user': ('-j', '--from_user', 'SAP Sybase ASE source user.'), 'from_passwd': ('-x', '--from_passwd', 'SAP Sybase ASE source user password.'), 'from_db_server': ('-n', '--from_db_server', 'SAP Sybase ASE source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with SAP Sybase ASE query files sql.')}, 
	{'to_db': ('-g', '--to_db', 'To Oracle database.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'To Oracle table.'), 'to_sub_partition': ('-N', '--to_sub_partition', 'To Oracle table.'), 'to_partition': ('-G', '--to_partition', 'To Oracle table.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to Oracle client home bin dir.')})
	