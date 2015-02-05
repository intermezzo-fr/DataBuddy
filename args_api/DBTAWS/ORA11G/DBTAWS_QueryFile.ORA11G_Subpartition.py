# Title:	DBTAWS_QueryFile -->> ORA11G_Subpartition
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtaws2ora11g', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Advanced Workgroup Server query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Advanced Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Advanced Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Advanced Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Advanced Workgroup Server source instance name.')}, 
	{'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.'), 'to_sub_partition': ('-N', '--to_sub_partition', 'part_15_sp1', 'To Oracle table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.')})
	