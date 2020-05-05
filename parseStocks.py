import sys
from xml.dom import minidom

argv = sys.argv

#setup csv file
filename = argv[1].split(".")[0] + ".csv"
header=["exchange","symbol","company","volume","price","change"]
csvFile=open(filename,mode="w")
csvFile.write(",".join(header)+"\n")

#parse xhtml body -> table nodes
doc = minidom.parse(argv[1])
body = doc.getElementsByTagName('div')[34]
mainColumn=body.getElementsByTagName('div')[4]
tableNodes=mainColumn.getElementsByTagName('table')

#loop through table elements
for row in tableNodes[0].getElementsByTagName('tr'):
    rowData=[]
    #loop through row elements
    for box in row.getElementsByTagName('td'):
        #if the box has numbers, text, or is aligned right (check attributes) 
        if("num" in box.getAttribute("class") or "text" in box.getAttribute("class") or box.getAttribute("align")=="right"):
            #loop through its children nodes
            for element in box.childNodes:
                #add number elements to row data
                if element.nodeType == minidom.Node.TEXT_NODE and element.nodeValue!='\n':
                    num=element.nodeValue
                    num=num.replace("$","")
                    num=num.replace(",","")
                    if(len(num) > 3):
                        rowData.append(num)
                #add symbol and company name to row data
                if(element.nodeName=="a"):
                    for children in element.childNodes:
                        if children.nodeType==minidom.Node.TEXT_NODE:
                            company=children.nodeValue
                            rowData.append(company[company.find("(")+1:company.find(")")])
                            company=company.replace(company[company.find("(")-1:company.find(")")+1],"")
                            company=company.replace("\n","")
                            rowData.append(company)
    #if the row data isnt empty then write it the csv file
    if(rowData):
		print(rowData)
        csvFile.write("Nasdaq,"+",".join(rowData[:-1])+"\n")
#end loop/close file
csvFile.close