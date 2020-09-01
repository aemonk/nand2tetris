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

	
	@SCREEN
	D=A
	@addr
	M=D // addr = 16384 screen memory map

	@8192 // height
	D=A
	@n
	M=D // n = RAM[0]

	@i
	M=0 // i = 

	// RAM[24576 KBD address
	// if KBD > 0 then 1
	// else 0

(LOOP)
	@i
	D=M
	@n
	D=D-M
	@END
	D;JGT // if i > n goto END
	
	@addr
	A=M
	M=-1 // RAM[addr] = 1111...

	@i 
	M=M+1 // i = i + 1
	@1 // 
	D=A
	@addr
	M=D+M // addr = addr + 1
	@LOOP
	0;JMP // goto LOOP

(END)
	@END // programs end
	0;JMP // infinite loop
