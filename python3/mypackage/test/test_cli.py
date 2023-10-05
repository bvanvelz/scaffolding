import sys
sys.path.append('../../mypackage')
import pytest
from mypackage import cli
from mock import patch
from datetime import datetime


def test_parse_args():
	args = cli.process_args(['30', '-f', '--option', 'test'])
	assert args.args == [30]
	assert args.flag == True
	assert args.option1_dest == 'test'

@patch('mypackage.cli.get_datestr.datetime.datetime')
def test_get_datestr(mock_datetime):
	mock_datetime.now.return_value = datetime(2019, 3, 15)
	print(mock_datetime.now())
