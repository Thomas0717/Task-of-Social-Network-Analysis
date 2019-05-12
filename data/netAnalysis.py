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
    print(data)

    pylab.figure('log-log ' + feature)
    pylab.title('Log-log Distribution of ' + feature + ' to User Count')
    pylab.xlabel(feature + ' Count(log10)')
    pylab.ylabel("User Count(log10)")

    
    feature_count_pairs = data.apply(pd.value_counts)
    
    lol = list(chain(*data.values.tolist()))
    pop=collections.Counter(lol)
    print(pop)

    feature_value = np.log10(list(pop.keys()))
    user_count = np.log10(list(pop.values()))
    #feature_value = np.log10(zip(*feature_count_pairs)[0])
    #user_count = np.log10(zip(*feature_count_pairs)[1])
    pylab.scatter(feature_value, user_count)

    pylab.show()
