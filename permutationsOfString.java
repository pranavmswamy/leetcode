// "static void main" must be defined in a public class.
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        permutation("ABC");
    }
    
    public static void permutation(String str) {
        permutation(str, "");
    }
    
    public static void permutation(String remaining, String current) {
        // if remaining == 0, || len(current) == len(str), one permutation is done. So print the number.
        if(remaining.length() == 0) {
            System.out.println(current);
        }
        else {
            for(int i=0; i<remaining.length(); i++) {
                // remove ith character
                String remainingAfterRemoved = remaining.substring(0, i) + remaining.substring(i+1);
                // continue recursive call after attaching ith character to current and trimming remaining.
                permutation(remainingAfterRemoved, current+remaining.charAt(i));
            }
        }
    }
    
}
