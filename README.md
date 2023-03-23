# JADWAL SHALAT KEMENAG
[![PyPI version](https://badge.fury.io/py/jadwal-shalat-kemenag.svg)](https://badge.fury.io/py/jadwal-shalat-kemenag)

Jadwal shalat untuk wilayah Indonesia berdasarkan data dari website [Ditjen Bimas Islam Kementerian Agama](https://bimasislam.kemenag.go.id/jadwalshalat).

## Install

```sh
pip install jadwal-shalat-kemenag
```

## Usage

Mendapatkan list daftar nama provinsi.

```python
from jadwal import jadwal_shalat

jws = jadwal_shalat.JadwalShalat()
listProv = jws.data_provinsi()

print(listProv)
```

Mendapatkan list nama kabupaten/kota.

```python
from jadwal import jadwal_shalat

jws = jadwal_shalat.JadwalShalat()
listProv = jws.data_provinsi()

# contoh ini menggunakan index list provinsi kode ID 13 (JAWA TENGAH)
prov_id = prov[13]['value']
listKota = jws.data_kabupaten_kota(prov_id)

print(listKota)
```

Mendapatkan list jadwal shalat di kabupaten/kota dalam satu bulan.

```python
from jadwal import jadwal_shalat

jws = jadwal_shalat.JadwalShalat()
listProv = jws.data_provinsi()

# contoh ini menggunakan index list provinsi 13 (JAWA TENGAH)
prov_id = listProv[13]['value']
listKota = jws.data_kabupaten_kota(prov_id)

# contoh ini menggunakan index list kabupaten/kota 7 (KAB. DEMAK)
# bulan 3 (Maret) tahun 2023
kota_id = listKota[7]['value']
jadwal = jws.jadwal_shalat(prov_id, kota_id, 3, 2023)

print(jadwal) # tampilkan jadwal shalat satu bulan
print(jadwal['data']['2023-03-24']) # tampilkan jadwal shalat tanggal 24 Maret 2023
```

Terima kasih.