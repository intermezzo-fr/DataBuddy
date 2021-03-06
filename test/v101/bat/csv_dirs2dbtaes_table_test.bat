::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-L[--email_to] is "Email job status."
::-M[--log_dir] is "Log destination."
::-B[--job_name] is "Job name (log_dir/job_name)."
::-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::-I[--input_dirs] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-a[--to_table] is "Target DB2 Advanced Enterprise Server table."
::-u[--to_user] is "Target DB2 Advanced Enterprise Server db user."
::-p[--to_passwd] is "Target DB2 Advanced Enterprise Server db user password."
::-d[--to_db_name] is "Target DB2 Advanced Enterprise Server database."
::-s[--to_db_server] is "Target DB2 Advanced Enterprise Server db instance name."
::-Z[--target_client_home] is "Path to DB2 Advanced Enterprise Server client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Python27\qc_dist_32\20150309_205118\qc32\qc32.exe ^
-w csv2dbtaes ^
-o 1 ^
-r 1 ^
-t "|" ^
-L alex_buz@yahoo.com;alexbuzunov@gmail.com ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20150309_205118_815000 ^
-I C:\Python27\data_migrator_1239\test\v101\data\db2_data_dir ^
-y 1000 ^
-a ALEX_BUZ.Timestamp_test_to ^
-u "ALEX_BUZ" ^
-p "198Morgan" ^
-d "SAMPLE" ^
-s "DB2" ^
-Z "C:\Program Files (x86)\IBM\SQLLIB_01\BIN"