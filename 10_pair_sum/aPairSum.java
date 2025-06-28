import java.util.HashMap;
class aPairSum {
    private static int[] getPairSum(int[] numbers, int targetSum) {
        HashMap<Integer, Integer> hMap = new HashMap<>();
        for (int i =0; i<= numbers.length; i++){
            int compliment = targetSum - numbers[i];

            if (hMap.containsKey(compliment)) {
                return new int[]{hMap.get(compliment), i};
            }
            hMap.put(numbers[i], i);
        }
        return null;
    }

    public static void main(String[] args) {
        int[] numbers = {3, 5, -4, 8, 11, 1, -1, 6};
        int targetSum = 10;
        int[] output = getPairSum(numbers, targetSum);
        System.out.println(output);
    }

}