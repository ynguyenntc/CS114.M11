# **Nhận diện biển báo giao thông bằng Yolov5**

## **Cách xây dựng dataset:**
  * Đầu tiên nhóm sẽ đi thu thập ảnh biển báo giao thông được lấy từ nhiều góc chụp khác nhau ở nhiều địa điểm khác nhau. Sau đó dùng Roborflow để thống kê số lượng ảnh.
  * Do mỗi biển báo có số lượng ảnh chênh lệch nhau nhiều nên nhóm sẽ đi chụp thêm nhiều loại biển báo, xóa bớt các loại biển báo có quá nhiều hình ảnh. Với loại biển báo ít gặp thì nhóm sử dụng thêm nguồn dữ liệu từ internet và nhờ một số bạn ở địa phương khác chụp giúp.
  * Sau khi hoàn thành nhóm có 3,812 hình ảnh. Sau đó gắn label trên makesense.ai và tiếp đến đưa lên roboflow để chia tập dữ liệu thành 2 phần gồm 80% train và 20% valid.

## **Cách sử dụng dataset:**
  * Sau khi xây dựng dataset xong sẽ có một thư mục tên train_data trong đó có images và labels. Tiếp đó đưa thư mục train_data lên Drive và tiến hành huấn luyện dữ liệu theo file NhanDienBienBao.ipynb trên colab.
