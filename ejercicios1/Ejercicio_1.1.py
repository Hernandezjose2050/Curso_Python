
#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_primedio = 4
dalto_curso = 1.5

#crudo promedio
crudo_promedio = 5
crudo_dalto_editado = 3.5


#Diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_primedio

#calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_primedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto_editado /10

print("--------------------------")
print("el curso de dalto dura:")
# mostrando las diferencia de duracion
print(f" - el curso de soy dalto dura un {diferencia_con_min} % menos que el mas rapido")
print(f" - el curso de soy dalto dura un {diferencia_con_max} % menos que el mas lento")
print(f" - el curso de soy dalto dura un {diferencia_con_promedio} % menos que el mas promedio")
print("--------------------------")

#mostrando la cantidad de espacios vacios que se remueven  en la edicion
print(f" - un curso promedio elimina un {tiempo_vacio_promedio} % de tiempo vacio")
print(f" - este curso elimino el {tiempo_vacio_dalto} % del tiempo vacio")
print("---------------------------")
 
#mostranfo diferencia si los cursos demoran 10 horas
print(f" - ver 10 horas de este curso equivale a ver {otros_cursos_primedio * 100 //dalto_curso / 10} % horas de otros cursos")
print(f" - ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_primedio / 10} % horas de otros cursos")
