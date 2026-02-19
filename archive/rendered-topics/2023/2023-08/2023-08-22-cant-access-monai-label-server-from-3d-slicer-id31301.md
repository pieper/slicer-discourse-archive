---
topic_id: 31301
title: "Cant Access Monai Label Server From 3D Slicer"
date: 2023-08-22
url: https://discourse.slicer.org/t/31301
---

# Can't access MONAI Label server from 3D Slicer

**Topic ID**: 31301
**Date**: 2023-08-22
**URL**: https://discourse.slicer.org/t/cant-access-monai-label-server-from-3d-slicer/31301

---

## Post #1 by @shihje (2023-08-22 22:23 UTC)

<p>I’m trying to use 3D Slicer as a visualization tool for MONAI Label. I started up the MONAI Label server using the monailabel CLI in an SSH terminal, and got an IP address of the Uvicorn session:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/048ec44e0b7e2ba240dbeadf86a0eb4c3219f572.png" data-download-href="/uploads/short-url/EjMKOY5WdkmeFL9v3wwvSnCTGG.png?dl=1" title="monai label server" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/048ec44e0b7e2ba240dbeadf86a0eb4c3219f572.png" alt="monai label server" data-base62-sha1="EjMKOY5WdkmeFL9v3wwvSnCTGG" width="690" height="74" data-dominant-color="2B2B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">monai label server</span><span class="informations">1390×150 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I then input this IP address in the MONAI Label extension of 3D Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be584df588eb48750c18c15dd0921436cbfb3f17.png" alt="3d monai" data-base62-sha1="r9RUtK8x5Gt1z203vCt9hLmOP2v" width="441" height="102"></p>
<p>I am unable to connect and receive the following error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86e002fd95f557b024725e9fbc30c5a56f7a3b2b.png" alt="image" data-base62-sha1="jf9VhiyNIBklPNb0oL5aPPltq43" width="514" height="123"></p>
<p>The details are below. Is this an access issue from my end, or with MONAI Label’s servers, or something else?</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:/Users/uXXXXXXX/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/MONAILabel/lib/Slicer-5.2/qt-scripted-modules/MONAILabel.py”, line 1072, in fetchInfo<br>
info = self.logic.info()<br>
File “C:/Users/uXXXXXXX/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/MONAILabel/lib/Slicer-5.2/qt-scripted-modules/MONAILabel.py”, line 2263, in info<br>
return self._client().info()<br>
File “C:/Users/uXXXXXXX/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/MONAILabel/lib/Slicer-5.2/qt-scripted-modules/MONAILabel.py”, line 2239, in _client<br>
if mc.auth_enabled():<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\MONAILabel\lib\Slicer-5.2\qt-scripted-modules\MONAILabelLib\client.py”, line 83, in auth_enabled<br>
status, response, _, _ = MONAILabelUtils.http_method(“GET”, self._server_url, selector)<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\MONAILabel\lib\Slicer-5.2\qt-scripted-modules\MONAILabelLib\client.py”, line 521, in http_method<br>
conn.request(method, selector, body=body, headers=headers)<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 1285, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 1331, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 1280, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 1040, in _send_output<br>
self.send(msg)<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 980, in send<br>
self.connect()<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 946, in connect<br>
self.sock = self._create_connection(<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\socket.py”, line 844, in create_connection<br>
raise err<br>
File “C:\Users\uXXXXXXX\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\socket.py”, line 832, in create_connection<br>
sock.connect(sa)<br>
OSError: [WinError 10049] The requested address is not valid in its context</p>
</blockquote>

---

## Post #2 by @mangotee (2023-08-23 08:48 UTC)

<p>Hi,<br>
sounds like you are almost there. The URL displayed in the CLI output needs to be modified. In <code>http://0.0.0.0:8000</code>, replace the <code>0.0.0.0</code> part with the IP address of your server where MONAI Label is running on. For example:</p>
<ul>
<li>If you are running this on localhost (i.e. MONAI Label server and 3D Slicer are running locally on the same laptop/workstation), then replace it with <code>http://127.0.0.1:8000</code></li>
<li>If you are running MONAI Label on a remote server and 3D Slicer locally, then enter that address, e.g. <code>http://123.456.789.012:8000</code></li>
</ul>
<p>If this does not help, it would be great if you could share the server setup - is this the same workstation, or is MONAI Label server running remotely? Did you start MONAI Label server from inside a docker container or barebone with a local conda/pip install?</p>

---

## Post #3 by @shihje (2023-09-01 17:30 UTC)

<p>Hi, I’ve tried the local server as well, and it does not help. I’m starting the server from a local pip install, attempting to run it from the same workstation. If it helps, I’m able to run a Jupyter Server to run jupyter notebooks, for instance. It runs on the local host and uses a token. Does the MONAI Label server have a similar protocol? Similarly, how do I try and run MONAI Label on a remote server? Do I have to set anything up, or is it as simple as entering a server address?</p>

---

## Post #4 by @shihje (2023-09-01 17:39 UTC)

<p>Actually - your comment gave me a clue. I tried the same port as jupyter notebook uses and it now works!</p>

---

## Post #5 by @nasibov_98 (2023-10-05 20:58 UTC)

<p>Hi guys, I am having a very similar issue.</p>
<ol>
<li>On institute HPC (linux), Built Nvidia Monai-Toolkit docker using Singularity (our institute does not allow use of docker).</li>
<li>Activated server on HPC</li>
<li>Tunneled into HPC Monai-toolkit server from local computer</li>
<li>Accessed Jupyter-lab that comes with Monai-toolkit container</li>
<li>Accessed terminal within Jupyter-lab</li>
<li>Installed radiology app and sample task Spleen09</li>
<li>Started Monai Label server - no problems so far</li>
<li>Installed 3D slicer on local computer and accessed MonaiLabel Module</li>
<li>I input the same server address that the Monai-Toolkit server gave me for accessing jupyter lab but I get the infamous error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c33ae137f2fe9257d78310471eb5989ab3f8f31d.png" alt="Screenshot 2023-10-05 at 21.56.38" data-base62-sha1="rR5fSdReJkXdDCa7vLRHvRSBPD7" width="626" height="161"></li>
</ol>
<p>I also tried putting in the IP that the jupyter server outputted, followed by :8888 but that isnt working either</p>
<p>Can you make any suggestions?</p>

---

## Post #6 by @muratmaga (2023-10-06 21:36 UTC)

<aside class="quote no-group" data-username="nasibov_98" data-post="5" data-topic="31301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/d26b3c/48.png" class="avatar"> nasibov_98:</div>
<blockquote>
<p>Installed 3D slicer on local computer and accessed MonaiLabel Module</p>
</blockquote>
</aside>
<p>Did you create the tunnel to the HPC server from the computer you installed the Slicer (In the last step)?</p>

---

## Post #7 by @nasibov_98 (2023-10-07 14:57 UTC)

<p>yes, I have tunneled in and connected successfully to the node running my server on the HPC.</p>

---

## Post #8 by @rbumm (2023-10-08 23:02 UTC)

<p>The way we implement MonaoLabel into Slicer is way too complicated. It is a science on its own and requires programming experience.<br>
It should be built into the program with its own automatic server and become an integral part of the segment editor. Same a Slicer LLM should assist in solving problems before people get lost.<br>
Slicer should have several detail layers (noob, beginner, expert) to facilitate clinical or scientific use.<br>
I suggest a roadmap for 2030 with a clear goal and strategy.</p>

---

## Post #9 by @pieper (2023-10-10 21:17 UTC)

<p>Agreed <a class="mention" href="/u/rbumm">@rbumm</a>, the current implementation of MONAI Label is hard for people to install and modify.  It would be great if we could figure out a way to improve that, perhaps with a funded effort via an NIH grant or similar.  As you know most of the core developers implement things they need for their own projects so general usability improvements are often hard to allocate resources for.</p>

---

## Post #10 by @nasibov_98 (2023-10-15 16:21 UTC)

<p>Dr. Andres emailed me suggesting port mapping may be the issue and thats exactly what it was (8000 is the default port), but thanks for the help everyone. I agree with the points made by <a class="mention" href="/u/rbumm">@rbumm</a> and <a class="mention" href="/u/pieper">@pieper</a>, I think the Monai label documentation needs a revamp, and it needs to be put in the context of the biomedical/clinical user’s experience rather than a bioinformatician’s.</p>
<p>Cheers,</p>
<p>Ulvi</p>

---

## Post #11 by @lhssu (2023-10-16 06:59 UTC)

<p><a class="mention" href="/u/mangotee">@mangotee</a>  Hi, i running the MONAI LABEL server  which inside a docker container from a server and i got the same access issue, do you know how to set correct server ip in 3dslicer in this case?<br>
For example,<br>
my server ip is 10.10.10.15<br>
the docker port is 5735:8888<br>
monailabel shows"http:0.0.0.0:8000"<br>
what the correct ip should be? i tried 10.10.10.15:5735, and 10.10.10.15:8000, it shows connect refused</p>

---

## Post #12 by @natachavalador (2025-01-27 18:10 UTC)

<p>Hi,<br>
It seems I am facing the same problem with the server.</p>
<p>. Running on my own pc (Windows 11)<br>
. 3D Slicer installed with MonaiLabel plug-in working<br>
. Tryed Anaconda, Python 3.11 and Visual Studio Code as an interface<br>
. Followed precisely all tutorials from Andres Pinto and the server remains not working<br>
. Tried to mix my personal IP with the Port :8000 and the error remains</p>
<p>Could you help me?</p>
<p>KR,<br>
Natacha Valador</p>

---
