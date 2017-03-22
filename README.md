# pythonAssignment
First code of my python assignment




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





