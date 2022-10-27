import os, nbody
from time import perf_counter

iterations_list=[5,50,500,5000] #to save time for testing
python_filename_list=['python_5.csv','python_50.csv','python_500.csv','python_5000.csv']
debug_filename_list=['c++_debug_5.csv','c++_debug_50.csv','c++_debug_500.csv','c++_debug_5000.csv']
release_filename_list=['c++_release_5.csv','c++_release_50.csv','c++_release_500.csv','c++_release_5000.csv']

for i in range(4):
    begin_python = perf_counter()
    os.system('nbody.py {} {}'.format(iterations_list[i],python_filename_list[i]))
    finish_python = perf_counter()

    '''begin_debug = perf_counter()
    os.system('D:\\Geomatics\\Q1\\Python Programming\\assignments\\assignment4\\nbody\\cmake-build-debug\\nbody.exe {} {}'.format(iterations_list[i],debug_filename_list[i])) #just change the filepath to that in your computer
    finish_debug = perf_counter()

    begin_release = perf_counter()
    os.system('D:\\Geomatics\\Q1\\Python Programming\\assignments\\assignment4\\nbody\\cmake-build-release\\nbody.exe {} {}'.format(iterations_list[i],release_filename_list[i]))
    finish_release = perf_counter()

    print('stimulation times: {}'.format(iterations_list[i]))
    print('python running times: {:.2f}ms'.format((finish_python - begin_python)*1000))
    print('c++ debug running times: {:.2f}ms'.format((finish_debug - begin_debug) * 1000))
    print('c++ release running times: {:.2f}ms\n'.format((finish_release - begin_release) * 1000))
    '''

