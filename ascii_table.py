# Problem:

# Write a program which prints out the ASCII characters which correspond with the ASCII codes from 32 to 127

# The output should look like this

# chr:      !   "   #   $   %   &   '   (   )   *   +   ,   -   .   / 
# asc: 32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47 
# chr:  0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ? 
# asc: 48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63 
# chr:  @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O 
# asc: 64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79 
# chr:  P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _ 
# asc: 80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95 
# chr:  `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o 
# asc: 96  97  98  99  100 101 102 103 104 105 106 107 108 109 110 111
# chr:  p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~     
# asc: 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127

# Caveats: Use very simple constructs (i.e., no `else` allowed). The Python `chr` built-in is allowed.

# Global constants
CHR_LINE_START = "chr: "
ASC_LINE_START = "asc: "
ASC_RANGE_BEGINNING = 32
ASC_RANGE_ENDING = 127
LARGEST_ASC_NUMBER_WIDTH = len(str(Asc_range_ending))
ASCII_CHARS_PER_LINE = 16

# Global variables
current_chr_string = CHR_LINE_START
current_asc_string = ASCII_CHARS_PER_LINE
ascii_numbers_processed = 0

# Loop through range 32 to 128 (exclusive)
for ascii_number in range(Asc_range_beginning, Asc_range_ending + 1):
# Signify that we are now processing a new ascii number
   ascii_numbers_processed = ascii_numbers_processed + 1
# If we've processed 16 ascii numbers, set a counter back to 0 to track how many
#    ascii numbers we've processed for the current chr and asc strings
# Build up strings
   if ascii_numbers_processed > Ascii_chars_per_line:
      current_chr_string = Chr_line_start
      current_asc_string = Asc_line_start
      ascii_numbers_processed = 1
#    First string is chr string consisting of each ascii char corresponding to
#       the current ascii number. It should be added to the string and padded
#       on on the left and right to make it sit in the middle of a box with a
#       width of Largest_asc_number_width
   new_chr_string = " " + chr(ascii_number) + " "

   if len(new_chr_string) != Largest_asc_number_width:
      print("Error: chr string should have a length of 3 chars")
      break

   current_chr_string = current_chr_string + new_chr_string

#    Second string is asc string consisting of each ascii number and it should be
#       padded on the right side to be equal in width to Largest_asc_number_width
   new_asc_string = str(ascii_number)
   new_asc_string = new_asc_string + " " * (Largest_asc_number_width - len(new_asc_string))

   if len(new_asc_string) != Largest_asc_number_width:
      print("Error: asc string should have a length of 3 chars")
      break

   current_asc_string = current_asc_string + new_asc_string

# An additional space should now be added to the end of the strings (unless
#   we're processing the last ascii number in the row
   if ascii_numbers_processed != Ascii_chars_per_line:
      current_chr_string = current_chr_string + " "
      current_asc_string = current_asc_string + " "
# If we have just processed the last ascii number of this line (ascii_numbers_process)
#   print both the chr and asc lines
   if ascii_numbers_processed == Ascii_chars_per_line:
      print(current_chr_string)
      print(current_asc_string)
