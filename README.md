# FastAPI (REST) vs GraphQL

### Installation:

#### Create a virtual enviroment and activate

``` 
python -m venv env
```

``` 
source ./env/bin/activate
```

#### Install dependencies

``` 
pip install -r requirements.txt
```

---

### API REST powered by FastAPI

#### Start the server:

```
uvicorn restapp:app
```

#### Make requests:

```
GET  http://localhost:8000/employee
```

```
GET  http://localhost:8000/employee?id=1001
```

---

### GraphQL powered by Ariadne

#### Start the server:

``` 
uvicorn graphqlapp:app 
```

or

``` 
uvicorn graphqlapp:app --port 8001 
```

#### Make requests with GraphQL Playground Interface:

Open in browser:

```
http://localhost:8000 
```

or

```
http://localhost:8001 
```

#### Make querys and press Play

``` 
{ employee { fullName } } 
```

``` 
{ employee(id: 1001) { fullName age } } 
```

```
{
  employee(id: 1001) { fullName age }
  product { name price }
  supplier { name address }
}
```

This example is only for fetching data, to show the principal differences between REST and 
GraphQL approaches.