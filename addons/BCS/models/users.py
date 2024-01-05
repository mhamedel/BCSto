from odoo import api, models, fields

class Clients(models.Model):
    _inherit = 'res.users'
    _description = 'bcs users'
   
   
    farms = fields.One2many('res.farm', 'client', string='Fermes')
    N_farms = fields.Integer(string='Nombre des Farms', compute='_compute_n_farms', store=True)

    T_max = fields.Integer(string='T max', store=True,default=37)
    T_min = fields.Integer(string='T min', store=True,default=10)

    H_max = fields.Integer(string='H max', store=True,default=37)
    H_min = fields.Integer(string='H min', store=True,default=10)

    PH_max = fields.Integer(string='PH max', store=True,default=37)
    PH_min = fields.Integer(string='PH min', store=True,default=10)

    S_max = fields.Integer(string='S max', store=True,default=37)
    S_min = fields.Integer(string='S min', store=True,default=10)

    
    @api.depends('farms')
    def _compute_n_farms(self):
        for user in self:
            user.N_farms = len(user.farms)


    def print_sample_report(self):
        return self.env.ref('BCS.action_report_user').report_action(self)
    

    