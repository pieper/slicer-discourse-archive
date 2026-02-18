# While running segment app in slicer, showing wrong url

**Topic ID**: 34703
**Date**: 2024-03-04
**URL**: https://discourse.slicer.org/t/while-running-segment-app-in-slicer-showing-wrong-url/34703

---

## Post #1 by @Ajay_Kumar (2024-03-04 19:14 UTC)

<p>--------After downloading this below dataset<br>
monailabel datasets --download --name Task07_Pancreas --output .</p>
<p>------and after runnig below the command to run the app<br>
monailabel start_server --app apps/radiology --studies C:\monai-projects\lung-images --conf models segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f989fb5f63000c3d6016e1f204484671c1a932ac.png" data-download-href="/uploads/short-url/zBwvVR5QmnUGUvhjCa487Oa5rWY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f989fb5f63000c3d6016e1f204484671c1a932ac_2_690x382.png" alt="image" data-base62-sha1="zBwvVR5QmnUGUvhjCa487Oa5rWY" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f989fb5f63000c3d6016e1f204484671c1a932ac_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f989fb5f63000c3d6016e1f204484671c1a932ac_2_1035x573.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f989fb5f63000c3d6016e1f204484671c1a932ac_2_1380x764.png 2x" data-dominant-color="191919"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1062 217 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>-------its successfully on my local server on  <a href="http://0.0.0.0:8000" rel="noopener nofollow ugc">http://0.0.0.0:8000</a></p>
<p>But after opening 3d Slicer and select module to MonaiLabel to check the output, Im getting error image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0379a7ba0c314008b8a50dc22ee14533118f0357.png" data-download-href="/uploads/short-url/uK4NFE3GKzBSrD8LhYxT6v47EX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0379a7ba0c314008b8a50dc22ee14533118f0357_2_690x402.png" alt="image" data-base62-sha1="uK4NFE3GKzBSrD8LhYxT6v47EX" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0379a7ba0c314008b8a50dc22ee14533118f0357_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0379a7ba0c314008b8a50dc22ee14533118f0357_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0379a7ba0c314008b8a50dc22ee14533118f0357_2_1380x804.png 2x" data-dominant-color="CFD5E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1120 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Traceback (most recent call last):<br>
File “C:/monai-projects/VISTA/monailabel/plugins/slicer/MONAILabel/MONAILabel.py”, line 1204, in fetchInfo<br>
info = self.logic.info()<br>
File “C:/monai-projects/VISTA/monailabel/plugins/slicer/MONAILabel/MONAILabel.py”, line 2586, in info<br>
return self._client().info()<br>
File “C:/monai-projects/VISTA/monailabel/plugins/slicer/MONAILabel/MONAILabel.py”, line 2562, in _client<br>
if mc.auth_enabled():<br>
File “C:\Softwares\Slicer 5.6.1\slicer.org\Extensions-32438\MONAILabel\lib\Slicer-5.6\qt-scripted-modules\MONAILabelLib\client.py”, line 83, in auth_enabled<br>
status, response, _, _ = MONAILabelUtils.http_method(“GET”, self._server_url, selector)<br>
File “C:\Softwares\Slicer 5.6.1\slicer.org\Extensions-32438\MONAILabel\lib\Slicer-5.6\qt-scripted-modules\MONAILabelLib\client.py”, line 521, in http_method<br>
conn.request(method, selector, body=body, headers=headers)<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\http\client.py”, line 1285, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\http\client.py”, line 1331, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\http\client.py”, line 1280, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\http\client.py”, line 1040, in _send_output<br>
self.send(msg)<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\http\client.py”, line 980, in send<br>
self.connect()<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\http\client.py”, line 946, in connect<br>
self.sock = self._create_connection(<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\socket.py”, line 844, in create_connection<br>
raise err<br>
File “C:\Softwares\Slicer 5.6.1\lib\Python\Lib\socket.py”, line 832, in create_connection<br>
sock.connect(sa)<br>
OSError: [WinError 10049] The requested address is not valid in its context</p>
<p>Please help me out.</p>
<p>Thanks<br>
Ajay</p>

---

## Post #2 by @muratmaga (2024-03-04 19:18 UTC)

<aside class="quote no-group" data-username="Ajay_Kumar" data-post="1" data-topic="34703">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ajay_kumar/48/69562_2.png" class="avatar"> Ajay_Kumar:</div>
<blockquote>
<p>-------its successfully on my local server on <a href="http://0.0.0.0:8000">http://0.0.0.0:8000 </a></p>
</blockquote>
</aside>
<p>0.0.0.0 doesn’t seem like a valid IP address. There might something wrong with your network settings. If the monai label is running on the same computer as the Slicer, try server address <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></p>

---
