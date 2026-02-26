# ============================================================
#         INSTITUTO TECNOLÓGICO SUPERIOR PROGRESO
#
#                      Carrera:
#         Ingeniería en Sistemas Computacionales
#
#                      Materia:
#               Lenguajes y automatas I
#
#                     Actividad:
#   Análisis de documentos con expresiones regulares
#
#                      Docente:
#               Ulises Morales Ramirez
#
#                       Alumno:
#            David Ezequiel Caballero González
#
#                  Fecha de entrega:
#            Jueves 19 de febrero de 2026
# ============================================================

import re
from pathlib import Path

# LECTURA DEL ARCHIVO TXT texto_maestro.txt
archivo = Path("contraseña.txt")

# GUARDAR EL CONTENIDO DEL ARCHIVO EN UNA VARIABLE
contenido = archivo.read_text(encoding="utf-8")

#---------------------------------------------------------------------#

regex_contraseña = r'\b\w(\w)'

#---- REGEXs PARA EXTRAER LOS DATOS ----#
# REGEX PARA EXTRAER ENCABEZADOS EN MAYUSCULAS
regex_encabezados = r'[A-ZÁÉÍÓÚÑ()]+(?:\s+[A-ZÁÉÍÓÚÑ()]+)+$'

# REGEX PARA EXTRAER FECHAS
regex_fechas = r'\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}'

# REGEX PARA EXTRAER CORREOS ELECTRÓNICOS
regex_correos = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# REGEX NUMEROS TELEFONICOS (YUCATÁN) CON LADA 999
regex_telefonos = r'\b999\d{7}\b'

# REGEX PARA EXTRAER IDENTIFICADORES ALFANUMÉRICOS 
regex_identificadores = r'\b(?=[A-Z0-9_]{8,12}\b)(?=[A-Z0-9_]*[A-Z])(?=[A-Z0-9_]*\d)[A-Z0-9_]{8,12}\b'

# REGEX PARA EXTRAER LINEAS CON PALABRAS REPETIDAS
regex_palabras_repetidas = r'^.*\b([A-Za-z0-9_]+)\b.*\b\1\b.*$'

# REGEX PARA EXTRAER RFC Y CURP
regex_rfc = r'\b[A-ZÑ&]{3,4}\d{6}[A-Z0-9]{3}\b'
regex_curp = r'\b[A-Z][AEIOU][A-Z]{2}\d{6}[HM][A-Z]{5}[A-Z0-9]\d\b'

# REGEX PARA EXTRAER LINEAS COMPLETAS CON LA PALABRA "ERROR"
regex_lineas_error = r'^.*ERROR.*$'


#---------------------------------------------------------------------#

#------------------ MENÚ DE OPCIONES DE EXTRACCIÓN ------------------#

while True:

    print("Seleccione el tipo de datos a extraer:")
    print("0. Contraseña")
    print("1. Encabezados en mayúsculas")
    print("2. Fechas")
    print("3. Correos electrónicos")
    print("4. Números telefónicos")
    print("5. Identificadores alfanuméricos")
    print("6. Lineas con palabras repetidas")
    print("7. RFC y CURP")
    print("8. Lineas completas con la palabra 'ERROR'")
    print("9. Todos los modos de extracción")
    print("10. Salir")

    opción = input("Ingrese el número de la opción deseada: ")

