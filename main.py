from tabulate import tabulate as tb

class Transaction:
    def __init__(self, username: str):
        """This shows a person's identity as an object attributes\n
        Purpose --> to be able to make a unique transaction ID for every person
        
        Args:
            self.username(): A person's name
        """
        self.username = username
        self.items = {}

    def add_item(self, *args):
        """Adding items to self.item in form of dictionary.\n
        Can accept single or multiple items in one call. Item(s) needs to be called with tuple

        Args:
            Item name: str, quantity: int, price per item:int
        Example: 
            Multiple items: object.add_item(("Item1", 2, 20000), ("Item2", 3, 40000))
            Single item: object.add_item(("Item1", 2, 20000))
        """
        for item in args:
            if not isinstance(item, tuple) or len(item) != 3:
                raise ValueError("Each item must be a tuple of (name, quantity, price)")
            nama_item, jumlah_item, harga_per_item = item
            self.items[nama_item] = [jumlah_item, harga_per_item]
        print(f"Item yang dibeli adalah: {self.items}\n")
        
    def validate_item(self, nama_item: str):
        """Checking if the item is in the dictionary before making changes"""
        try:
            _ = self.items[nama_item]
        except KeyError:
            raise Exception("Item tidak ditemukan!")
    
    def update_item_name(self, nama_item: str, update_nama_item: str):
        """Updating item's name by replacing the old name with the new name"""
        self.validate_item(nama_item)
        self.items[update_nama_item] = self.items.pop(nama_item)
        print(f"Item {nama_item} berhasil di update menjadi {update_nama_item}")
        
    def update_item_qty(self, nama_item: str, update_jumlah_item: int):
        """Updating item's quantity by directly replacing the dictionary values"""
        self.validate_item(nama_item)
        self.items[nama_item][0] = update_jumlah_item
        print(f"Jumlah item {nama_item} berhasil di update menjadi {update_jumlah_item}")
    
    def update_item_price(self, nama_item: str, update_harga_item: int):
        """Updating item's price by directly replacing the dictionary values"""
        self.validate_item(nama_item)
        self.items[nama_item][1] = update_harga_item
        print(f"Harga item {nama_item} berhasil di update menjadi Rp. {update_harga_item}")

    def delete_item(self, nama_item: str):
        """Deleting individual item alongside its quantity and price"""
        del self.items[nama_item]
        print(f"{nama_item} berhasil dihapus dari pesanan!")

    def reset_transaction(self):
        """Resetting the transaction, clearing all items alongside quantity and price"""
        self.items.clear()
        print("Semua item berhasil dihapus!")

    def check_order(self):
        """Showing customer's order using Tabulate if there are no error in the input"""
        try:
            for key, value in self.items.items():
                if key is None or key == "":
                    raise ValueError("Nama item tidak boleh kosong!")
                if not isinstance(key, str):
                    raise TypeError("Tipe data harus dalam bentuk string!")
        
                for items in value:
                    if items is None:
                        raise ValueError("Nama item tidak boleh kosong!")
                    if not isinstance(items, int):
                        raise TypeError("Tipe data harus dalam bentuk integer!")
                    
        except (TypeError, ValueError, Exception) as e:
            print(f"Terdapat kesalahan input data!: {e}")
            raise
        

        list_tab = []
        headers_tab = ["No", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
        for key, value in self.items.items():
            multiply = value[0] * value[1]
            list_tab.append((key, value[0], value[1], multiply))
        print(tb(list_tab, 
                 headers=headers_tab, 
                 tablefmt="github", 
                 showindex=range(1, len(list_tab) + 1),
                 numalign="left"))
    
    def total_price(self):
        """Showing the total or final price customer has to pay, including the discount"""

        list_tab = []
        total = 0

        for key, value in self.items.items():
            multiply = value[0] * value[1]
            list_tab.append((key, value[0], value[1], multiply))

        for _, _, _, sum_items in list_tab:
            total = total + sum_items
        
        if total > 200_000 and total <= 300_000:
            print("Selamat! Anda mendapatkan diskon sebesar 5%")
            discount = 0.05
        elif total > 300_000 and total <= 500_000:
            print("Selamat! Anda mendapatkan diskon sebesar 8%")
            discount = 0.08
        elif total > 500_000:
            print("Selamat! Anda mendapatkan diskon sebesar 10%")
            discount = 0.10
        else:
            discount = 0

        return print(f"Total belanjaan anda adalah sebesar: Rp. {total * (1 - discount)}")

TR_17234 = Transaction("Andi")
TR_17234.add_item(("Ayam Goreng", 2, 20_000), ("Pasta Gigi", 3, 15_000))

