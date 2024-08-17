
# L2_3

# Task for the week
- Find the process ID the your program
- Find what system calls are being used
- Change the default file descriptor


## Resources
- [Board Work L2](./board_Work/L2_board.png)
- [Board Work L3](./board_Work/L3_board.png)
- [Code](./code/)
- https://www.man7.org/linux/man-pages/man1/cat.1.html
- https://www.man7.org/linux/man-pages/man1/time.1.html
- https://man7.org/linux/man-pages/man1/top.1.html
- https://www.unix.com/man-page/v7/1/cc/
- https://linux.die.net/man/1/hexedit
- https://man7.org/linux/man-pages/man1/strace.1.html
- https://man7.org/linux/man-pages/man2/write.2.html
- https://github.com/torvalds/linux
- https://man7.org/linux/man-pages/man1/ps.1.html


### CLIs

#### Execute code
Execute Python scripts
```bash
python FILENAME.py
```

Compile C souce code
```bash
cc FILENAME.c -o EXECUTABLE_NAME
```
Execute the code
```bash
./EXECUTABLE_NAME
```

#### Other stuff
Look at running processes
```bash
top
```
```bash
htop
```

Measure runtime
```bash
time -p PROGRAM
```
Read text file
```bash
cat FILENAME
```
Read machine code
```bash
hexedit EXECUTABLE_NAME
```

Check the system calls of process id (PID)
```bash
sudo strace -p PID
```





## How a process is created from source code

**Step 1: Preprocessing**

1. The preprocessor reads the source code file (e.g., hello.c) and expands macros, includes header files (/usr/include), and performs other preliminary operations.
2. The preprocessor outputs a modified source code file (e.g., hello.i) with expanded macros and included headers.

**Step 2: Compilation**

1. The compiler (e.g., gcc) reads the preprocessed source code file (hello.i) and translates it into assembly code (e.g., hello.s).
2. The compiler checks for syntax errors, semantic errors, and performs optimization.

**Step 3: Assembly**

1. The assembler (e.g., as) reads the assembly code file (hello.s) and translates it into machine code (e.g., hello.o).
2. The assembler generates object code, which is machine-specific.

**Step 4: Linking**

1. The linker (e.g., ld) reads the object code file (hello.o) and combines it with library code (if necessary) to create an executable file (hello).
2. The linker resolves external references, allocates memory, and prepares the executable for loading.

**Step 5: Loading**

1. The loader reads the executable file (hello) and loads it into memory.
2. The loader allocates memory for the program, initializes registers, and sets up the program's stack.

**Step 6: Process Creation**

1. The operating system creates a new process by:
    - Allocating a unique process ID (PID).
    - Creating a process control block (PCB) to manage the process.
    - Initializing the process's memory space.
    - Setting up the process's file descriptors.
2. The operating system transfers control to the newly created process.

**Step 7: Execution**

1. The processor executes the instructions in the process's memory space.
2. The process runs until completion, termination, or interruption.



## How a process is created from a Python script

**Step 1: Parsing**

1. The Python interpreter (e.g., python) reads the Python script file (e.g., (link unavailable)) and parses it into an Abstract Syntax Tree (AST).
2. The parser checks for syntax errors and performs lexical analysis.

**Step 2: Compilation**

1. The Python interpreter compiles the AST into bytecode (e.g., (link unavailable)c).
2. The bytecode is platform-independent, intermediate code.

**Step 3: Loading**

1. The Python interpreter loads the bytecode into memory.
2. The interpreter initializes the Python runtime environment.

**Step 4: Interpretation**

1. The Python interpreter executes the bytecode line-by-line.
2. The interpreter performs dynamic typing, memory management, and binding.

**Step 5: Process Creation**

1. The operating system creates a new process for the Python interpreter.
2. The process is allocated memory, file descriptors, and other resources.

**Step 6: Execution**

1. The Python interpreter executes the script, using the loaded bytecode.
2. The script runs until completion, termination, or interruption.

Note: Python doesn't compile to machine code like C/C++. Instead, it compiles to bytecode, which is executed by the Python interpreter at runtime. This allows for platform independence and dynamic typing.

Additional steps for Python:

**Step 7: Module Loading**

1. The Python interpreter loads required modules and libraries.
2. Modules are cached in memory for future use.

**Step 8: Garbage Collection**

1. The Python interpreter periodically performs garbage collection.
2. Unused memory is reclaimed, and memory leaks are prevented.

