import threading

global timer

def fun_timer0():
    print 'hello 0'
    timer = threading.Timer(2, fun_timer1)
    timer.start()

def fun_timer1():
    print 'hello 1'
    timer = threading.Timer(2, fun_timer2)
    timer.start()

def fun_timer2():
    print 'hello 2'
    timer = threading.Timer(2, fun_timer3)
    timer.start()

def fun_timer3():
    print 'hello 3'
    timer = threading.Timer(2, fun_timer0)
    timer.start()

fun_timer0()
