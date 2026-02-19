---
topic_id: 35049
title: "Monailabel And Slicer Issues"
date: 2024-03-25
url: https://discourse.slicer.org/t/35049
---

# MonaiLabel and Slicer Issues

**Topic ID**: 35049
**Date**: 2024-03-25
**URL**: https://discourse.slicer.org/t/monailabel-and-slicer-issues/35049

---

## Post #1 by @evaherbst (2024-03-25 12:08 UTC)

<p>Hello,<br>
I am running into some issues with MonaiLabel.</p>
<p>I tried installing monailabel via docker. The image was created but I get several issues:<br>
-In docker:</p>
<blockquote>
<p>WARNING: The NVIDIA Driver was not detected.  GPU functionality will not be available.</p>
<p>Use the NVIDIA Container Toolkit to start this container with GPU support; see<br>
<a href="https://docs.nvidia.com/datacenter/cloud-native/" class="inline-onebox" rel="noopener nofollow ugc">NVIDIA Cloud Native Technologies - NVIDIA Docs</a></p>
</blockquote>
<p>-How do I install the Container toolkit on windows?</p>
<p>-do I need to install the cuda drivers on my system? or is this in the docker image?<br>
I assume it is still good to install on the system so that I can also use them for Slicer?</p>
<p>-Finally, I tried downloading slicer but it does not open. I am not sure if in the process of trying to install MonaiLabel I made a mistake.</p>
<p>Thank you!<br>
Eva</p>

---

## Post #2 by @evaherbst (2024-03-25 12:13 UTC)

<p>I also checked this and found no .dll error: <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start" rel="noopener nofollow ugc">Get Help — 3D Slicer documentation</a></p>
<p>and running in admin mode did not work</p>

---

## Post #3 by @muratmaga (2024-03-25 15:18 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="1" data-topic="35049">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>WARNING: The NVIDIA Driver was not detected. GPU functionality will not be available.</p>
<p>Use the NVIDIA Container Toolkit to start this container with GPU support; see<br>
<a href="https://docs.nvidia.com/datacenter/cloud-native/">NVIDIA Cloud Native Technologies - NVIDIA Docs</a></p>
</blockquote>
</aside>
<p>Try this link. I believe the best way of running docker on windows is through the WSL2 (windows subsystem for linux). <a href="https://docs.nvidia.com/cuda/wsl-user-guide/index.html">CUDA on WSL (nvidia.com)</a></p>

---

## Post #4 by @evaherbst (2024-03-25 15:57 UTC)

<p>Thank you Murat!<br>
Or do you recommend just installing without docker (either directly or with a conda venv)?</p>
<p>Regarding the Slicer bug, I just reinstalled windows since the computer was new and this seemed the best way to reset any issues I created with dependencies.<br>
Slicer works now (have not yet reinstalled monai and cuda and pytorch)</p>

---

## Post #5 by @muratmaga (2024-03-25 19:50 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="4" data-topic="35049">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>Or do you recommend just installing without docker (either directly or with a conda venv)?</p>
</blockquote>
</aside>
<p>I never tried that. Don’t have any info to share. Others may have.</p>

---

## Post #6 by @diazandr3s (2024-03-25 21:32 UTC)

<p>Hi <a class="mention" href="/u/evaherbst">@evaherbst</a>,</p>
<p>Thanks for sharing your experience.</p>
<blockquote>
<ul>
<li>I tried installing monailabel via docker. The image was created but I get several issues:</li>
</ul>
</blockquote>
<p>You don’t need to install monailabel via docker. Just download the MONAI Label Docker container and use MONAI Label.</p>
<p><code>docker pull projectmonai/monailabel</code></p>
<p><a href="https://hub.docker.com/r/projectmonai/monailabel" class="onebox" target="_blank" rel="noopener nofollow ugc">https://hub.docker.com/r/projectmonai/monailabel</a></p>
<p>Otherwise, you can also use this command to start the bash within the MONAI Label Docker container:</p>
<p><code>docker run --gpus all --rm -ti --ipc=host --net=host projectmonai/monailabel:latest bash</code></p>
<blockquote>
<ul>
<li>How do I install the Container toolkit on windows?</li>
</ul>
</blockquote>
<p>Did you make sure you have Docker on your computer? This is the first step to using the MONAI Label Docker container.</p>
<blockquote>
<p>-do I need to install the cuda drivers on my system? or is this in the docker image?<br>
I assume it is still good to install on the system so that I can also use them for Slicer?</p>
</blockquote>
<p>Yes, this is a requirement to use your GPU. Do you know which GPU you have on your PC?</p>
<blockquote>
<p>-Finally, I tried downloading slicer but it does not open. I am not sure if in the process of trying to install MonaiLabel I made a mistake.</p>
</blockquote>
<p>Sorry, I’m not sure what didn’t open - MONAI Label? Slicer?<br>
If MONAI Label, the first part of the process is to start the MONAI Label server. From what I understood, you haven’t managed to start the server.</p>
<p>Hope this helps,</p>

