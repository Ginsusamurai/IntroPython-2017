"""
you want to find a string formatting operator that will “pad” the number with zeros for you.

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'
"""

array = (2, 123.4567, 10000, 12345.67)
print ("file_00",array[0],":","{:.2f}".format(array[1]),"{:.2e}".format(array[2]),"{:.2e}".format(array[3]))
# .format()
