import time
import sched
import logging
from config import Config
from dailyTask import DailyTask
from minuteTask import MinuteTask


def perform(fun, interval):
    s.enter(interval, 0, perform, (fun, interval))
    fun()


def delay_minute():
    # calculate delay to one minute
    second = int(time.strftime("%S", time.localtime()))
    return 60 - second


def delay_day():
    # calculate delay to one day
    localtime = time.localtime()
    hour = int(time.strftime("%H", localtime))
    minute = int(time.strftime("%M", localtime))
    second = int(time.strftime("%S", localtime))
    return (24 - hour - 1) * 3600 + (60 - minute - 1) * 60 + (60 - second)


if __name__ == "__main__":
    # format of logging and time
    fmt = "%(asctime)-15s %(levelname)s\t\t%(message)s"
    date_fmt = "%m-%d %H:%M"
    formatter = logging.Formatter(fmt, date_fmt)
    sh = logging.StreamHandler(stream=None)
    sh.setLevel(logging.INFO)
    sh.setFormatter(formatter)
    logger = logging.getLogger("Server")
    logger.setLevel(logging.INFO)
    logger.addHandler(sh)
    # Scheduler
    s = sched.scheduler(time.time, time.sleep)
    # enter scheduler
    t1 = DailyTask(logger)
    t2 = MinuteTask(logger)
    s.enter(delay_day(), 0, perform, (t1.run, t1.interval))
    s.enter(delay_minute(), 0, perform, (t2.run, t2.interval))
    # run
    logger.info("Started...")
    Config.refresh()
    s.run()
