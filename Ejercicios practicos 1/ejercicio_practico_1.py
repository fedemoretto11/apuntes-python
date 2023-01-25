# Curso Dalto
# Duracion 1.5 hs // Crudo 3.5 hs
# Demas Cursos
# Duracion minima 2.5 hs // Maxima 7 hs // Promedio 4 hs // Crudo promedio 5 hs

dalto = {
    'duracion': 1.5,
    'crudo': 3.5
}

otros_cursos = {
    'duracion_minima': 2.5,
    'duracion_maxima': 7,
    'promedio': 4,
    'crudo': 5
}
# 1) Diferencia curso Dalto y:
#     a) + rapido
#     b) + lento
#     c) promedio

diferencia_con_minima = float(otros_cursos.get('duracion_minima')) - float(dalto.get('duracion'))
diferencia_con_maxima = float(otros_cursos.get('duracion_maxima')) - float(dalto.get('duracion'))
diferencia_con_promedio = float(otros_cursos.get('promedio')) - float(dalto.get('duracion'))
print('------------------------------------------')
print(f'El curso de dalto dura {diferencia_con_minima} hora/s menos que el de menor duracion de los otros cursos ')
print(f'El curso de dalto dura {diferencia_con_maxima} hora/s menos que el de mayor duracion de los otros cursos ')
print(f'El curso de dalto dura {diferencia_con_promedio} hora/s menos que el promedio de los otros cursos ')
print('------------------------------------------')

# 2) Porcentaje de materia inservible que se reduce en:
#     a)el promedio de los otros cursos
#     b) el curso de dalto

reduccion_otros = (float(otros_cursos.get('crudo')) - float(otros_cursos.get('promedio'))) * 100 / float(otros_cursos.get('crudo'))
reduccion_dalto = (float(dalto.get('crudo')) - float(dalto.get('duracion'))) * 100 // float(dalto.get('crudo'))

print(f'Los otros cursos con las ediciones se reducen en un {reduccion_otros} %')
print(f'El curso de Dalto con las ediciones se reduce en un {reduccion_dalto} %')
print('------------------------------------------')

# 3)
# a) 10 horas de este curso equivalen a cuantas de los otros
# b) y 10 de los otros a cuantas de este?
promedio_otros = float(otros_cursos.get('promedio'))
promedio_dalto = float(dalto.get('duracion'))
print(f'Ver 10 horas de este curso equivale a ver {promedio_otros * 100 // promedio_dalto / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {promedio_dalto * 100 // promedio_otros / 10} horas de este curso')
print('------------------------------------------')