// find the factorial of a number using recursion
public class Factorial {
    public static void main(String[] args) {
        int number = 7;
        long factorial = multiplyNumbers(number);
        System.out.println("Factorial of " + number + " = " + factorial);
    }
    public static long multiplyNumbers(int num) {
        if (num >= 1)
            return num * multiplyNumbers(num - 1);
        else
            return 1;
    }
}