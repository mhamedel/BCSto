from odoo import http
from datetime import datetime
from datetime import timedelta
from dateutil import parser
from odoo.http import request
import random  # Import the random module
import json



class SensorWebController(http.Controller):

    
    @http.route('/edit_info', methods=['POST'], csrf=False)
    def process_form(self, **post):
        if http.request.httprequest.method == 'POST':  # Corrected method access
            env = http.request.env
            # Ensure the 'id' and 'name' fields are included in the POST data
            if 'id' in post :
                user_to_update = env['res.users'].browse(int(post['id']))
                record={
                'name':     post['first_name'],
                "login":    post['email'],

                "T_max":    post['T_max'],
                "T_min":    post['T_min'], 
                "H_max":    post['H_max'], 
                "H_min":    post['H_min'],
                "PH_max":   post['PH_max'],
                "PH_min":   post['PH_min'],
                "S_max":    post['S_max'],
                "S_min":    post['S_min'],
                }
                user_to_update.write(record)

                # image_file = http.request.httprequest.files.get('image')
                # if image_file:
                #     user_to_update = env['res.users'].browse(post['id'])
                #     user_to_update.write({'image_1920': image_file.read()}
        return http.request.redirect('/my')
    
        
    @http.route('/my', type='http', auth="user", website=True)
    def sensor_data_page(self, **kw):
        user = request.env.user
        user_image =  bool(user.partner_id.image_1920)
       # Rechercher les fermes liées à l'utilisateur connecté
        farms = request.env['res.farm'].search([('client', '=', user.id)])
        result = []
        for farm in farms:
            farm_info = {
            'farm_id': farm.id,
            'farm_name': farm.name,
            'farm_label': farm.label or farm.name,
            'zones': [{'zone_id': zone.id, 'zone_label': zone.label or zone.name } for zone in farm.zones],
             }
            result.append(farm_info)
            # result[0].['zones'].[0]['zone_id']
        first_farm_id=result[0]['farm_id'] if result else None
        first_farm_label=result[0]['farm_label']if result else None
       
        # session = http.request.session
        # message = session.get('message')
       
        message= "Les données ont été sauvegardées avec succès."

        return http.request.render('WSC.layouts', {
            'user': user,
            'user_image': user_image,
            'message':  message ,
            'result':result,
            'first_farm_id': first_farm_id,
            'first_farm_label': first_farm_label,
        })
   
    
    
    
    @http.route('/web/get_zones', type='http', auth="user", website=True)
    def get_zones(self, **kw):
        user = request.env.user
        farm_id = kw.get('farm_id')
        
        if farm_id:
            farm = request.env['res.farm'].sudo().browse(int(farm_id))
            if farm:
                zone_info = []
                for zone in farm.zones:
                    zone_info.append({
                        'id': zone.id,
                        'name': zone.name,
                        'label': zone.label or zone.name,
                    })
                    # zone_info les info des zone 
        return request.make_response(json.dumps(zone_info), headers=[('Content-Type', 'application/json')])

      
    @http.route('/web/get_sensor', type='http', auth="user", website=True)
    def get_sensor(self, **kw):
        user = request.env.user
        zone_id = kw.get('zone_id')
        choiselect = kw.get('choiselect')
        dateselect = kw.get('dateselect')

        startOfWeek = kw.get('startOfWeek')
        endOfWeek = kw.get('endOfWeek')
        firstDayOfMonth = kw.get('firstDayOfMonth')
        lastDayOfMonth = kw.get('lastDayOfMonth')
                                   
        # # Récupérez les identifiants des sensor associées à la zone
        zone_data = request.env['res.zone'].search([('id', '=', zone_id)]).read(['sensors'])
        sensors_data_DID = request.env['res.sensor'].browse(zone_data[0]['sensors']).read(['DID'])
        # # Récupérez les données des zones associées
        data=[]
        data.append({'temperature':'temperature','T_max':user.T_max,'T_min':user.T_min})
        data.append({'humidity':'humidity','H_max':user.H_max,'H_min':user.H_min})
        data.append({'pH':'pH','PH_max':user.PH_max,'PH_min':user.PH_min})
        data.append({'salite':'salite','S_max':user.S_max,'S_min':user.S_min})
        if choiselect == "1":
            if dateselect is not None:

                current_date = datetime.now().date()
                formatted_datetime=formatdatatim(dateselect)

                if formatted_datetime.date() == current_date:
                    end_of_day = datetime.now()
                    start_of_day = end_of_day - timedelta(hours=24)
                else:
                    end_of_day = formatted_datetime.replace(hour=23, minute=59, second=59)
                    start_of_day = formatted_datetime.replace(hour=0, minute=0, second=0)

                domain = [
                    ('DID', '=', '00000M5'),
                    ('create_date', '>=', start_of_day),
                    ('create_date', '<=', end_of_day),
                    ]
                sensor_data = request.env['res.data'].search_read(domain, ['CHAN', 'MDR1', 'MDR2', 'MDR3','MDR4','create_date'])

                grouped_data = {}
                for record in sensor_data:
                    chan_value = record['CHAN']
                    if chan_value not in grouped_data:
                        grouped_data[chan_value] = []

                    grouped_data[chan_value].append({
                        'create_date': record['create_date'].strftime('%Y-%m-%d %H:%M:%S'), 
                        'MDR1': record['MDR1'],
                        'MDR2': record['MDR2'],
                        'MDR3': record['MDR3'],
                        'MDR4': record['MDR4'],
                    })
            data.append({'data':grouped_data})

        if choiselect == "2":
            startOfWeek=formatdatatim(startOfWeek)
            endOfWeek=formatdatatim(endOfWeek)
            endOfWeek=endOfWeek+ timedelta(days=2)
            
            domain = [
                    ('DID', '=', '00000M5'),
                    ('create_date', '>=', startOfWeek),
                    ('create_date', '<=', endOfWeek),
                    ]
            sensor_data = request.env['res.data'].search_read(domain, ['CHAN', 'MDR1', 'MDR2', 'MDR3','MDR4','create_date'])

            grouped_data = {}
            for record in sensor_data:
                chan_value = record['CHAN']
                if chan_value not in grouped_data:
                    grouped_data[chan_value] = []

                grouped_data[chan_value].append({
                    'create_date': record['create_date'], 
                    'MDR1': record['MDR1'],
                    'MDR2': record['MDR2'],
                    'MDR3': record['MDR3'],
                    'MDR4': record['MDR4'],
                    })

            data_per_day = {}
            keys=grouped_data.keys()
            for chan in keys:
                data_per_day[chan] = {}
                i=0
                for day in range((endOfWeek - startOfWeek).days + 1):
                    current_day = startOfWeek + timedelta(days=day)
                    daily_records = [record for record in grouped_data[chan] if record['create_date'].date() == current_day.date()]

                    if daily_records:
                        avg_temperature = sum(record['MDR1'] for record in daily_records) / len(daily_records)
                        avg_humidity = sum(record['MDR2'] for record in daily_records) / len(daily_records)
                        avg_salinity = sum(record['MDR3'] for record in daily_records) / len(daily_records)
                        avg_ph = sum(record['MDR4'] for record in daily_records) / len(daily_records)

                        data_per_day[chan][str(i)] = {
                            'MDR1': avg_temperature,
                            'MDR2': avg_humidity,
                            'MDR3': avg_salinity,
                            'MDR4': avg_ph
                        }
                        i += 1
 
            data.append({'data':data_per_day})

        if choiselect == "3":
            firstDayOfMonth=formatdatatim(firstDayOfMonth)
            lastDayOfMonth=formatdatatim(lastDayOfMonth)
            lastDayOfMonth=lastDayOfMonth+ timedelta(days=1)
            
            domain = [
                    ('DID', '=', '00000M5'),
                    ('create_date', '>=', firstDayOfMonth),
                    ('create_date', '<=', lastDayOfMonth),
                    ]
            sensor_data = request.env['res.data'].search_read(domain, ['CHAN', 'MDR1', 'MDR2', 'MDR3','MDR4','create_date'])

            grouped_data = {}
            for record in sensor_data:
                chan_value = record['CHAN']
                if chan_value not in grouped_data:
                    grouped_data[chan_value] = []

                grouped_data[chan_value].append({
                    'create_date': record['create_date'], 
                    'MDR1': record['MDR1'],
                    'MDR2': record['MDR2'],
                    'MDR3': record['MDR3'],
                    'MDR4': record['MDR4'],
                    })

            data_per_day = {}
            keys=grouped_data.keys()
            for chan in keys:
                data_per_day[chan] = {}
                i=0
                for day in range((lastDayOfMonth - firstDayOfMonth).days + 1):
                    current_day = firstDayOfMonth + timedelta(days=day)
                    daily_records = [record for record in grouped_data[chan] if record['create_date'].date() == current_day.date()]

                    if daily_records:
                        avg_temperature = sum(record['MDR1'] for record in daily_records) / len(daily_records)
                        avg_humidity = sum(record['MDR2'] for record in daily_records) / len(daily_records)
                        avg_salinity = sum(record['MDR3'] for record in daily_records) / len(daily_records)
                        avg_ph = sum(record['MDR4'] for record in daily_records) / len(daily_records)

                        data_per_day[chan][str(i)] = {
                            'MDR1': avg_temperature,
                            'MDR2': avg_humidity,
                            'MDR3': avg_salinity,
                            'MDR4': avg_ph
                        }
                        i += 1

            data.append({'data':data_per_day})
        return request.make_response(json.dumps(data), headers=[('Content-Type', 'application/json')])
            
       


  
def formatdatatim(dateselect):
    if dateselect is not None:
        parsed_date = parser.parse(dateselect, fuzzy_with_tokens=True)
        parsed_date = parsed_date[0]
        formatted_date = parsed_date.strftime('%m/%d/%Y')
        formatted_datetime = datetime.strptime(formatted_date, "%m/%d/%Y")
        return formatted_datetime
    else:
        # Gérez le cas où dateselect est None (peut-être renvoyer None ou une autre valeur par défaut)
        return None