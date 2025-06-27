
// importing hashmap class - to store key value pairs
import java.util.HashMap;


class aHashing {

    // helper function to return hashmap which has characters as keys as integer for counts 
    private static HashMap<Character, Integer> charCountFunc(String s) {
        // initializing hashmap
        HashMap<Character, Integer> count = new HashMap<Character, Integer>();

        for (char i : s.toCharArray()) { // converted string to character array
            if ( count.get(i) == null) { // if i not in map
                count.put(i, 0);

            } 
            count.put(i, count.get(i) + 1);
        }
        return count;

    }



    public static void main(String[] args) {
        HashMap<Character, Integer> count1 = charCountFunc("amazing");

        System.out.println(count1);


    }
}