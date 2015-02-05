# Title:	SSENT_QueryDir_Limit25 -->> SYASE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 25, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssent2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server Enterprise source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Enterprise client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Enterprise source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server Enterprise source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Enterprise source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_ss', 'Input dir with SQL Server Enterprise query sqls.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')})
	