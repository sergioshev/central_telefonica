# $Id: generate_area_codes.py,v 1.4 2012-03-19 14:20:46 sshevtsov Exp $
# Scritp que lee por entrada estandar el archivo codigos de area
# y genera por salida estandar la estructura hash al estilo python
# para utilizarla en los scripts. 
# Este script es de apoyo.
#

import csv
from sys import stdout


reader = csv.reader(open('/dev/stdin','rb'), delimiter='\t')

tree={}

def addValue(code,start,end,struct,value):
  try:
    struct[code[start]]['name']
  except KeyError:
    struct[code[start]]={'name' : None }
  if start<end:
    addValue(code,start+1,end,struct[code[start]],value)
  elif start==end:
    struct[code[start]]['name'] = value

def showData(struct,ident,coma):
  try:
    keys = list(struct.iterkeys())
  except AttributeError:
    if struct == None:
      quote=""
      utf8=""
    else:
      quote="'"
      utf8="u"
    stdout.write(utf8+quote+str(struct)+quote+coma)
    if coma == ',' : print
    return
  stdout.write("\n"+ident+"{\n")
  #stdout.write("\n"+ident+"{")
  for key in keys:
    #stdout.write("key="+key+"   keys[-1:]="+str(keys[-1:])+"   coma="+coma+"\n")
    stdout.write(ident+"  '"+key+"':")
    if key == keys[-1:][0]:
      nextcoma=""
    else: 
      nextcoma=","
    showData(struct[key],ident+"    ",nextcoma)
  stdout.write("\n"+ident+"}"+coma)
  if coma == ',' : print

def show(struct):
  stdout.write("areaCodesTree=")
  showData(struct,"    ","")
  print
  

for row in reader:
  code=row[0]
  area=row[1]
  try:
    prov=row[2]
  except IndexError, e:
    prot="no_prov"
  addValue(code,0,len(code)-1,tree,area)


show(tree)
      
