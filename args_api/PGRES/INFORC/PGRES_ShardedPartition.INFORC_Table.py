# Title:	PGRES_ShardedPartition -->> INFORC_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'pgres2inforc', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"postgres"', 'PostgreSQL source database.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'from_any_partition': ('-P', '--from_any_partition', 'Partitioned_test_from_2014', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home.'), 'from_user': ('-j', '--from_user', '"postgres"', 'PostgreSQL source user.'), 'source_port': ('-R', '--source_port', '5434', 'Connection port for source PostgreSQL.'), 'from_passwd': ('-x', '--from_passwd', '"postgre_pwd"', 'PostgreSQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'PostgreSQL source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix Innovator C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix Innovator C client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix Innovator C db user.'), 'to_passwd': ('-p', '--to_passwd', '"infor_pwd"', 'Target Informix Innovator C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix Innovator C db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix Innovator C table.')})
	