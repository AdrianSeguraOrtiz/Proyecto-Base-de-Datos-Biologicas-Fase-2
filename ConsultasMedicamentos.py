# -*- coding: utf-8 -*-
import pymysql.cursors  
 
# Connect to the database.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='adrianseguraortiz1999',                             
                             db='farmacos_bd',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
try:
    
    with connection.cursor() as cursor:
 
        
 # C1 Find all medicines whose name start by the letter 'F'.
        
        print("Consulta 1")
        sql1 = """SELECT *
                FROM medicamentos
                WHERE nombre LIKE 'F%';""" 
        cursor.execute(sql1)
        print()
        for row in cursor:
            print (row)
            
        print()
        
 #C2 Find all medicines which have an oral administration.
        
        print("Consula 2")
        sql2="""SELECT *
            FROM medicamentos
            WHERE viaAdministracion = 'Oral';"""
        cursor.execute(sql2)
        print()
        for row in cursor:
            print(row)
        
        print()
        
#C3 Find all medicines whose name starts by 'F' and which have an oral administration
        
        print("Consulta 3")
        sql3="""SELECT * 
        FROM medicamentos  
        WHERE nombre LIKE'F%' AND viaAdministracion = 'Oral';"""
        cursor.execute(sql3)
        print()
        for row in cursor:
            print(row)
        
        print()
        
#C4 List how many medicines have the same route of administration.
        
        print("Consulta 4")
        sql4="""SELECT viaAdministracion, count(*) AS numMedicamentos
        FROM medicamentos
        GROUP BY viaAdministracion;"""
        cursor.execute(sql4)
        print()
        for row in cursor:
            print(row)
            
        print()
        
#C5 Find all medicines whose presentation is in tablets.
        
        print("Consuta 5")
        sql5="""SELECT * 
        FROM medicamentos 
        WHERE presentacion LIKE 'Comprimidos%';"""
        cursor.execute(sql5)
        print()
        for row in cursor:
            print(row)
        
        print()
        
#C6 Find all medicines which are considered antipyretics.
        
        print("Consulta 6")
        sql6 = """SELECT *
        FROM medicamentos
        WHERE claseMedicamento LIKE '%Antipiretico%';"""
        cursor.execute(sql6)
        print()
        for row in cursor:
            print(row)
        
        print()

       
#C7 List all medicines whose indication is associated with the flu.
        
        print("Consulta 7")
        sql7= """SELECT *
        FROM medicamentos
        WHERE indicaciones LIKE '%gripe%';"""
        cursor.execute(sql7)
        print()
        for row in cursor:
            print(row)
        
        print()
        
#C8 Find all medicines which are on the market.   
        
        print("Consulta 8")
        sql8 = """SELECT * 
        FROM medicamentos 
        WHERE  comercializacion = TRUE;"""
        cursor.execute(sql8)
        print()
        for row in cursor:
            print(row)
        
        print()
        
#C9 Find all medicines which don't require a prescription.
        
        print("Consulta 9")
        sql9= """SELECT *
        FROM medicamentos
        WHERE prescripcionMedica = FALSE;"""
        cursor.execute(sql9)
        print()
        for row in cursor:
            print(row)
        
        print()
        
#C10 Find all medicines whose price is greater than 10 euros.
        
        print("Consulta 10")
        sql10="""SELECT *
        FROM medicamentos
        WHERE pvp > 10;"""
        cursor.execute(sql10)
        print()
        for row in cursor:
            print(row)
        
        print()
        
#C11 Sort medicnies depending on the price.
        
        print("Consulta 11")
        sql11="""SELECT *
        FROM medicamentos
        ORDER BY pvp;"""
        cursor.execute(sql11)
        print()
        for row in cursor:
            print(row)
        
        print()

#C12 Find all medications with more than three active ingredients.   
        
        print("Consulta 12")
        sql12="""SELECT *
        FROM medicamentos
        WHERE codigoNacional IN (SELECT MEDICAMENTOS_codigoNacional
		                         FROM med_tienen_pa
                                 GROUP BY MEDICAMENTOS_codigoNacional
		                         HAVING count(MEDICAMENTOS_codigoNacional) > 2);"""
        cursor.execute(sql12)
        print()
        for row in cursor:
            print(row)
        
        print()

