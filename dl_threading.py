import subprocess
import pandas as pd
import threading
import time

urls_len = 111
PATH = r'/home/ear/project_ybu/v_datasets/VCSL/videos_multi_threads/'
urls = pd.read_csv("videos_url_uuid.csv")

def ykdl_dl(link, name):
    subprocess.run('ykdl -o {0} -O {1} {2}'.format(PATH, name, link), shell=True)

def multi_thread():
    threads = []
    for u in range(urls_len):
        threads.append(
            threading.Thread(target=ykdl_dl, args=(urls.iloc[u][0], urls.iloc[u][1],))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    multi_thread()
    end_time = time.time()
    print("用时：", end_time - start_time)