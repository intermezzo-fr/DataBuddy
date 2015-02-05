# Title:	SYIQ_ShardedQueryFile -->> ORA11G_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'syiq2ora11g', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\sybase_query.sql', 'Input file with Sybase IQ query sql.'), 'from_db_name': ('-b', '--from_db_name', '"demo"', 'Sybase IQ source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to Sybase IQ client home.'), 'from_user': ('-j', '--from_user', '"dba"', 'Sybase IQ source user.'), 'from_passwd': ('-x', '--from_passwd', '"sql"', 'Sybase IQ source user password.'), 'from_db_server': ('-n', '--from_db_server', '"demo16"', 'Sybase IQ source instance name.')}, 
	{'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.'), 'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.')})
	