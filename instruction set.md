0000 0000 <0000> <0000> | add <address register a> <address register b>         | a + b into a
0000 0001 <0000> <0000> | sub <address register a> <address register b>         | a - b into a
0000 0010 <0000> <0000> | bitwise OR <address register a> <address register b>  | a or b into a
0000 0011 <0000> <0000> | bitwise AND <address register a> <address register b> | a and b into a
0000 0100 <0000> <0000> | bitwise XOR <address register a> <address register b> | a xor b into a
0000 0101 <0000> <0000> | bitwise invert <address register a> <_>               | a invert into a
0000 0110 <0000> <0000> | bitwise shift left 1 <address register a> <_>         | a shift left into a
0000 0111 <0000> <0000> | bitwise shift right 1 <address register a> <_>        | a shift right into a
0000 1000 <0000> <0000> | exchange register a to register b | a


0001 0000 <0000 0000> | load_A <RAM address>  | load RAM into A
0001 0001 <0000 0000> | load_B <RAM address>  | load RAM into B
0001 0010 <0000 0000> | load_C <RAM address>  | load RAM into C
0001 0011 <0000 0000> | load_D <RAM address>  | load RAM into D
0001 0100 <0000 0000> | store_A <RAM address> | store A into RAM
0001 0101 <0000 0000> | store_B <RAM address> | store B into RAM
0001 0110 <0000 0000> | store_C <RAM address> | store C into RAM
0001 0111 <0000 0000> | store_D <RAM address> | store D into RAM


0010 0000 <0000 0000> | print <RAM address>   | print RAM to screen
0010 0001 <0000 0000> | jump <RAM address>    | jump to spot in memory
0010 0010 <0000 0000> | jump if <RAM address> | jump to spot
