# Changes
This file shows the changes which have been done in the baseline benchmark.

* Edit config.sh:
	- DATA_ROOT=../tailbench.inputs
	- JDK_PATH=/usr/lib/jvm/java-8-openjdk-amd64
	- SCRATCH_DIR=../scratch

* Edit Makefile.config:
	- JDK_PATH=/usr/lib/jvm/java-8-openjdk-amd64

* Edit build.sh:
	- Line 17: ./build.sh &> build.log

* Edit sphinx/Makefile:
	- Line 43: $(CXX) $^ -o $@ `pkg-config --libs pocketsphinx sphinxbase` $(LDFLAGS)

* Edit silo/Makefile:
	- Line 78: CXXFLAGS := -g -Wall -Wno-error=maybe-uninitialized -std=c++0x

* Edit moses/Jamroot:
	- Line 77: external-lib bz2:wq

* Edit shore/run.sh:
    - Line 14: SCRATCH_DIR=../../scratch                                                                                                                                 

* Crate/Add run.sh
