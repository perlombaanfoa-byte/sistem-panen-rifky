# panen.py

def input_data_panen():
    """Fungsi untuk memasukkan data dasar hasil panen."""
    print("=== Masukkan Data Panen Dasar ===")
    nama_tanaman = input("Nama Tanaman: ")
    jumlah_panen = float(input("Jumlah Panen (kg): "))
    tanggal = input("Tanggal Panen (YYYY-MM-DD): ")
    
    data_panen = {
        "tanaman": nama_tanaman,
        "jumlah_kg": jumlah_panen,
        "tanggal": tanggal
    }
    
    print("\nData panen berhasil dimasukkan!")
    return data_panen

if __name__ == "__main__":
    input_data_panen()

def buat_laporan_panen(data):
    """Fungsi untuk menampilkan ringkasan laporan hasil panen."""
    print("\n================================")
    print("      LAPORAN HASIL PANEN       ")
    print("================================")
    print(f"Tanaman      : {data.get('tanaman')}")
    print(f"Jumlah Panen : {data.get('jumlah_kg')} kg")
    print(f"Tanggal      : {data.get('tanggal')}")
    print("Status       : Laporan berhasil dibuat.")
    print("================================")

if __name__ == "__main__":
    contoh_data = {
        "tanaman": "Jagung",
        "jumlah_kg": 500.0,
        "tanggal": "2026-06-10"
    }
    buat_laporan_panen(contoh_data)
