# Title:	ORAXE_TimestampTable -->> TTEN_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, 
	{'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD HH24.MI.SS"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24.MI.SS.FF2"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')})
	