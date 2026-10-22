
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("--- Chạy lần 1 (so_phut = 90) ---")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh - Kiểu dữ liệu: {type(dien_nang_kwh)}")
print(f"Chi phí điện: {chi_phi} VND - Kiểu dữ liệu: {type(chi_phi)}")

so_phut = 60
dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh

print("\n--- Chạy lần 2 (so_phut = 60) ---")
print(f"Điện năng mới: {dien_nang_kwh_moi} kWh")
print(f"Chi phí mới: {chi_phi_moi} VND")
print("So sánh: Khi thời gian giảm từ 90 phút xuống 60 phút, điện năng tiêu thụ giảm từ 0.375 kWh xuống 0.25 kWh và chi phí giảm từ 1125.0 VND xuống 750.0 VND.")