from django.http import HttpResponse
from importlib.metadata import files
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models.query import InstanceCheckMeta
from django.db.models import Q
import mysql.connector as sql
from ControlSilabico.models import *
#import pymysql as sql
from .forms import ResgistrarDocenteForm
from django.urls import reverse
import openpyxl
from django.db import connection
import pymysql
usuario=''
pwd=''
t=''

# Create your views here.
def asignation(request):
    global usuario,pwd,t,idDo

    if request.method=='POST':
        m=sql.connect(host="localhost", user="root",passwd="",database="dbsilabos")
        cursor=m.cursor()
        d=request.POST

        for key,value in d.items():
            if key=='usuario':
                usuario=value
            if key=='contrasenia':
                pwd=value
            if key=='tipo':
                t=value
            
        #c="insert into users('{}','{}','{}','{}');".format(nombre,pwd,t,idDo)
        c="INSERT INTO `dbsilabos`.`users` (`usuario`, `contrasenia`, `tipo`) VALUES ('{}','{}','{}');".format(usuario,pwd,t)
       
        p=cursor.execute(c)
        print("**************",p)
    
        m.commit()
    return render(request,'usuario/crear_usuario.html')
def buscarUsuario(lst,dato):
    try:
        ndx = lst.index(dato)
    except:
        ndx = -1
    return ndx
def busca_agrega(t,t2,id,k,lenn):
    if(lenn+1==k):
        print('if ',k)
        print(t2)
        print("-----------------------")
        return t2
    else:
        if(id==t[k][0]):
            t2.append(t[k])
            t.pop(k)
            if(k!=0):
                busca_agrega(t,t2,id,k,lenn-1)
            else:
                busca_agrega(t,t2,id,k,lenn-1)
        else:
            busca_agrega(t,t2,id,k+1,lenn)
