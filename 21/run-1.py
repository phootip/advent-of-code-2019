from computer import Computer

class Robot():
    def __init__(self,program):
        self.com = Computer(program)
        self.buffer = ''

    def load_outputs(self):
        while self.com.outputs:
            c = self.com.get_output()
            if c > 1000:
                print(c)
            self.buffer += chr(c)
        if self.buffer[-2:] == '\n\n':
            print(self.buffer)
            self.buffer = ''
            
    def str_to_ascii(self, string):
        if len(string) > 20:
            print(f'''Error too long didn't read : {len(string)}''')
        result = []
        for char in string:
            result.append(ord(char))
        result.append(10)
        return result

    def run(self):
        command = self.get_command()
        self.com.inputs += command
        while not (self.com.need_input or self.com.halted):
            self.com.execute()
            self.load_outputs()
    
    def get_command(self):
        command = []
        command += self.str_to_ascii('NOT A T')
        command += self.str_to_ascii('NOT B J')
        command += self.str_to_ascii('OR J T')
        command += self.str_to_ascii('NOT C J')
        command += self.str_to_ascii('OR T J')
        command += self.str_to_ascii('AND D J')
        command += self.str_to_ascii('WALK')
        return command

