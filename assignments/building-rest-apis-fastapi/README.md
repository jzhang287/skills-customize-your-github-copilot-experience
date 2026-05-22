# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI. You will define routes, validate request data, and implement CRUD-style behavior for a simple in-memory resource.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a FastAPI application and create a simple health check endpoint.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app
- Expose a `GET /health` endpoint
- Return a JSON response such as `{ "status": "ok" }`
- Run successfully with Uvicorn

### 🛠️ Build Resource Endpoints

#### Description
Create endpoints for a single resource type, such as books, tasks, or students. Keep the data in memory for this assignment.

#### Requirements
Completed program should:

- Define a list or dictionary to store sample records in memory
- Create a `GET /items` endpoint that returns all records
- Create a `GET /items/{item_id}` endpoint that returns one record by ID
- Return a `404` response when the record does not exist

### 🛠️ Add Validation and Write Operations

#### Description
Add request models and write endpoints so the API can create and update records safely.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming JSON data
- Create a `POST /items` endpoint that adds a new record
- Create a `PUT` or `PATCH /items/{item_id}` endpoint that updates an existing record
- Create a `DELETE /items/{item_id}` endpoint that removes a record
- Return clear error responses for invalid or missing data
