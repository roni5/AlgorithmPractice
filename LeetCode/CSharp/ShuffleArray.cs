public class Solution
{
    private int[] nums;
    private Random rnd = new Random();

    public Solution(int[] nums)
    {
        this.nums = nums;
    }

    public int[] Reset()
    {
        return this.nums;
    }

    public int[] Shuffle()
    {
        var n = this.nums.Length;
        var result = new int[n];
        Array.Copy(this.nums, result, n);
        for (int i = 0; i < n; i++)
        {
            var index =rnd.Next(i, n);
			this.Swap(result, i, index);
            
        }
        return result;
    }
    
    private void Swap(int[] result, int a, int b) {
        // swap i with index
            var t = result[a];
            result[a] = result[b];
            result[b] = t;
    }
}