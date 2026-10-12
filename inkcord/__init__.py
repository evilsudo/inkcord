"""
Copyright © 2025 sunset-hue

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# TODO:
# Make member and other objects like that support being a parameter
# Message object (working on)

from .client import *
from .exceptions import *
from .http_gateway import *
from .inter import *
from .listener import *
from .resourceid import *
from .shared_types import *
from .slash_cmd import *

# ----------------------------- #
#            Types              #
# ----------------------------- #
from .types.attach import *
from .types.avatar import *
from .types.channel import *
from .types.embed import *
from .types.emoji import *
from .types.guild import *
from .types.guild_mem import *
from .types.message import *
from .types.permissions import *
from .types.role import *
from .types.user import *
from .util import *
