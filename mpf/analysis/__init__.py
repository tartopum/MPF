"""
Contain classes to analyze data: load them if they exist, else generate them
 and save them.

{
    'type': int,
    'label': int,
    'parents': [ObjectId],
    'settings': {},
    'data': any
}
"""

from .abstracts import cache
from .acf import acf 
from .differencing import differencing
from .smoothing import smoothing
