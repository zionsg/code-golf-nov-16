# Question 1

Given an ASCII string, output the exploded suffixes of it. For example, if the string was abcde, there are 5 suffixes, ordered longest to shortest:

    abcde
    bcde
    cde
    de
    e

Each suffix is then exploded, meaning each character is copied as many times as its one-indexed location in that suffix. For example, exploding the suffixes of abcde,

    abcde
    12345
    abbcccddddeeeee
    
    bcde
    1234
    bccdddeeee
    
    cde
    123
    cddeee
    
    de
    12
    dee
    
    e
    1
    e

Altogether, the exploded suffixes of abcde are

    abbcccddddeeeee
    bccdddeeee
    cddeee
    dee
    e

## Rules

1. The input will consist of the printable ASCII characters. (This excludes newlines but includes spaces.)
2. The output will have each string on a separate line.
3. Trailing spaces are allowed on each line and there may be an extra newline at the end.

## Test Cases

    ''
    
    'a'
    a
    
    'bc'
    bcc
    c
    
    'xyz'
    xyyzzz
    yzz
    z
    
    'code-golf'
    coodddeeee-----ggggggooooooollllllllfffffffff
    oddeee----gggggoooooolllllllffffffff
    dee---ggggooooollllllfffffff
    e--gggoooolllllffffff
    -ggooollllfffff
    goolllffff
    ollfff
    lff
    f
    
    's p a c e'
    s  ppp    aaaaa      ccccccc        eeeeeeeee
     pp   aaaa     cccccc       eeeeeeee
    p  aaa    ccccc      eeeeeee
     aa   cccc     eeeeee
    a  ccc    eeeee
     cc   eeee
    c  eee
     ee
    e
