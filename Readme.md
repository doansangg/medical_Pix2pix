- Version 1 với sinh dữ liệu cho một class:
trong đó class chọn là 
```bash
../labeled-images/upper-gi-tract/anatomical-landmarks/pylorus
```
chạy file train.py để train và test.py để test

DETAIL
- 1. Create dataset:
    - Tạo file image đầu vào,đầu ra:
        ```bash
        python3 Genarel_split.py 
        ```
        ```
        chú ý chỉnh sửa dường dẫn trong file Genarel_split.py 
        ```
- 2. Install requiments: torch >= 1.4
- 3. Train:
        ```
        python3 train.py
        ```
- 4. Test:
        ```
        python3 test.py
        ```
- 5. Result:
    - Kết quả cuối cùng lưu trong file results