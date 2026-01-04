API Notes

Overview
- API = Application Program Interface: surface area for communication between software applications.
- Defines methods and data formats so different systems can interact.

Core Concepts
- Different types of APIs (REST, SOAP, GraphQL, gRPC, WebSockets).
- System design concepts for scalable systems.
- Pagination, authentication, versioning, etc.
- API documentation best practices.

API Types
1) REST (Representational State Transfer)
- Architectural style for networked apps; stateless communication.
- Uses HTTP methods (GET, POST, PUT, DELETE); resources identified by URIs.
- Commonly uses JSON or XML; simple and scalable for web services.

2) SOAP (Simple Object Access Protocol)
- Protocol for structured web service communication; XML message format.
- Works over multiple transports (HTTP, SMTP, etc.).
- More rigid/complex than REST; supports WS-Security; older and less common today.

3) GraphQL
- Query language and runtime for APIs; single endpoint.
- Clients specify exactly the data needed; reduces over- and under-fetching.
- Interacts with backends to return only requested fields; popular for modern web/mobile.

4) gRPC
- Open-source RPC framework (Google); uses HTTP/2 and Protocol Buffers (protobuf).
- Smaller messages and faster serialization/deserialization.
- Multi-language support; designed for high-performance, low-latency microservices.

5) WebSockets
- Full-duplex communication over a single TCP connection.
- Enables real-time client-server interaction (chat, live notifications, gaming).
- Bi-directional data without HTTP request overhead; reduces latency.

JSON
- Lightweight data interchange format.
- Easy for humans to read/write and for machines to parse/generate.
- Uses key-value pairs and arrays to model data.
- Commonly used in web APIs for data exchange.


REST API

methods - GET, POST, PUT, DELETE, PATCH
resources - Endpoints representing data entities ,db records

endpoint - compination of base URL + resource path
example: https://api.example.com/api/v1/resources 

nesting data - hierarchical representation of related resources
example: /users/{userId}/posts/{postId}/comments

GET - Retrieve data from server
- example: GET /users/{userId} - fetch user details
- response: 200 OK with user data in JSON
POST - Create new resource on server
- example: POST /users - create new user
- request body: JSON with user details
- response: 201 Created with new user data
PUT - Update existing resource on server  replaces entire resource
- example: PUT /users/{userId} - update user details
- request body: JSON with updated user details
- response: 200 OK with updated user data
DELETE - Remove resource from server
- example: DELETE /users/{userId} - delete user
- response: 204 No Content
- indicates successful deletion with no content returned
PATCH - Partially update existing resource on server selectively changes
- example: PATCH /users/{userId} - update specific user fields
- request body: JSON with fields to update
- response: 200 OK with updated user data
updates should be idempotent meaning multiple identical requests have same effect as single request
accidental duplicate requests should not cause unintended changes\
but if we do post multiple times we will create multiple resources 
  

nested data vs filtering
- Nested data: hierarchical representation of related resources
  - example: /users/{userId}/posts/{postId}/comments
- Filtering: query parameters to refine results
  - example: /posts?author={authorId}&date={date}
  - returns posts by specific author on specific date
- Both techniques can be combined for complex queries
- example: /users/{userId}/posts?date={date}
- returns posts by user on specific date
- Use nested data for relationships; filtering for specific criteria within resources
  
if you have complex access patterns use query parameters to filter data instead of creating deeply nested endpoints

how to pass data to backend
- Query parameters: appended to URL for filtering/sorting not use for sensitive data
  - example: /posts?author={authorId}&sort=date
- Request body: for POST/PUT/PATCH to send data
  - example: POST /users with JSON body containing user details
- Headers: metadata like authentication tokens, content type
- Path parameters: part of URL to identify specific resources
  - example: /users/{userId}    
  - used to specify which user to retrieve/update/delet

pagination
- Techniques to split large datasets into manageable chunks
1) Limit and Offset
- limit: number of items to return
- offset: number of items to skip
- example: /posts?limit=10&offset=20
- returns 10 posts starting from the 21st post
2) Page Numbering
- page: page number to retrieve
- per_page: number of items per page
- example: /posts?page=2&per_page=10
- returns 10 posts from the 2nd page
3) Cursor-based Pagination
- cursor: unique identifier for the last item in the previous page
- example: /posts?limit=10&cursor={lastPostId}
- returns next 10 posts after the specified cursor  
- more efficient for large datasets; avoids issues with data changes between requests
- choose pagination method based on use case and data size 

api request structure
<!-- ex with header and all include an api post -->
example: POST /users
Headers:
  Content-Type: application/json
  Authorization: Bearer {token}
Body:
{
    "name": "John Doe",
    "email":  ""
}

status codes
- 200 OK: Successful GET, PUT, PATCH, DELETE
- 201 Created: Successful POST creating a resource
- 204 No Content: Successful DELETE with no content returned
- 400 Bad Request: Invalid request syntax/parameters
- 401 Unauthorized: Missing/invalid authentication
- 403 Forbidden: Authenticated but lacks permission
- 404 Not Found: Resource not found
- 500 Internal Server Error: Server-side error
- 503 Service Unavailable: Server temporarily unavailable
- Use appropriate status codes to indicate request outcome


api response structure
example: GET /users
{
    "users: [
        {
            "id": 1,
            "name": "John Doe",
            "email": "
        },
    ],
    "meta": {
        "total": 100,
        "page": 1,
        "per_page": 10
    }
    "api-version": "1.0",
    "response":200,
    "continuation-token": "eyJ2IjoiMSIsImsiOiIxMjM0NSJ9",

}

- Standardize response format for consistency
- Include data, metadata (pagination info), status code, versioning info
- Use continuation tokens for pagination in large datasets
- Example: "continuation-token": "eyJ2IjoiMSIsImsiOiIxMjM0NSJ9"
- helps clients fetch subsequent pages without relying on page numbers
- Include error details in response body for failed requests
example: 400 Bad Request
{
    "error": {
        "code": 400,
        "message": "Invalid request parameters",
        "details": [
            "Missing 'email' field",
            "Password too short"
        ]
    }
}


middleware
- Software layer between client and server to process requests/responses
- Common functions: authentication, logging, rate limiting, data validation
- Enables modular and reusable components for API functionality
- Example: Authentication middleware checks for valid tokens before processing requests


api documentation and specs
- based on libries work with you api
- OpenAPI/Swagger: Standard for RESTful API documentation; interactive docs
- Postman: Tool for testing APIs; can generate documentation from collections
- API Blueprint: Markdown-based API documentation format; easy to read/write
- RAML (RESTful API Modeling Language): YAML-based API modeling language; focuses on design
- Good documentation includes endpoint descriptions, request/response examples, status codes, authentication methods
- Keep docs up-to-date with API changes for developer usability
- Use tools to automate documentation generation from code/comments

versioning
- Strategies to manage API changes without breaking existing clients
1) URI Versioning
- Include version in URL path
- example: /api/v1/resources
2) Query Parameter Versioning
- Include version as query parameter
- example: /api/resources?version=1
3) Header Versioning
- Specify version in custom header
- example: X-API-Version: 1
4) Content Negotiation
- Use Accept header to specify version
- example: Accept: application/vnd.example.v1+json
- Choose versioning strategy based on use case and client needs 
  
  