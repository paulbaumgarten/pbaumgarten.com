<!-- TITLE: Javascript Geolocation -->

# Geolocation

Test availability 

```js
if ("geolocation" in navigator) {
  /* geolocation is available */
}
```

Get current position (once)

```js
navigator.geolocation.getCurrentPosition( whereAmI );

function whereAmI( position ) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    console.log("You are at "+lat+" , "+lon);
}
```

Monitor current position (keep re-executing if I move)

```js
var id = navigator.geolocation.watchPosition( whereAmI );

function whereAmI( position ) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    console.log("You are at "+lat+" , "+lon);

    navigator.geolocation.clearWatch(id); // cancel monitor
}
```

