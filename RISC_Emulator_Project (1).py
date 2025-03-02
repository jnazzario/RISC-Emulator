class SimpleRISC:
    def __init__(self):
        # Initialize registers, memory, and program counter
        self.registers = {'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0}
        self.memory = {}
        self.pc = 0  # Program counter
    
    def execute(self, instructions):
        # Loop until program counter goes out of range
        while self.pc < len(instructions):
            # Fetch instruction
            instruction = instructions[self.pc].strip()
            parts = instruction.split()
            opcode = parts[0]

            # Decode and execute instructions
            if opcode == "LOAD":
                register = parts[1]
                value = int(parts[2])
                self.registers[register] = value
            
            elif opcode == "STORE":
                src = parts[1]
                addr = int(parts[2])
                self.memory[addr] = self.registers[src]
            
            elif opcode == "ADD":
                dest = parts[1]
                src1 = parts[2]
                src2 = parts[3]
                self.registers[dest] = self.registers[src1] + self.registers[src2]
            
            elif opcode == "SUB":
                dest = parts[1]
                src1 = parts[2]
                src2 = parts[3]
                self.registers[dest] = self.registers[src1] - self.registers[src2]
            
            elif opcode == "MUL":
                dest = parts[1]
                src1 = parts[2]
                src2 = parts[3]
                self.registers[dest] = self.registers[src1] * self.registers[src2]
            
            elif opcode == "JUMP":
                address = int(parts[1])
                self.pc = address - 1  # Subtract 1 because pc increments later
            
            elif opcode == "BRANCH_IF_ZERO":
                register = parts[1]
                address = int(parts[2])
                if self.registers[register] == 0:
                    self.pc = address - 1  # Subtract 1 because pc increments later
            
            elif opcode == "BRANCH_IF_NOT_ZERO":
                register = parts[1]
                address = int(parts[2])
                if self.registers[register] != 0:
                    self.pc = address - 1  # Subtract 1 because pc increments later
            
            elif opcode == "HALT":
                print("Program halted.")
                break
            
            else:
                print(f"Unknown instruction: {opcode}")
            
            # Increment the program counter
            self.pc += 1
    
    def print_state(self):
        print("Registers:", self.registers)
        print("Memory:", self.memory)
        print("Program Counter:", self.pc)


# Get instructions from user
def get_user_program():
    print("This program executes a series of instructions given by the user.")
    print("The instructions are as follows:")
    print("LOAD:  Loads a value into the register")
    print("STORE: Stores a value in memory")
    print("ADD:   Adds two values and stores the result in a register")
    print("MUL:   Multiplies two values and stores the result in a register")
    print("JUMP:  Jumps to a specific address")
    print("BRANCH_IF_ZERO: Branches to a specific address if a register is zero")
    print("BRANCH_IF_NOT_ZERO: Branches to a specific address if a register is not zero")
    print("HALT:  Halts the program")
    print("Enter your program, one instruction per line. Type 'RUN' to execute.")
    program = []
    while True:
        line = input(">> ").strip()
        if line.upper() == "RUN":
            break
        program.append(line)
    return program


# Main execution
emulator = SimpleRISC()
user_program = get_user_program()
emulator.execute(user_program)
emulator.print_state()
