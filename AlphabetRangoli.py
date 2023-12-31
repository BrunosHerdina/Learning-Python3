def print_rangoli(size):
    
    #first calculate the rangoli width
    wid=4*size-3
    
    #the first part is crescent, till middle where there is max number of letter
    for i in range(0,size):
        st=chr(96+size-i)
        for z in range(i):
            st=chr(96+size-i+z+1)+"-"+st+"-"+chr(96+size-i+z+1)
        print(st.center(wid,"-"))
        
    #the second part is descrescent, remember not to repeat the middle line    
    for i in range(size-2,-1,-1):
        st=chr(96+size-i)
        for z in range(i):
            st=chr(96+size-i+z+1)+"-"+st+"-"+chr(96+size-i+z+1)
        print(st.center(wid,"-"))    
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

"""PROBLEM DESCRIPTION STARTS HERE

You are given an integer, N. 
Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

-Function Description
Complete the rangoli function in the editor below.
rangoli has the following parameters:
*int size: the size of the rangoli

-Returns
string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

-Input Format
Only one line of input containing , the size of the rangoli.

-Constraints
0<size<27

-Sample Input
5
-Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------"""
