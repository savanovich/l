![arch](img/arch.jpg)

Service designed for about 3000 events per second. Further horizontal scaling also possible. 

## Tech stack
- Python >3.6
- Kafka
- asyncio
- autobahn https://autobahn.readthedocs.io/en/latest/

All components are Open Source projects. Python very fast for prototyping and widely used for
development such web services. Standard Python's asynchronous framework `asyncio` with `epoll`
event poll has sufficient performance for high loaded microservices.

## Rationale behind the design

**Web socket** minimizes overhead of calls to service, TCP handshakes and HTTP headers .

**Autobahn** - framework to work with WebSockets on both sides client and server. 
It has a wide range of supported programming languages. 
Also, it has high performance and fully asynchronous implementation (via `asyncio` for `python`).

**Kafka** can be thought as a сentral bus for a heterogeneous system of microservices.
Reporting system (Redshift for example) can be one of the Kafka's consumers.

 