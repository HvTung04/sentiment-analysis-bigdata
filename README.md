# Tổng quan

Đây là một dự án cho bài tập cuối kì bộ môn Big Data (INT3229 38) của trường Đại học Công Nghệ - Đại học Quốc gia Hà Nội.

Dự án được xây dựng dựa trên mã nguồn và tài liệu từ [Text Sentiment Analysis In Hadoop & Spark](https://github.com/Coursal/Text-Sentiment-Analysis-In-Hadoop-And-Spark). Đây là một dự án nghiên cứu và phát triển các ứng dụng phân tích cảm xúc văn bản sử dụng các framework Apache Hadoop và Apache Spark. Dự án này không chỉ cung cấp các mô hình phân loại cảm xúc mà còn phân tích hiệu suất của chúng trong môi trường tính toán song song và phân tán. Các kết quả và phương pháp từ dự án này đã được áp dụng và mở rộng để phù hợp với nhu cầu và mục tiêu của nhóm chúng tôi.

## Thông tin thành viên

| Họ và tên       | Mã sinh viên | Khóa               | Github                                         |
| --------------- | ------------ | ------------------ | ---------------------------------------------- |
| Trần An Thắng   | 22022525     | QH-2022-I/CQ-A-AI2 | [Trần An Thắng](https://github.com/angWindy)   |
| Hoàng Việt Tùng | 22022663     | QH-2022-I/CQ-A-AI2 | [Hoàng Việt Tùng](https://github.com/HvTung04) |
| Phạm Văn Trường | 22022564     | QH-2022-I/CQ-A-AI1 | [Truong](https://github.com/SmrfHdl)           |
| Vương Ngọc Quân | 22022616     | QH-2022-I/CQ-A-AI2 | [QuanVuong14](https://github.com/QuanVuong14)  |

## Text Sentiment Analysis In Hadoop & Spark

Dự án này phát triển mã nguồn cho phân tích cảm xúc văn bản sử dụng Hadoop và Spark, được thực hiện dưới sự hướng dẫn của giáo sư [Vasilis Mamalis](http://users.teiath.gr/vmamalis/) tại [Đại học Tây Attica](https://www.uniwa.gr/en/).

### Mục tiêu chính

- Nghiên cứu cơ bản về khai phá văn bản, phân tích cảm xúc, MapReduce, và tính toán song song/phân tán.
- Phát triển các ứng dụng phân tích cảm xúc sử dụng Apache Hadoop và Apache Spark.
- Phân tích kết quả về độ chính xác, thời gian thực thi, và khả năng mở rộng.
- Đưa ra kết luận và đề xuất mở rộng cho các ứng dụng.

### Ứng dụng đã phát triển

Các mô hình phân loại sử dụng 75% dữ liệu để huấn luyện và 25% để kiểm tra.

#### Sử dụng Hadoop

- Phiên bản đơn giản của Naive Bayes
- Phiên bản cải tiến của Naive Bayes (sử dụng TFIDF)

#### Sử dụng Spark

- Phiên bản đơn giản của Naive Bayes
- Phiên bản cải tiến của Naive Bayes (sử dụng TFIDF)
- Phiên bản đơn giản của SVM
- Phiên bản cải tiến của SVM (sử dụng TFIDF)
- Phiên bản Sử dụng mô hình học sâu DistilBERT

### Dữ liệu đầu vào

Sử dụng tập dữ liệu 1.6 triệu tweet để huấn luyện và kiểm tra.
