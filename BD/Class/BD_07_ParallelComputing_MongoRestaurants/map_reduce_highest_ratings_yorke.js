//=================== Highest rating for restauarants in the city of Yorke
// Map function emits a tuple with city as key and 1 as value
var mapFunction = function () {
    emit(this.city, this.rating);
};

// Reduce function which counts the number of occurances of each key by summing the value column which is always 1
var reduceFunction = function (key, values) {

    var max = values[0];
    values.forEach(function (val) {
        if (val > max)
            max = val;
    });
    return max
};

// Map reduce query using the map and reduce functions from above
db.Restaurants.mapReduce(mapFunction,
    reduceFunction, {
        out: {
            inline: 1
        },
        query: { city: "York" }
    }
);