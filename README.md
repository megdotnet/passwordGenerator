# Password Generator


This is a simple python script that will read from a list of words to create a simple password.  The lists used here are from the EFF wordlists. These can also be found online at:

[https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases)

This script does not follow the EFF guidelines of multi-word passphrases.  It also does not follow their guidelines for using dice to generate random numbers.  

This script is intended for generating quick simple passowrds that don't necessarily need to be of the highest security.  Future versions of this script might bump up the security, we'll see.

What this script will do:
- Read from one of the lists and select a random entry.
- Strip the leading digits used for the dice. 
- Capitalize the first letter.
- Add a randomly generated two digit number to the and.  

Examples of passwords generated with this script:
- Deity35
- Revocable86
- Comprised77
