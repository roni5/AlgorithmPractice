namespace LeetCode.CSharp.SecondRound
{
    public class ReorderRoutesToMakeAllPathsLeadToTheCityZero
    {
        public int MinReorder(int n, int[][] connections) 
        {
        
            int changes = 0;
            
            HashSet<(int, int)> edges = new HashSet<(int, int)>();
            foreach(var connection in connections)
            {
                edges.Add((connection[0], connection[1]));
            }
            
            Dictionary<int, List<int>> neighbors = new Dictionary<int, List<int>>();
            for(int i = 0; i < n; i++)
            {
                neighbors[i] = new List<int>();
            }
            foreach(var connection in connections)
            {
                neighbors[connection[0]].Add(connection[1]);
                neighbors[connection[1]].Add(connection[0]);
            }
            
            HashSet<int> visited = new HashSet<int>();
            visited.Add(0);
            
            return DFS(edges, neighbors, visited, 0, ref changes);
        
        }
    
        private int DFS(HashSet<(int, int)> edges, 
                    Dictionary<int, List<int>> neighbors,
                    HashSet<int> visited, int city, ref int changes)
        {
            foreach(var neighbor in neighbors[city])
            {
                if (!visited.Contains(neighbor))
                {
                    //Check if neighbor can reach 0
                    if (!edges.Contains((neighbor, city)))
                        changes++;
                    visited.Add(neighbor);
                    //Check if this neighbor's neighbor can also reach 0
                    DFS(edges, neighbors, visited, neighbor, ref changes);
                }
                
            
            }
            
            return changes;
        }
    }
}