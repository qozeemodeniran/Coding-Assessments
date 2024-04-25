using System;

class Program{
    static int Factorial(int n){
        if(n==0){
            return 1; // the factorial on 0 is 1
        }
        else {
            return n * Factorial(n-1); // Factorial of 5 = 5*(5-1)(4-1)(3-1)(2-1) = 5*4*3*2*1
        }
    }

    static void Main(string[] args){
        int number = 5;
        int factorial = Factorial(number);

        Console.WriteLine($"The factorial of {number} is {factorial}");
    }
}