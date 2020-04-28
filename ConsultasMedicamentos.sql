# Muestra todos los medicamentos
SELECT *
FROM medicamentos;
# Muestra todos los principios activos
SELECT * 
FROM principios_activos;
# Muestre todos los medicamentos cuyo nombre empiece por f
SELECT *
FROM medicamentos
WHERE nombre LIKE 'F%';
# Muestre todos los medicamentos de administración oral
SELECT *
FROM medicamentos
WHERE viaAdministracion = 'Oral';
# Muestre todos los mediacamentos que empiecen por f y sean de adminisración oral
SELECT *
FROM medicamentos
WHERE nombre LIKE 'F%' AND viaAdministracion = 'Oral';
# Muestre el número de medicamentos en función de la vía de administración
SELECT viaAdministracion, count(*) AS numMedicamentos
FROM medicamentos
GROUP BY viaAdministracion;
# Muestre los medicamentos cuya presentación sea en comprimidos
SELECT *
FROM medicamentos
WHERE presentacion LIKE 'Comprimidos%';
# Muestra todos los medicamentos que se consideren antipiretico
SELECT *
FROM medicamentos
WHERE claseMedicamento LIKE '%Antipiretico%';
# Muestra todos los medicamentos cuya indicación esté asociada con la gripe
SELECT *
FROM medicamentos
WHERE indicaciones LIKE '%gripe%';
# Muestra todos los medicamentos que se encuentren en comercialización
SELECT *
FROM medicamentos
WHERE comercializacion = TRUE;
# Muestra todos los medicamentos que no necesiten prescripción médica
SELECT *
FROM medicamentos
WHERE prescripcionMedica = FALSE;
# Muestra todos los medicamentos cuyo precio sea mayor que 10 euros
SELECT *
FROM medicamentos
WHERE pvp > 10;
# Ordena los medicamentos en función del precio
SELECT *
FROM medicamentos
ORDER BY pvp;
# Muestra todos los medicamentos con más de dos principios activos
SELECT *
FROM medicamentos
WHERE codigoNacional IN (SELECT MEDICAMENTOS_codigoNacional
						FROM med_tienen_pa
                        GROUP BY MEDICAMENTOS_codigoNacional
						HAVING count(MEDICAMENTOS_codigoNacional) > 2);
# Muestra todos los medicamentos que tengan paracetamol
SELECT *
FROM medicamentos
WHERE codigoNacional IN (SELECT MEDICAMENTOS_codigoNacional
						FROM med_tienen_pa
                        WHERE PRINCIPIOSACTIVOS_nombre = 'Paracetamol');
# Muestra todos los medicamentos ordenados en función del número de principios activos
SELECT nombre, count(MEDICAMENTOS_codigoNacional) AS numPrincipiosActivos
FROM medicamentos m JOIN med_tienen_pa mp
ON m.codigoNacional = mp.MEDICAMENTOS_codigoNacional
GROUP BY nombre
ORDER BY numPrincipiosActivos DESC;
# Muestra todos los medicamentos cuyos principios activos tengan un peso molecular mayor que 400
SELECT *
FROM medicamentos med
WHERE med.codigoNacional IN (SELECT MEDICAMENTOS_codigoNacional
							FROM med_tienen_pa
							WHERE PRINCIPIOSACTIVOS_nombre IN (SELECT Nombre
															FROM principios_activos
                                                            WHERE pesoMolecular > 400)
							GROUP BY MEDICAMENTOS_codigoNacional
							HAVING count(MEDICAMENTOS_codigoNacional) = (SELECT count(MEDICAMENTOS_codigoNacional)
																		FROM med_tienen_pa
																		WHERE MEDICAMENTOS_codigoNacional = med.codigoNacional));
# Muestra los principios activos del medicamento Frenadol Forte
SELECT *
FROM principios_activos
WHERE Nombre IN (SELECT PRINCIPIOSACTIVOS_nombre
				FROM med_tienen_pa
                WHERE MEDICAMENTOS_codigoNacional = (SELECT codigoNacional
													FROM medicamentos
                                                    WHERE nombre = 'Frenadol Forte'));
# Muestra los principios activos que se encuentren en más de dos medicamentos
SELECT *
FROM principios_activos
WHERE Nombre IN (SELECT PRINCIPIOSACTIVOS_nombre
				FROM med_tienen_pa
				GROUP BY PRINCIPIOSACTIVOS_nombre
                HAVING count(PRINCIPIOSACTIVOS_nombre) > 2);
# Muestra los principios activos ordenados por el peso molecular
SELECT *
FROM principios_activos
ORDER BY pesoMolecular DESC;
# Muestra los principios activos con un peso molecular mayor a 500
SELECT *
FROM principios_activos 
WHERE pesoMolecular > 500;
# Muestra los principios activos cuya fórmula tenga cloro
SELECT *
FROM principios_activos 
WHERE formulaMolecular LIKE '%Cl%';