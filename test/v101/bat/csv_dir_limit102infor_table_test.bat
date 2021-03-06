::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-I[--input_dir] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-a[--to_table] is "Target Informix IDS table."
::-u[--to_user] is "Target Informix IDS db user."
::-p[--to_passwd] is "Target Informix IDS db user password."
::-d[--to_db_name] is "Target Informix IDS database."
::-s[--to_db_server] is "Target Informix IDS db instance name."
::-Z[--target_client_home] is "Path to Informix IDS client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\qc_dist_32\20150207_115221\qc32\qc32.exe ^
-w csv2infor ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-I c:\Python27\data_migrator_1239\test\v101\data\infor_data_dir ^
-y 1000 ^
-a Timestamp_test_to ^
-u "informix" ^
-p "test_pwd" ^
-d "test" ^
-s "ol_s_121414_204157" ^
-Z "C:\Program Files (x86)\IBM Informix Software Bundle\bin"