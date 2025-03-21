from datetime import time, datetime, timedelta

funcionario_que_sai_cedo_na_terca = "Adriel"

class Vendedor:
    def __init__(self, nome, horario_semana, horario_semana_reduzido, horario_sexta, horario_sabado, almoco, almoco_reduzido, intervalos, trabalha_no_sabado):
        self.nome                     = nome
        self.horario_semana           = self._converter_horario(horario_semana)
        self.horario_semana_reduzido  = self._converter_horario(horario_semana_reduzido)
        self.horario_sexta            = self._converter_horario(horario_sexta)
        self.horario_sabado           = self._converter_horario(horario_sabado)
        self.almoco                   = self._converter_horario(almoco)
        self.almoco_reduzido          = self._converter_horario(almoco_reduzido)
        self.intervalos               = [self._str_para_time(h) for h in intervalos]
        self.trabalha_no_sabado       = trabalha_no_sabado

    def _converter_horario(self, horario):
        return tuple(self._str_para_time(h) for h in horario)

    def _str_para_time(self, horario):
        return datetime.strptime(horario, "%H:%M").time()



    def _obter_horario_por_dia(self, dia_semana):
        resposta = (None,None)
        if dia_semana == 6: # 6 = domingo 
          pass
        elif dia_semana == 5:  # 5 = Sábado
            resposta = self.horario_sabado if self.trabalha_no_sabado else (None, None)
        elif dia_semana == 4:
          resposta = self.horario_sexta
        elif dia_semana == 2: # terça
            if self.nome == funcionario_que_sai_cedo_na_terca:
                
        else:
            resposta =  self.horario_semana_reduzido if self.trabalha_no_sabado else self.horario_semana
        print('o horario do dia é:',resposta)
        return resposta
        

    def disponivel(self, horario, dia_semana):
        horario = self._str_para_time(horario)
        entrada, saida = self._obter_horario_por_dia(dia_semana)
        print('entrada é: ', entrada)
        print('saida é:', saida)
        if entrada is None or saida is None:
            return False

        # Checar se está no horário de trabalho
        if not (entrada <= horario < saida):
            return False

        # Checar se está no horário de almoço
        almoco_inicio, almoco_fim = self.almoco
        if almoco_inicio <= horario < almoco_fim:
            return False

        # Checar se está em algum intervalo
        if horario in self.intervalos:
            return False

        return True

    def horarios_disponiveis(self, dia_semana):
        entrada, saida = self._obter_horario_por_dia(dia_semana)

        if entrada is None or saida is None:
            return []

        horarios_livres = []
        atual = datetime.combine(datetime.today(), entrada)
        fim = datetime.combine(datetime.today(), saida)
        almoco_inicio,almoco_fim = self.almoco

        while atual < fim:
            hora_atual = atual.time()

            if not (almoco_inicio <= hora_atual < almoco_fim) and hora_atual not in self.intervalos:
                horarios_livres.append(hora_atual.strftime("%H:%M"))

            atual += timedelta(minutes=15)

        return horarios_livres
    

def listar_disponiveis(vendedores, horario, dia_semana):
    return [v.nome for v in vendedores if v.disponivel(horario, dia_semana)]

# Exemplo de uso
vendedores = [
    Vendedor(
        nome="Adiara",
        horario_semana          = ("08:00", "18:00"),
        horario_semana_reduzido = ("08:00", "17:00"),
        horario_sabado          = ("08:00", "12:00"),
        almoco                  = ("12:00", "13:00"),
        intervalos              = ["09:30"],
        trabalha_no_sabado      = True
    ),
    Vendedor(
        nome="Adriel",
        horario_semana          = ("08:00", "19:00"),
        horario_semana_reduzido = ("08:00", "18:00"),
        horario_sabado          = ("08:00", "12:00"),
        almoco                  = ("12:00", "13:00"),
        intervalos              = ["15:45"],
        trabalha_no_sabado      = False
    ),
    Vendedor(
        nome="Cristina",
        horario_semana          = ("10:00", "19:00"),
        horario_semana_reduzido = ("10:00", "16:00"),
        horario_sabado          = ("09:00", "14:00"),
        almoco                  = ("13:00", "14:00"),
        intervalos              = ["16:30"],
        trabalha_no_sabado=False
    ),
    Vendedor(
        nome="Ellen",
        horario_semana          = ("08:30", "17:30"),
        horario_semana_reduzido = ("08:30", "15:30"),
        horario_sabado          = ("09:00", "12:00"),
        almoco                  = ("12:30", "13:30"),
        intervalos              = ["20:30"],
        trabalha_no_sabado      = False
    ),
    Vendedor(
        nome="Elaine",
        horario_semana          = ("09:00", "18:00"),
        horario_semana_reduzido = ("09:00", "16:00"),
        horario_sabado          = ("08:00", "13:00"),
        almoco                  = ("12:00", "13:00"),
        intervalos              = ["20:15"],
        trabalha_no_sabado      = False
    ),
    Vendedor(
        nome="Mariele",
        horario_semana          = ("09:00", "18:00"),
        horario_semana_reduzido = ("09:00", "16:00"),
        horario_sabado          = ("08:00", "13:00"),
        almoco                  = ("12:00", "13:00"),
        intervalos              = ["20:00"],
        trabalha_no_sabado      = False
    ),
    Vendedor(
        nome="Tataine",
        horario_semana          = ("09:00", "18:00"),
        horario_semana_reduzido = ("09:00", "16:00"),
        horario_sabado          = ("08:00", "13:00"),
        almoco                  = ("12:00", "13:00"),
        intervalos              = ["19:30"],
        trabalha_no_sabado      = False
    ),
    Vendedor(
        nome="George",
        horario_semana          = ("09:00", "18:00"),
        horario_semana_reduzido = ("09:00", "16:00"),
        horario_sabado          = ("08:00", "13:00"),
        almoco                  = ("12:00", "13:00"),
        intervalos              = ["15:30"],
        trabalha_no_sabado      = False
    ),
    Vendedor(
        nome="Igor",
        horario_semana          = ("09:00", "18:00"),
        horario_semana_reduzido = ("09:00", "16:00"),
        horario_sabado          = ("08:00", "13:00"),
        almoco                  = ("12:00", "13:00"),
        intervalos              = ["15:45"],
        trabalha_no_sabado      = True
    )
]


# Testando no sábado
dia_semana = datetime.today().weekday()  # 5 = Sábado
print(listar_disponiveis(vendedores, "10:00", dia_semana))

# Ver horários disponíveis para João na segunda-feira (0 = Segunda)
print(vendedores[0].horarios_disponiveis(0))






