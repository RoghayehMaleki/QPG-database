f = open("markdown-table.md","r")
L = f.readlines()
V = []
for x in L:
    y = x.split("|")
    y.pop(0);
    y.pop(-1)
    V.append(y)
g = open("html-file.html","w+")

g.writelines("<html> \n <head> <meta http-equiv='Content-Type' content='text/html; charset=utf-8'>\n <title>Rank5SsinglegeneratorSITAs</title>\n </head> \n <body> ")
g.writelines("<table border='2'>")
for x in V:
	key = x[-1]
	if key == ' AS ':
		b = x[4]
		b = b.replace("[link]","")
		b = b.replace("(","'")
		b = b.replace(")","'")
		a = "<tr bgcolor='#b0ffb0'> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> <a href={4}>{4}</a> </td> <td> {5} </td>  </tr> \n".format(x[0],x[1],x[2],x[3],b,x[5])
		g.writelines(a)
	elif key == ' TA-xHL ':
		b = x[4]
		b = b.replace("[link]","")
		b = b.replace("(","'")
		b = b.replace(")","'")
		a = "<tr bgcolor='#b07478'> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> <a href={4}>{4}</a> </td> <td> {5} </td>  </tr>  \n".format(x[0],x[1],x[2],x[3],b,x[5])
		g.writelines(a)
	elif key == ' TA-xR ':
		b = x[4]
		b = b.replace("[link]","")
		b = b.replace("(","'")
		b = b.replace(")","'")
		a = "<tr bgcolor='#ffb0b0'> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> <a href={4}>{4}</a> </td> <td> {5} </td>  </tr>  \n".format(x[0],x[1],x[2],x[3],b,x[5])
		g.writelines(a)
	elif key == ' TA ':
		b = x[4]
		b = b.replace("[link]","")
		b = b.replace("(","'")
		b = b.replace(")","'")
		a = "<tr bgcolor='#6a6ad4'> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> <a href={4}>{4}</a> </td> <td> {5} </td>  </tr>  \n".format(x[0],x[1],x[2],x[3],b,x[5])
		g.writelines(a)
	elif key == ' TA-xIM ':
		b = x[4]
		b = b.replace("[link]","")
		b = b.replace("(","'")
		b = b.replace(")","'")
		a = "<tr bgcolor='pink'> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> <a href={4}>{4}</a> </td> <td> {5} </td>  </tr>  \n".format(x[0],x[1],x[2],x[3],b,x[5])
		g.writelines(a)
	elif key == ' F ':
		b = x[4]
		b = b.replace("[link]","")
		b = b.replace("(","'")
		b = b.replace(")","'")
		a = "<tr bgcolor='#e8acb6'> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> <a href={4}>{4}</a> </td> <td> {5} </td>  </tr>  \n".format(x[0],x[1],x[2],x[3],b,x[5])
		g.writelines(a)
	elif key == 'O':
		b = x[4]
		b = b.replace("[link]","")
		b = b.replace("(","'")
		b = b.replace(")","'")
		a = "<tr bgcolor='#d16fd6'> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> <a href={4}>{4}</a> </td> <td> {5} </td>  </tr>  \n".format(x[0],x[1],x[2],x[3],b,x[5])
		g.writelines(a)
	elif key == 'Existence':
		a = "<tr> <td> {0} </td> <td> {1} </td> <td> {2} </td> <td> {3} </td> <td> {4} </td> <td> {5} </td>  </tr>  \n".format(x[0],x[1],x[2],x[3],x[4],x[5])
		g.writelines(a)
g.writelines("</table> \n  </body> \n </html>")
g.close()
