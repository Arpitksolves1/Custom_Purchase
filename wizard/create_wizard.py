# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductWizard(models.TransientModel):
    _name = "product.wizard"
    _description = "Product Wizard"

    custom_product_id = fields.Many2one("product.product", String="Product")

    # name = fields.Char(string="Name")


