<!-- TITLE: Javascript Detect Device -->
# Detecting screen / device

Return true/false if we are on a mobile device (all 1 line).   

```js
var isMobile = navigator.userAgent.toLowerCase().indexOf('mobile') > 0 ? true : false;
```

Get the browser window dimensions.   

```js
var w = window.innerWidth;    
var h = window.innerHeight;
```

Detect if the window has resized (such as a phone/tablet being rotated) and adjust our width/height settings accordingly.   

```js
function adjustSize() {
   w = window.innerWidth;
   h = window.innerHeight;
}
window.onresize = adjustSize;
```
