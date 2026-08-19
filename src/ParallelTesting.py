# VTNJOS003

import subprocess
import csv
import numpy as np
import datetime

# Program to run mutliple tests while differing parameters

# initialise variables

initialSize = 40
seed = 69
all_data_parallel = np.array([])
all_data_serial = np.array([])
time_data_parallel = np.array([])
time_data_serial = np.array([])
sequentialCutoffs = np.array([2, 4, 5, 10, 20])

writerParallel = csv.writer(open("nightmare_output/timesParallel.csv", mode='w', newline='', encoding='utf-8'))
writerSerial = csv.writer(open("nightmare_output/timesSerial.csv", mode='w', newline='', encoding='utf-8'))

# run for different grid sizes

print(datetime.datetime.now())

for size in range(initialSize, 41, 40):

    # run for different landscapes

    for landscape in ["mixed", "grass"]:

        # run for different modes

        for mode in ["wildfire", "diffusion"]:

            time_data_serial = np.array([])
            
            for _ in range(1, 6):
            
                # Serial
                result_serial = subprocess.run(f"make run-serial ARGS=\"" + str(size) + " " + str(size) + " " + str(seed) + " " + mode + " nightmare_output/Serial_" + mode + "_" + landscape + "_" + str(size) + " 50000 0.05 " + landscape + "\"", shell = True, capture_output = True, text = True, check = True)
                data_serial = result_serial.stdout.split("\n")
            
                all_data_serial = np.append(all_data_serial, data_serial[4:])
                time_data_serial = np.append(time_data_serial, float(data_serial[15][22:len(data_serial[15]) - 3]))

            time_data_serial = np.append(time_data_serial, "Average: " + str(np.mean(time_data_serial[2:])))
            time_data_serial = np.append(time_data_serial, "Mode: " + mode + " Landscape: " + landscape + " Size: " + str(size))
            writerSerial.writerow(time_data_serial)

            # run for different cutoffs

            for cutoff in sequentialCutoffs:

                time_data_parallel = np.array([])
    
                for _ in range(1, 6):

                    # Parallel
                    result_parallel = subprocess.run(f"make run-parallel ARGS=\"" + str(size) + " " + str(size) + " " + str(seed) + " " + mode + " nightmare_output/Parallel_" + mode + "_" + landscape + "_" + str(size) + " " + str(cutoff) + " 50000 0.05 " + landscape + "\"", shell = True, capture_output = True, text = True, check = True)
                    data_parallel = result_parallel.stdout.split("\n")

                    all_data_parallel = np.append(all_data_parallel, data_parallel[4:])
                    time_data_parallel = np.append(time_data_parallel, float(data_parallel[15][22:len(data_parallel[15]) - 3]))

                time_data_parallel = np.append(time_data_parallel, "Average: " + str(np.mean(time_data_parallel[2:])))
                time_data_parallel = np.append(time_data_parallel, "Cutoff: " + str(cutoff) + " Mode: " + mode + " Landscape: " + landscape + " Size: " + str(size))
                writerParallel.writerow(time_data_parallel)

print("Done")
print(datetime.datetime.now())