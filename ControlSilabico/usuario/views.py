from django.shortcuts import render

from django.db.models.query import InstanceCheckMeta
from django.db.models import Q
from django.db import connection
import mysql.connector as sql
#import pymysql as sql


nombre=''
pwd=''
t=''
idDo=''
# Create your views here.
def asignation(request):
    global nombre,pwd,t,idDo

    if request.method=='POST':
        m=sql.connect(host="localhost", user="root",passwd="admin",database="dbsilabos")
        cursor=m.cursor()
        d=request.POST

        for key,value in d.items():
            if key=='nombre':
                nombre=value
            if key=='contrasenia':
                pwd=value
            if key=='tipo':
                t=value
            if key=='idDocente':
                idDo=value
        #c="insert into users('{}','{}','{}','{}');".format(nombre,pwd,t,idDo)
        c="INSERT INTO `dbsilabos`.`users` (`nombre`, `contrasenia`, `tipo`, `idDocente`) VALUES ('{}','{}','{}','{}');".format(nombre,pwd,t,idDo)
        cursor.execute(c)
        m.commit()
    return render(request,'usuario/crear_usuario.html')



        

