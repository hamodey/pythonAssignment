# pythonAssignment
First code of my python assignment

a b c t1 t2 t3
on(c,a) on(a,t1) on(b,t2)
on(a,b) on(b,c) on(c,t3) clear(t1) clear(t2)

Move( a, t1, b)√√√√√√√√√√
Move( b, t2, c)√√√√√√√√√√
Move( c, a, t3)√√√√√√√√√√


TEST TABLE:

    OBJECTS     |       CURRENT STATE                                       |       GOAL STATE      |  Y/N
     A B C      |     ON(A,B) CLEAR(C)                                      |    ON(A,C) CLEAR(B))  | MOVE(A,B,C)  
  A B C TABLE1  |ON(A,B) ON(B,C) CLEAR(TABLE1)                              |                       |
TABLE1 TABLE2 A |ON(A, table1) HEAVIER(table1, A)                           |                       |
                |   HEAVIER(table2, A) CLEAR(A) CLEAR(table2)|CLEAR(table1) |                       |
                |       CLEAR(A)|Move(A, table1, table2)                    | ON(A,TABLE1) CLEAR(B) | MOVE(A,B,TABLE1)

ON(A,B) CLEAR(C)
A B C
ON(A,C) CLEAR(B)
MOVE(A,B,C) √√√√√√√√√√√√√√√

A B C TABLE1
ON(A,B) ON(B,C) CLEAR(TABLE1)
ON(A,TABLE1) CLEAR(B)
MOVE(A,B,TABLE1) √√√√√√√√√√√√√√



===
table1 table2 a
on(a,table1) heavier(table1,a) heavier(table2,a) clear(a) clear(table2)
clear(table1) clear(a)

Move(A, table1, table2)√√√√√√√√√√

====

a b p1 p2 t1 t2 t3
clear(p2) on(p2,a) on(a,t2) on(t2,b) clear(t1) clear(p1) heavier(a,p2) heavier(t2,a) heavier(b,p2) heavier(p1,p2) heavier(t1,a) heavier(p1,t2)
on(p2,a) on(a,t2) on(t2,p1)

Move(P2, A, P1) x
Move(A, T2, T1) x
Move(P2, P1, A) x
Move(T2, B, P1) √√√√√
Move(P2, A, B)  x
Move(A, T1, T2) x
Move(P2, B, A)  x 

A B C D E F TABLE1 TABLE2 TABLE3 TABLE4 TABLE5

a b c t1 t2

clear(b) on(b,c) on(c,a) on(a,t1) clear(t1) clear(t2) heavier(b,a) heavier (c,b) heavier(t1,b) heavier(t2,c)

on(a,b) on(b,c) on(c,t2)

Move(b,c,t1) xxxxxxx
Move(c,a,t2) √√√√√√√
Move(b,t1,c) xxxxxxx
Move(a,t1,b) √√√√√√√
