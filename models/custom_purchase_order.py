# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomPurchaseOrderLine(models.Model):
    _inherit = "purchase.order"

    custom_purchase_line = fields.One2many("custom.product.order", "custom_product_id", string="Product Name")


class ProductOrderDetails(models.Model):
    _name = "custom.product.order"
    _description = "Product Order Details"

    def _compute_total_price(self):
        for rec in self:
            rec.product_total = rec.quantity * rec.product_price

    quantity = fields.Integer(string='Quantity', default=1)
    product_price = fields.Float(string="Price")
    product_total = fields.Float(string="Total", compute="_compute_total_price")
    custom_product_id = fields.Many2one("purchase.order", string="Product")
    product_id = fields.Many2one("product.product", string="Product")

    @api.onchange("product_id")
    def onchange_product_id(self):
        for rec in self:
            rec.product_price = rec.product_id.list_price
