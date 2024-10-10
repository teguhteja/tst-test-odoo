from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env['material']
        self.supplier = self.env['res.partner'].create({
            'name': 'Test Supplier',
        })

    def test_create_material(self):
        material = self.Material.create({
            'code': 'M001',
            'name': 'Test Material',
            'type': 'fabric',
            'buy_price': 150,
            'supplier_id': self.supplier.id
        })
        self.assertEqual(material.code, 'M001')
        self.assertEqual(material.name, 'Test Material')
        self.assertEqual(material.type, 'fabric')
        self.assertEqual(material.buy_price, 150)
        self.assertEqual(material.supplier_id, self.supplier)

    def test_buy_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.Material.create({
                'code': 'M002',
                'name': 'Invalid Material',
                'type': 'jeans',
                'buy_price': 50,
                'supplier_id': self.supplier.id
            })