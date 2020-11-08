//========= Number of ratings per city =====================
// Map function emits a tuple with city as key and 1 as value
var mapFunction = function () {
    emit(this.city, 1);
};

// Reduce function which counts the number of occurances of each key by summing the value column which is always 1
var reduceFunction = function (key, values) {
    reducedValue = Array.sum(values);
    return reducedValue;
};

// Map reduce query using the map and reduce functions from above                        
db.runCommand({
    mapReduce: 'Restaurants',
    map: mapFunction,
    reduce: reduceFunction,
    out: {
        inline: 1
    }
});

// Alternatively the same query can be written as              
db.Restaurants.mapReduce(mapFunction,
    reduceFunction, {
        out: {
            inline: 1
        }
    }
);