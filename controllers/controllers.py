# -*- coding: utf-8 -*-
# from odoo import http


# class Persona(http.Controller):
#     @http.route('/persona/persona/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/persona/persona/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('persona.listing', {
#             'root': '/persona/persona',
#             'objects': http.request.env['persona.persona'].search([]),
#         })

#     @http.route('/persona/persona/objects/<model("persona.persona"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('persona.object', {
#             'object': obj
#         })
