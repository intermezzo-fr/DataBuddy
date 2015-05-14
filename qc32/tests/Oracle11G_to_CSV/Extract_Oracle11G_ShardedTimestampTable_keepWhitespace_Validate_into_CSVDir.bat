::Test name: Oracle11G_ShardedTimestampTable keepWhitespace Validate
	::Description:	Extract Oracle11G table into CSVDir.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-K[--keep_data_file] is "Keep data dump."
::	-V[--validate] is "Check if source and target objects exist."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "Oracle 11G source user."
::	-x[--from_passwd] is "Oracle 11G source user password."
::	-b[--from_db_name] is "Oracle 11G source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-W[--keep_whitespace] is "Keep whitespace from CHAR type in "Oracle 11G" extract."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Python27\qc_dist_32\20150513_194648\qc32\qc32.exe ^
-w ora11g2csv ^
-o 3 ^
-r 3 ^
-t "|" ^
-K 1 ^
-V 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150513_194648_378000 ^
-5 ".\config\host_map_v2.py" ^
-c SCOTT.Timestamp_test_from ^
-j SCOTT ^
-x tiger ^
-b orcl ^
-e "YYYY/MM/DD" ^
-m "YYYY-MM-DD-HH24.MI.SS.FF" ^
-O "YYYY-MM-DD-HH24:MI:SS.FF" ^
-W 1 ^
-D C:\Python27\data_migrator_1239_ddl\CSV_OUT