// write a program that takes an array of integral numbers and returns the sum of all the positive numbers in the array.

using System;
public class PositiveSums{
    public static int Sum(int[] numbers){
        int sum = 0;
        foreach (int number in numbers){
            if (number > 0){
                sum += number;
            }
        }
        return sum;
    }
    public static void Main(string[] args){
        int[] numbers = { 1, 2, 3, 4, 5, -1, -2, -3, -4, -5 };
        System.Console.WriteLine("The sum of all positive integers from the array is: " + Sum(numbers));
    }
}