# Cybersecurity Club Assignment
This is my submission for the recruitment assignment of Cybersecurity Club IITB
 
## Details
1. Email id - jayesh11.3.01@gmail.com
2. Name - Jayesh Singla
3. Department - CSE (going into 2nd year)

I took part in my first CTF a few days ago. Though I could solve only one problem, it was fun trying out different approaches to extract hidden information. I feel being part of this club will help me learn and explore this field more as a team and contribute to widen interest in this field in the institute.    

## Task 1
It was a very "creative problem".First I looped over all possible 3-byte combinations and stored which were present in a 256x256x256m counter array. After that I just looked at the indices of the array entries which were zero and got the corresponding 3-byte combinations. After that it was just looking at which combinations had spaces and joining them to form a sentence.  

The answer is in [here](task1/answer.txt)

## Task 2
Had to write some code to solve the problems.First I thought if the numbers and symbols were encoded in some way but looking at the length of the lines in the file,I rejected this possibility. 

Then I observed that there were groups of 7 lines. Then I saw there were repeating patterns in all the groups.I replaced the zeros with " " " and voila!,I saw the equations.

There were too many to solve by hand so I extracted the equations as strings into [easy.txt](task2/easy.txt) using the [decode.py](task2/decode.py) script. Then used the [solve.py](task2/solve.py) script to solve each equation individually.

The answers are in [here](task2/answers.txt) 

## Task 3
This took a lot of time. 
First I had to understand every piece of PHP syntax and functions in the source code. After that I thought if I could somehow intercept the query result using some software but couldn't do much progress in that direction. 

Then I found out about 'SQL Injection'. After reading some more, I found regexps could be used in queries. After that, I just injected a REGEXP condition on password in the query with username="admin". 

I kept looping over a dictionary of characters and kept generating a prefix of the password. Lastly, I performed a check after every addition of a character if I had found the correct password. This was done by injecting a simple password = "..." condition in the query.

The password is in [here](task3/password.txt)

## Task 4
I first opened the friday.pcap file using Wireshark. I looked at the type of protocols present. I found a deauthentication protocol so it looked like it could have something to do with password, but alas nothing. Then I thought of using 'strings' command on the file but the only meaningful string was something like 'DESKTOP-...'.

After further reading,I found a software called Hashcat which can perform dictionary attacks to crack the password from converted handshake file. But it required some configuration of OpenCL runtimes which were not supported on my OS(Ubuntu 18.04LTS).

So I used another software called John-The-Ripper and it gave me a password. I don't have a full idea of what happened here and will continue reading about it. My current understanding is that wifi passswords are encryted using some encryption techniques which are difficult to reverse. Therefore, softwares like Hashcat(while doing a dictionary attack) apply different encryption techniques to a set of words(the wordlist) and see if the encrypted output matches.

Anyways, my answer is [here](task4/password.txt)


