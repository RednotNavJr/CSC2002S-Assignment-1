# vtnjos003

import numpy as np
import matplotlib.pyplot as plt

# read data out from .csv

StringAveragesSerial = np.genfromtxt("src/timesSerial.csv", delimiter=",", usecols=5, dtype=str)
AveragesSerial = np.array([float(average[9:]) for average in StringAveragesSerial])

StringAveragesParallel = np.genfromtxt("src/timesParallel.csv", delimiter=",", usecols=5, dtype=str)
AveragesParallel = np.array([float(average[9:]) for average in StringAveragesParallel])

nightmareStringAveragesSerial = np.genfromtxt("src/nightmare_output/timesSerial.csv", delimiter=",", usecols=5, dtype=str)
nightmareAveragesSerial = np.array([float(average[9:]) for average in nightmareStringAveragesSerial])

nightmareStringAveragesParallel = np.genfromtxt("src/nightmare_output/timesParallel.csv", delimiter=",", usecols=5, dtype=str)
nightmareAveragesParallel = np.array([float(average[9:]) for average in nightmareStringAveragesParallel])

# calculate data for wildfire mixed and store in arrays

wildFireMixedSerial = []
nightmarewildFireMixedSerial = []
Average2 = []
Average4 = []
Average5 = []
Average10 = []
Average20 = []
nightmareAverage2 = []
nightmareAverage4 = []
nightmareAverage5 = []
nightmareAverage10 = []
nightmareAverage20 = []
SpeedUp2 = []
SpeedUp4 = []
SpeedUp5 = []
SpeedUp10 = []
SpeedUp20 = []
nightmareSpeedUp2 = []
nightmareSpeedUp4 = []
nightmareSpeedUp5 = []
nightmareSpeedUp10 = []
nightmareSpeedUp20 = []

for i in range(0, len(AveragesSerial), 4):

    wildFireMixedSerial.append(AveragesSerial[i])
    nightmarewildFireMixedSerial.append(nightmareAveragesSerial[i])

    for j in range(0, 5):
        match j:
            case 0:
                SpeedUp2.append(AveragesSerial[i]/AveragesParallel[5*i+j])
                Average2.append(AveragesParallel[5*i+j])
                nightmareAverage2.append(nightmareAveragesParallel[5*i+j])
                nightmareSpeedUp2.append(nightmareAveragesSerial[i]/nightmareAveragesParallel[5*i+j])
            case 1:
                SpeedUp4.append(AveragesSerial[i]/AveragesParallel[5*i+j])
                Average4.append(AveragesParallel[5*i+j])
                nightmareAverage4.append(nightmareAveragesParallel[5*i+j])
                nightmareSpeedUp4.append(nightmareAveragesSerial[i]/nightmareAveragesParallel[5*i+j])
            case 2:
                SpeedUp5.append(AveragesSerial[i]/AveragesParallel[5*i+j])
                Average5.append(AveragesParallel[5*i+j])
                nightmareAverage5.append(nightmareAveragesParallel[5*i+j])
                nightmareSpeedUp5.append(nightmareAveragesSerial[i]/nightmareAveragesParallel[5*i+j])
            case 3:
                SpeedUp10.append(AveragesSerial[i]/AveragesParallel[5*i+j])
                Average10.append(AveragesParallel[5*i+j])
                nightmareAverage10.append(nightmareAveragesParallel[5*i+j])
                nightmareSpeedUp10.append(nightmareAveragesSerial[i]/nightmareAveragesParallel[5*i+j])
            case 4:
                SpeedUp20.append(AveragesSerial[i]/AveragesParallel[5*i+j])
                Average20.append(AveragesParallel[5*i+j])
                nightmareAverage20.append(nightmareAveragesParallel[5*i+j])
                nightmareSpeedUp20.append(nightmareAveragesSerial[i]/nightmareAveragesParallel[5*i+j])

