# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomPurchaseOrder(models.Model):
    _inherit = "purchase.order"

    custom_product_line = fields.One2many("custom.product.order", "custom_product_id", string="Product Name")
    # custom_product = fields.Char(string="Name")
    # custom_product_id = fields.Many2one('purchase.order', string="Name")


class ProductOrderDetails(models.Model):
    _name = "custom.product.order"
    _description = "Product Order Details"

    quantity = fields.Integer(string='Quantity')
    product_price = fields.Float(string="Price")
    product_total = fields.Float(string="Total", compute="_compute_total_price")
    custom_product_id = fields.Many2one("purchase.order", string="Product")
    choose_product_id = fields.Many2one("product.product", string="Product")

    @api.onchange("choose_product_id")
    def onchange_choose_product_id(self):
        for i in self:
            i.product_price = i.choose_product_id.list_price

    def _compute_total_price(self):
        for i in self:
            i.product_total = i.quantity * i.product_price
