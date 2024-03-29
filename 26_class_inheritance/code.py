class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.by_connected = connected_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r} ({self.connected_by})'
    
    def disconnected(self):
        self.connected = False
        print('Disconnected.')

# printer = Device("Printer", "USB")
# print(printer)
# printer.disconnected()

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        # super() method allows us to copy the first section of the parent class.
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

        def __str__(self):
            return f'{super(). __str__()} ({self.remaining_pages} pages remaining)'
        

        def print(self, pages):
            if not self.connected:
                print('Your printer is not connected!')
                return
            print(f'Printing {pages} pages.')
            self.remaining_pages -= pages

printer = Printer('Printer', 'USB', 500)
printer.print(20)

print(printer)

