
SET TAB OFF timing off head off line 32767 pages 0 newpage 0 echo off feedback on define off feed off arraysize 5000
set embedded on
set und off
set embedded on
set pagesize 0
set colsep '|'
set echo off
set feedback on
set trimspool on
set headsep off
SET newpage none 
SET verify off 
SET trims ON 
SET trimspool ON 
set underline off
SELECT * FROM (SELECT * FROM SCOTT.Sub_Partitioned_test_from  SUBPARTITION(part_15_sp1)  WHERE ROWID BETWEEN 'AAASzlAAEAAAATIAAA' AND 'AAASzlAAEAAAATPABk') ;
exit;