import requests,traceback
x=requests.get("https://static.haxagon.xyz/challenge-images/frequency-analysis-ct.txt").text
occ_f={}
for i in dict.fromkeys(x):
	occ_f[i]=x.count(i)
occ={}
f=open("lf.csv")
for i in f.readlines():
	try:
		if i.split(",")[0] in occ_f.keys():
			occ[i.split(",")[0]]=float(i.split(",")[1])
	except:	traceback.print_exc()
occ=sorted(occ.keys(),key=occ.get,reverse=True)
occ_f=sorted(occ_f.keys(),key=occ_f.get,reverse=True)
print(occ,occ_f)
a={}
for i in range(len(occ)):
	a[occ_f[i]=occ[i]
print(x.translate(a)[0:100])
