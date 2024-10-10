ERD (Entity Relationship Diagram) berdasarkan kebutuhan  
Berikut adalah deskripsi ERD yang sesuai dengan kebutuhan tersebut:

1. Entitas Utama:
   a. Material
   b. Supplier

2. Atribut Material:
   - id (Primary Key)
   - material_code
   - material_name
   - material_type (enum: Fabric, Jeans, Cotton)
   - material_buy_price
   - supplier_id (Foreign Key ke Supplier)

3. Atribut Supplier:
   - id (Primary Key)
   - name

4. Relasi:
   - Material memiliki relasi "belongs to" dengan Supplier (Many-to-One)

Berikut adalah representasi visual sederhana dari ERD tersebut:

```uml
+--------------------+            +------------+
|   Material         |            |  Supplier  |
+--------------------+            +------------+
| id                 |            | id         |
| material_code      |            | name       |
| material_name      |            +------------+
| material_type      |               |
| material_buy_price |               |
| supplier_id        |---------------+
+--------------------+
```

Penjelasan:
1. Material adalah entitas utama yang menyimpan informasi tentang material yang akan dijual.
2. Supplier adalah entitas yang menyimpan informasi tentang pemasok material.
3. Material memiliki foreign key `supplier_id` yang merujuk ke `id` pada entitas Supplier, menunjukkan hubungan Many-to-One (banyak material dapat berasal dari satu supplier).
4. `material_type` akan diimplementasikan sebagai field selection di Odoo dengan pilihan Fabric, Jeans, dan Cotton.
5. `material_buy_price` akan memiliki validasi untuk memastikan nilainya tidak kurang dari 100.


