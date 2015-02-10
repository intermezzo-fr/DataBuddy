::Test name: Oracle11G_Partition trimWhitespace
	::Description:	Extract Oracle11G table into CSVFile.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-c[--from_table] is "From table."
::	-P[--from_partition] is "From partition."
::	-f[--from_db] is "From database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-z[--source_client_home] is "Path to Oracle 11G client home."
::	-W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle 11G" extract."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Python27\qc_dist_32\20150209_104450\qc32\qc32.exe ^
-w ora11g2csv ^
-o 1 ^
-r 1 ^
-t "|" ^
-c SCOTT.Partitioned_test_from ^
-P part_15 ^
-f SCOTT/tiger2@orcl ^
-e "YYYY/MM/DD" ^
-m "YYYY-MM-DD-HH24.MI.SS.FF" ^
-O "YYYY-MM-DD-HH24:MI:SS.FF" ^
-z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
-W 1 ^
-g C:\Python27\data_migrator_1239\CSV_OUT\testORA11G_Partition_trimWhitespace.data