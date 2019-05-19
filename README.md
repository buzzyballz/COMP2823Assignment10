# Union-Box Assignment

Hey there!

We're trying something new with this assignment, a new marking framework and a
new submission system. (I'm also using Unit tests this time - so hopefully a bit
more stable and easier testing)

Read this *carefully* if you want to make your submissions count!

## Language file

Similar to previous sessions - we're going to be using the `LANGUAGE` file to
select what language you are using.

Please uncomment **ONLY ONE** language.


## Python

### union_box.py

This is the **ONLY** file you need to edit, simply implement the ``merge``
function and you're good to go!

The merge function simply takes two "boxes" (or outlines of multiple boxes) and
merges them together.

**Aside:**
The coordinates in python are Tuples, so `[0]` will reference the `X`, and
`[1]` will reference the `Y`.

E.g.

```
   ____           ____
 _|__  |        _|    |
| |  | |  ==>  |      |
|_|__|_|       |      |
```

## Java

***IMPORTANT NOTE - MAIN FOLDER IS REQUIRED***

We need the "main" folder, (for `package main`) to be able to run the files
in the test suite, so please make sure you don't change them from there!

### UnionBox.java

Again, this is the **ONLY** file that you're going to need to modify.

The merge function simply takes two "boxes" (or outlines of multiple boxes) and
merges them together.

E.g.

```
   ____           ____
 _|__  |        _|    |
| |  | |  ==>  |      |
|_|__|_|       |      |
```

### Coordinate.java

Unfortunately, Java didn't have a nice `Pair` or `Tuple` that we could use
nicely. So I implemented a `Coordinate` class.

The constructor: ``new Coordinate(x, y)`` takes 2 integers, the X position and
Y position.

#### ``Coordinate.x``

This returns the X position of the coordinate.

#### ``Coordinate.y``

This returns the Y position of the coordinate.

## SUBMISSIONS - DO NOT INCLUDE TESTS!!!

### Python

For Python, the submission **ZIP** should look like this:

```
.
├── box.py
├── LANGUAGE
├── union_box.py
└── union_interface.py

```

### Java

For Java, The submission **ZIP** should look like this:
(all your java files in the "main" folder)

```
.
├── LANGUAGE
├── main
    ├── Box.java
    ├── Coordinate.java
    ├── UnionBox.java
    └── UnionInterface.java

```
