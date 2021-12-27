import  pymysql
#from django.db import co
conn = pymysql.connect(host='bvxzku4jqpi5h93yqkrf-mysql.services.clever-cloud.com', user='upy42uypukqqpl2c', password='2StBffpYivierwHvqIil', database='bvxzku4jqpi5h93yqkrf', charset='utf8')
cur = conn.cursor()
Args=('IF421AIN',)
cur.callproc('sp_HroPorCurso',Args)
conn.commit()
result = cur.fetchall()
result1=[]
print('{0}   {1}   {2}   {3}   {4}   {5}   {6}   {7} '.format('id', 'tipo', 'ht', 'hp','dia','hrInicio','hrFin','Aula'))
for row in result:
    result1.append(list(row))
contexto={'consultas':result1}
conn.close()
print(result1)
 
