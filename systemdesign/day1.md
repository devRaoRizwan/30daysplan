# How a Browser Reaches a Website

When you enter a URL such as:

```text
https://example.com/products/phone
```

the browser needs to locate the server, establish a connection, and request the resource.

A simplified flow is:

```text
URL
 ↓
DNS Lookup
 ↓
TCP Connection
 ↓
TLS Handshake
 ↓
HTTP Request
 ↓
Server
 ↓
HTTP Response
```

---

## 1. URL

A **URL (Uniform Resource Locator)** tells the browser where and how to access a resource.

Example:

```text
https://example.com/products/phone
```

A URL can contain several parts:

```text
https://example.com/products/phone
  │          │          │      │
scheme     domain      path   resource
```

### Scheme

```text
https://
```

The scheme tells the browser which protocol to use.

`https` means:

> Use HTTP over a secure TLS connection.

The `S` in HTTPS stands for **Secure**. It means the HTTP communication is encrypted using TLS.

---

### Domain

```text
example.com
```

The domain is a human-readable name used to identify a website.

The browser cannot directly establish a network connection using a domain name. It first needs to find the IP address associated with that domain.

That's where **DNS** comes in.

> Note: A domain is not necessarily "the server." A domain can point to one or many servers, and the same server can host multiple domains.

---

### Path

```text
/products/phone
```

The path identifies the resource or route being requested from the server.

For example:

```text
/products
/products/phone
/users/123
/api/products
```

A path is **not necessarily a directory on the server's filesystem**.

In modern web applications, it is often a route handled by backend code.

---

### Is `phone` a file?

Not necessarily.

In:

```text
/products/phone
```

`phone` could be:

* a resource
* an API endpoint
* a dynamic route
* a database object
* or a file

For example, a Django application might receive:

```text
GET /products/phone
```

and use backend code to query a database and generate the response.

So don't assume that the last part of a URL is an actual file.

---

# 2. DNS Lookup

Before the browser can connect to the server, it needs an IP address.

For example:

```text
example.com
      ↓
93.184.216.34
```

DNS stands for **Domain Name System**.

It translates human-readable domain names into IP addresses.

You can think of DNS as a distributed naming system:

```text
Domain name → IP address
```

The browser/operating system may check caches first. If the address isn't already cached, a DNS resolver can query the DNS system to find the appropriate record.

DNS does **not** simply work like one universal database containing every IP address in one place. It is a distributed, hierarchical system.

---

# 3. TCP Connection

Once the browser knows the destination IP address, it needs to establish a network connection.

For traditional HTTPS over HTTP/1.1 or HTTP/2, this involves **TCP**.

TCP stands for:

**Transmission Control Protocol**

TCP provides a reliable connection between the client and server.

The connection begins with the TCP three-way handshake:

```text
Client                    Server

  SYN  -------------------->
       <-------------------- SYN-ACK
  ACK  -------------------->
```

After this connection is established, data can be exchanged reliably.

> Note: Modern HTTP/3 uses QUIC instead of TCP, so this flow is not universal for every HTTPS connection.

---

# 4. TLS Handshake

Because we're using:

```text
https://
```

the connection needs to be secured using **TLS**.

TLS stands for:

**Transport Layer Security**

Before normal HTTP data is exchanged, the client and server perform a TLS handshake.

The handshake allows them to establish the cryptographic parameters needed for secure communication and lets the client authenticate the server using its certificate.

Simplified:

```text
Client                     Server

       TLS handshake
  <------------------------>

       Secure connection
  ========================>
```

After TLS is established, HTTP messages can be sent through the encrypted connection.

### Important

TLS itself is **not the handshake**.

Rather:

> TLS is the security protocol, and the TLS handshake is the process used to establish the secure connection.

---

# 5. HTTP Request

Now the browser can send an HTTP request.

For example:

```http
GET /products/phone HTTP/1.1
Host: example.com
```

The request tells the server what the client wants.

An HTTP request can contain:

* Method
* Path
* Headers
* Query parameters
* Body

Common HTTP methods include:

```text
GET
POST
PUT
PATCH
DELETE
```

For example:

```http
GET /products/phone
```

means:

> Give me the resource at `/products/phone`.

---

# 6. Server

The request reaches a server responsible for handling it.

The server is not necessarily a single physical machine.

A real application may involve:

```text
Browser
   ↓
Load Balancer
   ↓
Web Server
   ↓
Application Server
   ↓
Database
```

For example, a Django application might receive:

```http
GET /products/phone
```

The application could then:

1. Match the URL to a Django route.
2. Execute backend logic.
3. Query PostgreSQL.
4. Serialize the data.
5. Return an HTTP response.

---

# 7. HTTP Response

The server sends an HTTP response back to the client.

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "name": "Phone",
    "price": 50000
}
```

The response usually contains:

* Status code
* Headers
* Body

### Status codes

Some common status codes are:

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
500 Internal Server Error
```

The response body contains the actual data returned by the server.

Depending on the request, it could be:

* HTML
* JSON
* CSS
* JavaScript
* an image
* a file
* or another type of data

---

# Complete Flow

For a traditional HTTPS connection using HTTP/1.1 or HTTP/2, a simplified flow looks like this:

```text
User enters URL
       ↓
https://example.com/products/phone
       ↓
DNS lookup
       ↓
Domain → IP address
       ↓
TCP connection
       ↓
TLS handshake
       ↓
Encrypted connection established
       ↓
HTTP request
       ↓
GET /products/phone
       ↓
Server/application processes request
       ↓
HTTP response
       ↓
200 OK + response data
       ↓
Browser processes and displays the result
```

---

# The Mental Model

Remember the process like this:

```text
DNS
"Where is example.com?"

TCP
"Let's establish a reliable connection."

TLS
"Let's make this connection secure."

HTTP
"I want /products/phone."

Server
"Let me process that request."

Response
"Here is the result."
```

---

## One-Line Summary

```text
DNS → finds the IP
TCP → establishes a reliable connection
TLS → establishes secure communication
HTTP → defines the request and response
Server → processes the request
Response → carries the result back to the client
```

> **Note:** This is a simplified model for learning. Real-world networking can involve DNS caching, proxies, CDNs, load balancers, connection reuse, HTTP/2 multiplexing, and HTTP/3/QUIC.
