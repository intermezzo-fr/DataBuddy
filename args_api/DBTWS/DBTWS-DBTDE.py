aa={'DBTWS_ShardedQueryFile.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Workgroup Server query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_Partition.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with DB2 Workgroup Server query sql.'), 'from_db_name': ('-b', '--from_db_name', 'DB2 Workgroup Server source database.'), 'from_partition': ('-P', '--from_partition', 'From partition.'), 'from_table': ('-c', '--from_table', 'From table.'), 'source_client_home': ('-z', '--source_client_home', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', 'DB2 Workgroup Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with DB2 Workgroup Server query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to DB2 Developer Edition client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'Target DB2 Developer Edition table.')}], 'DBTWS_ParallelQueryDir.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Workgroup Server query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_QueryFile_Limit10.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Workgroup Server query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_ShardedPartition_Limit50.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 50, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_QueryFile.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Workgroup Server query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_Table_Limit20.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_Table_KeepSpoolFile.DBTDE_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_QueryDir.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Workgroup Server query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_Table.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_QueryDir_Limit10.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Workgroup Server query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_ShardedTable.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_Partition_Limit30.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 30, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_ParallelQueryDir_Limit10.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Workgroup Server query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'DBTWS_ShardedTable_Limit65.DBTDE_Table': [{'lame_duck': ('-l', '--lame_duck', 65, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtws2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Workgroup Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Workgroup Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Workgroup Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Workgroup Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Workgroup Server source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}]}