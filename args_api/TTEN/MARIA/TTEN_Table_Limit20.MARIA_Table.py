# Title:	TTEN_Table_Limit20 -->> MARIA_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'from_table': ('-c', '--from_table', 'TERRY.Timestamp_test_from', 'From table.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')})
	