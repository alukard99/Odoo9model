# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ejemplo(models.Model):
#     _name = 'ejemplo.ejemplo'
#     _description = 'ejemplo.ejemplo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models, fields, api


class persona(models.Model):
    _name = 'persona.persona'
    _description = 'model persona'

    name = fields.Char('Id', required=True, unique=True)
    nombre = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono', required=True)

    dni = fields.One2one('persona.cliente', string='DNI')
    dni = fields.One2one('persona.trabajador', string='DNI')

class cliente(models.Model):
    _name = 'persona.cliente'
    _description = 'cliente'

    name = fields.Char('Id', required=True)
    fecha_alta = fields.Char(string='Fecha_alta', required=True)

    dni = fields.One2one('persona.trabajador', string='DNI')


class trabajador(models.Model):
    _name = 'persona.trabajador'
    _description = 'trabajador'

    name = fields.Char('Id', required=True)
    sueldo = fields.Char('Sueldo', required=True)
    horas = fields.Char('Horas', required=True)

    dni = fields.One2one('persona.persona', string='DNI')
    idtrabajador = fields.One2one('persona.propio', 'persona.ajeno', string='id_trabajadorp')


class propio(models.Model):
    _name = 'persona.propio'
    _description = 'trabajador propio'

    name = fields.Char('ID', required=True)

    id_trabajador = fields.One2one('persona.jefe', 'persona.administrativo', string='id_trabajadorp')


class jefe(models.Model):
    _name = 'persona.jefe'
    _description = 'jefe departamento'

    name = fields.Char('ID', required=True)
    trabajadores = fields.Integer(string='Trabajadores', required=True)
    id_trabajador = fields.One2many('persona.propio', string='id_trabajador')


class administrativo(models.Model):
    _name = 'persona.administrativo'
    _description = 'administrativo'

    name = fields.Char('ID', required=True)
    jefe = fields.Many2one('persona.jefe', string='jefe')
    id_trabajador = fields.One2one('persona.propio', string='id_trabajadorp')

class ajeno(models.Model):
    _name = 'persona.ajeno'
    _description = 'ajeno'

    name = fields.Char('ID', required=True)
    numempresa = fields.Char(string="num_empresa")

    idajeno = fields.One2one('persona.trabajador', string='idajeno')
    zona = fields.One2one('persona.basurero', 'persona.limpiador', string='zona')


class basurero(models.Model):
    _name = 'persona.basurero'
    _description = 'basurero'

    name = fields.Char('ID', required=True)

    idajeno = fields.One2one('persona.trabajador', string='idajeno')
    zona = fields.One2one('persona.ajeno', string='zona')


class limpiador(models.Model):
    _name = 'persona.limpiador'
    _description = 'limpiador'

    name = fields.Char('ID', required=True)

    idajeno = fields.One2one('persona.trabajador', string='idajeno')
    zona = fields.One2one('persona.ajeno', string='id_trabajadora')
