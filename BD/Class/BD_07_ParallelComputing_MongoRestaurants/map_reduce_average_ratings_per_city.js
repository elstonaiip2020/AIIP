//========== Average rating by city adding remarks ===================

// Map function emits a tuple with city as key and 1 as value
var mapFunction = function () {
    emit(this.city, this.rating);
};

// Reduce function which counts the number of occurances of each key by summing the value column which is always 1
var reduceFunction = function (key, values) {
    reducedValue = {
        avg: Array.avg(values)
    };

    //     reducedValue = {avg:Array.avg(values)};
    return reducedValue;
};

// Finalize function allows the output to modified. In here we add a new column "remarks"
var finalizeFunction = function (key, reducedValue) {
    if (reducedValue.avg < 3)
        reducedValue.remarks = "Fairly Good"
    else if (reducedValue.avg >= 3 && reducedValue.avg < 4.5)
        reducedValue.remarks = "Very Good"
    else if (reducedValue.avg >= 4.5)
        reducedValue.remarks = "Awesomely Good"
    else
        reducedValue.remarks = "No ratings"

    return reducedValue;
}
// Map reduce query using the map and reduce functions from above
db.Restaurants.mapReduce(mapFunction,
    reduceFunction, {
        out: {
            inline: 1
        },
        finalize: finalizeFunction
    }
);