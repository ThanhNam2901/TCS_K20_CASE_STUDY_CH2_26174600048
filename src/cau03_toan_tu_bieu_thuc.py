
tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(f"9. Thời gian: {so_gio} giờ và {so_phut_con_lai} phút.")

su_dung_lau = tong_phut > 60
print(f"10. Sử dụng lâu (>60p): {su_dung_lau} (Kiểu: {type(su_dung_lau)})")

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print(f"11. Dữ liệu hợp lệ: {du_lieu_hop_le}")

bt1 = 100 + 20 * 3    # Dự đoán: 160 (nhân trước cộng sau)
bt2 = (100 + 20) * 3  # Dự đoán: 360 (trong ngoặc trước)
print(f"12. Kết quả biểu thức 1: {bt1}")
print(f"    Kết quả biểu thức 2: {bt2}")