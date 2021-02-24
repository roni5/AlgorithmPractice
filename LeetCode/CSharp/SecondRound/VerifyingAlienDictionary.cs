// In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
// Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

// Example 1:

// Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
// Output: true
// Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
// Example 2:

// Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
// Output: false
// Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
// Example 3:

// Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
// Output: false
// Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

namespace LeetCode.CSharp.SecondRound
{
    public class VerifyingAlienDictionary
    {
        public bool IsAlienSorted(string[] words, string order)
        {
            //O(1)
            int[] map = new int[26];
            for(int i = 0; order.Length; i++)
            {
                map[order[i] - 'a'] = i;
            }

            //O(n * m -- max number of char to compare)
            for(int i = 0; i < words.Length - 1; i++ )
            {
                int minLenCompare = Math.Min(words[i].Length, words[i + 1].Length);
                for(int j = 0; j < minLenCompare; j++)
                {
                    char prev = words[i][j];
                    char next = words[i + 1][j];

                    if (map[prev - 'a'] < map[next - 'a'])
                        break;
                    else if (map[prev - 'a'] > map[next - 'a'])
                        return false;
                    else if (j == minLenCompare - 1 && words[i].Length > words[i + 1].Length)
                        return false;
                }
            }

            return true;
        }
    }
}