# Title:	MYSQL_Subpartition -->> SLITE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_sub_partition': ('-S', '--from_sub_partition', 'subpart200', 'From sub-partition.'), 'from_table': ('-c', '--from_table', 'TEST.Sub_Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')})
	