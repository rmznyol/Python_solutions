# Python Solutions

This repository presents the solutions to (some) Python programming challanges that I have solved. In particular it includes the following study programs from LeetCode and some other resources:
* LeetCode75 - LeetCode(Complete)
* Top Interview 150 - LeetCode
* Red Book programming chapter



#### Remarkable Python Features:
1. Order of evaluation in multiple assignment:
    - all expressions at the right part of the assignment are evaluated first
    - the items are assigned, from left to right, to the corresponding targets.
    e.g the expression `x.property, x = y , a + b` first evaluatues `y` and `a + b` and then assigns property of `x` to be `y` and then changes value of `x` to the `a + b`. This subtlety feature can shorten multiple lines to a single line at once.

2. a default value object will be pointed in function object:
 see the details at https://www.youtube.com/watch?v=0Om2gYU6clE&ab_channel=Sreekanth

3. an immutable tuple can contain mutable variables which can vary:
see the details at https://stackoverflow.com/questions/9755990/why-can-tuples-contain-mutable-items

 