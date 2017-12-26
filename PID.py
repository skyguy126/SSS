import time

class PID:

    def __init__(self, p, i, d, i_min, i_max):

        # multiplier constants: kp, ki, kd
        self.kp = p
        self.ki = i
        self.kd = d

        self.i_max = i_max
        self.i_min = i_min

        self.p = 0.0
        self.i = 0.0
        self.d = 0.0

        self.integrator = 0.0

        self.error = 0.0
        self.last_error = 0.0
        self.target_value = 0.0

        self.last_time = time.time()
        self.current_time = time.time()

    def update_pid(self, current_value):
        self.current_time = time.time()
        self.time_delta = self.current_time - self.last_time
        self.error = self.target_value - current_value

        self.p = self.kp * self.error
        self.integrator += self.error * self.time_delta

        if self.integrator > self.i_max:
            self.integrator = self.i_max
        elif self.integrator < self.i_min:
            self.integrator = self.i_min

        self.i = self.ki * self.integrator

        if self.time_delta > 0:
            self.d = self.kd * (self.error / self.time_delta)

        self.last_error = self.error
        self.last_time = self.current_time

    def get_pid(self):
        return self.p + self.i + self.d

    def get_target_value(self):
        return self.target_value

    def set_target_value(self, target_value):
        self.target_value = target_value

    def set_kp(self, kp):
        self.kp = kp

    def set_ki(self, ki):
        self.ki = ki

    def set_kd(self, kd):
        self.kd = kd

    def reset(self):
        self.p = 0.0
        self.i = 0.0
        self.d = 0.0
        self.integrator = 0.0
        self.error = 0.0
        self.last_error = 0.0
        self.target_value = 0.0
        self.last_time = time.time()
        self.current_time = time.time()
