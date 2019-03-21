import datetime
import time


class AplusB(object):

    @classmethod
    def _a(cls, a, b, **kwargs):
        now_time = datetime.datetime.now()
        return a + b, now_time, kwargs


sum, call_time, kwargs = AplusB._a(1, 2)
print(sum, call_time)
time.sleep(2)
sum, call_time, kwargs = AplusB._a(3, 4)
print(sum, call_time)
