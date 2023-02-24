from sql_alchemy import banco

class MsisdnModel(banco.Model):
    __tablename__ = 'msisdns'

    iccid = banco.Column(banco.Integer, primary_key=True)
    mvno = banco.Column(banco.String(80))
    ddd = banco.Column(banco.Integer)
    msisdn_inicial = banco.Column(banco.Integer)
    imsi = banco.Column(banco.Integer)

    def __init__(self, iccid, mvno, ddd, msisdn_inicial, imsi):
        self.iccid = iccid
        self.mvno = mvno
        self.ddd = ddd 
        self.msisdn_inicial = msisdn_inicial 
        self.imsi = imsi 

    def json(self):
        return {
            'iccid': self.iccid,
            'mvno': self.mvno,
            'ddd': self.ddd,
            'msisdn_inicial': self.msisdn_inicial,
            'imsi': self.imsi

        }
    
    @classmethod
    def find_msisdn(cls, iccid):
        msisdn = cls.query.filter_by(iccid=iccid).first()
        if msisdn:
            return msisdn
        return None

    def save_msisdn(self):
        banco.session.add(self)
        banco.session.commit()
        
    def update_msisdn(self, mvno, ddd, msisdn_inicial, imsi):
        self.mvno = mvno
        self.ddd = ddd 
        self.msisdn_inicial = msisdn_inicial 
        self.imsi = imsi

    def delete_msisdn(self):
        banco.session.delete(self)
        banco.session.commit()