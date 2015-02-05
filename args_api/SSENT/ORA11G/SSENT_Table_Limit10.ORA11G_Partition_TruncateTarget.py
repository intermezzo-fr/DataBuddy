# Title:	SSENT_Table_Limit10 -->> ORA11G_Partition_TruncateTarget
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssent2ora11g', 'Data copy direction.'), 'truncate_target': ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.')}, 
	{'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server Enterprise source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Enterprise client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Enterprise source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server Enterprise source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Enterprise source instance name.')}, 
	{'to_db': ('-g', '--to_db', 'SCOTT/tiger2@orcl', 'To Oracle database.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Partitioned_test_to', 'To Oracle table.'), 'to_partition': ('-G', '--to_partition', 'part_15', 'To Oracle table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home bin dir.')})
	