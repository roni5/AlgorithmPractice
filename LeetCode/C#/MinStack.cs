public class MinStack {
    private List<int[]> stack;
    /** initialize your data structure here. */
    public MinStack() {
        this.stack = new List<int[]>();
    }
    
    public void Push(int x) {
        int currentMin = GetMin();
        if(x < currentMin){
            currentMin = x;
        }
        this.stack.Add(new int[]{x, currentMin});
    }
    
    public void Pop() {
        this.stack.RemoveAt(this.stack.Count - 1);
    }
    
    public int Top() {
        return this.stack[this.stack.Count - 1][0];
    }
    
    public int GetMin() {
        if(this.stack.Count == 0) return Int32.MaxValue;
        return this.stack[this.stack.Count - 1][1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.Push(x);
 * obj.Pop();
 * int param_3 = obj.Top();
 * int param_4 = obj.GetMin();
 */