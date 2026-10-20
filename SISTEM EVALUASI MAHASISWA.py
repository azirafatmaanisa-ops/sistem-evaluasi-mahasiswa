tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))
kehadiran = float(input("Masukkan persentase kehadiran (%): "))

nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

print("\n===== HASIL EVALUASI MAHASISWA =====")
print(f"Nilai Akhir : {nilai_akhir:.2f}")
print(f"Kehadiran : {kehadiran:.2f}%")

if nilai_akhir >= 75 and kehadiran >= 80:

    if (
        nilai_akhir >= 85
        and kehadiran >= 90
        and nilai_akhir.is_integer()
        and int(nilai_akhir) % 2 == 0
    ):
        print("Status : LULUS DENGAN PREDIKAT")

    else:
        print("Status : LULUS")

else:
    print("Status : BELUM LULUS")