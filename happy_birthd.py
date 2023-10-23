def main():
    # Ask the user for their first and last name
    first_name = input("Enter your first name: ").lower()
    last_name = input("Enter your last name: ").lower()

    # Check if the input matches "jacob sargent"
    if first_name == "jacob" and last_name == "sargent":
        print("Happy birthday, Jacob Sargent!")
        response = input("\nDo you want to hear a special birthday message? (y/N): ").lower()
        if response == "y":
            print("""
                  \n\n Dearest Jacob, \n\n
                  Thank you for being such a great friend to me.
                  I admire how much you enjoy life, take it day by day, and stay balanced.
                  You're super fun to be around and you help people feel at ease. You cause
                  good things to happen that bring people together (Run Club) and create 
                  lasting relationships together. 
                  
                  You are going to go far in life, especially running-wise haha jk but in all ways.
                  Also I wish you luck in your internship search. Have a great birthday!!
                  

                  -Thomas
                   """)
            # Print an ASCII art bicycle
            print("""
                                                      $"   *.      *Bike*
              d$$$$$$$P"                  $    J
                  ^$.                     4r  "
                  d"b                    .db
                 P   $                  e" $
        ..ec.. ."     *.              zP   $.zec..
    .^        3*b.     *.           .P" .@"4F      "4
  ."         d"  ^b.    *c        .$"  d"   $         %
 /          P      $.    "c      d"   @     3r         3
4        .eE........$r===e$$$$eeP    J       *..        b
$       $$$$$       $   4$$$$$$$     F       d$$$.      4
$       $$$$$       $   4$$$$$$$     L       *$$$"      4
4         "      ""3P ===$$$$$$"     3                  P
 *                 $       \"""        b                J
  ".             .P                    %.             @
    %.         z*"                      ^%.        .r"
       "*==*""                             ^"*==*""     
            """)
        else:
            print("Ok, maybe next year.")
    else:
        print("I cannot confirm nor deny that it is your birthday. This program was built for one special guy in mind;)")

if __name__ == "__main__":
    main()
