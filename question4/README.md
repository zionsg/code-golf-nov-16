# Question 4

Given a string to encode, and a number of columns (the key), encode the string as follows:

I will be using the example `Hello, world!` and the key `3`

First, write out the number of columns:

    1 2 3

Next, write the text starting from the upper left, one character per column, and when you run out of columns, go to the next line.

    1 2 3
    H e l
    l o ,
      w o
    r l d
    !

Now, to get your encoded text, read the text starting from the top left corner, but this time, first read one column, and then the next, and so on. If there is not a character in the slot, put a space.

    Hl r!eowl l,od 

Note that here, there is a trailing space.

This is your encoded text.

Another test case is `Programming Puzzles and Code Golf SE` with key `5`:

    1 2 3 4 5
    P r o g r
    a m m i n
    g   P u z
    z l e s  
    a n d   C
    o d e   G
    o l f   S
    E

The encoded text is `PagzaooErm lndl omPedef gius    rnz CGS`.

More test cases

    "abcdefghijklmnopqrstuvwxyz", 2 -> "acegikmoqsuwybdfhjlnprtvxz"
    "codegolf.stackexchange.com", 4 -> "cg.ccgoooskhemdltea. efaxnc "
    "Pen Pineapple Apple Pen!!!", 7 -> "PeAeeapnnpp! pl!Ple!ie  n P "
    "1,1,2,3,5,8,13,21,34,55,89", 10 -> "18,,,5115,3,2,8,2931 ,, 53 ,4 "
