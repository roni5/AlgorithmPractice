namespace LeetCode.CSharp.SecondRound
{
    public class MinimumKnightMoves
    {
        private class Coordinate
        {
            public int x { get; set; }
            public int y { get; set; }

            public MinimumKnightMoves(int x, int y)
            {
                x = x;
                y = y;
            }
        }

        public int MinKnightMoves(int x, int y)
        {
            int moves = 0;

            x = Math.Abs(x);
            y = Math.Abs(y);

            int[] xDir = new int[] {-2,-2,-1,-1,1,1,2,2,};
            int[] yDir = new int[] {-1,1,-2,2,-2,2,-1,1};

            Queue<Coordinate> q = new Queue<Coordinate>();
            Coordinate starting = new Coordinate(0, 0);
            q.Enqueue(starting);

            HashSet<(int, int)> visited = new HashSet<(int, int)>();
            visited.Add((starting.x, starting.y));

            while (q.Count != 0)
            {
                int size = q.Count;

                for (int i = 0; i < size; i++)
                {
                    Coordinate point = q.Dequeue();
                    if (point.x == x && point.y == y) return moves;

                    for (int j = 0; j < xDir.Length; j++)
                    {
                        int newX = point.x + xDir[j];
                        int newY = point.y + yDir[j];
                        Coordinate newPoint = new Coordinate(newX, newY);

                        if(!visited.Contains((newX, newY)) && newX >= -2 && newY >= -2)
                        {
                            q.Enqueue(newPoint);
                            visited.Add((newX, newY));
                        }
                    }
                }

                moves++;
            }

            return -1;
        }
    }
}