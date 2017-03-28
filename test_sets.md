
Obj = A B C
S0 = ON(B,A) HEAVIER(A,B) HEAVIER(C,B) CLEAR(B) CLEAR(C)
Goal = ON(B,C) CLEAR(A)

Expected Output:\
MOVE(B,A,C)\
\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Test Set 02\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Obj = A B C D E\
\
S0 = ON(B,A) ON(C,B) HEAVIER(A,B) HEAVIER(B,C) HEAVIER(E,C) HEAVIER(D,B) HEAVIER(A,C) CLEAR(C) CLEAR(E) CLEAR(D)\
\
Goal = ON(C,A) CLEAR(B)\
\
Expected Output:\
MOVE(C,B,E)\
MOVE(B,A,D)\
MOVE(C,E,A)\
\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Test Set 03\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Obj = Table1 Table2 Box Toy Tree \
\
S0 = ON(Box,Table1) ON(Toy,Table2) HEAVIER(Table1,Box) HEAVIER(Table2,Toy) HEAVIER(Tree,Toy) HEAVIER(Table2,Box) CLEAR(Tree) CLEAR(Toy) CLEAR(Box)\
\
Goal = ON(Box,Table2) ON(Toy,Tree) \
\
Expected Output:\
MOVE(Toy,Table2,Tree)\
MOVE(Box,Table1,Table2)\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\tx8465\pardirnatural\partightenfactor0
\cf0 \'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 Test Set 04 \
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Obj = Table1 Table2 Box Toy Tree Shoe\
\
S0 = ON(Box,Table1) ON(Shoe,Box) ON(Toy,Table2) HEAVIER(Table1,Box) HEAVIER(Box,Shoe) HEAVIER(Table2,Toy) HEAVIER(Tree,Shoe) HEAVIER(Table2,Shoe) HEAVIER(Toy,Box) CLEAR(Shoe) CLEAR(Toy) CLEAR(Tree)\
\
Goal = CLEAR(Table1) ON(Box,Toy)\
\
Expected Output:\
MOVE(Shoe,Box,Tree)\
MOVE(Box,Table1,Toy)\
\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Test Set 05\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Obj = Table1 Table2 Box Toy Tree Shoe\
\
S0 = ON(Box,Table1) ON(Shoe,Box) ON(Toy,Table2) HEAVIER(Table1,Box) HEAVIER(Box,Shoe) HEAVIER(Table2,Toy) HEAVIER(Tree,Shoe) HEAVIER(Table2,Shoe) HEAVIER(Box,Toy) CLEAR(Shoe) CLEAR(Toy) CLEAR(Tree)\
\
Goal = CLEAR(Table2) ON(Toy,Box)\
\
Expected Output:\
MOVE(Shoe,Box,Tree)\
MOVE(Toy,Table2,Box)\
\
Run adds:\
MOVE(Shoe,Tree,Table2)\
MOVE(Shoe,Table2,Tree)\
\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Test Set 06\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Obj = Table1 Table2 Box Toy Tree Shoe\
\
S0 = ON(Box,Table1) ON(Shoe,Box) ON(Toy,Table2) HEAVIER(Toy,Shoe) HEAVIER(Tree,Box) HEAVIER(Table1,Shoe) HEAVIER(Box,Toy) CLEAR(Shoe) CLEAR(Toy) CLEAR(Tree)\
\
Goal = CLEAR(Table1) CLEAR(Table2)\
\
Expected Output:\
MOVE(Shoe,Box,Toy)\
MOVE(Box,Table1,Tree)\
MOVE(Shoe,Toy,Table1)\
MOVE(Toy,Table2,Box)\
MOVE(Shoe,Table1,Toy)\
\
Run adds:\
MOVE(Shoe,Toy,Table1)\
MOVE(Shoe,Table1,Toy)\
MOVE(Shoe,Toy,Table1)\
MOVE(Shoe,Table1,Toy)\
MOVE(Shoe,Toy,Table1)\
MOVE(Shoe,Table1,Toy)\
\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Test Set 07\
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
Obj = Table1 Table2 Box Toy Tree Shoe\
\
\pard\tx-100\tx-100\tx456\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 S0 = \
}