from flask_restful import Resource, reqparse
from models.msisdn import MsisdnModel
 

class Msisdns(Resource):
    def get(self):
        return{'msisdns': [msisdn.json() for msisdn in MsisdnModel.query.all()]}# Select * From msisdns
    
class Msisdn(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('mvno', type=str, required=True, help=" O campo não pode ser deixado em branco")
    atributos.add_argument('ddd')
    atributos.add_argument('msisdn_inicial')
    atributos.add_argument('imsi')

    def get(self, iccid):
        msisdn = MsisdnModel.find_msisdn(iccid)
        if msisdn:
            return msisdn.json()
        return{'message': 'Msisdn não encontrado'}, 404
    
    def post(self, iccid):
        if MsisdnModel.find_msisdn(iccid):
            return{"message": "Iccid '{}' já existe.".format(iccid)}, 400

        dados = Msisdn.atributos.parse_args()
        msisdn = MsisdnModel(iccid, **dados)
        try:
            msisdn.save_msisdn()
        except:
            return {'message': ' Um erro interno ocorreu ao salvar o msisdn'}, 500
        return msisdn.json()


    def put(self, iccid):
        dados = Msisdn.atributos.parse_args()
        msisdn_encontrado = MsisdnModel.find_msisdn(iccid)
        if msisdn_encontrado:
            msisdn_encontrado.update_msisdn(**dados)
            msisdn_encontrado.save_msisdn()
            return msisdn_encontrado.json(), 200
        msisdn = MsisdnModel(iccid, **dados)
        try:
            msisdn.save_msisdn()
        except:
            return {'message': ' Um erro interno ocorreu ao salvar o msisdn'}, 500
        return msisdn.json()
        
    def delete(self, iccid):
        msisdn = MsisdnModel.find_msisdn(iccid) 
        if msisdn:
            try:
               msisdn.delete_msisdn()
            except: 
                return {'message': 'Um erro ocorreu ao tentar deletar'}, 500 
            return {'message': 'Msisdn deletado'}
        return {'message': 'Msisdn não encontrado'}, 404