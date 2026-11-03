# Clock
The clocks in computers are a logic circuit that constantly switches between 0 and 1. With this we can coordinate the logic operations from the different circuits on the computer with high accuracy.
## Analogies
- trafficlights
## The Real World
The basic parts that all clock generators share are a resonant circuit and an amplifier.
- The resonant circuit or resonator is naturally oscillating. (because energy takes time to transfer between its electrical and magnetic fields.)
- The amplifier feeds back a bit of that same electrical signal to the resonant circuit.
# ALU (Arithmetic Logic Unit)
https://www.geeksforgeeks.org/computer-organization-architecture/introduction-of-alu-and-data-path/
The ALU is the module that performs the given logic and arithmetic operations. it takes input from registers, proccesses them, and stores the result in a destination register.
## functions and operations OF ALU
1. arithmetic operations
	- operations include addition, subtraction, increment, decrement.
	- used for the basic operations above.
2. logical operations
	- bitwise operations like AND, OR, XOR, NOT.
	- essential for masking, setting, clearing, or toggling bits.
3. shift operations
	- logical shift, arithmetic shift, rotate.
	- often used for multiplication/division by powers of 2 and bit-level data formatting.
4. comparison operations
	- checking for conditions like equals, greater than, less than.
	- usefull in branching and conditional intructions based on flag values.
5. Status flags
	- common flags: Zero, Carry, Sign, Overflow
	- Flags are used in conditional execution and exception handling.
## My ALU Implementation
I have mine made with the following operations:
1. addition (A+B)
2. subtraction (A-B)
3. bitwise OR (A | B)
4. bitwise AND (A & B)
5. bitwise XOR (A ^ B)
6. bitwise invert (~A)
7. bitwise shift left (<<A)
8. bitwise shift right (A>>)
Using these opcodes the ALU will do the given operation with inputs A and B. And output the 8-bit result.

I also have 3 flags currently to show extra info about the result:
- overflow
- signed
- is zero
# Memory
Is the module that data is stored the duration varies a lot from very short to very long.
## Variables
- geometry (how to fit as much as possible in a small as possible space)
- abstraction (when to choose abstracting the complexity away)
- size or complexity (how big or how complex till you abstract)