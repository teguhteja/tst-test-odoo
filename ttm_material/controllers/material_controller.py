from odoo import http
from odoo.http import request, Response
import logging
import json

_logger = logging.getLogger(__name__)

class MaterialController(http.Controller):

    # @http.route('/materials/all', website=True, auth='public',methods=['GET'])
    # def all_materials(self, **kwargs):
    #     return "Hello Materials All"

    @http.route('/materials', type='http', auth='public', methods=['GET'], website=True)
    def list_materials(self, **kwargs):
        materials = request.env['material'].search([])
        materials_list = []
        for material in materials:
            materials_list.append({
                'code': material.code,
                'name': material.name,
                'type': material.type,
                'buy_price': material.buy_price,
                'supplier_name': material.supplier_id.name,
            })
        # return request.render('ttm_material.material_list_template', {'materials': materials})
        return Response(json.dumps(materials_list), content_type='application/json', status=200)

    @http.route('/materials/create', type='json', auth='user', methods=['POST'], website=True, csrf=False)
    def create_material(self, **kwargs):
        _logger.info('Create Material: %s', kwargs)
        request.env['material'].create(kwargs)
        # return request.redirect('/materials')
        return {'success': True, 'message': 'Material created successfully'}


    @http.route('/materials/update/<int:material_id>', type='json', auth='public', methods=['POST'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        if not material.exists():
            return Response(
                json.dumps({'error': 'Material not found'}),
                content_type='application/json',
                status=404
            )
        material.write(kwargs)
        return Response(
            json.dumps({'success': True, 'message': 'Material updated successfully'}),
            content_type='application/json',
            status=200
        )

    @http.route('/materials/delete/<int:material_id>', type='json', auth='public', methods=['POST'])
    def delete_material(self, material_id, **kwargs):
        material = request.env['material'].browse(material_id)
        if not material.exists():
            return Response(
                json.dumps({'error': 'Material not found'}),
                content_type='application/json',
                status=404
            )
        material.unlink()
        return Response(
            json.dumps({'success': True, 'message': 'Material deleted successfully'}),
            content_type='application/json',
            status=200
        )