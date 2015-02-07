aa={'TTEN_QueryFile.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\timesten_query.sql', 'Input file with TimesTen query sql.'), 'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_ParallelQueryDir.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_tt', 'Input dir with TimesTen query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_QueryDir_Limit25.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 25, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_tt', 'Input dir with TimesTen query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_QueryFile_Limit15.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\timesten_query.sql', 'Input file with TimesTen query sql.'), 'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with TimesTen query sql.'), 'from_DSN_name': ('-b', '--from_DSN_name', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', 'Path to TimesTen client home.'), 'from_table': ('-c', '--from_table', 'From table.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'TimesTen source user password.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with TimesTen query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to Informix IDS client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Target Informix IDS table.')}], 'TTEN_ShardedQueryFile.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\timesten_query.sql', 'Input file with TimesTen query sql.'), 'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_QueryDir.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_tt', 'Input dir with TimesTen query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_ParallelQueryDir_Limit30.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 30, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_tt', 'Input dir with TimesTen query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_Table_KeepSpoolFile.INFOR_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'from_table': ('-c', '--from_table', 'TERRY.Timestamp_test_from', 'From table.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_Table.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'from_table': ('-c', '--from_table', 'TERRY.Timestamp_test_from', 'From table.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_ShardedTable.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'from_table': ('-c', '--from_table', 'TERRY.Timestamp_test_from', 'From table.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'TTEN_Table_Limit20.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'tten2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_DSN_name': ('-b', '--from_DSN_name', 'my_ttdb', 'Source server DSN for TimesTen.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home.'), 'from_table': ('-c', '--from_table', 'TERRY.Timestamp_test_from', 'From table.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF2"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"MM/DD/YYYY"', 'nls_date_format for source.'), 'from_user': ('-j', '--from_user', 'TERRY', 'TimesTen source user.'), 'from_passwd': ('-x', '--from_passwd', 'secret', 'TimesTen source user password.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}]}