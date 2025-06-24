// In Java, instance variables must be declared at the class level before you can assign to them in the constructor
// The name of the constructor must be exactly the same as the class name (case-sensitive) and must not have a return type — not even void.

class LongestWord {
    // Instance variables to store the sentence, longest word, and its length
    private String sentence;
    private int longestWordLength;
    private String longestWord;

    // Constructor
    public LongestWord (String sentence) {
        this.sentence = sentence;
        this.longestWordLength = Integer.MIN_VALUE;
    }

    // Method to find and return the longest word in the sentence
    public String findLongest() {
        String[] words = this.sentence.split(" ");
        
        for (String i : words) {
            if ( i.length() >= this.longestWordLength ) {
                this.longestWordLength = i.length();
                this.longestWord = i;
            }

        }
        return this.longestWord;
    }
    public static void main(String[] args) {
        LongestWord lw = new LongestWord("this is a wonderful place");
        String output = lw.findLongest();
        System.out.println(output);


    }
}