import subprocess
# import multiprocessing
import pandas as pd


urls_len = 111
PATH = r'/home/ear/project_ybu/v_datasets/VCSL/videos/'
# num_process = 12
urls = pd.read_csv("videos_url_uuid.csv")


# def _map(task):
#     pool = multiprocessing.Pool(num_process)
#     pool.map(task)

def ykdl_dl(link, name):
    subprocess.run('ykdl -o {0} -O {1} {2}'.format(PATH, name, link), shell=True)


if __name__ == "__main__":
    print("hello!!!")
    for u in range(urls_len):
        # print(urls.iloc[0][1])
        video_url = urls.iloc[u][0]
        video_name = urls.iloc[u][1]
        # L = list(video_url, video_name)
        # _map(ykdl_dl(video_url, video_name))
        ykdl_dl(video_url, video_name)