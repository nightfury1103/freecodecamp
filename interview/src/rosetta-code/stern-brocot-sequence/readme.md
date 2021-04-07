# Stern-Brocot sequence

[FCC link](https://www.freecodecamp.org/learn/coding-interview-prep/rosetta-code/stern-brocot-sequence)

For this task, the Stern-Brocot sequence is to be generated by an algorithm
similar to that employed in generating the
[Fibonacci sequence](https://rosettacode.org/wiki/Fibonacci%20sequence).

1.  The first and second members of the sequence are both 1:

- 1, 1

3.  Start by considering the second member of the sequence
4.  Sum the considered member of the sequence and its precedent, (1 + 1) = 2,
    and append it to the end of the sequence:

- 1, 1, 2

6.  Append the considered member of the sequence to the end of the sequence:

- 1, 1, 2, 1

8.  Consider the next member of the series, (the third member i.e. 2)
9.  GOTO 3

- ─── Expanding another loop we get: ───

11. Sum the considered member of the sequence and its precedent, (2 + 1) = 3,
    and append it to the end of the sequence:

- 1, 1, 2, 1, 3

13. Append the considered member of the sequence to the end of the sequence:

- 1, 1, 2, 1, 3, 2

15. Consider the next member of the series, (the fourth member i.e. 1)