## Prerequesites 
- Make sure you have Python3 installed on your system.
- MongDB install instructions here: [Install MongoDB](https://docs.mongodb.com/manual/installation/)
- Install [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) to make API calls 




## Task 1 

A Script to parse and injest into MongoDB the file `db_works_test.csv`.

### Instructions to Run Task 1 

Change directory into the `task1` folder. Make sure you create install all requirements from the `requirements.txt` using the command:

```pip install -r requirements.txt```

The script is configured to connect to a local instance of MongoDB so make sure you have MongoDB installed and change the parameters as neccesary if you want to connect to a hosted Mongo instance

To the run the script run the following command:

`python3 task1.py`

## Task 2 

A simple API that queries the Mongo Collection by ISWC and returns the right owners.

### Instructions to Run Task 2 

Change directory to `task2` folder. Make sure to install all the required packages from the `requirements.txt` file as follows:

```pip install -r requirements.txt```

The script is configured to connect to a local instance of MongoDB so make sure you have MongoDB installed and change the parameters as neccesary if you want to connect to a hosted Mongo instance. The REST API has been developed using the Flask Python framework. 

To run the API , use the following command:

```python3 app.py```

The endpoints included in the API are:

|  Endpoint | Description  |   
|---|---|
|  127.0.0.1:5000/`<iswc>` | Returns right owners from the record of corresponding ISWC code   |  

<br>
<br>

Example Request:

`http://127.0.0.1:5000/T-042088917-3`

Example Response:

```
[
  {
    "name": "RAFAEL MENDIZABAL ITURAIN",
    "role": "Autor",
    "ipi": 200703727.0
  },
  {
    "name": "JOSE CARPENA SORIANO",
    "role": "Autor",
    "ipi": 222061816.0
  },
  {
    "name": "FRANCISCO MARTINEZ SOCIAS",
    "role": "Compositor",
    "ipi": 222084113.0
  }
]

```


