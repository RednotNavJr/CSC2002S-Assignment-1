JAVAC = javac
JAVA = java
JFLAGS = --release 11 -d bin
SOURCES = FirelineSerial.java FireMap.java TerrainType.java FirelineParallel.java FireMapParallel.java FireTask.java
ARGS ?= 300 300 42 wildfire output/fireline

.PHONY: all run-serial run-parallel clean

all:
	mkdir -p bin
	$(JAVAC) $(JFLAGS) $(SOURCES)

run-serial: all
	$(JAVA) -cp bin FirelineSerial $(ARGS)

run-parallel: all
	$(JAVA) -cp bin FirelineParallel $(ARGS)

clean:
	rm -rf bin output