#-------------------- EXTRACCIÓN DE LOS DATOS ---------------------#
    # EXTRACCIÓN DE LOS ENCABEZADOS
    if opción == "0":
        contraseña = re.findall(regex_contraseña, contenido, re.MULTILINE)
        print("Contraseña encontrada:")
        for contraseña in contraseña:
            print(contraseña)

    if opción == "1":
        encabezados = re.findall(regex_encabezados, contenido, re.MULTILINE)

        #IMPRIMIR ENCABEZADOS EXTRAÍDOS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de encabezados:")
        print("[A-ZÁÉÍÓÚÑ()]+(?:\s+[A-ZÁÉÍÓÚÑ()]+)+$")
        print("========================================================")
        print("========================================================")
        print("El regex para encabezados en mayúsculas se compone de los siguientes elementos:")
        print("- [A-ZÁÉÍÓÚÑ()]+: Coincide con una o más letras mayúsculas, incluyendo caracteres acentuados y paréntesis")
        print("- (?:\s+[A-ZÁÉÍÓÚÑ()]+)+: Coincide con uno o más grupos de espacios seguidos de letras mayúsculas, permitiendo encabezados compuestos por varias palabras")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("NOTICIA INSTITUCIONAL TECNM CAMPUS PROGRESO")
        print("CONTACTO INSTITUCIONAL Y NO TAN OFICIAL")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("Tecnológico Nacional de México")
        print("Campus Progreso")
        print("Encabezado123")
        print("========================================================")
        print("========================================================")
        print("Encabezados encontrados:")
        for encabezado in encabezados:
            print(encabezado)

        # VERIFICACIÓN
        if encabezados == []:
            print("No se encontraron encabezados en mayúsculas")

    # EXTRACCIÓN DE LAS FECHAS
    if opción == "2":
        fechas = re.findall(regex_fechas, contenido, re.MULTILINE)

        # IMPRIMIR FECHAS EXTRAÍDAS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de fechas:")
        print("- r\"(\b\d{2}/\d{2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b)") 
        print("========================================================")
        print("========================================================")
        print("El regex para fechas se compone de los siguientes elementos:")
        print("- r\"\b\d{2}/\d{2}/\d{4}\b: Coincide con fechas en formato DD/MM/YYYY")
        print("- r\"\b\d{4}-\d{2}-\d{2}: Coincide con fechas en formato YYYY-MM-DD")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("01/02/2025")
        print("28/02/2023")
        print("2022-10-15")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("1/2/2025 (formato incorrecto)")
        print("2025/02/01 (formato incorrecto)")
        print("Febrero 2025 (texto)")
        print("20251015 (sin separadores)")
        print("========================================================")
        print("========================================================")
        print("Fechas encontradas:")
        for fechas in fechas:
            print(fechas)

        # VERIFICACIÓN
        if fechas == []:
            print("No se encontraron fechas validas")

    # EXTRACCIÓN DE LOS CORREOS ELECTRÓNICOS
    if opción == "3":
        correos = re.findall(regex_correos, contenido, re.MULTILINE)

        # IMPRIMIR CORREOS ELECTRÓNICOS EXTRAÍDOS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de correos electronicos")
        print("\\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\\b")
        print("========================================================")
        print("========================================================")
        print("El regex para correos electrónicos se compone de los siguientes elementos:")
        print("- \\b[a-zA-Z0-9._%+-]+: Coincide con el nombre de usuario del correo, que puede contener letras, números y algunos caracteres especiales")
        print("- @: Coincide con el símbolo '@' que separa el nombre de usuario del dominio")
        print("- [a-zA-Z0-9.-]+: Coincide con el dominio del correo, que puede contener letras, números, puntos y guiones")
        print("- \.[a-zA-Z]{2,}\\b: Coincide con la extensión del dominio, que debe comenzar con un punto seguido de al menos dos letras")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("usuario@dominio.com")
        print("soporte@regex.mx")
        print("difusion@tecnm.mx")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("usuario@dominio (sin TLD)")
        print("@dominio.com (sin usuario)")
        print("usuario.com (sin @)")
        print("usuario@.com (dominio inválido)")
        print("========================================================")
        print("========================================================")
        print("Correos electrónicos encontrados:")
        for correo in correos:
            print(correo)

        # VERIFICACIÓN
        if correos == []:
            print("No se encontraron correos electrónicos")

    # EXTRACCIÓN DE LOS NÚMEROS TELEFÓNICOS
    if opción == "4":
        telefonos = re.findall(regex_telefonos, contenido, re.MULTILINE)

        # IMPRIMIR NÚMEROS TELEFÓNICOS EXTRAÍDOS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de números telefónicos")
        print("\\b999\d{7}\\b")
        print("========================================================")
        print("========================================================")
        print("El regex para números telefónicos se compone de los siguientes elementos:")
        print("- \\b999\d{7}\\b: Coincide con números telefónicos que comienzan con 999 seguidos de 7 dígitos")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("9993124455")
        print("9998675309")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("(999) 312-4455 (formato diferente)")
        print("9985551212 (lada diferente)")
        print("999312445 (muy corto)")
        print("99931244555 (muy largo)")
        print("========================================================")
        print("========================================================")
        print("Números telefónicos encontrados:")
        for telefono in telefonos:
            print(telefono)

        # VERIFICACIÓN
        if telefonos == []:
            print("No se encontraron números telefónicos con lada 999.")

    # EXTRACCIÓN DE LOS IDENTIFICADORES ALFANUMÉRICOS
    if opción == "5":
        identificadores = re.findall(regex_identificadores, contenido, re.MULTILINE)

        # IMPRIMIR IDENTIFICADORES ALFANUMÉRICOS EXTRAÍDOS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de identificadores alfanuméricos")
        print("\\b(?=[A-Z0-9_]{8,12}\\b)(?=[A-Z0-9_]*[A-Z])(?=[A-Z0-9_]*\\d)[A-Z0-9_]{8,12}\\b\"")
        print("========================================================")
        print("========================================================")
        print("El regex para identificadores alfanuméricos se compone de los siguientes elementos:")
        print("- \\b: Límite de palabra")
        print("- (?=[A-Z0-9_]{8,12}\\b): Asegura que el identificador tenga entre 8 y 12 caracteres alfanuméricos o guiones bajos")
        print("- (?=[A-Z0-9_]*[A-Z]): Asegura que el identificador contenga al menos una letra mayúscula")
        print("- (?=[A-Z0-9_]*\\d): Asegura que el identificador contenga al menos un dígito")
        print("- [A-Z0-9_]{8,12}: Coincide con el identificador alfanumérico que cumple con las condiciones anteriores")  
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("SYS2025TEMP")
        print("PROG123456")
        print("SESSION1234")
        print("CONFIG8888")
        print("MORU820101")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("CRISTIAN (solo letras)")
        print("12345678 (solo números)")
        print("ADMIN (muy corto)")
        print("usuario123 (minúsculas)")
        print("ID_ALUMNO_01 (muy largo)")
        print("========================================================")
        print("========================================================")
        print("Identificadores alfanuméricos encontrados:")
        for identificador in identificadores:
            print(identificador)

        # VERIFICACIÓN
        if identificadores == []:
            print("No se encontraron identificadores alfanuméricos.")

    # EXTRACCIÓN DE LAS LINEAS CON PALABRAS REPETIDAS
    if opción == "6":    
        lineas_repetidas = re.findall(regex_palabras_repetidas, contenido, re.MULTILINE)

        # IMPRIMIR LINEAS CON PALABRAS REPETIDAS EXTRAÍDAS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de palabaras repetidas")
        print("^.*\\b([A-Za-z0-9_]+)\\b.*\\b\\1\\b.*$")
        print("========================================================")
        print("========================================================")
        print("El regex para palabaras repetidas se compone de los siguientes elementos:")
        print("- ^.*: Coincide con cualquier texto al inicio de la línea")
        print("- \\b([A-Za-z0-9_]+)\\b: Captura una palabra alfanumérica y la almacena en un grupo de captura")
        print("- .*: Coincide con cualquier texto entre la primera aparición de la palabra y la segunda aparición")
        print("- \\b\\1\\b: Coincide con la misma palabra capturada en el grupo de captura, asegurando que sea una palabra completa")
        print("- .*$: Coincide con cualquier texto al final de la línea")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("La actividad fue tan repetitiva que la palabra actividad se repetía.")
        print("ERROR crítico: el sistema generó otro ERROR.")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("El sistema funciona correctamente.")
        print("Esta línea no tiene duplicados.")
        print("Python es un lenguaje.")
        print("========================================================")
        print("========================================================")
        print("Lineas con palabras repetidas encontradas:")
        for linea in lineas_repetidas:
            print(linea)
        
        # VERIFICACIÓN
        if lineas_repetidas == []:
            print("No se encontraron líneas con palabras repetidas.")

    # EXTRACCIÓN DE RFC Y CURP
    if opción == "7":
        rfc = re.findall(regex_rfc, contenido, re.MULTILINE)
        curp = re.findall(regex_curp, contenido, re.MULTILINE)

        # IMPRIMIR RFC EXTRAÍDOS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de RFC y CURP")
        print("RFC: \\b[A-ZÑ&]{3,4}\\d{6}[A-Z0-9]{3}\\b")
        print("========================================================")
        print("========================================================")
        print("El regex para RFC se compone de los siguientes elementos:")
        print("- \\b: Límite de palabra")
        print("- [A-ZÑ&]{3,4}: Coincide con las primeras 3 o 4 letras mayúsculas del RFC, que pueden incluir la letra Ñ y el símbolo &")
        print("- \\d{6}: Coincide con los 6 dígitos correspondientes a la fecha de nacimiento en formato AAMMDD")
        print("- [A-Z0-9]{3}: Coincide con los últimos 3 caracteres del RFC, que pueden ser letras mayúsculas o dígitos")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("BAJC950101H23")
        print("CAGD960202M45")
        print("MORU820101XXX")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("BAJC950101 (sin homoclave)")
        print("1234567890123")
        print("RFC123")
        print("========================================================")
        print("========================================================")
        print("RFC encontrados:")
        for rfc in rfc:
            print(rfc)

        # VERIFICACIÓN
        if rfc == []:
            print("No se encontraron RFCs válidos.")    

        # IMPRIMIR CURP EXTRAÍDOS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de CURP")
        print("CURP: \\b[A-Z][AEIOU][A-Z]{2}\\d{6}[HM][A-Z]{5}[A-Z0-9]\\d\\b")
        print("========================================================")
        print("========================================================")
        print("El regex para CURP se compone de los siguientes elementos:")
        print("- \\b: Límite de palabra")
        print("- [A-Z]: Coincide con la primera letra mayúscula del CURP, que representa la primera letra del apellido paterno")
        print("- [AEIOU]: Coincide con la segunda letra del CURP, que debe ser una vocal mayúscula")
        print("- [A-Z]{2}: Coincide con las siguientes dos letras mayúsculas del CURP, que representan la primera letra del apellido materno y la primera letra del nombre")
        print("- \\d{6}: Coincide con los 6 dígitos correspondientes a la fecha de nacimiento en formato AAMMDD")
        print("- [HM]: Coincide con la letra mayúscula 'H' para hombres o 'M' para mujeres, que representa el género del individuo")
        print("- [A-Z]{5}: Coincide con las siguientes 5 letras mayúsculas del CURP, que representan las primeras letras de los apellidos y el nombre, así como una letra interna para evitar duplicados")
        print("- [A-Z0-9]\\d: Coincide con el último carácter del CURP, que puede ser una letra mayúscula o un dígito, seguido de un dígito que representa un número de homoclave para evitar duplicados")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("BAJC950101HYNSRS09")
        print("CAGD960202MYNLND00")
        print("XEXX010101MXXX000")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("BAJC950101")
        print("123456789012345678")
        print("CURP123")
        print("========================================================")
        print("========================================================")
        print("CURP encontrados:")
        for curp in curp:
            print(curp)
        
        # VERIFICACIÓN
        if curp == []:
            print("No se encontraron CURPs válidos.")

    # EXTRACCIÓN DE LINEAS COMPLETAS CON LA PALABRA "ERROR"
    if opción == "8":
        lineas_error = re.findall(regex_lineas_error, contenido, re.MULTILINE)

        # IMPRIMIR LINEAS COMPLETAS CON LA PALABRA "ERROR" EXTRAÍDAS
        print("========================================================")
        print("========================================================")
        print("Regex utilizado para la extracción de líneas completas con la palabra 'ERROR'")
        print("^.*ERROR.*$")
        print("========================================================")
        print("========================================================")
        print("El regex para líneas completas con la palabra 'ERROR' se compone de los siguientes elementos:")
        print("- ^.*: Coincide con cualquier texto al inicio de la línea")
        print("- ERROR: Coincide con la palabra 'ERROR' en cualquier parte de la línea")
        print("- .*$: Coincide con cualquier texto al final de la línea")
        print("========================================================")
        print("========================================================")
        print("Ejemplos de coincidencias correctas:")
        print("ERROR: No se pudo procesar la solicitud.")
        print("El sistema detectó un ERROR crítico.")
        print("========================================================")
        print("========================================================")
        print("Ejemplos que NO deben coincidir:")
        print("El sistema funciona correctamente.")
        print("Advertencia del sistema.")
        print("Proceso completado.")
        print("========================================================")
        print("========================================================")
        print("Lineas completas con la palabra 'ERROR' encontradas:")
        for linea in lineas_error:
            print(linea)

        # VERIFICACIÓN
        if lineas_error == []:
            print("No se encontraron líneas completas con la palabra 'ERROR'.")     

    # EXTRACCIÓN DE TODOS LOS MODOS DE EXTRACCIÓN
    if opción == "9":
        # ENCABEZADOS EN MAYÚSCULAS
        encabezados = re.findall(regex_encabezados, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("Encabezados encontrados:")
        for encabezado in encabezados:
            print(encabezado)

        # FECHAS ENCONTRADAS
        fechas = re.findall(regex_fechas, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("Fechas encontradas:")
        for fecha in fechas:
            print(fecha)

        # CORREOS ELECTRÓNICOS ENCONTRADOS    
        correos = re.findall(regex_correos, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("Correos electrónicos encontrados:")
        for correo in correos:
            print(correo)
        
        # NÚMEROS TELEFÓNICOS ENCONTRADOS
        telefonos = re.findall(regex_telefonos, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("Números telefónicos encontrados:")
        for telefono in telefonos:
            print(telefono)

        # IDENTIFICADORES ALFANUMÉRICOS ENCONTRADOS
        identificadores = re.findall(regex_identificadores, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("Identificadores alfanuméricos encontrados:")
        for identificador in identificadores:
            print(identificador)

        # LINEAS CON PALABRAS REPETIDAS ENCONTRADAS
        lineas_repetidas = re.findall(regex_palabras_repetidas, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("Lineas con palabras repetidas encontradas:")
        for linea in lineas_repetidas:
            print(linea)

        # RFC Y CURP ENCONTRADOS
        rfc = re.findall(regex_rfc, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("RFC encontrados:")
        for rfc in rfc:
            print(rfc)

        curp = re.findall(regex_curp, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("CURP encontrados:")
        for curp in curp:
            print(curp)

        # LINEAS COMPLETAS CON LA PALABRA "ERROR" ENCONTRADAS
        lineas_error = re.findall(regex_lineas_error, contenido, re.MULTILINE)
        print("========================================================")
        print("========================================================")
        print("Lineas completas con la palabra 'ERROR' encontradas:")
        for linea in lineas_error:
            print(linea)

    # SALIR DEL PROGRAMA
    if opción == "10":
        print("Saliendo del programa.")
        break

#---------------------------------------------------------------------#

#--------- REFERENCIAS DE LOS REGEXs UTILIZADOS EN EL PROGRAMA ---------#
# - Hoja de referencia de sintaxis de expresiones regulares - JavaScript | MDN. (2025, June 24). 
#   https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet
#
# - Regular Expressions cheat sheet. (n.d.). Cheatography. 
#   https://cheatography.com/davechild/cheat-sheets/regular-expressions/#google_vignette
#
# - Dib, F. (n.d.). regex101: build, test, and debug regex. Regex101. 
#   https://regex101.com/
#
# - Regular Expression Tutorial. (n.d.). Gist. 
#  https://gist.github.com/Mark33Mark/cfb5f6157d0ea885de2073237bc09e8b
#
# - Regex tutorial. (n.d.). Gist. 
#  https://gist.github.com/ahmadelgamal/d3ea09a794856a386aeb949ef7a91f4e