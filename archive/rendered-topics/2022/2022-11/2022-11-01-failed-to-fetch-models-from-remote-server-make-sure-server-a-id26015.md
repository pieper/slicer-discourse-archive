# Failed to fetch models from remote server. make sure server address is correct and <server_uri>/v1/models is accessible in browser

**Topic ID**: 26015
**Date**: 2022-11-01
**URL**: https://discourse.slicer.org/t/failed-to-fetch-models-from-remote-server-make-sure-server-address-is-correct-and-server-uri-v1-models-is-accessible-in-browser/26015

---

## Post #1 by @platanus (2022-11-01 23:54 UTC)

<p>Hello. 3D-Slicer members.</p>
<p>I have used well NVIDIA AIAA module in 3d-slicer since June first, 2022.</p>
<p>However, it occurred some error nvidia aiaa module in 3d-slicer yesterday.</p>
<p>The occurred error is as following.</p>
<ol>
<li>When I run segment editor, and then I pressed nvidia aiaa effect button in segment editor module. but nvidia aiaa didn’t work in 3d-slicer.<br>
I confirmed error message that ‘failed to fetch models from remote server. make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser’.</li>
</ol>
<p>I conducted well modeling using nvidia aiaa effect in segment editor of 3d-slicer until 2days ago.</p>
<p>I don’t know why this error occurs to me.</p>
<p>Please, let me know how to solve this error.</p>
<p>And…</p>
<p>Sometimes, it seems to stop network communication managing NVIDIA AIAA server because of the latest updates to the extension.</p>
<p>please check whether network communication regarding NVIDIA AIAA server run or not.</p>

---

## Post #2 by @platanus (2022-11-03 01:15 UTC)

<p>I checked revision of 3d-slicer(revision 31260 built 2022-11-02) today.</p>
<p>After I reinstalled as revision version and I ran 3d-slicer program, I pressed nvidia aiaa effect button in segment editor module.</p>
<p>But It also occurrs same error occurred in last version such as having that<br>
‘Failed to fetch models from remote server. make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser.’.</p>
<p>Does it have how to solve regarding this error?</p>

---

## Post #3 by @lassoan (2022-11-03 15:57 UTC)

<p>I’ll check this. Our university tightened restrictions of public access to servers, so I may need to request an exception to keep this service going.</p>

---

## Post #4 by @platanus (2022-11-04 00:41 UTC)

<p>Thank you for answering my quesion. If the server access problem is solved, please let me know in reply that the problem has been solved.</p>

---

## Post #5 by @lassoan (2022-11-15 14:02 UTC)

<p>The server is back online. Let me know if you still encounter any problem.</p>
<p>Note that development of NVIDIA AI-Assisted Annotation server is stopped and its developers recommend to switch to MONAILabel.</p>

---

## Post #6 by @platanus (2022-11-16 21:42 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>After I had checked your answer, I tested NVIDIA AIAA module in 3D-Slicer.</p>
<p>It is working well in 3D-Slicer.</p>
<p>From now on, I will try to handle MONAI Label.</p>
<p>Thank you helping me.</p>

---

## Post #7 by @Vasopressor (2023-01-25 07:06 UTC)

<p>HI everyone,</p>
<h1><a name="p-89494-failed-to-fetch-models-from-remote-server-1" class="anchor" href="#p-89494-failed-to-fetch-models-from-remote-server-1" aria-label="Heading link"></a>Failed to fetch models from remote server</h1>
<p>‘Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/info/ is accessible in browser’<br>
Traceback (most recent call last):<br>
File “C:/Users/aaron/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/MONAILabel/lib/Slicer-5.2/qt-scripted-modules/MONAILabel.py”, line 1071, in fetchInfo<br>
info = self.logic.info()<br>
File “C:/Users/aaron/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/MONAILabel/lib/Slicer-5.2/qt-scripted-modules/MONAILabel.py”, line 2196, in info<br>
return MONAILabelClient(self.server_url, self.tmpdir, self.client_id).info()<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\NA-MIC\Extensions-31317\MONAILabel\lib\Slicer-5.2\qt-scripted-modules\MONAILabelLib\client.py”, line 50, in info<br>
status, response, _, _ = MONAILabelUtils.http_method(“GET”, self._server_url, selector)<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\NA-MIC\Extensions-31317\MONAILabel\lib\Slicer-5.2\qt-scripted-modules\MONAILabelLib\client.py”, line 303, in http_method<br>
conn.request(method, selector, body=body, headers=headers)<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\http\client.py”, line 1285, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\http\client.py”, line 1331, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\http\client.py”, line 1280, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\http\client.py”, line 1040, in _send_output<br>
self.send(msg)<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\http\client.py”, line 980, in send<br>
self.connect()<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\http\client.py”, line 946, in connect<br>
self.sock = self._create_connection(<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\socket.py”, line 844, in create_connection<br>
raise err<br>
File “C:\Users\aaron\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\socket.py”, line 832, in create_connection<br>
sock.connect(sa)<br>
TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond</p>
<p>May I please have some help with this. I cannot connect to the MONAI server my supervisor created<br>
Best<br>
Aaron</p>
<p>Sorry, still very new here and to 3d slicer/MONAI</p>

---

## Post #8 by @Ahmed_el-Sinousy (2024-03-06 23:46 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cec05336c1ac00a8c84fafcd9d8c506ef640fdcb.png" data-download-href="/uploads/short-url/tv0pDgxElBDXuBKhEDFsTuV8xgn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cec05336c1ac00a8c84fafcd9d8c506ef640fdcb_2_690x312.png" alt="image" data-base62-sha1="tv0pDgxElBDXuBKhEDFsTuV8xgn" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cec05336c1ac00a8c84fafcd9d8c506ef640fdcb_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cec05336c1ac00a8c84fafcd9d8c506ef640fdcb_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/cec05336c1ac00a8c84fafcd9d8c506ef640fdcb_2_1380x624.png 2x" data-dominant-color="3B3739"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1387×628 61.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I’m facing the same error when clicking refresh button.</p>
<p>note: I’m working on windows and didn’t install any prior packages before use MONAI label. just install it from extensions manager on 3d slicer</p>

---

## Post #9 by @muratmaga (2024-03-07 00:36 UTC)

<aside class="quote no-group" data-username="Ahmed_el-Sinousy" data-post="8" data-topic="26015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ahmed_el-sinousy/48/69590_2.png" class="avatar"> Ahmed_el-Sinousy:</div>
<blockquote>
<p>note: I’m working on windows and didn’t install any prior packages before use MONAI label. just install it from extensions manager on 3d slicer</p>
</blockquote>
</aside>
<p>Thats only the client side of the MonaiLabel. You need to install the MonaiLabel server, which actually does the work. <a href="https://github.com/Project-MONAI/MONAILabel?tab=readme-ov-file#getting-started-with-monai-label" class="inline-onebox">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>

---

## Post #10 by @lassoan (2024-03-09 05:20 UTC)

<p>If you nust want to run pretrained models then you don’t need to set up a server, but you can use MONAIAuto3DSeg, TotalSegmentator, etc. extensions. What are you trying to achieve?</p>

---
