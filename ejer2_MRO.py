class Scanner:
    def scan(self):
        print('scan() method from Scanner class')

class Printer:
    def print(self):
        print('print() method from Printer class')

class Fax:
    def send(self):
        print('send() method from Fax class')
    
    def print(self):
        print('print() method from Fax class')

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

# Instantiate MFD_SPF and call the methods
mfd_spf = MFD_SPF()
print("MFD_SPF:")
mfd_spf.scan()
mfd_spf.print()
mfd_spf.send()

# Instantiate MFD_SFP and call the methods
mfd_sfp = MFD_SFP()
print("\nMFD_SFP:")
mfd_sfp.scan()
mfd_sfp.print()
mfd_sfp.send()