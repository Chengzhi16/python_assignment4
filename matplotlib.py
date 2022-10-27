import matplotlib.pyplot as plt
import numpy as np


# Bar chart for different mode of C++

instance_size = ['5,000', '500,000', '5,000,000', '50,000,000']
C_debug = [15.51, 296.804, 2829.96, 28455.6]
C_release = [0.32, 31.278, 348.964, 2700.39]

x = np.arange(len(instance_size))  # the label locations
width = 0.3 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x + width/2, C_debug, width, label='C++ debug')
rects2 = ax.bar(x - width/2, C_release, width, label='C++ release')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Run time (ms)')
ax.set_xlabel('Instance size')
ax.set_title('Program run time by using C++ in different modes')
ax.set_xticks(x, instance_size)
ax.legend()

ax.bar_label(rects1, label_type='edge', padding=3)
ax.bar_label(rects2, label_type='center',padding=5)

fig.tight_layout()

# Bar chart for only Python

instance_size = ['5,000', '500,000', '5,000,000', '50,000,000']
Python = [22.7, 2227.99, 21992.75, 537258.63]

x = np.arange(len(instance_size))  # the label locations
width = 0.3 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x + width/2, Python, width, label='Python', color='green')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Run time (ms)')
ax.set_xlabel('Instance size')
ax.set_title('Program run time by using Python')
ax.set_xticks(x, instance_size)
ax.legend()

ax.bar_label(rects1, label_type='edge', padding=2)

fig.tight_layout()

# Bar chart for combining all

instance_size = ['5,000', '500,000', '5,000,000', '50,000,000']
Python = [22.7, 2227.99, 21992.75, 537258.63]
C_debug = [15.51, 296.804, 2829.96, 28455.6]
C_release = [0.32, 31.278, 348.964, 2700.39]

x = np.arange(len(instance_size))  # the label locations
width = 0.2 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, Python, width, label='Python', color = 'green')
rects2 = ax.bar(x , C_debug, width, label='C++ debug')
rects3 = ax.bar(x + width, C_release, width, label='C++ release')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Run time (ms)')
ax.set_xlabel('Instance size')
ax.set_title('Comparison of program run time by using Python & C++')
ax.set_xticks(x, instance_size)
ax.legend()

#ax.bar_label(rects1, padding=3)
ax.bar_label(rects1, label_type='center', padding=3,)
ax.bar_label(rects2, label_type='edge',padding=10)
ax.bar_label(rects3, label_type='center',padding=5)

fig.tight_layout()