wildFireMixedSerial = np.array(wildFireMixedSerial)
nightmarewildFireMixedSerial = np.array(nightmarewildFireMixedSerial)
SpeedUp2 = np.array(SpeedUp2)
SpeedUp4 = np.array(SpeedUp4)
SpeedUp5 = np.array(SpeedUp5)
SpeedUp10 = np.array(SpeedUp10)
SpeedUp20 = np.array(SpeedUp20)
nightmareSpeedUp2 = np.array(nightmareSpeedUp2)
nightmareSpeedUp4 = np.array(nightmareSpeedUp4)
nightmareSpeedUp5 = np.array(nightmareSpeedUp5)
nightmareSpeedUp10 = np.array(nightmareSpeedUp10)
nightmareSpeedUp20 = np.array(nightmareSpeedUp20)
Average2 = np.array(Average2)
Average4 = np.array(Average4)
Average5 = np.array(Average5)
Average10 = np.array(Average10)
Average20 = np.array(Average20)
nightmareAverage2 = np.array(nightmareAverage2)
nightmareAverage4 = np.array(nightmareAverage4)
nightmareAverage5 = np.array(nightmareAverage5)
nightmareAverage10 = np.array(nightmareAverage10)
nightmareAverage20 = np.array(nightmareAverage20)

# plot graphs

plt.plot(np.arange(40, 640, 40), SpeedUp2, label="Cutoff: 2")
plt.plot(np.arange(40, 640, 40), SpeedUp4, label="Cutoff: 4")
plt.plot(np.arange(40, 640, 40), SpeedUp5, label="Cutoff: 5")
plt.plot(np.arange(40, 640, 40), SpeedUp10, label="Cutoff: 10")
plt.plot(np.arange(40, 640, 40), SpeedUp20, label="Cutoff: 20")
plt.title("Local speed-up achieved per grid size tested")
plt.xlabel("Grid Size (cells)")
plt.ylabel("Speed-up factor (Time_Serial/Time_Parallel)")
plt.legend()
plt.savefig("src/LocalSpeedUp.png")
#plt.show()
plt.close()

plt.plot(np.arange(40, 640, 40), nightmareSpeedUp2, label="Cutoff: 2")
plt.plot(np.arange(40, 640, 40), nightmareSpeedUp4, label="Cutoff: 4")
plt.plot(np.arange(40, 640, 40), nightmareSpeedUp5, label="Cutoff: 5")
plt.plot(np.arange(40, 640, 40), nightmareSpeedUp10, label="Cutoff: 10")
plt.plot(np.arange(40, 640, 40), nightmareSpeedUp20, label="Cutoff: 20")
plt.title("Nightmare speed-up achieved per grid size tested")
plt.xlabel("Grid Size (cells)")
plt.ylabel("Speed-up factor (Time_Serial/Time_Parallel)")
plt.legend()
plt.savefig("src/NightmareSpeedUp.png")
#plt.show()
plt.close()

plt.plot(wildFireMixedSerial, Average2, label="Cutoff: 2")
plt.plot(wildFireMixedSerial, Average4, label="Cutoff: 4")
plt.plot(wildFireMixedSerial, Average5, label="Cutoff: 5")
plt.plot(wildFireMixedSerial, Average10, label="Cutoff: 10")
plt.plot(wildFireMixedSerial, Average20, label="Cutoff: 20")
plt.plot(wildFireMixedSerial, wildFireMixedSerial, label="Baseline (y = x)")
plt.title("Relative times to execute for each sequential cutoff")
plt.xlabel("Time_Serial (s)")
plt.ylabel("Time_Parallel (s)")
plt.legend()
plt.savefig("src/RelativeTime.png")
#plt.show()
plt.close()

plt.plot(nightmarewildFireMixedSerial, nightmareAverage2, label="Cutoff: 2")
plt.plot(nightmarewildFireMixedSerial, nightmareAverage4, label="Cutoff: 4")
plt.plot(nightmarewildFireMixedSerial, nightmareAverage5, label="Cutoff: 5")
plt.plot(nightmarewildFireMixedSerial, nightmareAverage10, label="Cutoff: 10")
plt.plot(nightmarewildFireMixedSerial, nightmareAverage20, label="Cutoff: 20")
plt.plot(nightmarewildFireMixedSerial, nightmarewildFireMixedSerial, label="Baseline (y = x)")
plt.title("Nightmare Relative times to execute for each sequential cutoff")
plt.xlabel("Time_Serial (s)")
plt.ylabel("Time_Parallel (s)")
plt.legend()
plt.savefig("src/NightmareRelativeTime.png")
#plt.show()
plt.close()