#%%
import requests
import time
import os
import concurrent.futures

#%%

img_urls = [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]
  
t1 = time.time()
print("Downloading images with single process")
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    print("Downloading..")
      
for img in img_urls:
    download_image(img)
  
t2 = time.time()
print(f'Single Process Code Took :{t2-t1} seconds')
print('*'*50)
  
t1 = time.time()
print("Downloading images with Multiprocess")
  
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    print(f"[Process ID]:{os.getpid()} Downloading..")
  
with concurrent.futures.ProcessPoolExecutor(3) as exe:
    exe.map(download_image, img_urls)
  
t2 = time.time()
print(f'Multiprocess Code Took:{t2-t1} seconds')
# %%
