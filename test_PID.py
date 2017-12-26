import time
from PID import PID
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

if __name__ == "__main__":
    pid = PID(1.2, 1.0, 0.00001, -1.0, 1.0)
    pid.set_target_value(0.0)

    value_list = []
    time_list = []
    input_list = []

    current_value = 0.0

    for i in xrange(0, 100):
        pid.update_pid(current_value)
        output = pid.get_pid()

        if i >= 25:
            pid.set_target_value(1.0)
        else:
            pid.set_target_value(0.0)

        current_value += output

        time.sleep(0.02)

        value_list.append(current_value)
        time_list.append(i)
        input_list.append(pid.get_target_value())

    time_sm = np.array(time_list)
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
    value_smooth = spline(time_list, value_list, time_smooth)

    plt.plot(time_smooth, value_smooth)
    plt.plot(time_list, input_list)
    plt.xlim((0, 100))
    plt.ylim((min(value_list)-0.5, max(value_list)+0.5))
    plt.xlabel('time (s)')
    plt.ylabel('PID (PV)')
    plt.title('TEST PID')

    plt.ylim((1-0.5, 1+0.5))

    plt.grid(True)
    plt.show()
