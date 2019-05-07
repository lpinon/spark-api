@echo off
if [%1]==[] goto usage
rem del /F /Q dist
make build
cd dist && spark-submit --py-files jobs.zip,libs.zip main.py --job %1 && cd ..
goto :eof
:usage
@echo ERROR: JobName not defined
@echo Usage: %0 jobName
exit /B 1