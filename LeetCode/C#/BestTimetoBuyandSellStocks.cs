public class Solution {
    public int MaxProfit(int[] prices) {
        int minPrice = int.MaxValue;
        int maxProfit = 0;
        
        foreach(var price in prices){
            minPrice = Math.Min(price, minPrice);
            int profit = price - minPrice;
            maxProfit = Math.Max(profit, maxProfit);
        }
        
        return maxProfit;
    }
}