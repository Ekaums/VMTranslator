// INIT
@256
D = A
@SP
M = D
@Sys.init
0;JMP

// function Sys.init 0
(Sys.init)
@0
D = A
@13
M = D
(LOOP.Sys.init)
@13
D = M
@END.Sys.init
D;JEQ
// push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1

@13
M = M - 1
@LOOP.Sys.init
0;JMP
(END.Sys.init)

// push constant 4000
@4000
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop pointer 0
@THIS
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

// push constant 5000
@5000
D = A
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

// call Sys.main 0
@Sys.main$ret.0
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push LCL
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push ARG
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push THIS
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push THAT
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1

@SP
D = M
@ARG
M = D
@5
D = A
@ARG
M = M - D
@0
D = A
@ARG
M = M - D
@SP
D = M
@LCL
M = D
// goto Sys.main
@Sys.main
0;JMP

(Sys.main$ret.0)

// pop temp 1
@5
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

// (LOOP)
(LOOP)

// goto LOOP
@LOOP
0;JMP

// function Sys.main 5
(Sys.main)
@5
D = A
@13
M = D
(LOOP.Sys.main)
@13
D = M
@END.Sys.main
D;JEQ
// push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1

@13
M = M - 1
@LOOP.Sys.main
0;JMP
(END.Sys.main)

// push constant 4001
@4001
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop pointer 0
@THIS
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

// push constant 5001
@5001
D = A
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

// push constant 200
@200
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop local 1
@LCL
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

// push constant 40
@40
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop local 2
@LCL
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

// push constant 6
@6
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop local 3
@LCL
D = M
@3
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

// push constant 123
@123
D = A
@SP
A = M
M = D
@SP
M = M + 1

// call Sys.add12 1
@Sys.add12$ret.1
D = A
@SP
A = M
M = D
@SP
M = M + 1
// push LCL
@LCL
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push ARG
@ARG
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push THIS
@THIS
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push THAT
@THAT
D = M
@SP
A = M
M = D
@SP
M = M + 1

@SP
D = M
@ARG
M = D
@5
D = A
@ARG
M = M - D
@1
D = A
@ARG
M = M - D
@SP
D = M
@LCL
M = D
// goto Sys.add12
@Sys.add12
0;JMP

(Sys.add12$ret.1)

// pop temp 0
@5
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

// push LCL 0
@LCL
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

// push LCL 1
@LCL
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

// push LCL 2
@LCL
D = M
@2
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push LCL 3
@LCL
D = M
@3
D = D + A
A = D
D = M
@SP
A = M
M = D
@SP
M = M + 1

// push LCL 4
@LCL
D = M
@4
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

// return
@LCL
D = M
@14
M = D
@5
D = A
@14
D = M - D
A = D
D = M
@15
M = D
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

@ARG
D = M
D = D + 1
@SP
M = D
@14
D = M
D = D - 1
A = D
D = M
@THAT
M = D
@2
D = A
@14
D = M - D
A = D
D = M
@THIS
M = D
@3
D = A
@14
D = M - D
A = D
D = M
@ARG
M = D
@4
D = A
@14
D = M - D
A = D
D = M
@LCL
M = D
@15
A = M

// function Sys.add12 0
(Sys.add12)
@0
D = A
@13
M = D
(LOOP.Sys.add12)
@13
D = M
@END.Sys.add12
D;JEQ
// push constant 0
@0
D = A
@SP
A = M
M = D
@SP
M = M + 1

@13
M = M - 1
@LOOP.Sys.add12
0;JMP
(END.Sys.add12)

// push constant 4002
@4002
D = A
@SP
A = M
M = D
@SP
M = M + 1

// pop pointer 0
@THIS
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

// push constant 5002
@5002
D = A
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

// push constant 12
@12
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

// return
@LCL
D = M
@14
M = D
@5
D = A
@14
D = M - D
A = D
D = M
@15
M = D
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

@ARG
D = M
D = D + 1
@SP
M = D
@14
D = M
D = D - 1
A = D
D = M
@THAT
M = D
@2
D = A
@14
D = M - D
A = D
D = M
@THIS
M = D
@3
D = A
@14
D = M - D
A = D
D = M
@ARG
M = D
@4
D = A
@14
D = M - D
A = D
D = M
@LCL
M = D
@15
A = M

