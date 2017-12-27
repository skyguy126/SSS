import time, math
from PID import PID
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

def lookup(val):
    tmp = math.fabs(val)
    if tmp > 0.23:
        if val < 0:
            return -0.23
        else:
            return 0.23
    else:
        return val

if __name__ == "__main__":
    pid = PID(1.2, 5, 0.01, -5.0, 5.0)
    pid.set_target_value(0.0)

    value_list = []
    time_list = []
    input_list = []

    current_value = 0.0

    for i in xrange(0, 500):
        pid.update_pid(current_value)
        output = pid.get_pid()

        if i >= 50:
            pid.set_target_value(1)
        else:
            pid.set_target_value(0.0)

        print str(output)

        current_value += lookup(output)
        time.sleep(0.02)

        value_list.append(current_value)
        time_list.append(i)
        input_list.append(pid.get_target_value())

    plt.plot(time_list, value_list)
    plt.plot(time_list, input_list)
    plt.xlim((0, 500))
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('TEST PID')

    plt.grid(True)
    plt.show()
