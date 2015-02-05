# Title:	Default API.
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
# do not change below this line
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'Input file with PostgreSQL query sql.'), 'from_db_name': ('-b', '--from_db_name', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'From table.'), 'from_any_partition': ('-P', '--from_any_partition', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', 'PostgreSQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with PostgreSQL query files sql.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to DB2 Express client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'Target DB2 Express table.')})
	