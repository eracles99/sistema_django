import openpyxl
import csv
from django.db import connection
import pymysql

def carga_masiva(conn,list,semestre):
    cur = conn.cursor()
    Long=len(list)
    for i in range(Long):
        if(i==0):
            print(list[i][0])
            print(list[i][2])
            CatDocen=list[i][0]
            nombreDoc=list[i][2]
            Arg_CatDoc=(CatDocen,nombreDoc)
            #---migrations insert CatDocente
            cur.callproc('sp_migracionDocente',Arg_CatDoc)
            #---migrations insert Docente
        else:
            nombreDoc =list[0][2]
            tipocurso=list[i][4]
            codeCurso=list[i][0]
            nombre=list[i][2]
            carrera=list[i][1]
            Grupo=list[i][5]
            creditos=list[i][3]
            HT=list[i][6]
            HP=list[i][7]
            dia1=list[i][8]
            HrInicio=list[i][9]
            HrFin=list[i][10]
            AULA=list[i][11]
            args=(dia1,)
            cur.callproc('sp_migraDia',args)
            args_MIGRACION_MASIVA=(nombreDoc,tipocurso,codeCurso,nombre,carrera,Grupo,creditos,HT,HP,dia1,HrInicio,HrFin,AULA,semestre)
            cur.callproc('sp_migracion_masiva',args_MIGRACION_MASIVA)
            #print(list[i][k])
    conn.commit()
    cur.close()
def Normalizador(list):
    NewList=[]
    list[0][3]='CRED'
    for subList in list:
        #print("+++++++++++++++++++++++++++++SUBLIST++++++++++++++++++")
        #print(subList)
        lisCa0=subList[0]
        lisca1=subList[1]  
        if(lisCa0.find("/")>1):
            sublist0=lisCa0.split("/")
            sublist1=lisca1.split("/")
            for i in range(len(sublist0)):
                New=[]
                New.append(sublist0[i])
                New.append(sublist1[i])
                for k in range(2,13):
                    New.append(subList[k])
                NewList.append(New)
                
            #print(subList[0])
            #print(sublist0)
            #print(sublist1)
        else:
            NewList.append(subList)#'''
    return NewList
def Validador(Datos,rowII,rowIF):
    list=[]
    for fila in Datos['C'+str(rowII):'O'+str(rowIF)]:
        #print([datos.value for datos in fila])
        #print("Contdor:",K)
        list.append([datos.value for datos in fila])
        if(list[0][0] is None or list[0][0]==''):
            return False
        else: 
            return True
def Trozador(list,rowII,rowIF,Datos,conn,semestre):
    Condicion=True
    vacio=0
    k=0
    #list=[]
    mensaje=Validador(Datos,rowII,rowIF)
    print("def trozador:",mensaje,rowII,rowIF)
    if(mensaje==True):
        while(Condicion==True):
            #print("test While")
            #print('prueba ENTRANTE while')
            #print("WHILE rowII,rowII:",rowII,rowIF) 
            for fila in Datos['C'+str(rowII):'O'+str(rowIF)]:
                #print("For rowII,rowII:",rowII,rowIF)
                #print([datos.value for datos in fila])
                #Sublist=[]
                list.append([datos.value for datos in fila])
                #Sublist=[datos.value for datos in fila]
                #print("valor K:",k)
                #print("VALORElist[k][0] :",list[k][0])
                #print("----------------------------------------------------------------------tamaño por list:",len(list))
                #caracter=list[k][0]
                #print(Sublist)
                #print("vacio:",vacio)
                if(list[k][0] is None or list[k][0]==''):
                    #print("----------------------------------------------------------------------tamaño por list:",len(list))
                    #ultimo=len(list)-1
                    #print("valor aeliminar de lista:",ultimo)
                    #list.pop()
                    #print("PRUEBA DE NONE")
                    #print("prueba:",list[k][1])
                    vacio+=1
                if(vacio>1):
                    if(vacio<4):
                        if(list[k][0] is None or list[k][0]=='') :
                            Condicion=True
                            #vacio+=1
                        else:
                            vacio+=1
                            Condicion=False
                    else:
                        Condicion=False

              
                k+=1
                rowII+=1
                rowIF+=1                
        if(vacio>2):
            #print("VACIO :",vacio)
            del list[-(vacio):]
            list=Normalizador(list)
            carga_masiva(conn,list,semestre)
            return list,rowII-1,rowIF-1,True
        else:
            #print("Vacio en return else:",vacio)
            del list[-(vacio+1):]
            list=Normalizador(list)
            carga_masiva(conn,list,semestre)
            return list,rowII,rowIF,True
    return list,rowII-1,rowIF-1,False

