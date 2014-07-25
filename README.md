icfp2014
========

Registers
-----
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
-----
	three types of data value: integers, pairs and closures
	Pairs and closures are represented by pointers to objects in the data heap.
	The three types of values are distinguished by tag bits. The tag bits are not software visible (except for the ATOM instruction) but are used by the hardware for error checking.
	
Commands
-----
LDC $n		load an immediate literal; push it onto the data stack
LD $n $i	load an i-th value from the n-th frame in the environment; push it onto the data stack
ADD 		pop two integers off the data stack; push their sum
SUB			2nd integer -1st integer off the data stack; push the result of subtracting one from the other
MUL			2nd*1st, to data stack
DIV			FLOOR(2nd/1st), to data stack. 0 if it's 


Setup
-----

 $ pip install --user -r requirements.txt
