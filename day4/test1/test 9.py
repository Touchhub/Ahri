import time
start_time=time.time()
myD={1:'a',2:'b'}
for key,value in dict.items(myD):
    print(key,value)
    time.sleep(1)
end_time=time.time()
print("the func run is %s " %(end_time-start_time))