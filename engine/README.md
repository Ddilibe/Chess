# Chess Engine

This is a chess engine developed my me

### Bitboard

A bitboard is a way of representing the borad on a computer. Bitboards can also be applied to games that work in a square by square board. The bitboard is represented in ones and zeros. The bitboards are read from left to right and from top to bottom. Bitboard is very efficient and takes a lot less space. 

### How to find the Complements
1. One's Complement

The one's complement is the same for a positive binary number. But for a negative number, Once it is converted to binary, replace every where one is with zero and everywhere zero is to one.

```
	Decimal | Binary | One's complement
		-5  |   0101 |     1010
		-6  |   0110 |     1001
		-7  |   0111 |     1000
```

2. Two's complement

To find the second complement, find the one's complement and add one to it. This only occurs on negative numbers

## Bitwise Operations

Bitwise operations form my own point of view are those operations that involves the manipulations of bits in the computer. Bits are 1s and 0s. In python programming, bit operation can only be done on integers.

Before any integer is manipulated via bitwise operators, they are first converted into binary form (1s and 0s).

```

Example:
	a, b = 1, 2

	First, it converts a to binary form
	which is 1
	Then it converts b to its binary form
	which is 10
	a & b will be
	1 & 10 
	Then it goes on with the bitwise operation. 

	When It is done with the bitwise operation, it then converts it to denary (base 10)
	Answer: 0
```

There are different types of bit operators

--------------------------------------------
| Operators | Description | Syntax | Explanation
____________________________________________
| & | Bitwise AND | x & y | This bitwise operator compares both bit values and return 1 if both bits are 1 else it will return 0 `10001 & 11000 = 10000`
--------------------------------------------
| \| | Bitwise OR | x\|y | This bitwise operator compares both bit values and return 1 if either bits are 1 else it will return 0 `10001 & 11000 = 11001`
--------------------------------------------
| ~ | Bitwise NOT | ~x | 
--------------------------------------------
| ^ | Bitwise XOR | x^y |
--------------------------------------------
| \>\> | Bitwise Right Shift | x\>\> |
--------------------------------------------
| << | Bitwise Left Shift | x<<
____________________________________________

### Resources

1. [Wikipedia: Chess960 Starting Posi](https://en.wikipedia.org/wiki/Fischer_random_chess)

2. [Chess and Bitboards](https://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/index.html)

3. [Chess Programming](https://www.chessprogramming.org/General_Setwise_Operations)

4. 