public bool IsHappyNumber(int n) {

    var hash = new HashSet<int>();

    while(!hash.Contains(n)) {
        hash.Add(n);

        int sum = 0;
        while(n > 0) {
            sum += (int) Math.Pow(n % 10, 2);
            n /= 10;
        }

        if(sum == 1) return true;

        n = sum;
    }

    return false;
}