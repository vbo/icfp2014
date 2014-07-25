Registers
========

%c: control register (program counter / instruction pointer)
	The machine has logically separate address spaces for code versus data. The %c register is an instruction pointer, pointing to the next instruction to be executed. Programs are laid out from low addresses to high. The effect of most instructions on the instruction pointer is simply to increment its value by one.

%s: data stack register
	The data stack is used to save intermediate data values during calculations, and to return results from function calls.
	It is a logically contiguous stack. The %s register points to the top of the stack.
	Many of the instructions simply pop and push values on the data stack. For example the ADD instruction pops two integer values off the stack and pushes back their sum.
	
%d: control stack register
	The control stack is used to save return information in function calls. It saves return address and environment frame pointers.
	Only the complex control flow instructions affect the control stack and register. See SEL/JOIN and AP/RAP/RTN for details

%e: environment frame register
	environment = chain of frames
	frame consists of a pointer to its parent frame and zero or more data values
	The %e register points to the local frame.

	
Data Heap
========
three types of data value: integers, pairs and closures
Pairs and closures are represented by pointers to objects in the data heap.
Here and further [5, 4, 3, 2, 1] - 5 is the first element to pop and the firtst element pushed into the heap.

	
Commands
========
- LDC $n		load an immediate literal; push it onto the data stack
- LD $n $i	    load an i-th value from the n-th frame in the environment; push it onto the data stack
- ADD 		    2nd + 1st; replace last 2 values with the result
- SUB		    2nd - 1st; replace last 2 values with the result
- MUL		    2nd * 1st; replace last 2 values with the result
- DIV		    FLOOR(2nd/1st); replace last 2 values with the result
- CEQ		    2nd == 1st ? 1 : 0; replace last 2 values with the result
- CGT		    2nd > 1st ? 1 : 0; replace last 2 values with the result
- CGTE		    2nd >= 1st ? 1 : 0; replace last 2 values with the result
- ATOM		    is_int(1st) ? 1 : 0; replace last value with the result
- CONS		    [2st, 1nd]; replace last 2 values
- CAR		    get 1st elem from the CONS; replace CONS
- CDR		    get 2nd elem from CONC; replace CONS
- SEL $t $f	    1st == 0 ? goto $f : goto $t; remove 1st; JOIN can be used after to continue
- JOIN 
- LDF $f		add function starting from 0, save current pointer
- AP $n
- RTN
- DUM $n
- RAP $n
- STOP          end of program
- TSEL $t $f    like CELL but JOIN is not possible
- TAP $n
- TRAP $n
- ST $n $i
- DBUG		    echo 1st; remove 1st
- BRK
