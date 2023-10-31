class TimeInterval:
    max_hour = 99
    max_min  = 60
    max_sec  = 60
    
    def __init__(self, hour, min, sec):
        try:
            self.hour = int(hour)
            self.min   = int(min)
            self.sec   = int(sec)
            
            if self.hour > TimeInterval.max_hour or self.min> TimeInterval.max_min or self.sec> TimeInterval.max_sec:
                raise ValueError('Los valores introducidos no son correctos')
                
        except (TypeError):
            raise TypeError('El valor introducido no es un numero')            
        
    def __repr__(self):
        return (f'{str(self.hour).zfill(2)}:{str(self.min).zfill(2)}:{str(self.sec).zfill(2)}')      
        
    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Unsupported operand type for +: TimeInterval and {}".format(type(other).__name__))
            
        hour = self.hour + other.hour
        minutos = self.min + other.min
        if minutos > TimeInterval.max_min:
            minutos  -= 60
            hour += 1
        sec = self.sec + other.sec
        if sec > TimeInterval.max_min:
            sec -= 60
            minutos +=1
        if hour > TimeInterval.max_hour:
            raise ValueError("La suma excede las 100 horas") 
        return TimeInterval(hour, minutos, sec)          
        
    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Unsupported operand type for -: TimeInterval and {}".format(type(other).__name__))
            
        minutos = 0
        hour = 0
        
        sec = self.sec - other.sec
        if sec < 0:
            sec += 60
            minutos = -1

        minutos += self.min - other.min
        if minutos < 0: 
            minutos += 60
            hour = -1
        
        hour += self.hour - other.hour
        if hour < 0:
            raise ValueError("El intervalo restado es mayor, invierta el orden de la resta")
        return TimeInterval(hour, minutos, sec)
    
    def __mul__(other, integer):
        try:
            if not isinstance(other, TimeInterval):
                raise TypeError("Unsupported operand type for *: TimeInterval and {}".format(type(other).__name__))
            integer = int(integer)
            total_sec = (other.hour * 3600 + other.min *60 + other.sec)*2
            hour, reminder = divmod(total_sec,3600)
            minutos,sec = divmod(reminder,60)
            
            if hour > TimeInterval.max_hour:
                raise ValueError("La multiplicacion excede las 100 horas")
            
            return TimeInterval(hour, minutos, sec)
            
        except TypeError:
            print('Debe multiplicar por un entero')       
    
    
ti1=TimeInterval(10,58,40)
ti2=TimeInterval(5,45,59)
suma= ti1+ti2
resta = ti1 - ti2
mult = ti1*2
print(f'{suma} suma')
print(f'{resta} resta')
print(f'{mult} multiplicacion')
    