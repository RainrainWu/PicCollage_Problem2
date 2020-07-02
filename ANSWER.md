# Answer 1

## How I plan the project

### Tools
I have about two days of development time, which is really a bit stressful for me. I decided to use Python language which has a faster development speed, and Flask, the lightweight framework I am most familiar with.

### Schedule
Due to time limit, I decided to develop iteratively with the goal of the minimum viable product.

The core requirement in the specification is a shortened URL service, which is also the feature I implemented first. I implemented this part in the first pull request, and then other extended functions, they are sorted according to the implemented time as follows.

- metrix: tracking the visited times of shortened url。
- database: interact with external MongoDB database。
- tests: unit test and functional verification test.
- log: rotate logging for all request and error.
- tasks: tasks management for improving develop experience.

Some functions have a lower priority because they are less critical, but I don't have enough time to finish them. They are listed below, I think I need two more days to complete them all.

- containerize: improve portability and ease of deployment.
- jwt: make some admin endpoint require authorization to operate.
- better test: more integration-oriented test cases.
- better metrix: more tracking information for shortened url.

## High-level design of the architecture

![](https://i.imgur.com/JBEXUrU.png)

### Client-Server
The Client-Server model was adopted in my architecture, server will host the service and provide user interface, client can interact with server via HTTP/1.1 requests.

### Database
A MongoDB docker container would be used to store data, instead of storing in the python process. I also hope that the data is persistently stored, so I am not using volatile storage like Redis.

## Principles or design practices

### WSGI
Flask is a framework that takes advantage of the work already done by Werkzeug to properly interface WSGI, and provides a user-friendly interface so that I do not have to worry about the underlying details. I followed its design decisions for application development.

### RESTful API
I adopt RESTful specifications to design my web API endpoints, along with the Client-Server model. All of the API shoud be stateless, and implement a representational state transfer of the resource.
