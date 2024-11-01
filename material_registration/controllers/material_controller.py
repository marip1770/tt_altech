# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route('/materials', type='http', auth='user', website=True)
    def list_materials(self, **kwargs):
        materials = request.env['tbl_material'].sudo().search([])
        return request.render('material_registration.material_list_template', {
            'materials': materials,
        })

    @http.route('/material/<model("tbl_material"):material>', type='http', auth='user', website=True)
    def material_details(self, material):
        return request.render('material_registration.material_details_template', {
            'material': material,
        })

    @http.route('/material/update/<int:material_id>', type='http', auth='user', methods=['POST'], csrf=False)
    def update_material(self, material_id, **kwargs):
        material = request.env['tbl_material'].sudo().browse(material_id)
        if material.exists():
            material_buy_price = float(kwargs.get('material_buy_price', 0))
            if material_buy_price >= 100:
                material.write({
                    'material_code': kwargs.get('material_code'),
                    'material_name': kwargs.get('material_name'),
                    'material_type': kwargs.get('material_type'),
                    'material_buy_price': material_buy_price,
                    'supplier_id': int(kwargs.get('supplier_id')),
                })
        return request.redirect('/materials')

    @http.route('/material/delete/<int:material_id>', type='http', auth='user', methods=['POST'], csrf=False)
    def delete_material(self, material_id):
        material = request.env['tbl_material'].sudo().browse(material_id)
        if material.exists():
            material.unlink()
        return request.redirect('/materials')
