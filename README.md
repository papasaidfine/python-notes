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


## Python Interactive Charts
This issue is found in Python 3.10.12 (main, Nov 20 2023, 15:14:05). In a clean Python3 environment, do `pip install matplotlib`. Matplotlib will not show the figure. The below codes reproduce the issue.
```
import matplotlib.pyplot as plt
plt.plot([1,2],[1,2])
plt.show()
```
Output:
```
UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
```
This is because the charting back end is usually "Agg" which is non-interactive. A recommended back end is "TkAgg" by module `tkinter` which suprisingly is not a dependency of `matplotlib`. To install `tkinter`, do
```
sudo apt install python3-tk
```
> [!NOTE]
> Neither `pip install tkinter` nor `pip install tk` works.

Another back end found in some online solutions is `PyQt5`, which does NOT work for me.

To view the back end used by `matplotlib`
```
import matplotlib
matplotlib.get_back()
```
To change the back end
```
matplotlib.use('TkAgg')
```

