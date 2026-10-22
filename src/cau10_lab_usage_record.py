from datetime import datetime

# 1. Nhập các thông tin từ bàn phím theo đúng danh sách yêu cầu
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
thoi_gian_phut = float(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VND/kWh): "))

# 2. Tính toán các thông số điện năng và chi phí
dien_nang_kwh = cong_suat_w * thoi_gian_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 3. Sử dụng toán tử logic để kiểm tra điều kiện (Không dùng if)
tren_60_phut = thoi_gian_phut > 60

# 4. Lấy thời điểm ghi nhận hiện tại bằng datetime.now() và strftime()
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 5. Xuất kết quả ra màn hình chuẩn 100% theo định dạng mẫu trong đề bài
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {thoi_gian_phut:.0f} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")