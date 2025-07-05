// # pair product
// # Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

// # Be sure to return the indices, not the elements themselves.

// # There is guaranteed to be one such pair whose product is the target.

import java.util.HashMap;
import java.util.List;

public class aPairProduct {

    public static List<Integer> findPairProduct(List<Integer> arr, int target) {
        
        HashMap<Integer, Integer> hMap = new HashMap<>();
        for (int i = 0; i <= arr.size(); i++) {
            int num = arr.get(i);
            int compliment = target / num;

            if (hMap.containsKey(compliment)) {
                return hMap.get(compliment), i;
            }
             
        }
    }
}