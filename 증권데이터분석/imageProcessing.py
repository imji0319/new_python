#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 14:27:46 2021

@author: jihye
"""


# 1. 리퀘스트로 인터넷에서 이미지 파일 가져오기 

import requests 

url = 'https://mblogthumb-phinf.pstatic.net/MjAxODAxMjRfMjc3/MDAxNTE2Nzg1MjY3NTI4.iClImRAwoX8-kzJovtnOz7ZE4Ly1NUON2KBnw52oE64g.NUAM40ABoZO83pREyaOVEg4d1PZDBH9UBimIYj6IdXUg.JPEG.interpark_pet/grinning_happy_dog.jpg?type=w800'

r = requests.get(url, stream = True).raw

# 2. 필로로 이미지 보여주기 

from PIL import Image 

img = Image.open(r)
img.show()
img.save('src.png')

print(img.get_format_mimetype) # get_format_mimetype 속성 : 이미지의 정보 추출 

# 3. 'with ~ as 파일 객체:' 로 이미지 파일 복사 

BUF_size = 1024 # 한번에 읽어드릴 사이즈 

with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df : 
    while True :
        data = sf.read(BUF_size)
        
        if not data :
            break
        
        df.write(data)


# 4. SHA-256으로 파일 복사 
# 제대로 복사가 완료가 되었다면 두 파일의 내용이 동일하기 때문에 해시값 역시 동일해야 함 
import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())
    

print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))



# 5. 맷플롯립으로 이미지 가공
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


dst_img = mpimg.imread('dst.png')

### 의사 색상 적용 : 의사색상은 이미지의 색상 대비를 향상시켜서 데이터를 쉽게 시각화하는 용도로 사용 
pseudo_img = dst_img[:,:,0]


plt.suptitle('Image Processing', fontsize = 18)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122)
plt.title('PseudoColor Image')
plt.imshow(pseudo_img)

plt.show()

