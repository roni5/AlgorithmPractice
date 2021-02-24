namespace LeetCode.C#.SecondRound
{
    public class BsetTimeToBuyAndSellStock
    {
         public int MaxProfit(int[] prices)
         {
             int maxProfit = 0;

             if (prices.Length == 0) return maxProfit;

             int minPrice = prices[0];

             foreach (var price in prices)
             {
                 minPrice = Math.Min(minPrice, price);
                 maxProfit = Math.Max(maxProfit, price - minPrice);
             }

             return maxProfit;
         }
    }
}