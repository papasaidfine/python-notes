import time
import pytz
from datetime import datetime, timezone, timedelta

# From datetime at specific timezone to timestamp
dt = datetime(2023,2,25,9,30,tzinfo=spec_tz1)
dt = dt.replace(tzinfo=None) # revert back to naive datetime object
spec_tz1 = pytz.timezone('Asia/Hong_Kong')
spec_tz2 = pytz.timezone('America/New_York')
spec_tz1.localize(dt).timestamp()
spec_tz2.localize(dt).timestamp()

# From timestamp to datetime at specific timezone
spec_tz1 = pytz.timezone('Asia/Hong_Kong')
spec_tz2 = pytz.timezone('America/New_York')
spec_tz3 = pytz.timezone('UTC')
tstamp = 1677202200
datetime.fromtimestamp(tstamp, tz=spec_tz1)
datetime.fromtimestamp(tstamp, tz=spec_tz2)
datetime.fromtimestamp(tstamp, tz=spec_tz3)
datetime.fromtimestamp(tstamp, tz=spec_tz1).strftime('%Y-%m-%d %H:%M:%S')
datetime.fromtimestamp(tstamp, tz=spec_tz2).strftime('%Y-%m-%d %H:%M:%S')
datetime.fromtimestamp(tstamp, tz=spec_tz3).strftime('%Y-%m-%d %H:%M:%S')


## Incompatibility between pytz and datetime modules
# Winter - no DST
pytz.timezone('Europe/London').localize(datetime(2022,1,1,0,0)).timestamp() # the correct way to convert to timestamp given a timezone
datetime(2022,1,1,0,0,tzinfo=pytz.timezone('Europe/London')).timestamp() # wrong way to convert to timestamp given a timezone!!

# Summer - with DST
pytz.timezone('Europe/London').localize(datetime(2022,6,1,0,0)).timestamp() # the correct way to convert to timestamp given a timezone
datetime(2022,6,1,0,0,tzinfo=pytz.timezone('Europe/London')).timestamp() # wrong way to convert to timestamp given a timezone!!
