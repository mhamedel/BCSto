from odoo import models, fields, api

class Zone(models.Model):
    _name = 'res.zone'
    _description = 'Modèle pour les zones'


    # create_from_notebook = fields.Boolean(string='Create from Notebook', compute='_compute_create_from_notebook', default=False)
    name = fields.Char(string='Nom de la zone' , compute='_compute_zone_name', store=True)
    label = fields.Char(string='Label', store=True,default=lambda self: self.name)
    farm = fields.Many2one('res.farm', string='Ferme', required=True, ondelete='cascade')
    sensors = fields.One2many('res.sensor', 'zone', string='Capteurs' )
    N_sensors = fields.Integer(string='Nombre des capteurs', compute='_compute_n_sensors', store=True)
    farm_name=fields.Char(string='Nom de la farm' , compute='_compute_farm_name', store=True )
    from_notebook = fields.Boolean(string='From Notebook', default=False)

    @api.depends('sensors')
    def _compute_n_sensors(self):
        for zone in self:
            zone.N_sensors = len(zone.sensors)

    @api.depends('farm')
    def _compute_farm_name(self):
        for zone in self:
            zone.farm_name = zone.farm.name


    @api.model
    def create(self, vals):
        from_notebook = vals.get('from_notebook', False)
        if from_notebook:
            return super(Zone, self).create(vals)
        else:
            zone = super(Zone, self).create(vals)
            zone._compute_zone_name()
            return zone

    @api.depends('farm')
    def _compute_zone_name(self):
        for zone in self:
            zone.name = f"{zone.farm.client.name}_Ferme_{zone.farm.client.N_farms}_Zone_{zone.farm.N_zones}"
 
  