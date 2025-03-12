# SampleETL

SampleETL là một dự án ETL (Extract, Transform, Load) đơn giản nhằm thực hiện việc thu thập, chuyển đổi và tải dữ liệu từ các nguồn khác nhau vào hệ thống lưu trữ.

## 🚀 Tính năng chính
- Trích xuất dữ liệu từ nhiều nguồn khác nhau (CSV, API, Database,...)
- Chuyển đổi dữ liệu theo các quy tắc định sẵn
- Tải dữ liệu vào hệ thống đích
- Hỗ trợ logging và xử lý lỗi

## 📂 Cấu trúc thư mục
```
SampleETL/
│── data/               # Thư mục chứa dữ liệu đầu vào
│── src/                # Thư mục chứa mã nguồn
│   │── extract.py      # Module trích xuất dữ liệu
│   │── transform.py    # Module xử lý và biến đổi dữ liệu
│   │── load.py         # Module tải dữ liệu vào hệ thống đích
│── config/             # Cấu hình dự án
│── requirements.txt    # Danh sách các thư viện cần thiết
│── README.md           # Tài liệu hướng dẫn
```

## 🔧 Cài đặt
1. Clone repository:
   ```bash
   git clone https://github.com/HoangCuong0811/SampleETL.git
   cd SampleETL
   ```
2. Tạo môi trường ảo và cài đặt thư viện:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên macOS/Linux
   venv\Scripts\activate     # Trên Windows
   pip install -r requirements.txt
   ```

## 🛠 Cách sử dụng
Chạy pipeline ETL:
```bash
python src/main.py
```
Hoặc có thể chạy từng bước riêng lẻ:
```bash
python src/extract.py
python src/transform.py
python src/load.py
```

## 📌 Yêu cầu hệ thống
- Python 3.x
- Các thư viện cần thiết được liệt kê trong `requirements.txt`

## 📜 Giấy phép
Dự án này được phát hành dưới giấy phép MIT. Xem chi tiết trong [LICENSE](LICENSE).

## 🤝 Đóng góp
Mọi đóng góp đều được hoan nghênh! Nếu bạn muốn đóng góp, hãy fork repository này và tạo pull request.

## 📬 Liên hệ
Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ qua email: hoangcuong0811@example.com.
