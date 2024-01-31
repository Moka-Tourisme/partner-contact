from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    url_base_test = fields.Char(string='URL Base Test', help="URL de base pour les tests")
    url_base_definitive = fields.Char(string='URL Base Définitive', help="URL de base définitive")