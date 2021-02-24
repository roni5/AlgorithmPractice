public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        var answer = new List<int>();
        int beginRow = 0;
        int endRow = matrix.Length - 1;
        int beginCol = 0;
        int endCol = matrix[0].Length - 1;

        while(beginRow <= endRow && beginCol <= endCol)
        {
            for(int i = beginCol; i<=endCol; i++)
            {
                answer.Add(matrix[beginRow][i]);
            }
            beginRow += 1;

            for(int i = beginRow; i <= endRow; i++)
            {
                answer.Add(matrix[i][endCol]);
            }
            endCol -= 1;

            if(beginRow <= endRow)
            {
                for(int i = endCol; i >= beginCol; i--)
                {
                    answer.Add(matrix[endRow][i]);
                }
            }
            endRow -= 1;

            if(beginCol <= endCol)
            {
                for(int i = endRow; i>= beginRow; i--)
                {
                    answer.Add(matrix[i][beginCol]);
                }
                
            }
            beginCol += 1;
        }

        return answer;
    }
}