---

## Post #7 by @evaherbst (2024-03-26 08:53 UTC)

<p>Thank you so much <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>
<p>Sorry for being unclear. I am still learning all of the terminology around docker.<br>
I did not install monailabel - I installed docker and then used:</p>
<blockquote>
<p>docker pull projectmonai/monailabel:latest</p>
</blockquote>
<blockquote>
<p>docker run -it --rm --gpus all --ipc=host --net=host -v ~:/workspace/ projectmonai/monailabel:latest bash</p>
</blockquote>
<p>I read that I need to also install the Nvidia Container Toolkit for the monailabel docker container, is this true? In docker in the container I got the warning: “WARNING: The NVIDIA Driver was not detected. GPU functionality will not be available.”</p>
<blockquote>
<p>Yes, this is a requirement to use your GPU. Do you know which GPU you have on your PC?</p>
</blockquote>
<p>I have the following GPU: NVIDIA GeForce RTX 4090 24GB<br>
I use Windows 11.</p>
<p>I had CUDA 12.1 installed on my system before installing docker etc. Is this the right version of CUDA to install? I saw there is also 12.4.</p>
<blockquote>
<p>Sorry, I’m not sure what didn’t open - MONAI Label? Slicer?</p>
</blockquote>
<p>Slicer just started loading and then crashed before fully opening. I had no error logs. In the end I reinstalled windows (I was worried I had messed up some dependencies, and since it was a new machine this seemed the simplest solution).</p>
<p>So now I want to make sure I install everything correctly to not cause any issues with Slicer again.</p>
<p>Thank you very much!<br>
Eva</p>

---

## Post #8 by @diazandr3s (2024-03-26 13:34 UTC)

<p>Hi <a class="mention" href="/u/evaherbst">@evaherbst</a>,</p>
<blockquote>
<p>I read that I need to also install the Nvidia Container Toolkit for the monailabel docker container, is this true?</p>
</blockquote>
<p>No, you don’t need that for the MONAI Label Docker container to work.</p>
<blockquote>
<p>In docker in the container I got the warning: “WARNING: The NVIDIA Driver was not detected. GPU functionality will not be available.”</p>
</blockquote>
<p>Once you are in the MONAI Label Docker bash terminal, can you run <strong>nvidia-smi</strong> to check whether the GPU is visible?</p>
<p>Have you tried starting the MONAI Label server?</p>

---

## Post #9 by @evaherbst (2024-03-26 14:17 UTC)

<p>Thank you so much <a class="mention" href="/u/diazandr3s">@diazandr3s</a> for the quick reply!</p>
<p>That is really helpful.</p>
<p>This is for our computer at the clinic, and I am not there today, but I will try it tomorrow.<br>
Just to clarify, which CUDA version should I install? Does it amtter?</p>
<p>Thanks!<br>
Eva</p>

---

## Post #10 by @evaherbst (2024-04-03 13:42 UTC)