def cursos_usuario(request,iddocente):
    docente=Docente.objects.get(iddocente=iddocente)
    print(docente.correo)
    print("$$$$$$$$$$$$$$$$$$$$$$$:",iddocente)
    m=sql.connect(host="localhost", user="root",passwd="",database="dbsilabos")
    cursor=m.cursor()
    CuDocente="select curso.idCurso,curso.nombre,curso.carrera,creditos,idtipoCurso,grupo,hT,hP,idD,hrInicio,hrFin,Aula,semestrec from ((((docente as d inner join  carga as c on d.idDocente=c.idDocente)inner join  horario as h on h.idhorario=c.idhorario)inner join cursodetalle as cd on cd.idCursoDetalle=h.idCursoDetalle)inner join curso on curso.idCurso=cd.idCurso)where c.idDocente='{}';".format(iddocente)
    cursor.execute(CuDocente)
    t=cursor.fetchall()
    CodCursCarr=[]
    hor=[]
    list=[]
    '''try:
    ndx = lst.index(21)
    except:
    ndx = -1'''
    print("longitud",len(t))
    print("------------------------vista de la la lista original de los horarios--------------------")
    print(t)
    print("-----------------------------------------------------------------------------------------")
    t2=[]
    while(len(t)!=0):
        id=t[0][0]
        k=0
        lenn=len(t)-1
        print('lenn=len(t)-1',lenn)
        busca_agrega(t,t2,id,k,lenn)
    print("por ue no muestra")
    t=t2
    print("por ue no muestra")
    print(t)
    long=len(t)
    aux=True
    k=0
    for row in t:
        k+=1
        if(len(list)==0):
            horario=[]
            contenhorios=[]
            if(row[4]=='T'):
                if(k!=long):
                    print("kkk",k)
                    print("primer if")
                    list.append(row[0])
                    list.append(row[1])
                    list.append(row[2])
                    list.append('TEORICO')
                    list.append(row[5])
                    list.append(row[12])

                    horario.append(row[6])
                    horario.append(row[7])
                    horario.append(row[8])
                    horario.append('TEORICO')
                    horario.append(row[9])
                    horario.append(row[10])
                    horario.append(row[11])
                    contenhorios.append(horario)
                else:
                    print("kkk",k)
                    print("primer if")
                    list.append(row[0])
                    list.append(row[1])
                    list.append(row[2])
                    list.append('TEORICO')
                    list.append(row[5])
                    list.append(row[12])
                    
                    horario.append(row[6])
                    horario.append(row[7])
                    horario.append(row[8])
                    horario.append('TEORICO')
                    horario.append(row[9])
                    horario.append(row[10])
                    horario.append(row[11])

                    contenhorios.append(horario)
                    hor.append(list)
                    hor.append(contenhorios)
                    CodCursCarr.append(hor)
                    print(hor)
                #hor.append(list)
                #hor.append(contenhorios)
            elif(row[4]=='P'):
                if(k!=long):
                    print("kkk",k)
                    list.append(row[0])
                    list.append(row[1])
                    list.append(row[2])
                    list.append('PRACTICO')
                    list.append(row[5])
                    list.append(row[12])

                    horario.append(row[6])
                    horario.append(row[7])
                    horario.append(row[8])
                    horario.append('PRACTICO')
                    horario.append(row[9])
                    horario.append(row[10])
                    horario.append(row[11])
                    contenhorios.append(horario)
                else:
                    print("kkk",k)
                    list.append(row[0])
                    list.append(row[1])
                    list.append(row[2])
                    list.append('PRACTICO')
                    list.append(row[5])
                    list.append(row[12])

                    horario.append(row[6])
                    horario.append(row[7])
                    horario.append(row[8])
                    horario.append('PRACTICO')
                    horario.append(row[9])
                    horario.append(row[10])
                    horario.append(row[11])
                    contenhorios.append(horario)
                    hor.append(list)
                    hor.append(contenhorios)
                    CodCursCarr.append(hor)
                    print(hor)
                #hor.append(list)
                #hor.append(contenhorios)
            print("curso")
            print(list)
            print('horarios del curso')
            print(contenhorios)
            print("----------------------------------------------------------------------------")
        elif(buscarUsuario(list,row[0])>=0):
            print(buscarUsuario(list,row[0]))
            tipo=list[3]
            print(tipo)
            print("....tipo...",tipo[0])
            print(row[0])
            print(tipo,row[4])
            #teorico==T?
            if(tipo[0]=='T' and row[4]=='T'):
                if(k!=long):
                    print(tipo[0]+"-"+row[4],k)
                    print("////")
                    horario2=[]
                    horario2.append(row[6])
                    horario2.append(row[7])
                    horario2.append(row[8])
                    horario2.append('TEORICO')
                    horario2.append(row[9])
                    horario2.append(row[10])
                    horario2.append(row[11])
                    contenhorios.append(horario2)
                    print("--prieba contenhorRIOS:",contenhorios)
                    print(list)
                    print("or")
                    print(hor)
                else:
                    print("2921")
                    print(tipo[0]+"-"+row[4],k)
                    print("////")
                    horario2=[]
                    horario2.append(row[6])
                    horario2.append(row[7])
                    horario2.append(row[8])
                    horario2.append('TEORICO')
                    horario2.append(row[9])
                    horario2.append(row[10])
                    horario2.append(row[11])
                   
                    contenhorios.append(horario2)
                    print("--prieba contenhorRIOS:",contenhorios)
                    print(list)
                    hor.append(list)
                    hor.append(contenhorios)
                    CodCursCarr.append(hor)
                    print(hor)
            elif(tipo[0]=='P' and row[4]=='P'):
                if(k!=long):
                    print(tipo[0]+"-"+row[4],k)
                    print("////",)
                    horario2=[]
                    horario2.append(row[6])
                    horario2.append(row[7])
                    horario2.append(row[8])
                    horario2.append('PRACTICO')
                    horario2.append(row[9])
                    horario2.append(row[10])
                    horario2.append(row[11])
                    
                    contenhorios.append(horario2)
                    print("--prieba contenhorRIOS:",contenhorios)
                    print(list)
                else:
                    print("ññññññ")
                    print(tipo[0]+"-"+row[4],k)
                    print("////",)
                    horario2=[]
                    horario2.append(row[6])
                    horario2.append(row[7])
                    horario2.append(row[8])
                    horario2.append('PRACTICO')
                    horario2.append(row[9])
                    horario2.append(row[10])
                    horario2.append(row[11])
                    
                    contenhorios.append(horario2)
                    print("--prieba contenhorRIOS:",contenhorios)
                    print(list)
                    hor.append(list)
                    hor.append(contenhorios)
                    CodCursCarr.append(hor)
                    print(hor)
            else:
                if(tipo[0]=='P' and row[4]!='P'):
                    if(k!=long):
                        print(tipo[0]+"-"+row[4],k)
                        print("////")
                        horario2=[]
                        horario2.append(row[6])
                        horario2.append(row[7])
                        horario2.append(row[8])
                        horario2.append('TEORICO')
                        list[3]='PRACTICO Y TEORICO'
                        horario2.append(row[9])
                        horario2.append(row[10])
                        horario2.append(row[11])
                        
                        print(list)
                        contenhorios.append(horario2)
                        print("--prieba contenhorRIOS:",contenhorios)
                    else:
                        print("####")
                        print(tipo[0]+"-"+row[4],k)
                        print("////")
                        horario2=[]
                        horario2.append(row[6])
                        horario2.append(row[7])
                        horario2.append(row[8])
                        horario2.append('TEORICO')
                        list[3]='PRACTICO Y TEORICO'
                        horario2.append(row[9])
                        horario2.append(row[10])
                        horario2.append(row[11])
                        
                        print(list)
                        contenhorios.append(horario2)
                        print("--prieba contenhorRIOS:",contenhorios)
                        hor.append(list)
                        hor.append(contenhorios)
                        CodCursCarr.append(hor)
                        print(hor)
                elif(tipo[0]=='T' and row[4]!='T'):
                    if(k!=long):
                        print("eeeeee")
                        print(k,long)
                        print(tipo[0]+"-"+row[4],k)
                        print("aca va entara")
                        horario=[]
                        horario.append(row[6])
                        horario.append(row[7])
                        horario.append(row[8])
                        horario.append('PRACTICO')
                        list[3]='TEORICO Y PRACTICO'
                        horario.append(row[9])
                        horario.append(row[10])
                        horario.append(row[11])
                        
                        print(list)
                        contenhorios.append(horario)
                        print("--prieba contenhorRIOS:",contenhorios)
                        print("or")
                        print(hor)
                    else:
                        print("aaaaaa")
                        print(tipo[0]+"-"+row[4],k)
                        print("aca va entara")
                        horario=[]
                        horario.append(row[6])
                        horario.append(row[7])
                        horario.append(row[8])
                        horario.append('PRACTICO')
                        list[3]='TEORICO Y PRACTICO'
                        horario.append(row[9])
                        horario.append(row[10])
                        horario.append(row[11])
                        
                        print(list)
                        contenhorios.append(horario)
                        print("--prieba contenhorRIOS:",contenhorios)
                        hor.append(list)
                        hor.append(contenhorios)
                        CodCursCarr.append(hor)
                        print(hor)
                    print("curso")
                print("----------------------------------------------------------------------------")
                print(list)
                print('horarios del curso')
                print(contenhorios)
                print("----------------------------------------------------------------------------")
        elif(buscarUsuario(list,row[0])==-1 ):
            print("buscar(list,row[0])==-1 1")
            print(hor)
            print("kkk",k)
            print("----siguienteeee!!!!!!")
            hor.append(list)
            hor.append(contenhorios)
            CodCursCarr.append(hor)
            print("buscar(list,row[0])==-1 2")
            print("or")
            print(hor)
            print("CodCursCarr1")
            print(CodCursCarr)
            list=[]
            hor=[]
            if(len(list)==0):
                print("primer if -1")
                print("CodCursCarr2")
                print(CodCursCarr)
                horario=[]
                contenhorios=[]
                if(row[4]=='T'):
                    if(k!=long):
                        
                        print("kkk",k)
                        print("primer if -1")
                        list.append(row[0])
                        list.append(row[1])
                        list.append(row[2])
                        list.append('TEORICO')
                        list.append(row[5])
                        list.append(row[12])

                        horario.append(row[6])
                        horario.append(row[7])
                        horario.append(row[8])
                        horario.append('TEORICO')
                        horario.append(row[9])
                        horario.append(row[10])
                        horario.append(row[11])
                        
                        #CodCursCarr.append(list)
                        contenhorios.append(horario)
                        
                        print(list)
                        print(contenhorios)
                        print("CodCursCar3")
                        print(CodCursCarr)
                        #hor.append(list)
                        #hor.append(contenhorios)
                        print(list)
                    else:
                        print("kkk",k)
                        print("primer if -1")
                        list.append(row[0])
                        list.append(row[1])
                        list.append(row[2])
                        list.append('TEORICO')
                        list.append(row[5])
                        list.append(row[12])

                        horario.append(row[6])
                        horario.append(row[7])
                        horario.append(row[8])
                        horario.append('TEORICO')
                        horario.append(row[9])
                        horario.append(row[10])
                        horario.append(row[11])
                        
                        #CodCursCarr.append(list)
                        contenhorios.append(horario)
                        hor.append(list)
                        hor.append(contenhorios)
                        CodCursCarr.append(hor)
                        print(list)
                        print(contenhorios)
                        print("CodCursCar3")
                        print(row)
                        print(CodCursCarr)
                        #hor.append(list)
                        #hor.append(contenhorios)
                        print(list)

                elif(row[4]=='P'):
                    if(k!=long):
                        print("kkk--",k)
                        list.append(row[0])
                        list.append(row[1])
                        list.append(row[2])
                        list.append('PRACTICO')
                        list.append(row[5])
                        list.append(row[12])

                        horario.append(row[6])
                        horario.append(row[7])
                        horario.append(row[8])
                        horario.append('PRACTICO')
                        horario.append(row[9])
                        horario.append(row[10])
                        horario.append(row[11])
                        
                        print("Cntenido si es P y ")
                        print(list)
                        contenhorios.append(horario)
                        print(contenhorios)
                        print("CodCursCar3")
                        print(row)
                        print(CodCursCarr)
                            #hor.append(list)
                            #hor.append(contenhorios)
                    else:
                        print("kkk--",k)
                        list.append(row[0])
                        list.append(row[1])
                        list.append(row[2])
                        list.append('PRACTICO')
                        list.append(row[5])
                        list.append(row[12])

                        horario.append(row[6])
                        horario.append(row[7])
                        horario.append(row[8])
                        horario.append('PRACTICO')
                        horario.append(row[9])
                        horario.append(row[10])
                        horario.append(row[11])
                        
                        print("Cntenido si es P y ")
                        print(list)
                        contenhorios.append(horario)
                        hor.append(list)
                        hor.append(contenhorios)
                        CodCursCarr.append(hor)
                        print(contenhorios)
                        print("CodCursCar3")
                        print(row)
                        print(CodCursCarr)
                        
    print("MOstararrrr")
    print(CodCursCarr)
    #print(t)
    return render(request,"usuario/cursos_usuario.html",{'asignaciones':t,'docente':docente,'cursosUsuario':CodCursCarr})
