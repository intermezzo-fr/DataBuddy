# Title:	PGRES_Table_Limit15 -->> DBTE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')})
	