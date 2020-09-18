import sys
import os

# Make sure that the testing framework is imported from the repository root
grandparent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, grandparent)

from lib.tptest import *
