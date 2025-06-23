// max value

// Write a method, maxValue, that takes in an array of numbers as an argument. The method should return the largest number in the array.

// Solve this without using any built-in array methods.

// You can assume that the array is non-empty.

class Source {
    public static double maxValue(double[] numbers) {
        double max_value = Double.NEGATIVE_INFINITY;
        for (double i : numbers) {
            if (i > max_value) {
                max_value = i;


            }
        
        }
        return max_value;
    }

    public static void main (String[] args) {
        double[] numbers = { 4, 7, 2, 8, 10, 9 };
        double output = maxValue(numbers);
        System.out.println(output);
    }
}