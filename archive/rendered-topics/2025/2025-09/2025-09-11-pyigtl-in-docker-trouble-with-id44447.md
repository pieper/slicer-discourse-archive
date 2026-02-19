---
topic_id: 44447
title: "Pyigtl In Docker Trouble With"
date: 2025-09-11
url: https://discourse.slicer.org/t/44447
---

# PyIGTL in Docker: Trouble with 

**Topic ID**: 44447
**Date**: 2025-09-11
**URL**: https://discourse.slicer.org/t/pyigtl-in-docker-trouble-with/44447

---

## Post #1 by @Oskey999 (2025-09-11 14:11 UTC)

<p>Hello, would this be the right place to post this?</p>
<p>I am trying to run a python script that communicates with a 3d slicer extension using the pyigtl library.</p>
<p>However, I am struggling to get the script to communicate with slicer. which is outside the container.</p>
<p>The docker Image is the <em>python:3.10-slim-bullseye</em>, but the same errors occur with the <em>nvidia/cuda:12.3.0-base-ubuntu22.04 image.</em></p>
<p>Basically, the script runs :</p>
<pre data-code-wrap="python"><code class="lang-python">text_server = pyigtl.OpenIGTLinkServer(port=18945, local_server=True)
</code></pre>
<p>the code will stall on the next part:</p>
<pre data-code-wrap="python"><code class="lang-python">string_message = pyigtl.StringMessage(f, device_name="TextMessage")
text_server.send_message(string_message)
</code></pre>
<p>Attempting to set local server to false like so:</p>
<pre data-code-wrap="python"><code class="lang-python">text_server = pyigtl.OpenIGTLinkServer(port=18945, local_server=False, iface="0.0.0.0".encode('utf-8'))
</code></pre>
<p>reuslts in this error:</p>
<pre data-code-wrap="bash"><code class="lang-bash">Traceback (most recent call last):
  File "/app/server/server.py", line 174, in &lt;module&gt;
    asyncio.run(main())
  File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
  File "/app/server/server.py", line 170, in main
    await tmsserver.run_server()
  File "/app/server/server.py", line 43, in run_server
    servertms = pyigtl.OpenIGTLinkServer(port=18944, local_server=False, iface="0.0.0.0".encode('utf-8'))
  File "/usr/local/lib/python3.10/dist-packages/pyigtl/comm.py", line 178, in __init__
    self.host = socket.inet_ntoa(fcntl.ioctl(soc.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])
struct.error: argument for 's' must be a bytes object
</code></pre>
<p>the same error occurs if the iface var is set to wifi0 and wlan0 and eth0 stalls like the local version</p>
<p>For added context the script is SlicerTMS/server/server.py in the <a href="https://github.com/lorifranke/SlicerTMS.git" rel="noopener nofollow ugc">SlicerTMS</a> github page</p>

---

## Post #2 by @pieper (2025-09-11 14:13 UTC)

<p>Maybe it’s as simple as making sure the port is mapped from the docker instance?</p>

---

## Post #3 by @Oskey999 (2025-09-11 14:51 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="44447">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>making sure the port is m</p>
</blockquote>
</aside>
<p>I run the docker containers with<br>
``<code> bash</code><br>
<code>docker run -it -p 18944:18944 -p 18945:18945 test</code><br>
```</p>
<p>and expose both ports in the docker file with</p>
<pre><code class="lang-auto">EXPOSE 18944
EXPOSE 18945
</code></pre>
<p>but that does not change the errors I am experiencing</p>
<p>was there anything I need to do for port mapping?</p>
<p>would it help if I changed the ports used by the python script?</p>
<p>Thanks</p>

---

## Post #4 by @pieper (2025-09-11 15:13 UTC)

<p>I suggest getting the communication working with pyigtl outside of docker with simple test cases and then try those test cases inside docker to debug.</p>

---

## Post #5 by @Oskey999 (2025-09-12 01:40 UTC)

<aside class="quote no-group" data-username="Oskey999" data-post="3" data-topic="44447">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/oskey999/48/81011_2.png" class="avatar"> Oskey999:</div>
<blockquote>
<p>18945</p>
</blockquote>
</aside>
<p>I have been able to get the same script running in a dev environment on my windows 11 PC,</p>
<p>doing that it connects fine and doesn’t cause any problems.</p>
<p>Otherwise, I will looking into getting simpler test cases running, likely sometime next week</p>
<p>Thanks</p>

---

## Post #6 by @Oskey999 (2025-09-15 02:20 UTC)

<p>Also, forgot to mention a weird bit, I got 3d slicer and the python script to run in the same container and had the same issue</p>

---

## Post #7 by @lassoan (2025-09-15 05:25 UTC)

<p>We used OpenIGTLink between Slicer instances in linux docker containers and it worked well.</p>
<aside class="quote no-group" data-username="Oskey999" data-post="1" data-topic="44447">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/oskey999/48/81011_2.png" class="avatar"> Oskey999:</div>
<blockquote>
<p>the code will stall on the next part:</p>
<pre><code class="lang-auto">string_message = pyigtl.StringMessage(f, device_name="TextMessage")
text_server.send_message(string_message)
</code></pre>
</blockquote>
</aside>
<p>This is supposed to stall until a client is connected. You can attach a debugger to confirm that indeed the server is waiting on a client to connect.</p>
<p>Do you run pyigtl in Slicer application’s Python environment or in a different Python executable?<br>
In Slicer, you need to use the OpenIGTLinkIF module instead of pyigtl.</p>

---

## Post #8 by @Oskey999 (2025-09-19 02:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="44447">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>module</p>
</blockquote>
</aside>
<p>HI, Thanks for all the help.</p>
<p>It works now, after uninstalling and reinstalling the OpenIGTLinkIF extension, I could connect using</p>
<pre data-code-wrap="python"><code class="lang-python">text_server = pyigtl.OpenIGTLinkServer(port=18945, local_server=False, iface="eth0".encode('utf-8'))
string_message = pyigtl.StringMessage(f, device_name="TextMessage")
text_server.send_message(string_message)
</code></pre>
<p>I don’t really know what changed when it was reinstalled but it now showed this connection when on the OpenIGTLinkIF menu.</p>
<p>As for the development environment from before, it was a separate environment to the one associated with the slicer application.</p>

---
