using System;

class Solution
{
    public static int BracketMatch(string text)
    {
      // your code goes here
      int numOfClosingNeeded = 0;
      int numOfOpenNeeded = 0;
      for(int i = 0; i < text.Length; i++)
      {
        if(text[i] == '(')
        {
          numOfClosingNeeded += 1;
        }
        else if(text[i] == ')')
        {
          numOfClosingNeeded -= 1;
        }
        if(numOfClosingNeeded < 0)
        {
          numOfClosingNeeded += 1;
          numOfOpenNeeded += 1;
        }
      }
      
      return numOfOpenNeeded + numOfClosingNeeded;
    }

    static void Main(string[] args)
    {

    }
}