# python-notes
Python coding tips.

## Date Time & Time Zone
There are different types of classes to deal with date time and time zones: `datetime`, `zoneinfo`, `pytz`, `pandas`.

Use `zoneinfo` to specify the time zone of an `datetime` object, do NOT use `pytz`.
```
from datetime import datetime
from zoneinfo import ZoneInfo
dt = datetime(2048,1,1,9,30, tzinfo=ZoneInfo('Asia/Hong_Kong'))
dt.timestamp() # convert to unix timestamp
```

> [!CAUTION]
> Below is the wrong way to specify the time zone:
> ```
> dt = datetime(2048,1,1,9,30, tzinfo=pytz.timezone('Asia/Hong_Kong'))
> dt.timestamp() # this will convert to a wrong unix timestamp
> ```

Naive `datetime` vs time-zone-aware `datetime`
```
dt_naive = datetime(2048,1,1,9,30) # naive
dt_tz = datetime(2048,1,1,9,30, tzinfo=ZoneInfo('Asia/Hong_Kong')) # tz-aware

# conversion
dt_naive = dt_tz.replace(tzinfo=None)
dt_tz = dt_naive.replace(tzinfo=ZoneInfo('Asia/Hong_Kong'))
```

Unix timestamp => date time is not that tricky but I suggest still stick with `zoneinfo` instead of `pytz`
```
tstamp = 2461455000
datetime.fromtimestamp(tstamp, tz=ZoneInfo('Asia/Hong_Kong')).strftime('%Y-%m-%d %H:%M:%S')
# datetime.fromtimestamp(tstamp, tz=pytz.timezone('Asia/Hong_Kong')).strftime('%Y-%m-%d %H:%M:%S') # also works but not suggested
```

For class `pandas._libs.tslibs.timestamps.Timestamp` object, it can be converted to a tz-aware `datetime` object
```
dt_pandas.to_pydatetime()
```

> [!NOTE]
> If you insist to use `pytz` with `datetime`, follow the steps below to convert to the correct unix timestamp:
> ```
> dt = datetime(2048,1,1,9,30, tzinfo=pytz.timezone('Asia/Hong_Kong'))
> # dt.timestamp() # this will convert to a wrong unix timestamp
> dt_naive = dt.replace(tzinfo=None) # convert back to naive
> pytz.timezone('Asia/Hong_Kong').localize(dt_naive).timestamp()
> ```
