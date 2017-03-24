# pythonAssignment
First code of my python assignment

a b c t1 t2 t3

on(c,a) on(a,t1) on(b,t2)

on(a,b) on(b,c) on(c,t3) clear(t1) clear(t2)


TEST TABLE:

    OBJECTS     |       CURRENT STATE                                       |       GOAL STATE      |  Y/N
     A B C      |     ON(A,B) CLEAR(C)                                      |    ON(A,C) CLEAR(B))  | MOVE(A,B,C)  
  A B C TABLE1  |ON(A,B) ON(B,C) CLEAR(TABLE1)                              |                       |
TABLE1 TABLE2 A |ON(A, table1) HEAVIER(table1, A)                           |                       |
                |   HEAVIER(table2, A) CLEAR(A) CLEAR(table2)|CLEAR(table1) |                       |
                |       CLEAR(A)|Move(A, table1, table2)                    | ON(A,TABLE1) CLEAR(B) | MOVE(A,B,TABLE1)

A B C
ON(A,B) CLEAR(C)
ON(A,C) CLEAR(B)
MOVE(A,B,C)

A B C TABLE1
ON(A,B) ON(B,C) CLEAR(TABLE1)
ON(A,TABLE1) CLEAR(B)
MOVE(A,B,TABLE1)

TABLE1 TABLE2 A
ON(A, table1) HEAVIER(table1, A) HEAVIER(table2, A) CLEAR(A) CLEAR(table2)

CLEAR(table1) CLEAR(A)

Move(A, table1, table2)


A B C D E F TABLE1 TABLE2 TABLE3 TABLE4 TABLE5
