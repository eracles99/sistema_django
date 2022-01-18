from django.shortcuts import render
from django.db.models.query import InstanceCheckMeta
from django.db.models import Q
from django.db import connection
import mysql.connector as sql
#import pymysql as sql


usuario=''
pwd=''
t=''
# Create your views here.
def iniciar(request):
    global usuario,pwd,t
    print("================= tipo: ",t)

    if request.method=='POST':
        m=sql.connect(host="localhost", user="root",passwd="admin",database="dbsilabos")
        cursor=m.cursor()
        d=request.POST

        for key,value in d.items():
            if key=='usuario':
                usuario=value
            if key=='contrasenia':
                pwd=value
            if key=='tipo':
                t=value
        print("******* tipo:",usuario)
        print("******* tipo:",pwd)
        print("******* tipo:",t)
        if t=="administrador":
            #c="insert into users('{}','{}','{}','{}');".format(nombre,pwd,t,idDo)
            c="select * from users where usuario='{}' and contrasenia='{}' and tipo='{}';".format(usuario,pwd,t)
            cursor.execute(c)
            t=tuple(cursor.fetchall())
            #m.commit()
            if t==():
                return render(request,"login/error.html")
            else:
                return render(request,"index1.html")
        else:
            #c="insert into users('{}','{}','{}','{}');".format(nombre,pwd,t,idDo)
            c="select * from users where usuario='{}' and contrasenia='{}' and tipo='{}';".format(usuario,pwd,t)
            cursor.execute(c)
            t=tuple(cursor.fetchall())
            #m.commit()
            if t==():
                return render(request,"login/error.html")
            else:
                return render(request,"index2.html",{'nombre':usuario})


    return render(request,'login/iniciar_sesion.html')


        

