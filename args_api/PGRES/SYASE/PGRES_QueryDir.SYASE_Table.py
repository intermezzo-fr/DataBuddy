# Title:	PGRES_QueryDir -->> SYASE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_pgres', 'Input dir with PostgreSQL query files sql.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')})
	