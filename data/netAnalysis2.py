# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd
import pylab
import collections
import numpy as np
import networkx as nx
import time
import math
import operator
from itertools import chain
from functools import reduce
from collections import defaultdict


def plot_user_summary_log_log_distribution():

    feature = 'fan_num'

    data = pd.read_csv('D:\kkk.csv')
    user = pd.read_csv('D:\kkkk.csv')
    print(data)
    print(user)
    pylab.figure('tweet_nums per user')
    pylab.title('tweet_nums per user')
    pylab.xlabel('user')
    pylab.ylabel("tweet_nums")

    pylab.scatter(user, data)
    pylab.show()


#plot_user_summary_log_log_distribution()
