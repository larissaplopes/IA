fstreamout = open('C:\\Programa\\IA\\nucleos.txt', 'w')

nuc = "ATCG"

di = []
tri = []
quadra = []
quinta = []

for i in range(4): # for (i = 0; i < 4; ++i)
	for j in range(4): # for (j = 0; j < 4; ++j)
		di.append(nuc[i] + nuc[j])
		for k in range(4): # for (k = 0; k < 4; ++k)
			tri.append(nuc[i] + nuc[j] + nuc[k])
			for l in range(4): # for (l = 0; l < 4; ++l)
				quadra.append(nuc[i] + nuc[j] + nuc[k] + nuc[l])
				for m in range(4):
					quinta.append(nuc[i] + nuc[j] + nuc[k] + nuc[l] + nuc[m])
					
tamd = len(di)
tamt = len(tri)
tamq1 = len(quadra)
tamq2 = len(quinta)
tamnuc = len(nuc)

for i in range(tamnuc):
	fstreamout.write("@ATTRIBUTE " + nuc[i] + " NUMERIC" + "\n")
					
for i in range(tamd):
	fstreamout.write("@ATTRIBUTE " + di[i] + " NUMERIC" + "\n")
	
for i in range(tamt):
	fstreamout.write("@ATTRIBUTE " + tri[i] + " NUMERIC" + "\n")
	
for i in range(tamq1):
	fstreamout.write("@ATTRIBUTE " + quadra[i] + " NUMERIC" + "\n")
	
for i in range(tamq2):
	fstreamout.write("@ATTRIBUTE " +quinta[i] + " NUMERIC" + "\n")