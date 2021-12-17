# Project 6 Overview

Unit Videos
- [ ] 6
- [ ] 6.1
- [ ] 6.2
- [ ] 6.3
- [ ] 6.4
- [ ] 6.5
- [X] 6.6
- [ ] 6.6B
- [ ] 6.7

## Proposed software architecture

- Parser
  - unpacks each instruction into its underlying fields
- Code
  - translates each field into its corresponding binary value
- SymbolTable
  - manages the symbol table
- Main
  - initializes the I/O files and drives the process

## Staged development

- develop basic assembler that translates assembly programs without symbols (test)
- develop an ability to handle symbols (SymbolTable)
- Morph the basic assembler into an assembler that can translate any assembly program

## Supplied Test Programs

- `L` stands for `less/without Symbols`
- Test first on the `L` programs

Testfiles
- Add.asm
  - white space
  - instructions
- Max.asm
- MaxL.asm
  - find max of two values
- Rectangle.asm
- RectangleL.asm
  - draw rectangle
- Pong.asm
- PongL.asm
  - no white space
  - strange addresses
  - strange labels
  - strange pre-defined symbols

## Testing

- use assembler to generate executable xxx.hack file
- load into hack computer and execute it
  - or with the CPUEmulator
  - or use the Assembler and diff both files


## Resources

- Supplied Assembler
- Supplied CPU emulator
- Assembler Tutorial
- Proposed Assembler API
- [Project06](https://www.nand2tetris.org/project06)
- [Chapter06 Slides](https://drive.google.com/file/d/1uKGRMnL-gqk9DsgeN50z0EpHoSMWe6F5/view)
- [Chapter06 Book](https://www.nand2tetris.org/_files/ugd/44046b_89a8e226476741a3b7c5204575b8a0b2.pdf)

