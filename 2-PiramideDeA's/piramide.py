texto = f'''
    A
   AAA
  AAAAA
 AAAAAAA
AAAAAAAAA
'''

print(texto)

linea1 =[ "{0}{1}{2}{3}{4}".format(" "," "," "," ","A"),
"{0}{1}{2}{3}{4}{5}".format(" "," "," ","A","A","A"),
"{0}{1}{2}{3}{4}{5}{6}".format(" "," ","A","A","A","A","A"),
"{0}{1}{2}{3}{4}{5}{6}{7}".format(" ","A","A","A","A","A","A","A"),
"{0}{1}{2}{3}{4}{5}{6}{7}{8}".format("A","A","A","A","A","A","A","A","A")]

for i in linea1:
    print(i)