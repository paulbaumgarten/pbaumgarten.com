<!-- TITLE: Read Uploaded File In Broswer -->

# Read an uploaded text file in the browser

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<input type="file" id="names">

<script>
    function callback(data) {
        let lines = data.content.split("\n");
        for (let line of lines) {
            console.log(line);
        }
    }

    function upload(){
        let f = document.querySelector("#myfile").files[0];
        var reader = new FileReader();
        reader.onload = function (e) {
            callback({
                name: f.name,
                size: f.size,
                type: f.type,
                content: e.target.result
            });
        };
        reader.readAsText(f);
    }
    function main(){
        document.querySelector("#myfile").addEventListener("change",upload);
    }
    window.onload=main;
</script>

</body>
</html>
```