<p>Dear <a class="mention" href="/u/diazandr3s">@diazandr3s</a> ,</p>
<p>I was able to start the server:</p>
<blockquote>
<p>[2024-04-03 13:44:13,200] [657] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set<br>
[2024-04-03 13:44:13,200] [657] [MainThread] [INFO] (uvicorn.error:62) - Application startup complete.<br>
[2024-04-03 13:44:13,200] [657] [MainThread] [INFO] (uvicorn.error:217) - Uvicorn running on <a href="http://0.0.0.0:8000" rel="noopener nofollow ugc">http://0.0.0.0:8000</a></p>
</blockquote>
<p>I then tried the tutorial <a href="https://docs.monai.io/projects/label/en/latest/quickstart.html" rel="noopener nofollow ugc">here</a>, I downloaded the models and tried to connect to the server in Slicer but am getting the following error:</p>
<blockquote>
<p>Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/info/ is accessible in browser.</p>
</blockquote>
<p>I tried using hosts:<br>
<a href="http://0.0.0.0:8000" rel="noopener nofollow ugc">http://0.0.0.0:8000</a> or<br>
<a href="http://127.0.0.1:8000" rel="noopener nofollow ugc">http://127.0.0.1:8000</a> or<br>
<a href="http://localhost:8000" rel="noopener nofollow ugc">http://localhost:8000</a> or leaving it blank</p>
<p>details:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
File "C:/Users/Eva/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py", line 1085, in fetchInfo
info = self.logic.info()
File "C:/Users/Eva/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py", line 2288, in info
return self._client().info()
File "C:/Users/Eva/AppData/Local/slicer.org/Slicer 5.6.1/slicer.org/Extensions-32438/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py", line 2264, in _client
if mc.auth_enabled():
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\slicer.org\Extensions-32438\MONAILabel\lib\Slicer-5.6\qt-scripted-modules\MONAILabelLib\client.py", line 83, in auth_enabled
status, response, _, _ = MONAILabelUtils.http_method("GET", self._server_url, selector)
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\slicer.org\Extensions-32438\MONAILabel\lib\Slicer-5.6\qt-scripted-modules\MONAILabelLib\client.py", line 521, in http_method
conn.request(method, selector, body=body, headers=headers)
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\http\client.py", line 1285, in request
self._send_request(method, url, body, headers, encode_chunked)
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\http\client.py", line 1331, in _send_request
self.endheaders(body, encode_chunked=encode_chunked)
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\http\client.py", line 1280, in endheaders
self._send_output(message_body, encode_chunked=encode_chunked)
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\http\client.py", line 1040, in _send_output
self.send(msg)
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\http\client.py", line 980, in send
self.connect()
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\http\client.py", line 946, in connect
self.sock = self._create_connection(
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\socket.py", line 844, in create_connection
raise err
File "C:\Users\Eva\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\socket.py", line 832, in create_connection
sock.connect(sa)
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it
</code></pre>
<p><strong>I am using Slicer 5.6 - I tried installing 5.7 but it does not open, similar to the behaviour I had a while back</strong></p>
<p><strong>Please let me know if this should be posted on the Monai Forum instead</strong></p>

---

## Post #11 by @evaherbst (2024-04-03 16:01 UTC)

<p>maybe it is a problem with the university proxy server I am using</p>

---

## Post #12 by @muratmaga (2024-04-03 16:36 UTC)

<p>Those addresses are local to your computer, so proxy shouldn’t be an issue. However, if this is a company managed device, there might be policies blocking what you can do on the computer.</p>
<p>After you start monaiLabel server, launch web browser and type those addresses, and see it connects (again on the same computer you launched monaiLabel). If it they do not connect, there is a problem with the server.</p>

---

## Post #13 by @evaherbst (2024-04-10 15:18 UTC)

<p>Thank you Murat. I was waiting for IT to check out if it is an issue with the proxy server, but they had no solutions.</p>
<p>maybe I am doing something wrong with docker - it did look like the server started but I cannot view those addresses in a web browser nor access them with slicer.</p>
<p>I also attempted to install via an anaconda venv and also just directly in my system.</p>
<p>I checked “nvcc-version” and cuda 11.8 is installed so I used:<br>
pip install torch torchvision torchaudio --extra-index-url <a href="https://download.pytorch.org/whl/cu118" rel="noopener nofollow ugc">https://download.pytorch.org/whl/cu118</a></p>
<p>however, when I run “python -c “import torch; print(torch.cuda.is_available())”” it just stalls.</p>
<p>It is strange because this worked before.</p>
<p>Thanks,<br>
Eva</p>

---

## Post #14 by @evaherbst (2024-05-07 14:19 UTC)

<p>Hi everyone,</p>
<p>I am not sure why (since I was running MonaiLabel locally) but it seems that the cause of my installation issues was due to the university proxy (which I was told to use to access the internet).<br>
I instead purchased a WIFI dongle and used WIFI (to avoid the proxy). I installed monailabel in a miniconda venv on Windows and everything worked well.</p>
<p>Thanks for everyone’s help.</p>

---

## Post #15 by @muratmaga (2024-05-08 02:58 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="14" data-topic="35049">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>ssues was due to the university proxy</p>
</blockquote>
</aside>
<p>proxy and security policies on network can break things in a very unpredictable and difficult to diagnose way (since you are the only one with that issue, nobody can replicate). When I encounter an issue which I suspect may be due to security policies, I try the same on a personal computer not tied to the company network to see if it replicates.</p>
<p>Glad that wifi solved the issue.</p>

---
