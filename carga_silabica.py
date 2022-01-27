import openpyxl
import csv
from django.db import connection
import pymysql

def Validador(Datos,rowII,rowIF):
    list=[]
    for fila in Datos['A'+str(rowII):'D'+str(rowIF)]:
        #print([datos.value for datos in fila])
        #print("Contdor:",K)
        list.append([datos.value for datos in fila])
        if(list[0][0] is None or list[0][0]==''):
            return False
        else: 
            return True

def Trozador(list,rowII,rowIF,Datos):
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
            for fila in Datos['A'+str(rowII):'D'+str(rowIF)]:
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
            return list,rowII-1,rowIF-1,True
        else:
            #print("Vacio en return else:",vacio)
            del list[-(vacio+1):]
            return list,rowII,rowIF,True
    return list,rowII-1,rowIF-1,False
def buscar(list,E):
    count=0
    for k in list:
        if k==E:
            count+=1
    return count
def sp_procedure(tipoIdCarga,row,L,cursor,SEMESTRE):
    UNIDAD=row[0]
    CAPITULO=row[1]
    TEMA=row[2]
    SESION=row[3]
    IDCARGA=tipoIdCarga[L][1]
    args=(UNIDAD,CAPITULO,TEMA,SESION,SEMESTRE,IDCARGA)
    print('procedure',args)
    cursor.callproc('sp_migracion_silabos',args)
def repartidor_secion(tipoIdCarga,row,count,sesion,v,L,cursor,SEMESTRE):
    for i in range(1,sesion+1):
        print('hola')
        print(v)
        print("entra L",L)
        while(count!=i):
            if(tipoIdCarga[L][0]==v ):
                print('(tipoIdCarga[L][0]==',v)
                if(L==len(tipoIdCarga)-1):
                    print('if(L==len(tipoIdCarga)-1)')
                    count+=1
                    indice=L
                    #migrar
                    sp_procedure(tipoIdCarga,row,L,cursor,SEMESTRE)
                    print("tupla ingreso")
                    #dddd
                    print("migrara:",tipoIdCarga[L][1])
                    #-------
                    print('indice',indice)
                    print(tipoIdCarga[L][0])
                    print("count",count)
                    L=0
                    validador=indice
                    print("L",L)
                else:
                    print('if(L==len(tipoIdCarga)-1)')
                    count+=1
                    indice=L
                    #migrar
                    sp_procedure(tipoIdCarga,row,L,cursor,SEMESTRE)
                    print("tupla ingreso")
                    #dddd
                    print("migrara:",tipoIdCarga[L][1])
                    #---------------
                    print('indice',indice)
                    print(tipoIdCarga[L][0])
                    L=L+1
                    print("L",L)
            elif(tipoIdCarga[L][0]!=v):
                print('tipoIdCarga[L][0]!=',v)
                if(L==len(tipoIdCarga)-1):
                    print(tipoIdCarga[L][0],L)
                    L=0
                    indice=L
                    print("indice",L)
                    print('indice se reinicia',indice)
                else:
                    L=L+1
                    print("L",L)
    return indice
def MigracionPracticox2(tipoIdCarga,row,count,sesion,v,L,cursor,SEMESTRE):
    print('hola')
    print(v)
    print("entra L",L)
    inicio=L
    if(L>1):
        L=0
        inicio=L
    for i in range(1,sesion+1):
        while(count!=i):
            if(tipoIdCarga[L][0]==v ):
                print('(tipoIdCarga[L][0]==',v)
                if(L==len(tipoIdCarga)-1):
                    print('if(L==len(tipoIdCarga)-1)')
                    count+=1
                    indice=L
                    #migrar
                    sp_procedure(tipoIdCarga,row,L,cursor,SEMESTRE)
                    print("tupla ingreso")
                    #dddd
                    print("migrara:",tipoIdCarga[L][1])
                    #-------
                    print('indice',indice)
                    print(tipoIdCarga[L][0])
                    print("count",count)
                    L=0
                    print("inicio",inicio)
                else:
                    print('else')
                    count+=1
                    indice=L
                    #migrar
                    sp_procedure(tipoIdCarga,row,L,cursor,SEMESTRE)
                    print("tupla ingreso")
                    #dddd
                    print("migrara:",tipoIdCarga[L][1])
                    #---------------
                    print('indice',indice)
                    print(tipoIdCarga[L][0])
                    L=L+1
                    print("L",L)
    return inicio +1
def importar_silabo(tipoIdCarga,rowII,rowIF,conn,cursor,SEMESTRE,exel):
    book=openpyxl.load_workbook(exel,data_only=True)
    Datos=book.active
    list=[]
    K=0
    list,rowII,rowIF,mensaje=Trozador(list,rowII,rowIF,Datos)
    tipoinicio=tipoIdCarga[0][0]
    indice=0
    count=0
    L=0
    M=0
    for row in list:
        print("-----",row)
        N=0
        if( tipoinicio=='T'):
            lAB=row[1]
            LAB=lAB[0:4]
            sesion=row[3]
            if(LAB!='LAB.'):
                print(row)
                v='T'
                L=repartidor_secion(tipoIdCarga,row,count,sesion,v,L,cursor,SEMESTRE)
                L=L+1
                print("aaaa",L)
            else:
                print(row)
                v='P'
                M=repartidor_secion(tipoIdCarga,row,count,sesion,v,L,cursor,SEMESTRE)
                print("aaaa",M)
        else:
            sesion=row[3]
            print(row)
            v='P'
            L=MigracionPracticox2(tipoIdCarga,row,count,sesion,v,L,cursor,SEMESTRE)
            print("main L:",L)
        print("-------------------------------------------------------------")
    conn.commit()
    cursor.close()

#def main_carga(exel):
#exel='C:\\Users\\angel\\Downloads\\carga silabica.xlsx'
#tipoIdCarga=[('T', 283), ('T', 284), ('P', 285)]
semestre='2021-II'
exel='C:\\Users\\angel\\Downloads\\carga-silabo-solo-practico.xlsx'
tipoIdCarga=[('P', 308), ('P', 309)]
conn = pymysql.connect(host='localhost', user='root', password='', database='dbsilabos', charset='utf8mb4')
rowII=2
rowIF=2
cursor=conn.cursor()
importar_silabo(tipoIdCarga,rowII,rowIF,conn,cursor,semestre,exel)
'''for row in list:
    print("-----",row)
    N=0
    if( tipoinicio=='T'):
        lAB=row[1]
        LAB=lAB[0:4]
        sesion=row[3]
        if(LAB!='LAB.'):
            print(row)
            v='T'
            L=repartidor_secion(row,count,sesion,v,L,conn)
            L=L+1
            print("aaaa",L)
        else:
            print(row)
            v='P'
            M=repartidor_secion(row,count,sesion,v,L,conn)
            print("aaaa",M)
    else:
        sesion=row[3]
        print(row)
        v='P'
        L=MigracionPracticox2(row,count,sesion,v,L,conn)
        print("main L:",L)
    print("-------------------------------------------------------------")
conn.commit()
cursor.close()
    



#----------------------

for fila in Datos['A2':'D46']:
    #print([datos.value for datos in fila])
    for datos in fila:
        print(datos.value)
    print("-------------------------------------------")
    #print("Contdor:",K)
    list.append([datos.value for datos in fila])#'''
#print(list)
