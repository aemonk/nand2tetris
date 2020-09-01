// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(LOOP)
	@SCREEN
	D=A

	@addr
	M=D // addr = 16384 screen memory map

	@8192 // height
	D=A

	@n
	M=D // n = RAM[0]

	@i
	M=0 // i = 0

	@KBD
	D=M

	@WHITE
	D; JEQ // if KBD == 0 goto WHITE
	
	@BLACK
	D; JGT // if KBD > 0 goto BLACK

(WHITE)
	@i
	D=M
	@n
	D=D-M
	@LOOP
	D; JEQ // if i > n goto LOOP
	
	@addr
	A=M
	M=0 // white 0

	@i 
	M=M+1 // i = i + 1

	@addr
	M=M+1

	@WHITE
	0; JMP 

(BLACK)
	@i
	D=M

	@n
	D=D-M

	@LOOP
	D; JEQ // if i > n goto LOOP
	
	@addr
	A=M
	M=-1 // black 1

	@i 
	M=M+1 // i = i + 1

	@addr
	M=M+1

	@BLACK
	0; JMP