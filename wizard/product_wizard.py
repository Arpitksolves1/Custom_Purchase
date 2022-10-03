# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductWizard(models.TransientModel):
    _name = "product.wizard"
    _description = "Product Wizard"

    custom_product_line = fields.One2many('custom.product.wizard', 'product_wiz_id', String="Product")

    @api.model
    def default_get(self, field_list=[]):
        res = super(ProductWizard, self).default_get(field_list)
        active_id = self._context.get('active_id')
        if active_id:
            purchase_id = self.env['purchase.order'].browse(active_id)
            lst = []
            for rec in purchase_id.order_line:
                lst.append((0, 0, {'product_id': rec.product_id.id, 'quantity': rec.product_qty,
                                   'product_price': rec.price_unit, 'product_total': rec.price_subtotal}))
            res['custom_product_line'] = lst
            return res

        ###########################################
        # Search Method
        # srch = self.env['purchase.order'].search([])
        #
        # for val in srch.custom_purchase_line:
        #     print(val.product_id.name)

        ############################################

    def action_save(self):
        active_id = self._context.get('active_id')
        print(active_id)
        if active_id:
            purchase_id = self.env['purchase.order'].browse(active_id)
            # print(product_browse_id)
            lst = []
            purchase_id.custom_purchase_line.unlink()
            for val in self.custom_product_line:
                lst.append((0, 0, {'product_id': val.product_id.id, 'quantity': val.quantity,
                                   'product_price': val.product_price, 'product_total': val.product_total}))
            purchase_id['custom_purchase_line'] = lst
            # return purchase_id


class ProductWizardLine(models.TransientModel):
    _name = "custom.product.wizard"
    _description = "Custom Product Wizard"

    quantity = fields.Float(string='Quantity', default=1)
    product_price = fields.Float(string="Price")
    product_total = fields.Float(string="Total")
    product_wiz_id = fields.Many2one("product.wizard", 'Products Wizard')
    product_id = fields.Many2one("product.product", string="Product")
