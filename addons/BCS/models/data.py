from odoo import models, fields, api

class Data(models.Model):
    _name = 'res.data'
    _description = 'Model for storing sensor readings'
 
    sensor = fields.Many2one('res.sensor', string='Capteur', ondelete='cascade')

     # Ajout des champs supplémentaires
    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)
    PID = fields.Char(string='Identifiant du parametre 41')
    DID = fields.Char(string='Identifiant du capteur')
    auth = fields.Char(string='Authentification')
    IMEI = fields.Char(string='Numéro d\'IMEI')
    CHAN = fields.Char(string='profondeur')
    
    MDR1 = fields.Float(string='Temperature')
    MDS1 = fields.Integer(string='status')
    MDT1 = fields.Integer(string='type')

    MDR2 = fields.Float(string='humidite')
    MDS2 = fields.Integer(string='status')
    MDT2 = fields.Integer(string='type')

    MDR3 = fields.Float(string='PH')
    MDS3 = fields.Integer(string='status')
    MDT3 = fields.Integer(string='type')

    MDR4 = fields.Float(string='salinité')
    MDS4 = fields.Integer(string='status')
    MDT4 = fields.Integer(string='type')

   
# ['IMEI', 'DID', 'auth', 'PID', 'CHAN',
#  'MDR1', 'MDS1', 'MDT1','MDR2', 'MDS2', 'MDT2','MDR3', 'MDS3', 'MDT3','MDR4', 'MDS4', 'MDT4']

    def action_website(self):
        return{
            'type':'ir.actions.act_url',
            'target': 'new',
            'url':'/my'
        }
    def action_edit(self):
        return{
            'type':'ir.actions.act_url',
            'target': 'new',
            'url':'https://www.youtube.com/watch?v=qdC1nfTOCvw'
        }
