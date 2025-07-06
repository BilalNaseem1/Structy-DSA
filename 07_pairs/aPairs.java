import java.util.List;
import java.util.ArrayList;

class aPairs {

    public static List<List<String>> aPairs(List<String> arr) {
        List<List<String>> result = new ArrayList<>();
        
        int x = 0;
        for (int i = 0; i<= arr.size(); i++) {
            for (int j = x; j<= arr.size() - x; j++) {
                
                System.out.println(arr.get(i));
                System.out.println(arr.get(j));

                

            }
            
        }
    return result;
    
    
    }

    public static void main(String[] args) {
        List<String> input = List.of("A", "B", "C");

        List<List<String>> pairs = aPairs(input);
        System.out.println(pairs);
    }
}