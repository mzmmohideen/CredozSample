import json
import MySQLdb
from datetime import datetime, date


class DbConn(object):
	"""docstring for DbConn"""
		
	query = """select 
		nickName, res.emp_id, r.start_date, r.role, 
	    case
			when isnull(rd.dept) and r.role like "%Account%" then "Mgmt"
	        when isnull(rd.dept) and r.role like "%HR%" then "Talent Management"
	        when isnull(rd.dept) and r.role like "%Sys%" then "IT"
	        when isnull(rd.dept) and r.role like "%comp%" then "Comp"
	        when isnull(rd.dept) and r.role REGEXP 'software|developer|Programmer' then "SoftwareDev"
			when isnull(rd.dept) and r.role REGEXP 'Paint|Prep' then "Paint"
	        when isnull(rd.dept) and r.role REGEXP 'Matchmove|3D|MM|Tracking|Rotomation|Texturing' then "Matchmove"
	        when isnull(rd.dept) and r.role like "%Roto%" then "Roto"
	        when isnull(rd.dept) and r.role like "%Production%" then "Production"
	        when isnull(rd.dept) and r.role like "%PSB%" then "PSB"
	        else rd.dept end as der_dept
	    from shotbot_production.resource res 
	    join shotbot_production.role r on res.emp_id = r.emp_id
	    left join shotbot_production.role_details rd on rd.role = r.role where res.emp_id like "B%";
	"""

	def __init1__(self):
		self.conn = MySQLdb.connect(host='18.185.234.94', port=3306, user='Developer', passwd='Ted9#garish', db='shotbot_production')
		print self.connect()

	def dateFormat(self, inp):
		if isinstance(inp, date):
			return datetime.strftime(inp, "%Y-%m-%d")
		return inp

	def connect(self):
		out = []
		self.curr = self.conn.cursor()
		self.curr.execute(self.query)
		_data = self.curr.fetchall()
		header = [i[0] for i in self.curr.description]
		for i in _data[1:]:
			# out.append(dict(zip(header, i)))
			out.append({k:self.dateFormat(v) for k,v in zip(header, i)})
		return out

	def parseJson(self):
		print(json.load(open('data.json')))



if __name__ == "__main__":
	cls = DbConn()
	cls.parseJson()
	# cl
