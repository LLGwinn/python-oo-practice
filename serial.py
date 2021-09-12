"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        # Creates starting serial number based on 'start' parameter
        self.start = start
        self.currentSerialNumber = self.start - 1

    def __repr__(self):
        # Show representation of serial number instance
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        # Returns current serial number incremented by 1
        self.currentSerialNumber += 1
        return self.currentSerialNumber
        
    def reset(self):
        # Resets value of current serial number to starting number
        self.currentSerialNumber = self.start - 1
        

