This is a simple RESTful API built with Flask to sort arrays using the quicksort algorithm.

API Endpoints
POST /sort
Sort an array using the quicksort algorithm.

URL: /sort
Method: POST
Content-Type: application/json
Request Body

array (list): The array of elements to be sorted.
reverse (boolean, optional): If set to true, the array will be sorted in descending order. Defaults to false.

Example Request
curl -X POST http://127.0.0.1:5000/sort \
-H "Content-Type: application/json" \
-d '{"array": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5], "reverse": false}'

Example Response
{
    "sorted_array": [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
}

Error Response
Condition: If array is not provided in the request body.
Code: 400 BAD REQUEST
Content:
{
    "error": "Array is required"
}
