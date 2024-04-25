using System;

class ReverseString{
    static string Reverse(string str){
        char[] charArray = str.ToCharArray();
        int left = 0;
        int right = str.Length - 1;

        while (left < right){
            char temp = charArray[left];
            charArray[left] = charArray[right];
            charArray[right] = temp;

            left++;
            right--;
        }
        return new string(charArray);
    }

    static void Main(string[] args){
        string input = "Qozeem";
        string reversed = Reverse(input);
        Console.WriteLine($"The reversed of {input} is {reversed}");
    }
}