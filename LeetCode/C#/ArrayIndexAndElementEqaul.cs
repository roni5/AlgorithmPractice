class Solution
{
    public static int IndexEqualsValueSearch(int[] arr)
    {
      if(arr[0] == 0) return 0;
      // your code goes here
      int start = 0;
      int end = arr.Length - 1;
      int currentMin = Int32.MaxValue;
      
      while(start <= end)
      {
        int mid = (start + end) / 2;
        if(arr[mid] == mid)
        {
          currentMin = Math.Min(currentMin, mid);
          end = mid - 1;
        }
        else if(arr[mid] > mid) end = mid - 1;
        else start = mid + 1;
      }
      
      if(currentMin != Int32.MaxValue) return currentMin;
      else return -1;
    }

    static void Main(string[] args)
    {
      int[] arr = new int[]{-1,1,2,3,4};
      Console.WriteLine(IndexEqualsValueSearch(arr));

    }
}
