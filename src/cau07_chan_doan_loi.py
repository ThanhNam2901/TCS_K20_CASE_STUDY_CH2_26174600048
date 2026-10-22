ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
# Lỗi 1: Thiếu dấu ngoặc đóng ) ở câu lệnh print cuối cùng.
# Lỗi 2: input() trả về chuỗi, cần chuyển công suất sang kiểu số để tính toán.