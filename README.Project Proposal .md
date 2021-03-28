# ReadMe
Myron Layese

## Final project Proposal
Hiya Dr. Rome! I've got actually two project proposals that I'm very keen on so I'll show both of them to you.

------------------------------------------------------


## Luhmann Theorem - Credit Card Detection!

So for this one the concept is simple - I'll be building a program that can detect whether or not credit cards are real or fake. It's already established that credit cards aren't just random jargon but rather a precise set of numbers. Luhmann's Theorem describes this as such: Data we use isn't random - it has a pattern. If it has a pattern that means we can probably code it! 

## The Skinny of it all

I'll be coding a program that lets me detect whether or not a card is real or fake and which company it's from. If I were to make it more efficient and it could scan a card rather than just type in numbers - I could see this being used anywhere that takes card. Think of it as a precaution.
I believe this'll be a good demomnstartion of what we've learned in class because it'll take into consideration: strings, elif, get, int, machine learning, etc.

## Resources
I've being coding this project on the side in C so I'll being translating it into python. It's a good excercise for me to be able to decipher what exactly I've written and trnsfer it into a diofferent language. Here's the code.

```
#include <stdio.h>
#include <cs50.h>

/**
 * Hello Dr. Rome! This is my comment section and I've explained how it works
 * Example:
 *
 * 378282246310005
 *  - - - - - - -
 *
 * 0*2 + 0*2 + 3*2 + 4*2 + 2*2 + 2*2 + 7*2 = 27
 *
 * 378282246310005
 * - - - - - - - -
 *
 * 3 + 8 + 8 + 2 + 6 + 1 + 0 + 5 = 33
 *
 * 27 + 33 = 60
 *
 * 60 % 10 == 0 / VALID CARD
 *
 */

int main()
{
    long long cc_number = get_long_long("Number: ");
    int digit1 = 0, digit2 = 0, num_digits = 0, sum_of_double_odds = 0, sum_of_evens = 0;

    while (cc_number > 0)
    {
      
        digit2 = digit1;
        digit1 = cc_number % 10;

        if (num_digits % 2 == 0)
        {
            sum_of_evens += digit1;
        }
        else
        {
            int multiple = 2 * digit1;
            sum_of_double_odds += (multiple / 10) + (multiple % 10);
        }

        cc_number /= 10;
        num_digits++;
    }

    bool is_valid = (sum_of_evens + sum_of_double_odds) % 10 == 0;
    int first_two_digits = (digit1 * 10) + digit2;

    if (digit1 == 4 && num_digits >= 13 && num_digits <= 16 && is_valid)
    {
        printf("VISA\n");
    }
    else if (first_two_digits >= 51 && first_two_digits <= 55 && num_digits == 16 && is_valid)
    {
        printf("MASTERCARD\n");
    }
    else if ((first_two_digits == 34 || first_two_digits == 37) && num_digits == 15 && is_valid)
    {
        printf("AMEX\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
```

### Timeline
This is the timeline I used

 - Week 1: Read up on Luhmann's Theorem and understand how it works
 
 - Week 1.5: Apply previous knowledge to C
  
 - Week 2: Learn different patterns for different card companies 
 
 - Week 2.5: Apply it into C
 
 - Week 3: Debug and run the code in C
 
 - Week 4: Translate it all into Python
 
 ----------------------------------------------
 
## Quantative Value Investing - Stock Prediction
 
 For this one I'll be making an AI that'll analyze a certain stock and determine if it goes up or down based on: Earnings report, pattern from last year, Volume, Open Interest, Market Cap, etc. I'm keen on this one because I enjoy learning about the stock market and I'm essentially making this bot for myself. I understand that Data Science in this aspect can be more convulted than our class delves into it but I'm very excited to tackle this problem (and probably create something very rudimentary).
 
## Resources 

I found a nifty little [tutorial](https://www.youtube.com/watch?v=URTZ2jKCgBc&list=PLQVvvaa0QuDd0flgGphKCej-9jp-QdzZ3&index=2)
for this kind of stuff on youtube so I'll be using that. I've also got "The Technical analysis of Stock trends" by John Magee that I've been reading up on. If I use anything from stackexchange or github I'll post it in the project read me.

## Timeline

- Week 1: Make some pseudocode on how exactly I want my code to run

- Week 1.5: Watch the tutorial on data science in Python.

- Week 1.75: Decide whether or not to make it in R if the python version seems boring.

- Week 2: Start building the code

- Week 3: Debug 

- Week 4: Make it more effiecient if need be

## Pseudocode

Here's a really really dumbed down version of what it should look like

```
Insert data Nasdaq
Insert data S&P500
Insert data Yahoo Finance

Get_tick(What symbol are you searching for: "")
Search tick in Nasdaq
            in S&P500
            
Look Up Earnings report for tick
  if earnings are good:
      return variable x
  if earnings are bad:
      return variable y
Look Up Volume from Past six months
  if volume > 50,000,000:
      return variable x
  if volume < 50,000,000:
      return variable y
Look Up other factors that determine stock growth/decay
  if good:
      return x
  if bad:
      return y

Calculate if x > y or if x < y
  if x < y:
    print ((tick) is predicted to go up in the next six months)
  else:
    print ((tick) is predicted to decrease in the next six months)
*** I'd also really like it of I could get a percentage of growth/decay. We shall see

```
