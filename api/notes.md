API 

concepts 
- different types of APIs (REST, SOAP, GraphQL)
- system design concepts 
- scalable systems
- pagination authentication versioning etc
- API documentation best practices 

api = application program interface 
surface area for communication between different software applications
allows different software systems to interact with each other
APIs define the methods and data formats that applications can use to communicate with each other

types of APIs
1. REST (Representational State Transfer)
- architectural style for designing networked applications
- stateless communication
- uses standard HTTP methods (GET, POST, PUT, DELETE)
- resources are identified by URIs
- commonly uses JSON or XML for data exchange
- widely used for web services due to its simplicity and scalability
2. SOAP (Simple Object Access Protocol)
- protocol for exchanging structured information in web services
- relies on XML for message format
- uses various transport protocols (HTTP, SMTP, etc.)
- more rigid and complex compared to REST
- supports advanced security features (WS-Security)
- older and less commonly used than REST
3. GraphQL
- query language for APIs and runtime for executing those queries
- it interact with a backend service to fetch only the data that is requested
- instead of multiple endpoints, it exposes a single endpoint
- clients can specify exactly what data they need
- frontend provides query flexibility and reduces over-fetching or under-fetching of data
- gaining popularity for modern web and mobile applications
3. gRPC
- open-source remote procedure call (RPC) framework developed by Google
- uses HTTP/2 for transport and Protocol Buffers (protobuf) for serialization
- protobuf means smaller message sizes and faster serialization/deserialization
- supports multiple programming languages
- designed for high-performance and low-latency communication
- commonly used in microservices architectures
 5. WebSockets
- protocol for full-duplex communication channels over a single TCP connection
- enables real-time communication between client and server
- commonly used in applications like chat apps, live notifications, and online gaming
- allows for bi-directional data exchange without the overhead of HTTP requests
- reduces latency and improves responsiveness in real-time applications

Json 
- lightweight data interchange format
- easy for humans to read and write
- easy for machines to parse and generate
- uses key-value pairs and arrays to represent data structures
- commonly used in web APIs for data exchange
