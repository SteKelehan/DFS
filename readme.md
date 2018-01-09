
# Internet Apps Distributed File System

Student Name: Stephen Kelehan<br />
Student Number: 14316006<br />

## Project

This project was to construct a simple distributed file system. 

### Choice to implement the following
* Distributed Transparent File Access
* Directory Service
* Caching
* Locking Server

## Code

There are multiple python scrips, they are explained below.

### File Server

The file server was split into two scrips, one acts as the local machine and the other interacts with the other nodes.<br />
The API was forther split into two blocks of code alowing one blolk to control the individual files. 

### Directory Server

The Directory Server is just like the file sever in the way it is split into a lockal and an API.<br />
The Directory is flat, meaning it only has one level.


### Locking Server

This is a Server that again like the previuos to is serperated into API and lockal.<br />
It locks the files when a user is using it so it does not have any concurrency issues.

### Cache

The cache is set up in the client lib. It is a simple caching mechanisim whereby it keeps the most resent 10 files.<br />
When a call is made by the users it the client lib will first check the local cache before fetching from the file server.

### Client Lib

This is the file that the users useses to access the files.

## Built With

* [REST Tutorial](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful) - Used to build templated of rest servers - api 
* [Flask](https://flask-restful.readthedocs.io/en/latest/) - Used to communicated between node and task setter
