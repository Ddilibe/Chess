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



### Resources

1. [Wikipedia: Chess960 Starting Posi](https://en.wikipedia.org/wiki/Fischer_random_chess)

2. [Chess and Bitboards](https://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/index.html)

3. [Chess Programming](https://www.chessprogramming.org/General_Setwise_Operations)

4. 