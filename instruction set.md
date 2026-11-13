# CPU rules & architecture
- 16 bit instructions
- access RAM module with 8-bit address
- every RAM address has 16-bits of data
- data and the instructions are stored in the same RAM module
- all values are encoded from hex values and decoded to hex values.\
- cpu has 4 registers

# 16-bit instuction structure
4 1e bits are the operation group.
4 2e bits are the specfic operation.
4 3e bits are the first part of the address
4 4e bits are the second part of the address

## assembly instructions
binary representation          | assembly instruction                                               | instruction explained                             | note


0000 0000 <00><00> <00><__>    | add <register address a> <register address b> <register address c> | register A + register B into register C           |
0000 0001 <00><00> <00><__>    | sub <register address a> <register address b> <register address c> | register A - register B into register C           |
0000 0010 <00><00> <00><__>    | OR <register address a> <register address b> <register address c>  | register A or register B bitwise into register C  |
0000 0011 <00><00> <00><__>    | AND <register address a> <register address b> <register address c> | register A and register B bitwise into register C |
0000 0100 <00><00> <00><__>    | XOR <register address a> <register address b> <register address c> | register A xor register B bitwise into register C |
0000 0101 <00><__> <00><__>    | inv <register address a> <register address c>                      | register A invert bitwise into register C         |
0000 0110 <00><__> <00><__>    | shift_l1 <register address a> <register address c>                 | register A shift left bitwise into register C     |
0000 0111 <00><__> <00><__>    | shift_r1 <register address a> <register address c>                 | register A shift right bitwise into register C    |

0000 1000 <00><__> <00><__>    | incr_1 <register address a> <register address c>                   | increment register A by 1 into register C         | not implemented by ALU. use ADD 1 instead?
0000 1001 <00><__> <00><__>    | decr_1 <register address a> <register address c>                   | decrement register A by 1 into register C         | not implemented by ALU. use SUB 1 instead?


0001 00 <00> <00  00   00  00> | load <register address a> <RAM address>                            | load RAM into register A                          |
0001 01 <00> <00  00   00  00> | store <register address a> <RAM address>                           | store register A into RAM                         |
0001 10 <__> <00><__> <00><__> | copy <register address a> <register address c>                     | copy data in register A into register C           |


0010 0000 <0000 0000>          | jump <RAM address>                                                 | jump to spot in memory always                     |
0010 0001 <0000 0000>          | jump zero <RAM address>                                            | jump to spot in memory if ALU has zero flag       |
0010 0010 <0000 0000>          | jump neg <RAM address>                                             | jump to spot in memory if ALU has negative flag   |


0011 0000 <____ ____>          | HALT                                                               | the program is done and halts the computer        |
0011 0001 <0000 0000>          | PRINT <RAM address>                                                | print the data from ram to screen as HEX value    |

## assembly data
"0000 0101" @1000 0000 | "5" @80
"0000 0110" @1000 0001 | "6" @81

# test programs
# 1e simple add program
this program will take values "5" and "6" from RAM. add them together. and write the result "B" back to RAM.
## program assembly
@ marks memory address one hex digit is for registers. two hex digits is for RAM addresses.
```
data:
"5" @80
"6" @81

program:
load @rA @80
load @rB @81

add @rA @rB @rC # cpu will store this in a temporary register turn the ALU off and then store it in the register A. This is to prevent the result rippling.

store @rC @82

HALT
```
## program binary
the program in binary will consider all data already written to disk

@ marks memory address four bits is for registers. 8 bits is for RAM addresses.
_ marks unused and not important space / bits in the instuction.
```
data:
"0000 0101" @1000 0000
"0000 0110" @1000 0001

program:
0001 00 @00 @1000 0000
0001 00 @01 @1000 0001

0000 0000 @00 @01 @10 _00_ # cpu will store this result in a temporary register turn the ALU off and then store it in register A. This is to prevent the result rippling and recalulating.

0001 01 @10 @1000 0010

0011 0000 _0000 0000_
```
