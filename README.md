# README 

# Movie API in GOLANG


# Need to do 
Movie

	- director
	
	- cast/actors
	
	- release year
	
	

# Install and Start mongodb
```
sudo mongod
```
# Start your go server
``` 
go run app.go 
```


# Add a movie

```
curl -sSX POST -d '{"name":"Star Wars: Episode IV - A New Hope","cover_image":"https://images-na.ssl-images-amazon.com/images/I/81aA7hEEykL.jpg","year":"1977","description":"Star Wars Episode IV - A New Hope"}' http://localhost:3000/movies
```

# Get list of all value

```
curl -sSX GET http://localhost:3000/movies | jq '.'
```

# Update a movie
```
curl -sSX PUT -d '{"name":"Star Wars: Episode IV - A New Hope","cover_image":"https://images-na.ssl-images-amazon.com/images/I/81aA7hEEykL.jpg","year":"1977","description":"Star Wars Episode IV - A New Hope"}' http://localhost:3000/movies

```


# Delete a movie
```
curl -sSX DELETE -d '{"name":"Star Wars: Episode IV - A New Hope","cover_image":"https://images-na.ssl-images-amazon.com/images/I/81aA7hEEykL.jpg","year":"1977","description":"Star Wars Episode IV - A New Hope"}' http://localhost:3000/movies | jq '.'
```



# Test Data

```
curl -sSX POST -d '{"name":"Star Wars","cover_image":"https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Supertrooper.jpg/220px-Supertrooper.jpg", "description":"the room","year":"1977"}' http://localhost:3000/movies

curl -sSX POST -d '{"name":"Super Troopers","cover_image":"https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Supertrooper.jpg/220px-Supertrooper.jpg", "description":"the room","year":"1977"}' http://localhost:3000/movies

curl -sSX POST -d '{"name":"Forgetting Sarah Marshall","cover_image":"http://www.gstatic.com/tv/thumb/v22vodart/175320/p175320_v_v8_ad.jpg", "description":"best movie ever","year":"1977"}' http://localhost:3000/movies

curl -sSX POST -d '{"name":"The Room","cover_image":"http://t3.gstatic.com/images?q=tbn:ANd9GcREEsN-qCwFIPE7-FglJVTrE0ijr7-VwggC6CXNtMLYtMnHWthZ", "description":"the room","year":"1977"}' http://localhost:3000/movies

```






