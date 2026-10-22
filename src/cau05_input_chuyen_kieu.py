
ma_may = input("Nhập mã máy: ")
print(f"-> Kiểu dữ liệu mã máy: {type(ma_may)}")

cong_suat_w_str = input("Nhập công suất (W): ")
print(f"-> Kiểu dữ liệu công suất trước khi chuyển: {type(cong_suat_w_str)}")

so_phut_str = input("Nhập số phút sử dụng: ")
print(f"-> Kiểu dữ liệu số phút trước khi chuyển: {type(so_phut_str)}")

don_gia_kwh_str = input("Nhập đơn giá điện/kWh: ")
print(f"-> Kiểu dữ liệu đơn giá trước khi chuyển: {type(don_gia_kwh_str)}")

cong_suat_w = float(cong_suat_w_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_kwh_str)

print("\n--- Sau khi chuyển đổi kiểu dữ liệu ---")
print(f"cong_suat_w: {type(cong_suat_w)}, so_phut: {type(so_phut)}, don_gia_kwh: {type(don_gia_kwh)}")

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print(f"\nKết quả tính toán với dữ liệu nhập vào:")
print(f"Mã máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} VND")