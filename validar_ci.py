class Cedula:

    def validar_ci_ruc(numero):
        num_privincias = 24
        total = 0
        if numero.isdigit():  # verifica solo numeros
            if len(numero) == 10 or len(numero) == 13:  # verifica longitud
                if int(numero[0:2]) > 0 and int(numero[0:2]) < num_privincias:  # verifica provincia
                    if int(numero[2]) >= 0 and int(numero[2]) < 6:  # verifica 3er digito ci/ruc persona natural
                        if len(numero) == 10:
                            tipo = 0
                        elif len(numero) == 13:
                            # Los 3 últimos dígitos son 001, 002, etc., dependiendo el nro de locales adicionales
                            if numero[10:13] != '000':
                                tipo = 0
                            else:
                                raise Exception('r.u.c incorrecto')
                    elif int(numero[2]) == 6 and numero[
                                                 10:13] != '000':  # verifica tercer digito ruc publicos y los 3 ultimos
                        tipo = 1
                    elif int(numero[2]) == 9 and numero[
                                                 10:13] != '000':  # verifica tercer digito ruc juridicos y extranjeros sin cedula
                        tipo = 2
                    else:
                        raise Exception('Tercer digito no valido')
                else:
                    raise Exception('Codigo de provincia no valido')
            else:
                raise Exception("Tiene que ser solo numeros")
        else:
            raise Exception("Longitud incorrecta")

        if tipo == 0:  # c.i y r.u.c persona natural
            base = 10
            digito_v = int(numero[9])
            coeficiente = (2, 1, 2, 1, 2, 1, 2, 1, 2)
        elif tipo == 1:  # r.u.c. publicos
            base = 11
            digito_v = int(numero[8])
            coeficiente = (3, 2, 7, 6, 5, 4, 3, 2)
        elif tipo == 2:  # r.u.c. juridicos y extranjeros sin cedula
            base = 11
            digito_v = int(numero[9])
            coeficiente = (4, 3, 2, 7, 6, 5, 4, 3, 2)

        for i in range(0, len(coeficiente)):
            subtotal = int(numero[i]) * coeficiente[i]
            if tipo == 0:
                # Multiplica cada dígito de la c.i por el coeficiente, si es mayor a 10 suma entre digitps
                total += subtotal if subtotal < 10 else int(str(subtotal)[0]) + int(str(subtotal)[1])
            else:
                total += subtotal

        mod = total % base
        val = base - mod if mod != 0 else 0
        if val == digito_v:
            return True
        else:
            raise Exception("c.i/ruc incorrecto")