import pandas as pd
import numpy as np
import os
import zlib
import bz2
import lzma
import json

### CAN data Compression

file_path = "C:\\Users\\k_moo\\Google 드라이브\\KETI\\Data\\차량 보안 과제 데이터\\Can_network_data\\2020_챌린지 데이터\\[사이버 보안 챌린지 2020] 자동차 해킹공격방어_데이터셋\\예선\\학습용 데이터셋\\Raw"
file_name = "Cybersecurity_Car_Hacking_D_training-0.csv"

data = pd.read_csv(os.path.join(file_path, file_name))
display(data)

origin_data = ""
origin_id = ""
start_point = 0
comp_model = lzma  ### Select bz2, zlib, lzma

l = len(data)
len_li = list(data["DLC"][0:l])
# print(len_li)

origin_data = [origin_data + data["Data"][n].replace(" ", "") for n in range(l)]
origin_data = "".join(origin_data)

print("Origin_Len", len(origin_data))
# print("original_Data : {}".format(to))

compress_data = comp_model.compress(origin_data.encode(encoding='utf-8'))
print("\ncompressed_data_Len : {}".format(len(compress_data)))

decompress_data = comp_model.decompress(compress_data).decode("utf-8")
print("Decompress_data_Len : ", len(decompress_data))
# print("Decompress_Data : ", decompress_data)

origin_id = [origin_id + data["Arbitration_ID"][n] for n in range(l)]
origin_id = "".join(origin_id)

compress_id = comp_model.compress(origin_id.encode(encoding='utf-8'))
print("\ncompressed_id_Len : {}".format(len(compress_id)))

decompress_id = comp_model.decompress(compress_id).decode("utf-8")
print("Decompress_id_Len : ", len(decompress_id))
# print("Decompress_Data : ", decompress_data)

### Show splited data
# for k in len_li:

#     print("Origin_Data : {}, Len : {}".format(decompress_data[start_point:start_point+k*2], len(decompress_data[start_point:start_point+k*2])))

#     start_point = start_point+k*2

### Show splited id
# len_li_id = []
# [len_li_id.append(3) for i in range(l)]

# for k in len_li_id:

#     print("Origin_Data : {}, Len : {}".format(decompress_id[start_point:start_point+k], len(decompress_id[start_point:start_point+k])))

#     start_point = start_point+k

print("\ndata_len_space_saving :", (1 - (len(compress_data) / len(origin_data))))
print("id_len_compression_ratio :", (1 - (len(compress_id) / len(origin_id))))

te_data = data[0:l]

te_data.to_csv("before.csv", index=0)

te_data["Data"] = ""
te_data["Arbitration_ID"] = ""

te_data.to_csv("empty.csv", index=0)

te_data["Data"][0] = compress_data
te_data["Arbitration_ID"][0] = compress_id

# te_data.to_csv("after_compress.csv",index= 0)


### GPS data(주행) Compression

file_name = "gps.json"

comp_model = zlib ### Select bz2, zlib, lzma
gps_list = []
# file = os.path.join(path, file_name)
# print(file_name)

with open(file_name) as f:
    data = json.load(f)

print("json_example_data : ",data[0])


for k in range(len(data)):
    gps_list.append(str(data[k]["lat"]))


# print("Raw_data : ", gps_list)
concated_data = "".join(gps_list)
print("Concated_data : {} \nConcated_data_len : {}".format(concated_data, len(concated_data)))

compress_data = comp_model.compress(concated_data.encode(encoding='utf-8'))
print("\nCompressed_data : {} \nCompressed_data_Len : {}".format(compress_data, len(compress_data)))

decompress_data = comp_model.decompress(compress_data).decode("utf-8")
print("\nDecompress_data: {} \nDecompress_data_Len : {}" .format(decompress_data , len(decompress_data)))

print("\ndata_len_space_saving :" , (1-(len(compress_data) / len(concated_data))))



### GPS data(정차) Compression -> 데이터 임의 작성
test = []

for k in range(69):
    test.append("37.46692676990950637")

test = "".join(test)
print("test: {} \ntest_len : {}".format(test, len(test)))

print("Concated_data : {} \nConcated_data_len : {}".format(test, len(test)))

compress_data = comp_model.compress(test.encode(encoding='utf-8'))
print("\nCompressed_data : {} \nCompressed_data_Len : {}".format(compress_data, len(compress_data)))

decompress_data = comp_model.decompress(compress_data).decode("utf-8")
print("\nDecompress_data: {} \nDecompress_data_Len : {}".format(decompress_data, len(decompress_data)))

print("\ndata_len_space_saving :", (1 - (len(compress_data) / len(concated_data))))



### BSM Compression

comp_model = lzma ### Select bz2, zlib, lzma

file_path = "G:\내 드라이브\KETI\Data\예타2세부\BSM_sample"
file_name = "BSM sample.txt"

# data = pd.read_(os.path.join(file_path, file_name))
# display(data)

file = open(os.path.join(file_path, file_name), "r")
data = file.read()
# print(data)
print("Original_Data_len : ", len(data))

compress_data = comp_model.compress(data.encode(encoding='utf-8'))
print("\nCompressed_data : {} \nCompressed_data_Len : {}".format(compress_data, len(compress_data)))

decompress_data = comp_model.decompress(compress_data).decode("utf-8")
print("\nDecompress_data: {} \nDecompress_data_Len : {}" .format(decompress_data , len(decompress_data)))

print("\ndata_len_space_saving :" , (1-(len(compress_data) / len(data))))