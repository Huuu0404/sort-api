# RESTful API Documentation

This is a simple RESTful API built with Flask to sort arrays using the quicksort algorithm.

## API Endpoints

### GET /arrays/sorted

Sort an array using the quicksort algorithm.

- **URL**: `/arrays/sorted`
- **Method**: `GET`
- **Content-Type**: `application/json`

#### Query Parameters

- **array** (list): The array of elements to be sorted. This should be passed as a query parameter.
- **reverse** (boolean, optional): If set to `true`, the array will be sorted in descending order. Defaults to `false`. This should be passed as a query parameter.

#### Example Request

To send a request with `GET`, the data should be included in the query string. Since query strings can be limited in size, it’s better to use `POST` for larger data, but for demonstration:

```sh
curl -G 'http://127.0.0.1:5000/arrays/sorted' \
-d 'array=[3,1,4,1,5,9,2,6,5,3,5]' \
-d 'reverse=false'
