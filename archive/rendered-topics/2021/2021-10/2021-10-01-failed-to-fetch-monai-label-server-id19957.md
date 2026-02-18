# Failed to fetch MONAI label server

**Topic ID**: 19957
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/failed-to-fetch-monai-label-server/19957

---

## Post #1 by @ragwing_mmh (2021-10-01 17:36 UTC)

<p>Operating system: Windows 7 Build 6.1.7601<br>
Slicer version: 4.13.0 2021-08-16<br>
The version of Python: Python 3.6.7<br>
Expected behavior: Fetch MONAI label server and start Deepedit<br>
Actual behavior: failed</p>
<p>I have setuped MONAI &amp; MONAI label at my workstation, which running ubuntu 18.04. Both fetch local MONAI label server &amp; Deepedit work fine at ubuntu server under 4.13.0 2021-09-29 build</p>
<p>The address of MONAI label server is correct and can be opened in browser at both windows 7 &amp; ubuntu.</p>
<p>But when I use the 3D slicer client with MONAI label plug-in at windows 7, it failed to fetch MONAI label server and showed following error message:</p>
<p>KeyError: 'config’Traceback (most recent call last):<br>
File “C:/ProgramData/NA-MIC/Slicer 4.13.0-2021-08-16/NA-MIC/Extensions-30121/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py”, line 960, in onClickFetchInfo<br>
self.fetchInfo()<br>
File “C:/ProgramData/NA-MIC/Slicer 4.13.0-2021-08-16/NA-MIC/Extensions-30121/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py”, line 987, in fetchInfo<br>
self.config = info[“config”]<br>
KeyError: ‘config’</p>
<p>I also tried to install the same bulid of 3D slicer as ubuntu (4.13.0 2021-09-29) in windows 7 but it failed to start 3D slicer when launching, the error message is:</p>
<p>SlicerApp-real.exe stopped to work<br>
Error module name: ucrtbase.DLL</p>
<p>How can I fix these issue and use the MONAI label at windows 3D slicer?<br>
Thank you.</p>

---

## Post #2 by @lassoan (2021-10-01 17:48 UTC)

<p>2021-08-16 version is almost 6 weeks old and features are added/bugs are fixed at a rapid pace in MONAILabel. Use the latest Slicer Preview Release and let us know if you run into any issues.</p>

---

## Post #3 by @jamesobutler (2021-10-01 18:03 UTC)

<aside class="quote no-group" data-username="ragwing_mmh" data-post="1" data-topic="19957">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ragwing_mmh/48/8504_2.png" class="avatar"> ragwing_mmh:</div>
<blockquote>
<p>I also tried to install the same bulid of 3D slicer as ubuntu (4.13.0 2021-09-29) in windows 7 but it failed to start 3D slicer when launching</p>
</blockquote>
</aside>
<p>Windows 7 is going to be a problem when trying to use latest Slicer Preview. See the below information</p>
<aside class="quote quote-modified" data-post="2" data-topic="16749">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/application-failed-to-start-on-windows-7/16749/2">Application failed to start on Windows 7</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Windows 7 is not supported (Microsoft dropped support for it long time ago). We have not made any breaking changes intentionally, but we don’t test impact of changes on these old systems. It is not very likely that you can get help from the community to troubleshoot this, so if running Slicer on Windows7 is a priority for you and you cannot resolve the problem yourself then you may contract <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#commercial-partners" rel="noopener nofollow ugc">commercial partners</a> to investigate the issue. 
I would recommend to upgrade the operating system on your c…
  </blockquote>
</aside>


---

## Post #4 by @ragwing_mmh (2021-10-01 18:05 UTC)

<p>Thank you sir for instant reply</p>
<p>I tried to install the latest bulid of 3D slicer 4.13.0 2021-09-28 in windows 7, same latest build as ubuntu; but it failed to start 3D slicer when launching, even under the previous build at 2021-09-21</p>
<p>the error message (partial) is:<br>
SlicerApp-real.exe has stopped to work<br>
Error module name: ucrtbase.DLL</p>
<p>The 4.13.0 2021-08-16 build is one build that can lanuch normally</p>

---

## Post #5 by @lassoan (2021-10-01 19:28 UTC)

<p>Supporting old hardware and operating systems have very high cost and very low value, therefore we generally stay away from it.</p>
<p>You can try all Slicer releases between 08-16 and 09-21 and see which exact day the startup started to fail. Then you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build Slicer from source code</a> and confirm which exact commit made the difference and build Slicer without that change. Note that if you build Slicer then it means that you also need to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-list-of-extensions-manually">build all extensions</a>. These are all doable, but will most likely you will need to invest several days of work into it, therefore it may be cheaper to buy a used (not more than 3-year-old) computer that is compatible with current Windows version.</p>

---

## Post #6 by @NPC (2022-02-28 10:29 UTC)

<p><a class="mention" href="/u/ragwing_mmh">@ragwing_mmh</a> have you been able to resolve the fetch issue? I have the similar Slicer version and I tried installing it on Mac, It throws the same error as you mentioned and I was wondering if were able to bypass this issue. If yes, kind share with us how you resolved it. It was be a great help. Thank you.</p>
<p>here the error if it helps</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-30657/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py”, line 949, in fetchInfo<br>
info = self.logic.info()<br>
File “/Applications/Slicer.app/Contents/Extensions-30657/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py”, line 1965, in info<br>
return MONAILabelClient(self.server_url, self.tmpdir, self.client_id).info()<br>
File “/Applications/Slicer.app/Contents/Extensions-30657/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabelLib/client.py”, line 47, in info<br>
status, response, _ = MONAILabelUtils.http_method(“GET”, self._server_url, selector)<br>
File “/Applications/Slicer.app/Contents/Extensions-30657/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabelLib/client.py”, line 260, in http_method<br>
conn.request(method, selector, body=body, headers=headers)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1285, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1331, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1280, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 1040, in _send_output<br>
self.send(msg)<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 980, in send<br>
self.connect()<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/http/client.py”, line 946, in connect<br>
self.sock = self._create_connection(<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/socket.py”, line 844, in create_connection<br>
raise err<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/socket.py”, line 832, in create_connection<br>
sock.connect(sa)<br>
ConnectionRefusedError: [Errno 61] Connection refused</p>

---
