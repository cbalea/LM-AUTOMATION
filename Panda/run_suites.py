'''
Created on 15.10.2012

@author: cbalea
'''

from subprocess import Popen
import glob
import os
import sys
from time import time
 

all_tests = glob.glob('cms/tests/login/test*.py')
all_tests += glob.glob('cms/tests/asset/test*.py')
all_tests += glob.glob('cms/tests/media/test*.py')
all_tests += glob.glob('cms/tests/reports/test*.py')
all_tests += glob.glob('cms/tests/resource/test*.py')
all_tests += glob.glob('cms/tests/station_site_cms/test*.py')
all_tests += glob.glob('cms/tests/test*.py')
all_tests += glob.glob('ss/tests/test*.py')

smoke_tests = glob.glob('cms/tests/login/test*.py')
smoke_tests += glob.glob('ss/tests/test*smoke.py')




def start_processes(start_index, nb_of_processes):
    for i in xrange(start_index, start_index+nb_of_processes):
        try:
            processes.append(Popen('nosetests %s --with-xunit --xunit-file=testsresults/testresults%i.xml' %(tests[i], i), shell=True))
        except IndexError:
            break
    for i in xrange(start_index, start_index+nb_of_processes):
        print "started new process: " + tests[i]
        processes[i].poll()


def count_old_alive_processes(current_process):
    alive_processes=0
    for i in xrange(current_process):
        try:
            if(processes[i].poll() == None):
                alive_processes+=1
        except IndexError:
            alive_processes+=0
    return alive_processes


def wait_for_all_processes_to_complete():
    while count_old_alive_processes(total_test_suites) != 0:
        True
     
     
     
     

try:
    if sys.argv[1] == "smoke":
        tests = smoke_tests
    elif sys.argv[1] == "all":
        tests = all_tests
except (IndexError):
    tests = all_tests

start_time = time()
total_test_suites = len(tests)
processes = []
parallel_tests = int(os.environ["PARALLEL_TESTS"])

start_processes(0, parallel_tests)

j = parallel_tests
while j < total_test_suites:
    alive_processes = count_old_alive_processes(j)
    if(alive_processes < parallel_tests):
        needed_processes = parallel_tests - alive_processes
        start_processes(j, needed_processes)
        j+=needed_processes

wait_for_all_processes_to_complete()


print "parallel tests = %d" %parallel_tests
run_time = time() - start_time
print "TOTAL RUN TIME: %dmin %dsec." %(run_time/60, run_time%60)
