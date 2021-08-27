
import textwrap     # textwrap is imported, so we will use textwrap methods

def wrap(string, max_width):
    draken = textwrap.fill(string,max_width)      # textwrap.wrap returns a list whereas textwrap.fill returns the string in different lines
    return draken
  
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
