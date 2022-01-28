from tkinter import TRUE


t=[('IF481BIN', 'INGENIERIA ECONOMICA', 'INGENIERIA INFORMATICA', '3', 'T', 'B', 2, 0, 'LUNES', '19', '21', 'VIRT 4 IN'), ('IF481BIN', 'INGENIERIA ECONOMICA', 'INGENIERIA INFORMATICA', '3', 'P', 'B', 0, 2, 'MIÉRCOLES', '19', '21', 'VIRT 4 IN'), ('IF902BAT', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', 'ARQUITECTURA(B) ', '3', 'T', 'A', 2, 0, 'MARTES', '14', '16', '0'), ('IF902AEI', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' ING. ELECTRICA ', '3', 'T', 'A', 2, 0, 'MARTES', '14', '16', '0'), ('IF902BLI', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' ING. ELECTRONICA(B)', '3', 'T', 'A', 2, 0, 'MARTES', '14', '16', '0'), ('IF902BAT', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', 'ARQUITECTURA(B) ', '3', 'P', 'A', 0, 2, 'JUEVES', '14', '16', '0'), ('IF902AEI', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' ING. ELECTRICA ', '3', 'P', 'A', 0, 2, 'JUEVES', '14', '16', '0'), ('IF902BLI', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' ING. ELECTRONICA(B)', '3', 'P', 'A', 0, 2, 'JUEVES', '14', '16', '0'), ('IF902AME', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', 'MATEMATICAS ', '3', 'T', 'A', 2, 0, 'MARTES', '18', '20', 'B-104'), ('IF902AQM', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' QUIMICA(A)', '3', 'T', 'A', 2, 0, 'MARTES', '18', '20', 'B-104'), ('IF902AME', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', 'MATEMATICAS ', '3', 'P', 'A', 0, 2, 'JUEVES', '18', '20', 'LAB VIRT-7'), ('IF902AQM', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' QUIMICA(A)', '3', 'P', 'A', 0, 2, 'JUEVES', '18', '20', 'LAB VIRT-7'), ('IF902AMD', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', 'MEDICINA HUMANA ', '3', 'T', 'A', 2, 0, 'MIÉRCOLES', '16', '18', 'MH-402'), ('IF902AOD', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' ODONTOLOGIA(A)', '3', 'T', 'A', 2, 0, 'MIÉRCOLES', '16', '18', 'MH-402'), ('IF902AMD', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', 'MEDICINA HUMANA ', '3', 'P', 'A', 0, 2, 'LUNES', '16', '18', 'LAB VIRT-5'), ('IF902AOD', 'TECNOLOGIAS DE LA INFORMACION Y LA COMUNICACION', ' ODONTOLOGIA(A)', '3', 'P', 'A', 0, 2, 'LUNES', '16', '18', 'LAB VIRT-5')]
aux=t.copy()


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

'''t2=[]
id='IF481BIN'
k=0
lenn=len(t)-1'''
t2=[]
while(len(t)!=0):
    id=t[0][0]
    k=0
    lenn=len(t)-1
    busca_agrega(t,t2,id,k,lenn)
#busca_agrega(t,t2,id,k,lenn)
print(t)
print("------------")
print(t2)
print(len(t2))