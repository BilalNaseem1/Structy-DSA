

class IsPrime {
    private int x;
    private int n;

    public IsPrime(int n) {
        this.n = n;
        this.x = (int) Math.sqrt(n);
    }

    public boolean findisprime() {
        if (n <=1) {
            return false;
        }


        for (int i = 2; i<= x; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }


    public static void main(String[] args) {
        IsPrime ip = new IsPrime(5);
        boolean output = ip.findisprime();
        System.out.println(output);
    }
}