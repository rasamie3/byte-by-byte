# Python gRPC Example

This is my first implementation of **gRPC** in Python.  
I know I should probably learn Go at some point (maybe later), but for now, I wanted to understand the basics of gRPC and build a small project to truly grasp it — including running into real problems along the way.

## Overview

The project is simple:

- **GetUsers API** – returns a list of users.
- **GetUserById API** – returns a single user by ID.

I also separated the client and server into different **Docker containers** to simulate microservices (I know this is not exactly the same thing, but it serves the learning purpose).