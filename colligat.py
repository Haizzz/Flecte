from yahoo_finance import Share
import json
import time
# pull data every day at 15:55 [Sydney], 13:55 [Perth]
from datetime import datetime
from threading import Timer

# x=datetime.today()
# y=x.replace(day=x.day+1, hour=13, minute=55, second=0, microsecond=0)
# delta_t=y-x

# secs=delta_t.seconds+1

# t = Timer(secs, stocks)
# t.start()
# companies | sort by industries
# banks
cba = Share("CBA.ax")
nab = Share("NAB.ax")
anz = Share("ANZ.ax")
wbc = Share("WBC.ax") # westpac
# retail
wow = Share("WOW.ax")
jbh = Share("JBH.ax") # jb hifi
wes = Share("WES.ax") # west farmer 
# misc
asx = Share("ASX.ax")
bhp = Share("BHP.ax")
ccl = Share("CCL.ax") # coca cola
dmp = Share("DMP.ax") # domino pizza
price = [cba.get_price(), nab.get_price(), anz.get_price(), wbc.get_price(), wow.get_price(), jbh.get_price(), wes.get_price(), asx.get_price(), bhp.get_price(), ccl.get_price(), dmp.get_price()]
volume = [cba.get_volume(), nab.get_volume(), anz.get_volume(), wbc.get_volume(), wow.get_volume(), jbh.get_volume(), wes.get_volume(), asx.get_volume(), bhp.get_volume(), ccl.get_volume(), dmp.get_volume()]
change = [cba.get_change(), nab.get_change(), anz.get_change(), wbc.get_change(), wow.get_change(), jbh.get_change(), wes.get_change(), asx.get_change(), bhp.get_change(), ccl.get_change(), dmp.get_change()]
print "ASX overall price:", asx.get_price()
# write to data.json
counter = 0
def appendData(name):
	with open('data.json', 'r+') as f:
		global counter
		json_data = json.load(f)
		json_data["price"][name].append(float(price[counter]))
		f.seek(0)
		f.write(json.dumps(json_data))
		f.truncate()
		json_data["volume"][name].append(float(volume[counter]))
		f.seek(0)
		f.write(json.dumps(json_data))
		f.truncate()
		json_data["change"][name].append(float(change[counter]))
		f.seek(0)
		f.write(json.dumps(json_data))
		f.truncate()
		json_data["lastChanged"] = time.strftime("%d/%m/%Y")
		f.seek(0)
		f.write(json.dumps(json_data))
		f.truncate()
		counter += 1

appendData("cba")
appendData("nab")
appendData("anz")
appendData("wbc")
appendData("wow")
appendData("jbh")
appendData("wes")
appendData("asx")
appendData("bhp")
appendData("ccl")
appendData("dmp")
print("prices:", price)
print("volume:", volume)
print("change:", change)
print (time.strftime("%d/%m/%Y"))
""" default data.json
{"volume":{"nab":[],"wes":[],"cba":[],"wow":[],"asx":[],"dmp":[],"ccl":[],"wbc":[],"bhp":[],"anz":[],"jbh":[]},"price":{"nab":[],"wes":[],"cba":[],"wow":[],"asx":[],"dmp":[],"ccl":[],"wbc":[],"bhp":[],"anz":[],"jbh":[]},"change":{"nab":[],"wes":[],"cba":[],"wow":[],"asx":[],"dmp":[],"ccl":[],"wbc":[],"bhp":[],"anz":[],"jbh":[]}}
"""