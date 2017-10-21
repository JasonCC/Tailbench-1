# start from base
FROM ubuntu:16.04
MAINTAINER Alberto Alvarez Aldea <alberto6@illinois.edu>

# install system-wide deps 
RUN apt-get update 
RUN apt-get -yqq install openjdk-8-jdk libopencv-dev autoconf ant libtcmalloc-minimal4 swig google-perftools libboost1.58-all-dev bzip2 libnuma-dev libjemalloc-dev libgoogle-perftools-dev libdb5.3++-dev libmysqld-dev libaio-dev uuid-dev libbz2-dev python-numpy python-scipy libgtop2-dev

# copy our application code
ADD ./tailbench-v0.9 /opt/Tailbench/tailbench-v.09
ADD ./tailbench.inputs /opt/Tailbench/tailbench.inputs
WORKDIR /opt/Tailbench/tailbench-v.09

# start app
CMD ./build.sh
CMD sudo bash
CMD ./run.sh
