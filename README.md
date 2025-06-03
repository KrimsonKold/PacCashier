# Background Project
Andi, the owner of a large supermarket in Indonesia, aims to modernize his business by implementing a self-service cashier system. This system will allow customers to:
1. Independently input purchased items, quantities, and prices
2. Access the service remotely (enabling purchases from any location)
3. Streamline the checkout process without staff assistance

# Objective
1. Develop a Transaction Class
    - Create a system where each customer transaction is uniquely identifiable.
2. Implement Item Management
    - Allow customers to independently:
        - Add items (name, quantity, price) to their transaction.
        - Modify existing items (update names, quantities, or prices).
3. Enable Transaction Editing
    - Provide functionality to:
        - Remove individual items.
        - Fully reset transactions if needed.
4. Design Order Verification
    - Build a feature to:
        - Review all items in a clear, formatted display.
        - Validate input data (e.g., correct types, no missing values).
5. Automate Pricing Calculations
    - Calculate total costs with:
        - Real-time subtotals.
        - Tiered discounts (5%, 8%, or 10%) based on purchase amount.

# Flowchart
1. **Initialized Transaction** 
    - Create a new transaction instance using the `Transaction` class, passing the object variable as the unique identifier.
    - Example: TR04280525 = Transaction("Ndaru")
2. **Add Item(s)**
    - Use the  `add_item(*args)` method to add one or more items to the transaction.
    - Each item must be provided as a tuple in the format: (name, quantity, price_per_item)
    - Example:
        - Single item: `TR04280525.add_item(("Laptop", 1, 10000000))`
        - Multiple items: `TR04280525.add_item(("Mouse", 2, 250000), ("Keyboard", 1, 500000))`
3. **Update Items (Optional)**
    - Modify item details using the following methods:
        - `update_item_name(nama_item, update_nama_item)` → Renames an item.
        - `update_item_qty(nama_item, update_jumlah_item)` → Updates an item's quantity.
        - `update_item_price(nama_item, update_harga_item)` → Updates an item's unit price.
4. **Delete Items (Optional)**
    - Remove a specific item using `delete_item(nama_item)`.
    - Reset the entire transaction with `reset_transaction()`.
5. **Review Order**
    - Verify all items and their details using `check_order()`, which displays a formatted table.
6. **Calculate Total Price**
    - Finalize the transaction and compute the total amount using `total_price()`.
    - Applies automatic discounts based on the total purchase value:
        - 5% discount for purchases > Rp 200,000
        - 8% discount for purchases > Rp 300,000
        - 10% discount for purchases > Rp 500,000

# Code Function
1. The `Transaction` class represents a customer's shopping transaction with the following attributes:
    - `username`: Stores the customer's name as a unique identifier
    - `items`: Dictionary to track all purchased items with their details
    ```
    class Transaction:
        def __init__(self, username: str):
            """This shows a person's identity as an object attributes\n
            Purpose --> to be able to make a unique transaction ID for every person
            
            Args:
                self.username(): A person's name
            """
            self.username = username
            self.items = {}
    ```
2. The `add_item()` method accepts items in tuple format (name, quantity, price) with flexible input:
    - Handles single or multiple items in one call
    - Validates input format before processing
    - Stores items in dictionary structure for easy access
    ```
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
    ```
3. The `validate_item()` method serves as a helper function to:
    - Verify item existence before modification operations
    - Prevent errors in update/delete operations
    - Provide clear error messages for missing items.
    ```
    def validate_item(self, nama_item: str):
        """Checking if the item is in the dictionary before making changes"""
        try:
            _ = self.items[nama_item]
        except KeyError:
            raise Exception("Item tidak ditemukan!")
    ```
4. These three methods are dedicated to handle specific updates:
    1. `update_item_name()` - Modifies an item's name
    2. `update_item_qty()` - Changes item quantity
    3. `update_item_price()` - Adjusts item pricing

    All update methods:
    - First validate item existence
    - Ensure type consistency (quantity/price as integers)
    - Provide confirmation messages
    ```
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
    ```
5. These two methods are being used to cleanup:
    - `delete_item()` - Removes specific items
    - `reset_transaction()` - Clears entire transaction
    ```
    def delete_item(self, nama_item: str):
        """Deleting individual item alongside its quantity and price"""
        del self.items[nama_item]
        print(f"{nama_item} berhasil dihapus dari pesanan!")

    def reset_transaction(self):
        """Resetting the transaction, clearing all items alongside quantity and price"""
        self.items.clear()
        print("Semua item berhasil dihapus!")
    ```
6. The `check_order()` method provides:
    - Comprehensive input validation (empty values, data types)
    - Tabular display of all items using tabulate
    - Clear error reporting for data issues
    ```
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
    ```
6. The `total_price()` method features:
    - Automatic discount tier calculation:
        - 5% for 200K-300K
        - 8% for 300K-500K
        - 10% above 500K
    - Detailed breakdown of all items
    - Final total with applied discounts
    ```
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
    ```

# Test Case
1. Adding two items with `add_item(self, *args)`
![alt text](https://raw.githubusercontent.com/KrimsonKold/PacCashier/refs/heads/master/image/Test1.png)
2. Deleting an item with `delete_item(self, nama_item)`
![alt text](https://raw.githubusercontent.com/KrimsonKold/PacCashier/refs/heads/master/image/Test2.png) 
3. Resetting transactions with `reset_transaction(self)`
![alt text](https://raw.githubusercontent.com/KrimsonKold/PacCashier/refs/heads/master/image/Test3.png)
4. Showing the total price of all items with `total_price(self)`
![alt text](https://raw.githubusercontent.com/KrimsonKold/PacCashier/refs/heads/master/image/Test4.png)

# Conclusion 
This self-service cashier system successfully modernizes Andi's supermarket by providing an efficient, user-friendly solution for independent transactions. The Transaction class enables customers to manage their purchases seamlessly, from adding and modifying items to calculating discounts automatically. With robust validation and clear output formatting, the system ensures accuracy while reducing reliance on staff. The tiered discount feature further enhances customer satisfaction by rewarding higher purchases. Overall, this implementation streamlines the checkout process, making it accessible both in-store and remotely. For future improvements, this system could be enhanced by implementing persistent storage, allowing transaction data to be saved externally (e.g., in a database or file). This would ensure transactions remain accessible even after the program terminates or the session ends.
