import time

def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print(f"{func.__name__} function executed in {end_time-start_time} seconds")
    return wrapper

@execution_time
def sum_num():
    sum =0
    for i in range(1,1000000):
        sum+=i
    print(sum)   
sum_num()    

