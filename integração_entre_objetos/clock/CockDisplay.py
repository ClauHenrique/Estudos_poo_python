from integração_entre_objetos.display.NumberDisplay import NumberDisplay


class ClockDisplay:
    def __init__(self, *args):
        self.displayString = ""

        # o metodo construtor pode iniciar a classe com horario ja configurado
        if len(args) == 3:
            self.hours = NumberDisplay(24)
            self.minutes = NumberDisplay(60)
            self.seconds = NumberDisplay(60)
            # hours, minuts e seconds
            self.setTime(args[0], args[1], args[2])

        # caso nenhum parametro seja passado a classe é iniciada as 00:00:00
        else:
            self.hours = NumberDisplay(24)
            self.minutes = NumberDisplay(60)
            self.seconds = NumberDisplay(60)
            self.updateDisplay()

    # metodo que faz o relogio avançar
    def timeTick(self):
        self.seconds.increment()
        if self.seconds.getValue() == 0:
            self.minutes.increment()
            if self.minutes.getValue() == 0:
                self.hours. increment()

        self.updateDisplay()

    # ajusta a hora de acordo com o que é passado como parametro
    def setTime(self, hour, minute, second):
        self.hours.setValue(hour)
        self.minutes.setValue(minute)
        self.seconds.setValue(second)
        self.updateDisplay()

    def getTime(self):
        return self.displayString

    def updateDisplay(self):
        self.displayString = self.hours.getDisplayValue() + \
                             ":" + self.minutes.getDisplayValue() + ":" + self.seconds.getDisplayValue()

