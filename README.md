# AI-Compression-AVSensorData

- **Contributors** : 강동묵, 장수현
- **Task** : 차량 센서 데이터의 압축 기술 구현



## Directory Layout

- **Data**
  - Sensor data
    - Data_link (AI 허브, Apollo, Ford, LYFT_Level_5, Pandaset)
  - BSM data
    - BSM sample
- **Compression Code**
  - lzma, zlib, bz2 compression code.py (for .txt data)
  - Binary to PCD.py
  - Voxelization, Reconstruction, ROI crop code.py (for .pcd data)




---
## Compression Code Description
- **lzma, zlib, bz2 compression code.py (for .txt data)** : 텍스트 데이터(CAN, GPS, BSM) 압축을 위한 3가지(lzma, zlib, bz2) 압축 알고리즘 구현 코드.
- **Binary to PCD.py** : Binary 형태로 되어있는 lidar 데이터를 .pcd 형태로 변환하는 코드.
- **Voxelization, Reconstruction, ROI crop code.py (for .pcd data)** : PCD 데이터의 압축을 위한 복셀화 및 복셀화가 적용된 데이터를 복원하기 위한 Reconstruction, PCD 내에서 원하는 구역만 Crop 할 수 있는 ROI crop 구현 코드.

---
# Environment
- Python 3.6.10
- Open3D 0.13.0
- numpy 1.18.2
- pandas 1.0.3
- zlib 1.2.11

---
# Result
### CAN Compression
![image](https://user-images.githubusercontent.com/57205953/146713387-fae02409-7890-49b6-befe-bf382b5719b8.png)

### GPS Compression
![image](https://user-images.githubusercontent.com/57205953/146713493-b6e7e00c-5a0b-40a8-b904-544dd17e62e6.png)

### BSM Compression
![image](https://user-images.githubusercontent.com/57205953/146713543-e0c2be31-3027-459a-81cc-47a1def02659.png)

### PCD Voxelization
![image](https://user-images.githubusercontent.com/57205953/146713609-0e9748a0-7d0d-41b6-ad85-f70607323a58.png)

### PCD object detection
![image](https://user-images.githubusercontent.com/57205953/146713674-52c747f2-dac7-4b24-9a75-c20aba954161.png)
