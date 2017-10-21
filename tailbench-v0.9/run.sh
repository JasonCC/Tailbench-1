#!/bin/bash

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [[ $# -eq 0 ]]
then
    HARNESS_DIR=harness
    APP_DIRS="img-dnn masstree moses shore silo specjbb sphinx xapian"
else
    APP_DIRS=$@
fi

for dir in ${APP_DIRS}
do
    echo "Running $dir"
    cd ${ROOT}/${dir}
    if [ $dir == "xapian" ]
    then
        LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/xapian-core-1.2.13/install/lib/
        export LD_LIBRARY_PATH
        echo "Hola"# sudo ./run.sh &> run.log
    fi
    ./run.sh &> run.log
    EXIT_CODE=$?
    if [[ $EXIT_CODE -ne 0 ]]
    then
        echo "WARNING: Running $dir returned error status $EXIT_CODE"
    fi
    cd -
done
