
			set pagesize 0 feedback off TIMING OFF
			SELECT COLUMN_NAME||':'||DATA_LENGTH||':'||DATA_TYPE
			FROM ALL_TAB_COLUMNS WHERE OWNER=UPPER('SCOTT') AND TABLE_NAME=UPPER('PARTITIONED_TEST_FROM')
			ORDER BY COLUMN_ID;
			exit;
			