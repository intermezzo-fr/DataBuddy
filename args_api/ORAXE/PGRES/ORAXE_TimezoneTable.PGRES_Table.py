# Title:	ORAXE_TimezoneTable -->> PGRES_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2pgres', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH24:MI:SS.FF3 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24:MI:SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timezone_test_from', 'From table.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'to_table': ('-a', '--to_table', '"Timezone_test_to"', 'Target PostgreSQL table.')})
	