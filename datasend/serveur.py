import xmlrpc.client
from flask import Flask, request, jsonify
from urllib.parse import parse_qs
import json

app = Flask(__name__)

@app.route('/device/save_log', methods=['POST'])
def recevoir_donnees():
    created_id=0
    odoo_service_name = 'odoo15'  # Update with the name of your Odoo service
    url = f'http://{odoo_service_name}:8069'
    db = 'DBBCS'
    username = 'bcs.lab.irrgation@gmail.com'
    password = 'BCSLABirrigation@&&'
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid  = common.authenticate(db, username, password, {})
    if uid:
        try:
            # Check if the content type is application/x-www-form-urlencoded
            if request.content_type == 'application/x-www-form-urlencoded':
                # Get the form data from the request
                form_data = request.get_data().decode('utf-8')
                # Parse the x-www-form-urlencoded data
                parsed_data = parse_qs(form_data)

                # Convert to a dictionary
                donnees_json = {key: value[0] for key, value in parsed_data.items()}
                if donnees_json["PID"] == "41":
                    models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
                    id_record=models.execute_kw(db, uid, password, 'res.sensor', 'search', [[['DID', '=', donnees_json["DID"]]]])

                    if id_record:
                        cles_a_garder = ["IMEI", "DID", "auth", "PID", "CHAN",
                        "MDR1", "MDS1", "MDT1", "MDR2", "MDS2", "MDT2", 
                        "MDR3", "MDS3", "MDT3", "MDR4", "MDS4", "MDT4", 
                        "MDR0", "MDS0", "MDT0", "MDR5", "MDS5", "MDT5", 
                        "MDR6", "MDS6", "MDT6", "MDR7", "MDS7", "MDT7", 
                        "MDR12", "MDS12", "MDT12", "MDR13", "MDS13", "MDT13", 
                        "MDR14", "MDS14", "MDT14", "MDR15", "MDS15", "MDT15", 
                        "MDR8", "MDS8", "MDT8", "MDR9", "MDS9", "MDT9", 
                        "MDR10", "MDS10", "MDT10", "MDR11", "MDS11", "MDT11"]

                        nouveau_dictionnaire = {cle: valeur for cle, valeur in donnees_json.items() if cle in cles_a_garder}
 
                        keytable=['IMEI', 'DID',  'auth', 'PID', 'CHAN',
                                'MDR1', 'MDS1', 'MDT1',
                                'MDR2', 'MDS2', 'MDT2',
                                'MDR3', 'MDS3', 'MDT3',
                                'MDR4', 'MDS4', 'MDT4']
                        vals = {}
                        for ancienne_cle, nouvelle_cle in zip(nouveau_dictionnaire.keys(), keytable):
                            vals[nouvelle_cle] = nouveau_dictionnaire[ancienne_cle]
                        
                        if vals["CHAN"]=="0,4":
                            vals["CHAN"]=1
                        elif vals["CHAN"]=="4,4":
                            vals["CHAN"]=2
                        elif vals["CHAN"]=="8,4":
                            vals["CHAN"]=3
                        elif vals["CHAN"]=="12,4":
                            vals["CHAN"]=4

                        if all(vals[key] == "0" for key in ["MDS1", "MDS2", "MDS3", "MDS4"]):
                            created_id=models.execute_kw(db, uid, password, 'res.data', 'create', [vals])
                            with open('data.txt', 'a') as file:
                                file.write(json.dumps(nouveau_dictionnaire, indent=4))
                                file.write('\n')
                                file.write(json.dumps(vals, indent=4))
                                file.write('\n')
                            return {
                                    "vals":vals,
                                    "created_id":created_id}
                        else:
                            with open('data.txt', 'a') as file:
                                file.write(json.dumps(nouveau_dictionnaire, indent=4))
                                file.write('\n')
                                file.write(json.dumps(vals, indent=4))
                                file.write('\n')
                            return {"error ": vals}
                else:
                    return "error DID"   
            else:
                return {'error': 'Invalid content type'}, 400
        except Exception as e:
            app.logger.error(f'Error processing request: {str(e)}')
            return {'error': 'Internal server error'}, 500

        return {'donnees': nouveau_dictionnaire,'created_id':created_id}
    else:
        return {'error': 'Invalid PWD and user'}, 400
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
