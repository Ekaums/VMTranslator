import os
import glob
import sys
import regex as re

global j
j = 0


# Parser: Determine which command is present. Returns the instruction
def ParseArgs(inst):
    
    Pattern = r"^(.*?)(?=\/|$)"  # Match up to end of line / up to a comment
    
    if (inst[0] != "\n") and (inst[0] != "/"):
        match = re.search(Pattern, inst)
        match = (match.group()).strip()
        return match
    else:
        return


# Initialize data
def initialize():
    
    content = []
    length = len(sys.argv)
    
    #Initializtion
    if length != 2: 
        sys.exit("Error: Provide a File/Directory")
    else:
        
        [name] = sys.argv[1:]  # Unpack full file/directory name to variable
        
        OutName = name.split(".")[0]  # Get file/directory name, without extension
        OutName += ".asm"  # Used for output
    
        
        if os.path.isfile(name):  # If this is a file:
            with open(name) as f:
                for line in f:
                    if ParseArgs(line):
                        content.append(ParseArgs(line))
                        
        else:  # This is a directory
            paths = glob.glob(os.path.join(name, '*'))  # Get all files in this directory
                    
            for file_path in paths:  # Go through every file
                with open(file_path) as f:
                    for line in f:
                        if ParseArgs(line):
                            content.append(ParseArgs(line))
                    
            
    global SymbolName
    SymbolName = OutName  # Need this name to use for static variables
    
    return content, OutName



