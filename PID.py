#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PID():
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.p_error = 0.0
        self.i_error = 0.0
        self.d_error = 0.0
        # PID gain설정 (pid = PID(0.56, 0.0005, 0.12))
    def pid_control(self, cte):
        #cte = 화면의 중앙점과 좌우차선의 중점과의 차이
        self.d_error = cte - self.p_error # 현재 cte값과 이전 p_error 값의 차이
        self.p_error = cte # 현재 cte값
        self.i_error += cte

        return self.Kp*self.p_error + self.Ki*self.i_error + self.Kd*self.d_error

    #error = (rpos+lpos)/2 - width/2
    #p gain은 1 이하, I gain은 매우작게 0.001이하, D gain은 0.1이하로 설정
    # 통상적으로 P = 0.5, I = 0.0005, D = P_gain/10로 시작

    # 튜닝한 값에서 속도를 증가시키면 제어값 다시 설정필요함
    # 속도가 높으면 정착시간이 일어나지 않기에 I제어기 필요없