def silabos(request,codCurso,IdDocente,carrera,semestre):
    
    conn=pymysql.connect(host="localhost", user="root",passwd="",database="dbsilabos")
    cursor=conn.cursor()
    docente=Docente.objects.get(iddocente=IdDocente)
    curso=Curso.objects.get(idcurso=codCurso)
    CuDocente="select idtipoCurso,c.idCarga from ((((docente as d inner join  carga as c on d.idDocente=c.idDocente)inner join  horario as h on h.idhorario=c.idhorario)inner join cursodetalle as cd on cd.idCursoDetalle=h.idCursoDetalle)inner join curso on curso.idCurso=cd.idCurso) where c.idDocente='{}' and curso.idCurso='{}';".format(IdDocente,codCurso)
    cursor.execute(CuDocente)
    Tipo_cursos=cursor.fetchall()
    #carrera=[carrera]
    print('carrera prueba',carrera)
    if(request.method=='POST'):
        exel=request.FILES['exel_silabo']
        print(exel)
        print(semestre)
        print("TIPO",Tipo_cursos)
        #-----------------------------carga silabic-----------------
        consulta="select * from silabo where idCargac='{}';".format(Tipo_cursos[0][1])
        cursor.execute(consulta)
        execute=cursor.fetchall()
        if(len(execute)!=0):
            cursor.execute('select * from silabo ')
            temasborrar=cursor.fetchall()
            #---borrar--
            for rowsila in temasborrar:
                bor="delete from silabo where unidadc='{}' and capituloc='{}' and temac='{}' and sesionc='{}' and semestrec='{}' and idCargac='{}';".format(rowsila[1],rowsila[2],rowsila[3],rowsila[4],rowsila[5],rowsila[6])
                cursor.execute(bor)
            print("temasborrar",temasborrar)

        print("execute:",execute)
        
        rowII=2
        rowIF=2
        cursor=conn.cursor()
        importar_silabo(Tipo_cursos,rowII,rowIF,conn,cursor,semestre,exel)
        #-----------------------------------------------------------
        temascons="select unidadc, capituloc, temac, sesionc, S.semestrec, idCargac from (((silabo as S inner join carga as C on S.idCargac= C.idCarga)inner join horario as H on H.idHorario=C.idHOrario) inner join cursodetalle as Cud on Cud.idCursoDetalle=H.idCursoDetalle) where idCurso='{}' and C.idDocente='{}' and S.semestrec='{}';".format(codCurso,IdDocente,semestre)
        cursor.execute(temascons)
        temas=cursor.fetchall()
        conn.commit()
        cursor.close()
        #----------
        contexto={'curso':curso,'docente':docente,'carrera':carrera,'tipo':Tipo_cursos,'DATOsemestre':semestre,'horario':temas}
        return redirect ('silabo',codCurso,IdDocente,carrera,semestre)
    print("TIPO",Tipo_cursos)
    print(semestre)
    temascons="select unidadc, capituloc, temac, sesionc, S.semestrec, idCargac from (((silabo as S inner join carga as C on S.idCargac= C.idCarga)inner join horario as H on H.idHorario=C.idHOrario) inner join cursodetalle as Cud on Cud.idCursoDetalle=H.idCursoDetalle) where idCurso='{}' and C.idDocente='{}' and S.semestrec='{}';".format(codCurso,IdDocente,semestre)
    cursor.execute(temascons)
    temas=cursor.fetchall()
    print("#--------------vista de silabo  con django---------------")
    #print(temas)
    listtemas=[]
    for rowtemas in temas:
        listtemas.append([dato for dato in rowtemas])
    temas1=listtemas
    #----------------elimanar  repetidos
    if(len(temas1)!=0):
        k=0
        eliminar_repetidos(temas1,k)
    #-------------
    print(temas1)
    print("---------------------------------------------------------")
    contexto={'curso':curso,'docente':docente,'carrera':carrera,'tipo':Tipo_cursos,'DATOsemestre':semestre,'temas':temas1}
    return render(request,'usuario/silabo.html',contexto)
#--------------------------vista sin repetir temas del silabo-----------------------
def  eliminar_repetidos(temas,k):
    if(k==len(temas)-1):
        return temas
    else:
        if(temas[k][0]==temas[k+1][0] and temas[k][1]==temas[k+1][1] and temas[k][2]==temas[k+1][2] and temas[k][3]==temas[k+1][3]):
            temas.pop(k+1)
            eliminar_repetidos(temas,k)
        else:
            eliminar_repetidos(temas,k+1)
#----------------------------modulos import silabos-------------------
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
'''
def registrar_usuario_docente(request):
    initial_data={'usuario':'','contrasenia':'','tipo':'docente'}
    #docente_form=ResgistrarDocenteForm(initial=inicializar)
    
    if request.method=="POST":
        docente_form=ResgistrarDocenteForm(request.POST)
        
        if docente_form.is_valid():
            docente_form.save()
            #return redirect('iniciar')
            return render(request,'login/iniciar_sesion.html')
    else:
        docente_form=ResgistrarDocenteForm(initial=initial_data)
    return render(request,'usuario/registrar_usuario_docente.html',{'registrar_docente_form':docente_form})
'''
