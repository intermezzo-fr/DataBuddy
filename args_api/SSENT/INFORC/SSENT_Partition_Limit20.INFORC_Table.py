# Title:	SSENT_Partition_Limit20 -->> INFORC_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssent2inforc', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server Enterprise source database.'), 'from_partition': ('-P', '--from_partition', 'DateRange(Created)=3', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Enterprise client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Enterprise source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server Enterprise source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Enterprise source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix Innovator C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix Innovator C client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix Innovator C db user.'), 'to_passwd': ('-p', '--to_passwd', '"infor_pwd"', 'Target Informix Innovator C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix Innovator C db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix Innovator C table.')})
	