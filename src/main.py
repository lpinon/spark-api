import pyspark
import os
import sys
import argparse
import time
import importlib

if os.path.exists('libs.zip'):
    sys.path.insert(0, 'libs.zip')
else:
    sys.path.insert(0, './libs')

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a PySpark job')
    parser.add_argument('--job', type=str, required=True, dest='job_name', help="The name of the job module you want to run. (ex: poc will run job on jobs.poc package)")
    parser.add_argument('--jobargs', nargs='*', help="Extra arguments to send to the PySpark job (example: --job-args template=manual-email1 foo=bar")

    args = parser.parse_args()
    print('Called with arguments: {0}'.format(args))

    environment = {
        'PYSPARK_JOB_ARGS': ' '.join(args.jobargs) if args.jobargs else ''
    }

    job_args = dict()
    if args.jobargs:
        job_args_tuples = [arg_str.split('=') for arg_str in args.jobargs]
        print('job_args_tuples: {}'.format(job_args_tuples))
        job_args = {a[0]: a[1] for a in job_args_tuples}

    print('\nRunning job {0}...\nenvironment is {1}\n'.format(args.job_name, environment))

    os.environ.update(environment)
    sc = pyspark.SparkContext(appName=args.job_name, environment=environment, master='spark://localhost:7077')
    job_module = importlib.import_module('jobs.{0}'.format(args.job_name))

    start = time.time()
    job_module.analyze(sc, **job_args)
    end = time.time()

    print("\nExecution of job {0} took {1} seconds".format(args.job_name, end-start))
