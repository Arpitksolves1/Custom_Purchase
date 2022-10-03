# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CustomVendorBillLine(models.Model):
    _inherit = "account.move"

    custom_vendor_bill_line = fields.One2many("vendor.bill.line", "product_id", string="Product Name")


class VendorBillLine(models.Model):
    _name = 'vendor.bill.line'
    _description = "Vendor Bill Line"

    product_id = fields.Many2one('account.move', string='Product')
    product_purchase = fields.Many2one('product.product', string='Products')
    price = fields.Float(string='Price')
    quantity = fields.Float(string='Quantity')
    total = fields.Float(string='Total')

