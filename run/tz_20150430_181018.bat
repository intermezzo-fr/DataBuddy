echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe ^
-E 1 ^
-t | ^
-r 1 ^
-C C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml ^
-w ora11g2ora11g ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-U 1 ^
-Y 20150430_180439_896000 ^
-5 C:\Users\alex_buz\sessions\My_Sessions\tz\host_map_v2.py ^
-o 1 ^
-B qc_job ^
-K 1 ^
-q C:\Python27\data_migrator_1239_ddl\test\v101\query\oracle_query_tz.sql ^
-b orcl ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-j SCOTT ^
-d orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-u SCOTT ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-a SCOTT.Timezone_test_to 