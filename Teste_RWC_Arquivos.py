teste = open('testeTxt.html','r')
teste2 = open('testeExcel.xls','w')
teste3 = open('testeWord.docx','w')
teste4 = open('testeCSV.csv','w')
teste5 = open('testePython.py','w')

if (teste.read().isdigit()):
        teste = open('testeTxt.html', 'w')
        teste.write(input())
        teste.close()
elif (teste.read().isalpha()):
        teste = open('testeTxt.html', 'w')
        teste.write(str(input()))
        teste.close()
elif (teste.read().isdecimal()):
        teste = open('testeTxt.html', 'w')
        teste.write(float(input()))
        teste.close()
else:
    teste = open('testeTxt.html','w')
    teste.write(input())
    teste.close()


teste2.write(input())
teste3.write(input())
teste4.write(input())
teste5.write(input())


teste2.close()
teste3.close()
teste4.close()
teste5.close()