def test_pembayaran_keranjang():
    harga_barang = 50000
    diskon = 10000
    total_bayar = harga_barang - diskon
    
    
    assert total_bayar == 50000, "Harga total setelah diskon tidak sesuai!"