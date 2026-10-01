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
