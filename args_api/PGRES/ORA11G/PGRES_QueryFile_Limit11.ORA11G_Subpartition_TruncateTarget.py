# Title:	PGRES_QueryFile_Limit11 -->> ORA11G_Subpartition_TruncateTarget
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 11, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2ora11g', 'Data copy direction.'), 'truncate_target': ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\postgre_query.sql', 'Input file with PostgreSQL query sql.'), 'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, 
	{'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF3"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24:MI:SS"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF3 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Sub_Partitioned_test_to', 'To Oracle table.'), 'to_sub_partition': ('-N', '--to_sub_partition', 'part_15_sp1', 'To Oracle table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.')})
	