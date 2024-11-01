from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.supplier = self.env['tbl_supplier'].create({'name': 'Test Supplier'})
        self.material = self.env['tbl_material'].create({
            'material_code': 'MAT001',
            'material_name': 'Material 1',
            'material_type': 'Fabric',
            'material_buy_price': 150,
            'supplier_id': self.supplier.id,
        })

    def test_create_valid_material(self):
        material = self.env['tbl_material'].create({
            'material_code': 'MAT001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'supplier_id': self.supplier.id,
        })
        self.assertEqual(material.material_name, 'Test Material')

    def test_material_buy_price_below_100(self):
        with self.assertRaises(ValidationError):
            self.env['tbl_material'].create({
                'material_code': 'MAT002',
                'material_name': 'Invalid Material',
                'material_type': 'cotton',
                'material_buy_price': 50,
                'supplier_id': self.supplier.id,
            })
    
    def test_list_materials(self):
        response = self.env['ir.http'].sudo().dispatch('/materials')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Material 1', response.data)

    def test_material_details(self):
        response = self.env['ir.http'].sudo().dispatch('/material/%d' % self.material.id)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Material 1', response.data)

    def test_update_material(self):
        response = self.env['ir.http'].sudo().dispatch('/material/update/%d' % self.material.id, {
            'material_code': 'MAT002',
            'material_name': 'Material Updated',
            'material_type': 'Jeans',
            'material_buy_price': 200,
            'supplier_id': self.supplier.id,
        }, method='POST')
        self.material.refresh()
        self.assertEqual(self.material.material_code, 'MAT002')
        self.assertEqual(self.material.material_name, 'Material Updated')

    def test_delete_material(self):
        response = self.env['ir.http'].sudo().dispatch('/material/delete/%d' % self.material.id, method='POST')
        self.assertFalse(self.env['tbl_material'].search([('id', '=', self.material.id)]))
