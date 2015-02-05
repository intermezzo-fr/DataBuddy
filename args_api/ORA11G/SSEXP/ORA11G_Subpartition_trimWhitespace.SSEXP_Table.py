# Title:	ORA11G_Subpartition_trimWhitespace -->> SSEXP_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ora11g2ssexp', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_sub_partition': ('-S', '--from_sub_partition', 'part_15_sp1', 'From sub-partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24:MI:SS"', 'nls_date_format for source.'), 'trim_whitespace': ('-W', '--trim_whitespace', 1, 'Trim whitespace from varchar2 in "Oracle" extract.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF3 TZH:TZM"', 'nls_timestamp_tz_format for source.'), 'from_table': ('-c', '--from_table', 'SCOTT.Sub_Partitioned_test_from', 'From table.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'master', 'SQL Server Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server Express db user.'), 'to_passwd': ('-p', '--to_passwd', '198Morgan', 'SQL Server Express user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')})
	