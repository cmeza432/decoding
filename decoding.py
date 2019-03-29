"""
Name:   Carlos Meza
Date:   02/11/2019
"""

import numpy as np

"""   Represent the pulses in Python (Given)   """
pulse0 = np.ones( 10 )
pulse0 = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
pulse1 = pulse1/np.linalg.norm(pulse1) 


"""   Cauchy-Schwarz inequality function   """
def matched_filter(v, w):
    return np.linalg.norm(np.dot( v, w )) / np.linalg.norm(np.dot(abs(v), abs(w)))


"""   Read in csv file to use values for filtering   """
data = np.genfromtxt('data.csv', delimiter=',')
# Get amount of 10 set values of list and resize it by that many rows
data_length = int(len(data)/10)
data = np.resize(data, (data_length, 10))
# Get amount of 8 sets of bit numbers of previous 10 set values and create empty list
num_char = int(data_length/8)
# Array to insert 0 or 1 after comparison
bits = np.zeros((num_char, 8))
# Variables for iterating
col_tracker = 0
row_tracker = 0
N = 0


"""   Use Cauchy-Schwarz function and check if 0 or 1 bit value   """
for x in range(data_length):
    # Get normalized value for both comparisons
    value1 = matched_filter(data[x], pulse0)
    value2 = matched_filter(data[x], pulse1)
    # The column and row vector trackers incremented or restarted
    if(col_tracker == 8):
        col_tracker = 0
        row_tracker += 1
    # Compare norm value and decide either 0 or 1 value
    if(value1 > value2):
        bits[row_tracker][col_tracker] = 0
    else:
        bits[row_tracker][col_tracker] = 1
    col_tracker += 1

# Convert array into int to remove decimal and join rows of 0 and 1's
bits = bits.astype(int)
# Empty string to hold final value
final = []
while(N < num_char):
    # Join each row of binary values into continous binary
    temp = ''.join(str(x) for x in bits[N])
    # Convert into int from binary
    temp = int(temp, 2)
    # Append the int numbers equal ASCII number into 'final' string
    final.append(chr(temp))
    N += 1
    
print(''.join(final))
