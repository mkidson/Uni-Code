import time
import concurrent.futures

def do_something(seconds):
    print(f'Sleeping {seconds} seconds...')
    time.sleep(seconds)
    return f'Done sleeping {seconds}'

def conc():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs=[5,4,3,2,1]
        results=executor.map(do_something, secs)

        for result in results:
            print(result)

if __name__ == "__main__":
    t1=time.time()
    conc()
    t2=time.time()
    print(f'Time taken: {t2-t1:.3}s')