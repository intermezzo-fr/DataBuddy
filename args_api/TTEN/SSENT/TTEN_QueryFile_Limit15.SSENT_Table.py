# Title:	TTEN_QueryFile_Limit15 -->> SSENT_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2ssent', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\timesten_query.sql', 'Input file with TimesTen query sql.'), 'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24:MI:SS"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'test', 'SQL Server Enterprise database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Enterprise client home bin dir.'), 'to_user': ('-u', '--to_user', 'sa', 'Target SQL Server Enterprise db user.'), 'to_passwd': ('-p', '--to_passwd', 'ssent_pwd', 'SQL Server Enterprise user password.'), 'to_db_server': ('-s', '--to_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Enterprise instance name.'), 'to_table': ('-a', '--to_table', 'dbo.Timestamp_test_to', 'To table.')})
	