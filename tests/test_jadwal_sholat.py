from datetime import datetime
import pytz
import jadwal.jadwal_shalat as jws
import unittest
# import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '../'))


class TestJadwalShalat(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.jadwal_sholat = jws.JadwalShalat()
        cls.list_provinsi = cls.jadwal_sholat.data_provinsi()
        cls.provinsi_pertama = cls.list_provinsi[0]

    def test_data_provinsi(self):
        provinsi = self.list_provinsi
        # print('\n')
        # print(provinsi)
        # print('\n')
        self.assertGreater(len(provinsi), 0)
        self.assertIsNotNone(provinsi)
        self.assertGreater(len(provinsi), 0)

    def test_data_kabupaten_kota(self):
        provinsi_id = self.provinsi_pertama['value']
        kabkota = self.jadwal_sholat.data_kabupaten_kota(provinsi_id)
        # print('\n')
        # print(self.provinsi_pertama['text'])
        # print(kabkota)
        # print('\n')
        self.assertIsNotNone(kabkota)
        self.assertGreater(len(kabkota), 0)

    def test_jadwal_shalat(self):
        provinsi_id = self.provinsi_pertama['value']
        kabupaten_kota = self.jadwal_sholat.data_kabupaten_kota(provinsi_id)
        kabkota_id = kabupaten_kota[0]['value']
        # set timezone to Jakarta
        tz_Jakarta = pytz.timezone('Asia/Jakarta')
        # get current datetime with Jakarta timezone
        now = datetime.now(tz_Jakarta)
        # print current datetime in Jakarta timezone
        # print("Current date and time in Jakarta: ", now.strftime('%Y-%m-%d %H:%M:%S %Z'))
        bulan = now.month
        tahun = now.year
        jadwal = self.jadwal_sholat.jadwal_shalat(provinsi_id, kabkota_id, bulan, tahun)
        # print('\n')
        # print(kabupaten_kota[0])
        # print(jadwal)
        # print(jadwal['data'])
        # print(jadwal['data']['2023-03-24'])
        # print('\n')
        self.assertIsNotNone(jadwal)
        self.assertIn('data', jadwal)
        self.assertGreater(len(jadwal['data']), 0)


if __name__ == '__main__':
    unittest.main()