# Translator: Translate each VM command to assembly
class Translator:
    
    @staticmethod
    def push(segment, i=None):
        #Initializing
        segment = segment.lower()
        
        if segment == "local":
            segment = "LCL"
        if segment == "argument":
            segment = "ARG"
        if segment == "this":
            segment = "THIS"
        if segment == "that":
            segment = "THAT"
        
        if i is None:  # Used for saving state of functions
            line = f"// push {segment}\n"
            
            # Get value and insert atop stack
            line += f"@{segment}\n"
            line += "D = M\n"
            line += "@SP\n"
            line += "A = M\n"
            line += "M = D\n"
            
            # Increment stack
            line += "@SP\n"
            line += "M = M + 1\n"
            
            line += "\n"
            return line
        
        
        line = f"// push {segment} {i}\n"
        
        
        if segment == "constant":
                
            # Access i
            line += f"@{i}\n"
            line += "D = A\n"
                
            # Insert i atop stack
            line += "@SP\n"
            line += "A = M\n"
            line += "M = D\n"
                
            # Increment stack
            line += "@SP\n"
            line += "M = M + 1\n"
            
            line += "\n"
            return line
            
                
        else:  # For lcl, arg, this, that, temp, pointer, and static
            
            # Determine address to push from
            
            if segment == "pointer":  # If pointer, go to this/that address
                if i == "0":
                    line += "@THIS\n"
                else:  ## i == 1
                    line += "@THAT\n"
            
            elif segment == "static":  # If static, simply go to address
                line += f"@{SymbolName}.{i}\n"
                
            elif segment == "temp":  # If temp, use base address of 5
                line += "@5\n"  
                line += "D = M\n" 
                line += f"@{i}\n"
                line += "D = D + A\n"
                line += "A = D\n"
                
            else:  # Otherwise, get segment and number for address
                line += f"@{segment}\n"    
                line += "D = M\n" 
                line += f"@{i}\n"
                line += "D = D + A\n"
                line += "A = D\n"
                
                
            # Then, get value to push from this address
            line += "D = M\n"
            
            # Go to stack, push value
            line += "@SP\n"
            line += "A = M\n"
            line += "M = D\n"
            
            # Increment stack
            line += "@SP\n"
            line += "M = M + 1\n"
            
            line += "\n"
            return line
        


    @staticmethod
    def pop(segment, i):
            
        # Initializing
        segment = segment.lower()
        line = f"// pop {segment} {i}\n"
        
        if segment == "local":
            segment = "LCL"
        elif segment == "argument":
            segment = "ARG"
        elif segment == "this":
            segment = "THIS"
        elif segment == "that":
            segment = "THAT"

        # Determine address to pop to
        if segment == "pointer":  # If pointer, go to this/that address
            if i == "0":
                line += "@THIS\n"
            else:  ## i == 1
                line += "@THAT\n"
            line += "D = A\n"
        
        elif segment == "static":  # If static, simply go to address
            line += f"@{SymbolName}.{i}\n"
            line += "D = A\n"
            
        elif segment == "temp":  # If temp, use base address of 5
            line += "@5\n"  
            line += "D = M\n" 
            line += f"@{i}\n"
            line += "D = D + A\n"

        else:  # Otherwise, get segment and number for address
            line += f"@{segment}\n"    
            line += "D = M\n" 
            line += f"@{i}\n"
            line += "D = D + A\n"

        # Store address in temp variable
        line += "@Pop\n"
        line += "M = D\n"
        
        # Get value from stack
        line += "@SP\n"
        line += "M = M - 1\n"
        line += "A = M\n"
        line += "D = M\n"
        
        # Pop to location
        line += "@Pop\n"
        line += "A = M\n"
        line += "M = D\n"
        
        line += "\n"
        return line



    @staticmethod
    def Arithmetic(arg):
        
        arg = arg.lower()
        line = f"// {arg}\n"
        
        # Get values to perform operation
        
        line += "@SP\n"
        line += "M = M - 1\n"
        line += "A = M\n"
        
        # These two operations only use first stack value, so can just be performed
        if arg == "neg":
            line += "M = -M\n"
            line += "@SP\n"
            line += "M = M + 1\n"
            line += "\n"
            return line
        
        elif arg == "not":
            line += "M = !M\n"
            line += "@SP\n"
            line += "M = M + 1\n"            
            line += "\n"
            return line
        
        
        # Otherwise, store first value from stack
        line += "D = M\n"
        line += "@arg\n"
        line += "M = D\n"
        
        # Get other value
        line += "@SP\n"
        line += "M = M - 1\n"
        line += "A = M\n"
        line += "D = M\n"
        
        line += "@arg\n"  # Now, arg1 = M, arg2 = D
        
        
        # DO COMPUTATION
        if arg == "add":
            line += "D = D + M\n"
            
        elif arg == "sub":
            line += "D = D - M\n"  # MAY BE OTHER WAY
                        
        elif arg == "and":
            line += "D = D & M\n"
        
        elif arg == "or":
            line += "D = D | M\n"
            
        elif arg in ("eq", "lt", "gt"):
            line += "D = D - M\n"
            
            line += "@true\n"  # Depending on case. Jump if true
            
            if arg == "eq": 
                line += "D;JEQ\n"
            if arg == "lt":
                line += "D;JLT\n"
            if arg == "gt":
                line += "D;JGT\n"
            
            line += "D = 0\n"  # If false, D = 0
            line += "@false\n"
            line += "0;JMP\n"
            
            line += "(true)\n"  # If true, D = 1
            line += "D = 1\n"
            line += "(false)\n"
            
            
        # After computing value, add to stack
        line += "@SP\n"
        line += "A = M\n"
        line += "M = D\n"
        line += "@SP\n"
        line += "M = M + 1\n"
        
        line += "\n"
        return line



    @staticmethod
    def label(loc):
        line = f"// ({loc})\n"
        
        line += f"({loc})\n"
        
        line += "\n"
        return line
        
        

    @staticmethod
    def goto(loc):
        line = f"// goto {loc}\n"
        
        line += f"@{loc}\n"
        line += "0;JMP\n"
        
        line += "\n"
        return line
    
    
    
    @staticmethod
    def if_goto(loc):
        line = f"// if-goto {loc}\n"
        
        line += "@SP\n"
        line += "M = M - 1\n"
        line += "A = M\n"
        line += "D = M\n"  # Get value at top of stack, to determine the jump

        line += f"@{loc}\n"
        line += "D;JNE\n"  # Look at top of stack value, and jump if true
        
        line += "\n"
        return line
        
        
    
    @staticmethod
    def func(funcName, numVars):
        line = f"// function {funcName} {numVars}\n"
        
        line += f"({funcName})\n"
        
        # Add numVars amount of local variables to stack
        line += f"@{numVars}\n"
        line += "D = A\n"
        line += "@13\n"  # General purpose register
        line += "M = D\n"
        
        line += f"(LOOP.{funcName})\n"  # Loops must be labeled so they don't clash
        line += "@13\n"
        line += "D = M\n"
        
        line += f"@END.{funcName}\n"
        line += "D;JEQ\n"
        
        line += Translator.push("constant", "0")
        line += "@13\n"
        line += "M = M - 1\n"
        
        line += f"@LOOP.{funcName}\n"
        line += "0;JMP\n"
        
        line += f"(END.{funcName})\n"
        
        line += "\n"
        return line
    
    
    @staticmethod
    def funcReturn():
        line = "// return\n"
        
        # endFrame = LCL
        line += "@LCL\n"
        line += "D = M\n"
        line += "@14\n"  # endFrame
        line += "M = D\n"
        
        # retAddr = *(endFrame-5)
        line += "@5\n"
        line += "D = A\n"
        line += "@14\n"
        line += "D = M - D\n"
        line += "A = D\n"
        line += "D = M\n"
        line += "@15\n"  # retAddr
        line += "M = D\n"
        
        # *ARG = pop()
        line += Translator.pop("argument", "0")
        
        # SP = ARG + 1
        line += "@ARG\n"
        line += "D = M\n"
        line += "D = D + 1\n"
        line += "@SP\n"
        line += "M = D\n"
        
        # THAT = *(endFrame - 1)
        line += "@14\n"  # endFrame
        line += "D = M\n"
        line += "D = D - 1\n"
        line += "A = D\n"
        line += "D = M\n"
        line += "@THAT\n"
        line += "M = D\n"
        
        # THIS = *(endFrame - 2)
        line += "@2\n"
        line += "D = A\n"
        line += "@14\n"  # endFrame
        line += "D = M - D\n"
        line += "A = D\n"
        line += "D = M\n"
        line += "@THIS\n"
        line += "M = D\n"
        
        # ARG = *(endFrame - 3)
        line += "@3\n"
        line += "D = A\n"
        line += "@14\n"  # endFrame
        line += "D = M - D\n"
        line += "A = D\n"
        line += "D = M\n"
        line += "@ARG\n"
        line += "M = D\n"

        # LCL = *(endFrame - 4)
        line += "@4\n"
        line += "D = A\n"
        line += "@14\n"  # endFrame
        line += "D = M - D\n"
        line += "A = D\n"
        line += "D = M\n"
        line += "@LCL\n"
        line += "M = D\n"
        
        # goto retAddr
        line += "@15\n"
        line += "A = M\n"
        
        line += "\n"
        return line
    

    
    @staticmethod
    def call(funcName, numArgs):
        line = f"// call {funcName} {numArgs}\n"
        global j
        
        # Push returnAddress
        returnAddress = f"{funcName}$ret.{j}"
        line += f"@{returnAddress}\n"
        line += "D = A\n"
        line += "@SP\n"
        line += "A = M\n"
        line += "M = D\n"
        line += "@SP\n"
        line += "M = M + 1\n"
        
        # Push LCL
        line += Translator.push("local")
        # Push ARG
        line += Translator.push("argument")
        # Push THIS
        line += Translator.push("this")
        # Push THAT
        line += Translator.push("that")
        
        
        # Reposition ARG
        #ARG = SP - 5 - nArgs
        
        line += "@SP\n"
        line += "D = M\n"
        line += "@ARG\n"
        line += "M = D\n"
        
        line += "@5\n"
        line += "D = A\n"
        line += "@ARG\n"
        line += "M = M - D\n"
        
        line += f"@{numArgs}\n"
        line += "D = A\n"
        line += "@ARG\n"
        line += "M = M - D\n"
        
        # LCL = SP
        line += "@SP\n"
        line += "D = M\n"
        
        line += "@LCL\n"
        line += "M = D\n"
        
        #Go to function
        line += Translator.goto(funcName)
        line += f"({returnAddress})\n"
        
        line += "\n"
        j += 1
        return line
        
    @staticmethod
    def init():
        line = "// INIT\n"
        
        line += "@256\n"
        line += "D = A\n"
        line += "@SP\n"
        line += "M = D\n"
        
        line += "@Sys.init\n"
        line += "0;JMP\n"
        
        line += "\n"
        return line
        
        


def main():
    
    content, name = initialize()
    
    dest = open(name, "w")
    
    result = Translator.init()
    dest.write(result)
    
    for line in content:
        args = line.split() 
        if len(args) == 1:
            if args[0] == "return":
                result = Translator.funcReturn()
            else:
                result = Translator.Arithmetic(args[0])
        else:
            if (args[0]).lower() == "push":
                if len(args) == 2:
                    result = Translator.push(args[1])
                else:
                    result = Translator.push(args[1], args[2])
            elif (args[0]).lower() == "pop":
                result = Translator.pop(args[1], args[2])
            elif (args[0]).lower() == "label":
                result = Translator.label(args[1])
            elif (args[0]).lower() == "goto":
                result = Translator.goto(args[1])
            elif (args[0]).lower() == "if-goto":        
                result = Translator.if_goto(args[1])
            elif (args[0]).lower() == "function":   
                result = Translator.func(args[1], args[2])
            elif (args[0]).lower() == "call": 
                result = Translator.call(args[1], args[2])
                
        dest.write(result)
    
    return