def main_carga(exel,semestre):
    book=openpyxl.load_workbook(exel,data_only=True)
    Datos=book.active
    conn = pymysql.connect(host='localhost', user='root', password='', database='dbsilabos', charset='utf8mb4')
    rowII=3
    rowIF=3
    list=[]
    mensaje=True
    while(mensaje==True):
        list=[]
        list,rowII,rowIF,mensaje=Trozador(list,rowII,rowIF,Datos,conn,semestre)

exel='C:\\Users\\angel\\Downloads\\reporte carga academica.xlsx'
semestre='2021-II'
main_carga(exel,semestre)
'''list,rowII,rowIF,mensaje=Trozador(list,rowII,rowIF,Datos,conn)
print(list)
print("mensaje:",mensaje,rowII)
print("longitud de ista:",len(list))#'''
#print("***********************************************")
#----Insercion BD-----------------
#--conectar a bd
    #from django.db import co
'''conn = pymysql.connect(host='localhost', user='root', password='', database='dbsistema', charset='utf8_general_ci')
cur = conn.cursor()
Long=len(list)
for i in range(Long):
    if(i==0):
        print(list[i][0])
        print(list[i][2])
        CatDocen=list[i][0]
        nombreDoc=list[i][2]
        Arg_CatDoc=(CatDocen,nombreDoc)
        #---migrations insert CatDocente
        cur.callproc('sp_migracionDocente',Arg_CatDoc)
        #---migrations insert Docente
    else:
        nombreDoc =list[0][2]
        tipocurso=list[i][4]
        codeCurso=list[i][0]
        nombre=list[i][2]
        carrera=list[i][1]
        Grupo=list[i][5]
        creditos=list[i][3]
        HT=list[i][6]
        HP=list[i][7]
        dia1=list[i][8]
        HrInicio=list[i][9]
        HrFin=list[i][10]
        AULA=list[i][11]
        args_MIGRACION_MASIVA=(nombreDoc,tipocurso,codeCurso,nombre,carrera,Grupo,creditos,HT,HP,dia1,HrInicio,HrFin,AULA)
        cur.callproc('sp_migracion_masiva',args_MIGRACION_MASIVA)
        #print(list[i][k])
conn.commit()
cur.close()#'''
#lisCa=cadena.split("/")
#s.find("/")  # Retorna la primera ocurrencia.
'''NewList=[]
list[0][3]='CRED'
for subList in list:
    print("+++++++++++++++++++++++++++++SUBLIST++++++++++++++++++")
    #print(subList)
    lisCa0=subList[0]
    lisca1=subList[1]  
    if(lisCa0.find("/")>1):
        sublist0=lisCa0.split("/")
        sublist1=lisca1.split("/")
        for i in range(len(sublist0)):
            New=[]
            New.append(sublist0[i])
            New.append(sublist1[i])
            for k in range(2,13):
                New.append(subList[k])
            NewList.append(New)
            
        #print(subList[0])
        #print(sublist0)
        #print(sublist1)
    else:
        NewList.append(subList)
          
print(list)   
print("________________________________")
print(NewList)    
print(len(NewList))     
#print(list)
#(rowII,mensaje)
#print("longitud de ista:",len(list))#'''


#datos=hoja['C3':'O9']
'''list=[]
K=0
for fila in Datos['C496':'O496']:
    #print([datos.value for datos in fila])
    #print("Contdor:",K)
    list.append([datos.value for datos in fila])
#print(len(list))
#list.pop(6)
print(len(list))
print(list)

#print(list[0][0])
#print(list)
#'''
contexto={
    
}
