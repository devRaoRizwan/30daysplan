<!-- Notes: DNS → TCP → TLS → HTTP request → server → response, one line each -->

A URL Contains of multiple parts 
https://example.com/products/phone

here are the following things in a url 
1- https:// --> it is the scheme of the url , this tells the browers to connect to the server using https protocol , with s at end means encrypted

2- example.com/ --> it is the domain of the server , 
3- products/ --> path or directory aka endpoint 
4- phone --> it is the actual file required

to reach the server the browser uses a DNS lookup it is the universal directory of ips and we fetch it 

TCP is the protocl that is being used to connect with the server 
TLS is the handshake between server and client before sending data 
HTTP request is the REQUEST of resource made by the cleint agent to the server 
server is the machine that responds to the request of users
respinse is the acual data being sent by the server inresponse of that request 