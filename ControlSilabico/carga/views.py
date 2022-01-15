from django.shortcuts import render,redirect,get_object_or_404
from django.db.models.query import InstanceCheckMeta
from django.core.exceptions import ObjectDoesNotExist
from ControlSilabico.curso.froms import CursoDetallForm
from ControlSilabico.models import *
from ControlSilabico.carga.froms import *
# Create your views here.
from django.db.models.query import InstanceCheckMeta
from django.db.models import Q
from django.db import connection
import openpyxl
import pymysql

def listar_carga(request):
    cursor=connection.cursor()
    try:
        cursor.execute('select * from vcargadocente')
        resultado=cursor.fetchall()
        print(resultado)
        print("holaaaaaaaaa")
        #-------------------------------------------------
        if(request.method =='POST'):
            print("HOLAAAAAAAAAAA")
            file=request.FILES["file"]
            print("****************************************:",file)
            book=openpyxl.load_workbook(file,data_only=True)
            Datos=book.active
            conn = pymysql.connect(host='localhost', user='root', password='admin', database='dbsilabos', charset='utf8mb4')
            rowII=3
            rowIF=3
            list=[]
            mensaje=True
            while(mensaje==True):
                list=[]
                list,rowII,rowIF,mensaje=Trozador(list,rowII,rowIF,Datos,conn)
            return redirect('listar_carga')
        return render(request,'carga/inicio.html',{'carga':resultado}) # con esto le mande al templetes
    finally:
        cursor.close()
    
def listar_cursos(request):
    cursor=connection.cursor()
    try:
        cursor.execute('select * from vcursosdisponibles')
        resultado=cursor.fetchall()
        print(resultado)
        return render(request,'carga/cursos_disponibles.html',{'cursosd':resultado}) # con esto le mande al templetes
    finally:
        cursor.close()
def asignar_cargafail(request,idCursoDetalle):
    #carga1= Cursodetalle.objects.filter(idcursodetalle=idCursoDetalle).first()
    print("************************",idCursoDetalle)

    return render(request,'carga/generar_carga.html',{'CursoDetalle':idCursoDetalle})
def asignando(request,idCursoDetalle):
    codeDetalle=idCursoDetalle
    codeDocente=request.POST['txtCodigo']

    #print("==========",codeDetalle,codeDocente)

    carga=Carga.objects.create(iddocente=codeDocente , idcursodetalle=codeDetalle)
    return render(request,'carga/generar_carga.html')

def asignar_carga(request,idCursoDetalle):
    print('****************',idCursoDetalle)
    carga_form=None
    error=None
    try:
        if request.method=='POST':
            carga_form = cargaForm(initial={'idCursoDetalle': idCursoDetalle})
            carga_form=cargaForm(request.POST)
            if carga_form.is_valid():
                carga_form.save()
                return redirect('listar_curso') 
        else:
            carga_form=cargaForm()
    except ObjectDoesNotExist as e:
        error=e 
    return render(request,'carga/generar_carga.html',{'carga_form':carga_form})
#---------------------------------------------------------MIGRACION EXEL------------------------------------------------
def carga_masiva(conn,list):
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
            args_MIGRACION_MASIVA=(nombreDoc,tipocurso,codeCurso,nombre,carrera,Grupo,creditos,HT,HP,dia1,HrInicio,HrFin,AULA)
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
def Trozador(list,rowII,rowIF,Datos,conn):
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
            carga_masiva(conn,list)
            return list,rowII-1,rowIF-1,True
        else:
            #print("Vacio en return else:",vacio)
            del list[-(vacio+1):]
            list=Normalizador(list)
            carga_masiva(conn,list)
            return list,rowII,rowIF,True
    return list,rowII-1,rowIF-1,False

#def main_carga(request):
def upload(request):
    return render(request,'carga/upload.html')
    