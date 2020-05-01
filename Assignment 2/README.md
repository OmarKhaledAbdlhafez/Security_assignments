##Assignment2
~~~~
genfei challenge in cybertalent check it form this [link](https://cybertalents.com/challenges/cryptography/genfei)
~~~~
##How to solve this 
~~~~
 don't change anything in the encrypt file your role is to decrypt this algorithm 
 the key of this problem is to discover that 
 **It's a Feistel Network and hence the name generalized feistel.
 Basically chain rule. We can start by decrypting the d in
 the second step of encryption. 
 From there it is easy to follow the chain and undo it.** 
 and do this steps :
 ~~~~
 - F() function do xor operation then it's the reverse of itself
 so we don't need to change it 
 -decryption stage two first 
 - start by decrypt d then  a ,b , c   
 - note that we use a to get c in the end so we save it in temp before do anything 
 - repeat the last 2  steps again on stage one 
 - run and get the ouput and remove all # and submit 
