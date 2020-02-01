from peewee import *
import requests

# r = requests.get("https://api.bseindia.com/BseIndiaAPI/api/getScripHeaderData/w?Debtflag=&scripcode=500820&seriesid=")
# print 'r', r.json()

mydb = MySQLDatabase("stock_analysis", host="", port=3306, user="root", passwd="mohideen")
print mydb

class CommonModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mydb

class Company(CommonModel):
    comp_code = IntegerField(primary_key=True)
    nickname = TextField()
    full_name = TextField()
    isin = TextField()
    ipo_year = IntegerField()
    group = CharField()
    industry = CharField()
    index = TextField()

class ScrapCompData:
    comp = ["500820", "532215", "532977", "500034", "532454", "533278", "500180", "532281", "500182", "500696", "500010", "532174", "532187", "500209", "500875", "500247", "500510", "500520", "532500", "532555", "500312", "532898", "500325", "500112", "524715", "532540", "500570", "570001", "500470", "500295", "532648", "500400", "500440", "500295", "500103", "532155", "500087", "500257", "532712", "500390", "500124", "507685", "532921"]
    
    def compData(self):
        for i in self.comp:
            r = requests.get("https://api.bseindia.com/BseIndiaAPI/api/ComHeader/w?quotetype=EQ&scripcode={}&seriesid=".format(i)).json()
            d = {k.lower():v for k,v in r.items() if (len(k) > 4 or k == "ISIN") and k not in ("FaceVal", "Grp_Index")}
            d["comp_code"] = eval(d.pop("securitycode"))
            d["nickname"] = d.pop("securityid")
            # Company.create(**d)
            proc, iscreated = Company.get_or_create(comp_code=d['comp_code'], defaults= d)
            if not iscreated:
                for key in d:
                    print 'k',key 
                    setattr(proc,key,d[key])
                proc.save()


if __name__ == "__main__":
    cls = ScrapCompData()
    cls.compData()
    # print list(Company.select())
    # for i in Company.select():
    #   print 'i', i.__data__
    # mydb.connect()

