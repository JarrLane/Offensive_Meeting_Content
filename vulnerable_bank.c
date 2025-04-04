#include <stdio.h>

int main()
{
    int dollars = 0;
    printf("Welcome to the bank, you have %d dollars, input an 8 digit code to check your balance again: ", dollars);
    
    int balance = 0;
    char response [8];
    gets(response);
    dollars = balance;
    printf("You have %d dollars, have a good day", dollars);
    
    return 0;
}