# bitcoin-monitor
Update the .env file 
Run the docker-compose.yml using the cmd docker-compose up.
Then Please fire a REST call with url http://localhost:5000/api/prices?date=06-04-22&offset=0&limit=100
The response should be similar to 
{
"count": 3,
"data":[
{
"coin": "btc",
"price": 44868,
"timestamp": "06-04-2022"
},
{
"coin": "btc",
"price": 44769,
"timestamp": "06-04-2022"
},
{
"coin": "btc",
"price": 44769,
"timestamp": "06-04-2022"
}
],
"next": "http://127.0.0.1:5000/api/prices?date=06-04-22&offset=100&limit=100",
"url": "http://127.0.0.1:5000/api/prices?date=06-04-22&offset=0&limit=100"
}

When the btc value exceeds or reduces against the threshold given in the .env You should be recieving a mail in the mail id specified in the .env file
Now the Currency is defaulted to "BTC" and date format is defaulted to "DD-MM-YYY".
Please adhere to that in your API calls.
