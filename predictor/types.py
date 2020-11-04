from typing import Literal, Union
from datetime import datetime, date
from .data import Data

PERIOD = Literal['day', 'year', ]
DATE = Union[datetime, date]
CURRENCY = Literal['rub', 'usd', 'eu', ]
DATA = Data
