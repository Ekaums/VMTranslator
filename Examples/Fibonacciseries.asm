// INIT
@256
D = A
@SP
M = D
@Sys.init
0;JMP

// push ARG 1
@ARG
D = M
@1
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// pop pointer 1
@THAT
D = A
@Pop
M = D
@SP
M = M - 1
A = M
D = M
@Pop
A = M
M = D

// push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop that 0
@THAT
D = M
@0
D = D + A
@Pop
M = D
@SP
M = M - 1
A = M
D = M
@Pop
A = M
M = D

// push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop that 1
@THAT
D = M
@1
D = D + A
@Pop
M = D
@SP
M = M - 1
A = M
D = M
@Pop
A = M
M = D

// push ARG 0
@ARG
D = M
@0
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push constant 2
@2
D = A
@SP
A = M
M = D
@SP
M = M + 1

// sub
@SP
M = M - 1
A = M
D = M
@arg
M = D
@SP
M = M - 1
A = M
D = M
@arg
D = D - M
@SP
A = M
M = D
@SP
M = M + 1

// pop argument 0
@ARG
D = M
@0
D = D + A
@Pop
M = D
@SP
M = M - 1
A = M
D = M
@Pop
A = M
M = D

// (MAIN_LOOP_START)
(MAIN_LOOP_START)

// push ARG 0
@ARG
D = M
@0
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// if-goto COMPUTE_ELEMENT
@SP
M = M - 1
A = M
D = M
@COMPUTE_ELEMENT
D;JNE

// goto END_PROGRAM
@END_PROGRAM
0;JMP

// (COMPUTE_ELEMENT)
(COMPUTE_ELEMENT)

// push THAT 0
@THAT
D = M
@0
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push THAT 1
@THAT
D = M
@1
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// add
@SP
M = M - 1
A = M
D = M
@arg
M = D
@SP
M = M - 1
A = M
D = M
@arg
D = D + M
@SP
A = M
M = D
@SP
M = M + 1

// pop that 2
@THAT
D = M
@2
D = D + A
@Pop
M = D
@SP
M = M - 1
A = M
D = M
@Pop
A = M
M = D

// push pointer 1
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1

// add
@SP
M = M - 1
A = M
D = M
@arg
M = D
@SP
M = M - 1
A = M
D = M
@arg
D = D + M
@SP
A = M
M = D
@SP
M = M + 1

// pop pointer 1
@THAT
D = A
@Pop
M = D
@SP
M = M - 1
A = M
D = M
@Pop
A = M
M = D

// push ARG 0
@ARG
D = M
@0
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push constant 1
@1
D = A
@SP
A = M
M = D
@SP
M = M + 1

// sub
@SP
M = M - 1
A = M
D = M
@arg
M = D
@SP
M = M - 1
A = M
D = M
@arg
D = D - M
@SP
A = M
M = D
@SP
M = M + 1

// pop argument 0
@ARG
D = M
@0
D = D + A
@Pop
M = D
@SP
M = M - 1
A = M
D = M
@Pop
A = M
M = D

// goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP

// (END_PROGRAM)
(END_PROGRAM)