# C13 Find all medicines whcih have 'Paracetamol'.
        
        print("Consulta 13")
        sql14="""SELECT *
        FROM medicamentos
        WHERE codigoNacional IN (SELECT MEDICAMENTOS_codigoNacional
		                         FROM med_tienen_pa
                                 WHERE PRINCIPIOSACTIVOS_nombre = 'Paracetamol');"""
        cursor.execute(sql13)
        print()
        for row in cursor:
            print(row)
            
        print()
        
# C14 List all medicines ordered by active ingredients.
        
        print("Consulta 14")
        sql15="""SELECT nombre, count(MEDICAMENTOS_codigoNacional) AS numPrincipiosActivos
        FROM medicamentos m JOIN med_tienen_pa mp
        ON m.codigoNacional = mp.MEDICAMENTOS_codigoNacional
        GROUP BY nombre
        ORDER BY numPrincipiosActivos DESC;"""
        cursor.execute(sql14)
        print()
        for row in cursor:
            print(row)
            
        print()

# C15 Find all medicines whose active ingredients have a molecular weight greater than 400.
       
        print("Consulta 15")
        sql16="""SELECT *
                 FROM medicamentos med
                 WHERE med.codigoNacional IN (SELECT MEDICAMENTOS_codigoNacional
							                  FROM med_tienen_pa
							                  WHERE PRINCIPIOSACTIVOS_nombre IN (SELECT Nombre
															                     FROM principios_activos
                                                                                 WHERE pesoMolecular > 400)
							                  GROUP BY MEDICAMENTOS_codigoNacional
							                  HAVING count(MEDICAMENTOS_codigoNacional) = (SELECT count(MEDICAMENTOS_codigoNacional)
																		                   FROM med_tienen_pa
																		                   WHERE MEDICAMENTOS_codigoNacional = med.codigoNacional));"""
        cursor.execute(sql15)
        print()
        for row in cursor:
            print(row)
            
        print()
        
#C16 Find all Frenadol's active ingredients Muestra los principios activos del medicamento Frenadol Forte
        
        print("Consulta 16")
        sql13="""SELECT *
        FROM principios_activos
        WHERE Nombre IN (SELECT PRINCIPIOSACTIVOS_nombre
                         FROM med_tienen_pa
                         WHERE MEDICAMENTOS_codigoNacional = (SELECT codigoNacional
                                                              FROM medicamentos
                                                              WHERE nombre = 'Frenadol Forte'));"""
        cursor.execute(sql16)
        print()
        for row in cursor:
            print(row)
            
        print()
        
# C17 List all active ingredients found in more than two medicines.
        
        print("Consulta 17")
        sql17="""SELECT *
                 FROM principios_activos
                 WHERE Nombre IN (SELECT PRINCIPIOSACTIVOS_nombre
		                          FROM med_tienen_pa
		                          GROUP BY PRINCIPIOSACTIVOS_nombre
                                  HAVING count(PRINCIPIOSACTIVOS_nombre) > 2);;"""
        cursor.execute(sql17)
        print()
        for row in cursor:
            print(row)
            
        print()
        
# C18 Find all active ingredients orderd by molecular weight.
        
        print("Consulta 18")
        sql18="""SELECT *
        FROM principios_activos
        ORDER BY pesoMolecular DESC;"""
        cursor.execute(sql18)
        print()
        for row in cursor:
            print(row)
            
        print()
        
# C19 List all active ingredients which have a molecular weight greater than 500.
        
        print("Consulta 19")
        sql19="""SELECT *
        FROM principios_activos 
        WHERE pesoMolecular > 500;"""
        cursor.execute(sql19)
        print()
        for row in cursor:
            print(row)
            
        print()
        
# C20 Find all active ingredients whose formula has 'Cloro'.
        
        print("Consulta 20")
        sql20="""SELECT *
        FROM principios_activos 
        WHERE formulaMolecular LIKE '%Cl%';"""
        cursor.execute(sql20)
        print()
        for row in cursor:
            print(row)
            
        print()
        
finally:
    # Close connection.
    connection.close()
        
