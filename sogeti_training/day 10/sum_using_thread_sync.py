import threading
def process_sum(chunk):
    result=sum(chunk)
    print(f'result is {result}')

data_chunks=[
    list(range(1000)),
    list(range(1000,2000)),
    list(range(2000,3000))
]

threads=[]
for chunk in data_chunks:
    thread=threading.Thread(target=process_sum,args=(chunk,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
