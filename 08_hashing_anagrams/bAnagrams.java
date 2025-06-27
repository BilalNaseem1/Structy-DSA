import java.util.HashMap;

public class bAnagrams {

    private static HashMap<Character, Integer> getCounter(String s) {

        HashMap<Character, Integer> counter = new HashMap<Character, Integer>();

        for (char i : s.toCharArray()) {
            if (counter.get(i) == null) {
                counter.put(i, 0);
            }
            counter.put(i, counter.get(i) + 1);
        }

        return counter;
    }



    public static void main(String[] args) {
        HashMap<Character, Integer> count1 = getCounter("abbc");
        HashMap<Character, Integer> count2 = getCounter("aabc");

        System.out.println(count1.equals(count2));
    }
    
}
