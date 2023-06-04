import sys 

bitmap = """
...................................................................
   **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
**      *****************       ******************************
         *************          **  * **** ** ************** *
         *********            *******   **************** * *
         ********           ***************************  *
 *      * **** ***         *************** ******  ** *
            ****  *         ***************   *** ***  *
           ******         *************    **   **  *
            ********        *************    *  ** ***
              ********         ********          * *** ****
              *********         ******  *        **** ** * **
              *********         ****** * *           *** *   *
                 ******          ***** **             *****   *
                  *****            **** *            ********
                   *****             ****              *********
                    ****              **                 *******   *
                     ***                                       *    
                      **     *                    *
..................................................................."""

print('Enter the message to display with the bitmap : ')
message = input('> ')

if message == '':
    sys.exit()

#Loop over the each line in the bitmap:
for line in bitmap.splitlines():
    #Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == '':
            #Print an empty space since there's a space in the bitmap:
            print('', end ='')
        else:
            #Print a chracter from the message:
            print(message[i % len(message)], end='')
            
    print() # Prints new line 