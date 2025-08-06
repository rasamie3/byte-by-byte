"""
Main concepts of Recursion functions
    - base case
        - the condition that stops the recursion
        - prevents infinite recursion

    - recursive case
        - the part of the function where it calls itself with a modified argument (mostly smaller version of the previou one)
        - brings the problem closer to base case -sure- 

    - call stack
        - each recursive call is pushed onto call stack (that's why it is hated by people who care about their memory)
        - once base is reached, the stack begins to .. idk the word... like when we pop its values

    - input reduction
        - the input must change on each recursive call to eventually reach the base case (i think this is like how we live our lives and base case is death... nvm)

    - correct return handling
        - recursive functions are often return values from deeper calls and it's surely used for combining the results
"""


# example (from my brain not chat or whatever)

def stopwatch(time):
    # base case 
    if time == 0:
        return 'Beeeeeeeeeeeeep'
    print(f"{time}s")
    return stopwatch(time - 1) 

print(stopwatch(10))