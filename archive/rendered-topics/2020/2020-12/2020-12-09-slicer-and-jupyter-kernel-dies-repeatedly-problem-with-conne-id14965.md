---
topic_id: 14965
title: "Slicer And Jupyter Kernel Dies Repeatedly Problem With Conne"
date: 2020-12-09
url: https://discourse.slicer.org/t/14965
---

# Slicer and jupyter kernel dies repeatedly, problem with connection.

**Topic ID**: 14965
**Date**: 2020-12-09
**URL**: https://discourse.slicer.org/t/slicer-and-jupyter-kernel-dies-repeatedly-problem-with-connection/14965

---

## Post #1 by @coconutattitude (2020-12-09 14:05 UTC)

<p>When I install SlicerJupyter and run it, it tries to connect and the dies. The messsage ist: “The kernel appears to have died. It will restart automatically.” It then restarts and dies again.<br>
This happens both when I’m using standalone Slicer/Jupyter or Docker image.<br>
I feel hopeless.</p>
<p>The other message is: “A connection to the notebook server could not be established. The notebook will continue trying to reconnect. Check your network connection or notebook server configuration.”</p>
<p>I’m using newst Slicer app and Ubuntu 18</p>

---

## Post #2 by @coconutattitude (2020-12-09 16:47 UTC)

<p>What I found to be strange is that Slicer app repeatedly starts and closes. After I close it, and shutdown jupyter I still have like 4 Slicer processes.</p>
<p>It’s strange to me that the same error is when I’m using docker and standalone app.</p>

---

## Post #3 by @lassoan (2020-12-09 18:05 UTC)

<p>The docker image works fine - you can try it in binder: <a href="https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master">https://mybinder.org/v2/gh/Slicer/SlicerNotebooks/master</a></p>
<p>Do you see any errors in Slicer application log files? (in Slicer, menu: Help / Report a bug -&gt; check for logs of other sessions)</p>

---

## Post #4 by @coconutattitude (2020-12-09 18:36 UTC)

<p>So below is the application log. I noticed that there’s a message ‘device not open’:</p>
<ul>
<li>QIODevice::read (QFile, “/home/mikolaj/.config/NA-MIC/Extensions-29402/SlicerJupyter/share/Slicer-4.11/qt-loadable-modules/JupyterKernel/Slicer-4.11/kernel-template.json”): device not open</li>
</ul>
<p>apart from that, standard message about abnormal exit:</p>
<p>[CRITICAL][FD] 09.12.2020 19:33:29 [] (unknown:0) - error: [/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.<br>
[CRITICAL][FD] 09.12.2020 19:33:30 [] (unknown:0) - [I 19:33:30.948 NotebookApp] KernelRestarter: restarting kernel (1/5), keep random ports</p>
<p>more logs below:</p>
<p>[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Session start time …: 2020-12-09 19:27:11<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) linux-amd64 - installed release<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Operating system …: Linux / 4.15.0-126-generic / <span class="hashtag">#129-Ubuntu</span> SMP Mon Nov 23 18:53:38 UTC 2020 - 64-bit<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Memory …: 7861 MB physical, 10239 MB virtual<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i3-3217U CPU @ 1.80GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Application path …: /home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/bin<br>
[DEBUG][Qt] 09.12.2020 19:27:11 [] (unknown:0) - Additional module paths …: /home/mikolaj/.config/NA-MIC/Extensions-29402/SlicerJupyter/lib/Slicer-4.11/qt-loadable-modules, /home/mikolaj/.config/NA-MIC/Extensions-29402/SlicerJupyter/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 09.12.2020 19:27:15 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 09.12.2020 19:27:24 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 09.12.2020 19:27:25 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 09.12.2020 19:27:25 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 09.12.2020 19:27:25 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 09.12.2020 19:27:37 [] (unknown:0) - Switch to module:  “JupyterKernel”<br>
[WARNING][Qt] 09.12.2020 19:27:37 [] (unknown:0) - QIODevice::read (QFile, “/home/mikolaj/.config/NA-MIC/Extensions-29402/SlicerJupyter/share/Slicer-4.11/qt-loadable-modules/JupyterKernel/Slicer-4.11/kernel-template.json”): device not open<br>
[DEBUG][Python] 09.12.2020 19:28:32 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/jupyter_client/kernelspec.py:333) - Installing kernelspec in /home/mikolaj/.local/share/jupyter/kernels/slicer-4.11<br>
[INFO][Python] 09.12.2020 19:28:32 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/jupyter_client/kernelspec.py:342) - Removing existing kernelspec in /home/mikolaj/.local/share/jupyter/kernels/slicer-4.11<br>
[INFO][Python] 09.12.2020 19:28:32 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/jupyter_client/kernelspec.py:346) - Installed kernelspec slicer-4.11 in /home/mikolaj/.local/share/jupyter/kernels/slicer-4.11<br>
[WARNING][Qt] 09.12.2020 19:28:32 [] (unknown:0) - QIODevice::read (QFile, “/home/mikolaj/.config/NA-MIC/Extensions-29402/SlicerJupyter/share/Slicer-4.11/qt-loadable-modules/JupyterKernel/Slicer-4.11/kernel-template.json”): device not open<br>
[INFO][Stream] 09.12.2020 19:28:32 [] (unknown:0) - Removing existing kernelspec in /home/mikolaj/.local/share/jupyter/kernels/slicer-4.11<br>
[INFO][Stream] 09.12.2020 19:28:32 [] (unknown:0) - Installed kernelspec slicer-4.11 in /home/mikolaj/.local/share/jupyter/kernels/slicer-4.11<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) - [I 19:28:34.300 NotebookApp] Serving notebooks from local directory: /home/mikolaj/codete/git_repos/medtransfer-ml/slicerdemo<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) - [I 19:28:34.300 NotebookApp] Jupyter Notebook 6.1.5 is running at:<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) - [I 19:28:34.300 NotebookApp] <a href="http://localhost:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532" rel="noopener nofollow ugc">http://localhost:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532</a><br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) - [I 19:28:34.301 NotebookApp]  or <a href="http://127.0.0.1:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532" rel="noopener nofollow ugc">http://127.0.0.1:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532</a><br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) - [I 19:28:34.301 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) - [C 19:28:34.333 NotebookApp]<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) -<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) -     To access the notebook, open this file in a browser:<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) -         file:///home/mikolaj/.local/share/jupyter/runtime/nbserver-13993-open.html<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) -     Or copy and paste one of these URLs:<br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) -         <a href="http://localhost:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532" rel="noopener nofollow ugc">http://localhost:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532</a><br>
[CRITICAL][FD] 09.12.2020 19:28:34 [] (unknown:0) -      or <a href="http://127.0.0.1:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532" rel="noopener nofollow ugc">http://127.0.0.1:8888/?token=16e888901eaa0ae4140cb0e7cb1e980f6441887e6a58b532</a><br>
[CRITICAL][FD] 09.12.2020 19:29:27 [] (unknown:0) - [I 19:29:27.199 NotebookApp] Kernel started: cca1c750-cb5e-49b0-8300-9b44431ee743, name: slicer-4.11</p>

---

## Post #5 by @lassoan (2020-12-09 18:41 UTC)

<p>Can you check if you can find logs of a Slicer instance that the notebook server started?</p>
<p>Can you try if you start Slicer and launch the kernel manually? (see instructions <a href="https://github.com/Slicer/SlicerJupyter#launch-a-kernel-manually">here</a>)</p>

---

## Post #6 by @coconutattitude (2020-12-09 19:15 UTC)

<p>Ad) Can you check if you can find logs of a Slicer instance that the notebook server started?<br>
So I went to /tmp/Slicer-mikolaj (I believe this is where logs are stored) and after few minutes of running slicer with jupyter server (started from slicer standalone app with extension) I have 12 separate files. I think this is because something is spawning slicer app processes. I see a Slicer window popup for a second and then it shuts down. after about 10 seconds it happens again - Slicer window pops up and closes. This happens ad infinitum until I go to htop and kill every process that has ‘slicer’ in it (there are usually like maybe 6 or more simultanious processes).</p>
<p>Those are the files:<br>
Slicer_29402_20201209_195740_529.log , Slicer_29402_20201209_200027_758.log, Slicer_29402_20201209_200050_524.log  etc</p>
<p>And the messages in those logs look like this:<br>
[DEBUG][Python] 09.12.2020 20:01:17 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 09.12.2020 20:01:26 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 09.12.2020 20:01:27 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 09.12.2020 20:01:27 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Session start time …: 2020-12-09 20:01:14<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) linux-amd64 - installed release<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Operating system …: Linux / 4.15.0-126-generic / <span class="hashtag">#129-Ubuntu</span> SMP Mon Nov 23 18:53:38 UTC 2020 - 64-bit<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Memory …: 7861 MB physical, 10239 MB virtual<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i3-3217U CPU @ 1.80GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Application path …: /home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/bin<br>
[DEBUG][Qt] 09.12.2020 20:01:14 [] (unknown:0) - Additional module paths …: /home/mikolaj/.config/NA-MIC/Extensions-29402/SlicerJupyter/lib/Slicer-4.11/qt-loadable-modules, /home/mikolaj/.config/NA-MIC/Extensions-29402/SlicerJupyter/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Qt] 09.12.2020 20:01:27 [] (unknown:0) - Switch to module:  “Welcome”</p>
<p>Or like this:<br>
[DEBUG][Python] 09.12.2020 20:02:28 [Python] (/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…</p>
<p>And I have 5 log files with the shorter version and 6 log files with longer version</p>

---

## Post #7 by @coconutattitude (2020-12-09 19:19 UTC)

<p>Ad) Can you try if you start Slicer and launch the kernel manually?</p>
<p>I  don’t understand this:<br>
Build the extension against the newly built Slicer with Qt5 and VTK9 enabled.</p>
<p>is this step necessary and if so how can I build it?</p>

---

## Post #8 by @lassoan (2020-12-09 19:28 UTC)

<aside class="quote no-group" data-username="coconutattitude" data-post="7" data-topic="14965">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coconutattitude/48/9123_2.png" class="avatar"> coconutattitude:</div>
<blockquote>
<p>don’t understand this:<br>
Build the extension against the newly built Slicer with Qt5 and VTK9 enabled.</p>
<p>is this step necessary and if so how can I build it?</p>
</blockquote>
</aside>
<p>No need to build anything, just launch the kernel manually (<a href="https://github.com/Slicer/SlicerJupyter#launch-a-kernel-manually" class="inline-onebox">GitHub - Slicer/SlicerJupyter: Extension for 3D Slicer that allows the application to be used from Jupyter notebook</a>).</p>

---

## Post #9 by @lassoan (2020-12-09 20:10 UTC)

<aside class="quote no-group" data-username="coconutattitude" data-post="6" data-topic="14965">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coconutattitude/48/9123_2.png" class="avatar"> coconutattitude:</div>
<blockquote>
<p>So I went to /tmp/Slicer-mikolaj (I believe this is where logs are stored) and after few minutes of running slicer with jupyter server (started from slicer standalone app with extension) I have 12 separate files. I think this is because something is spawning slicer app processes. I see a Slicer window popup for a second and then it shuts down. after about 10 seconds it happens again - Slicer window pops up and closes. This happens ad infinitum until I go to htop and kill every process that has ‘slicer’ in it (there are usually like maybe 6 or more simultanious processes).</p>
</blockquote>
</aside>
<p>Launching of Slicer processes is expected, it means that the kernel is successfully registered to the jupyter server and the jupyter server attempts to start the kernel (=Slicer application).</p>
<p>Have you launched the server? You should only see Slicer instances popping up after you open a notebook with Slicer kernel. If you see Slicer instances started before that then it means that you have Jupyter server(s) running in the background. You can find and kill all Jupyter server instances or just reboot your computer to get rid of them.</p>
<p>How things should work:</p>
<ul>
<li>Start Slicer, go to JupyterKernel module, click on “Start Jupyter server” =&gt; after a minute or so, your browser is opened (<code>http://localhost:8888/tree</code>) and you see the Jupyter server web interface</li>
<li>Create a notebook, choose Slicer 4.11 as kernel (or 4.13 if you use latest preview release) =&gt; a new notebook is created, a Slicer instance is launched</li>
</ul>
<p>The Jupyter server launches Slicer with a command like this:</p>
<pre><code class="lang-auto">"C:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2020-11-25\bin\SlicerApp-real.exe"  --no-splash --python-code "connection_file=r'C:\Users\andra\AppData\Roaming\jupyter\runtime\kernel-b1663e74-4f82-455e-9fa4-7abd9db6c811.json'; print('Jupyter connection file: ['+connection_file+']'); slicer.modules.jupyterkernel.startKernel(connection_file);slicer.util.mainWindow().showMinimized()"
</code></pre>
<p>Therefore, in the logs of the Slicer instance that Jupyter server started you should see something like this:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 09.12.2020 14:52:12 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][Stream] 09.12.2020 14:52:13 [] (unknown:0) - Loading Slicer RC file [C:/Users/andra/.slicerrc.py]
[INFO][Stream] 09.12.2020 14:52:13 [] (unknown:0) - Jupyter connection file: [C:\Users\andra\AppData\Roaming\jupyter\runtime\kernel-b1663e74-4f82-455e-9fa4-7abd9db6c811.json]
[DEBUG][Qt] 09.12.2020 14:52:14 [] (unknown:0) - Starting Jupyter kernel server
</code></pre>

---

## Post #10 by @coconutattitude (2020-12-09 20:52 UTC)

<blockquote>
<p>How things should work:</p>
<ul>
<li>Start Slicer, go to JupyterKernel module, click on “Start Jupyter server” =&gt; after a minute or so, your browser is opened ( <code>http://localhost:8888/tree</code> ) and you see the Jupyter server web interface</li>
<li>Create a notebook, choose Slicer 4.11 as kernel (or 4.13 if you use latest preview release) =&gt; a new notebook is created, a Slicer instance is launched</li>
</ul>
</blockquote>
<p>This is exactly what I did. However, after I create a notebook and choose slicer 4.11 as kernel I get message that the kernel died and it will restart. A slicer instance window pops up and briefly closes. It then goes on and on like this (restarting kernel, problem with connection to kernel, slicer window up and down, restarting).</p>
<p>What I think it should do, is that jupyter notebook should stay connected to the Slicer kernel and allow me use it. Instead it looses connection and restarts.</p>

---

## Post #11 by @coconutattitude (2020-12-09 20:54 UTC)

<p>I can’t interact with instances of Slicer that pop up, because after a second they disappear. I can only interact with instance of Slicer that I run with ./Slicer</p>
<p>The same behaviour is also inside docker container.</p>
<p>I wonder what may cause this.</p>

---

## Post #12 by @lassoan (2020-12-09 21:01 UTC)

<p>OK, this is pretty good. The next step is to see why startup fails:<br>
A. because Slicer crashes at startup, when it starts the kernel (e.g., due to conflicts with some system libraries)<br>
B. because the server cannot connect to the kernel (e.g., due to network access issues).</p>
<p>If you launch Slicer and launch a kernel manually and it crashes then we know it is A, otherwise it is B.</p>

---

## Post #13 by @coconutattitude (2020-12-09 21:09 UTC)

<p>It crashed when launched manually.</p>

---

## Post #14 by @lassoan (2020-12-09 21:13 UTC)

<p>Great, this information narrows down what the issue can be. Can you get a stack trace of the crash?</p>

---

## Post #15 by @coconutattitude (2020-12-09 21:37 UTC)

<p>I don’t know where it might be, the console where I ran ./Slicer has this:</p>
<p>Switch to module:  “Welcome”<br>
Python console user input: connection_file=r’/home/mikolaj/.local/share/jupyter/runtime/kernel-7a4a79ef-474e-4810-8ec7-dd86d6eaaf38.json’<br>
Python console user input: slicer.modules.jupyterkernel.startKernel(connection_file)<br>
error: [/home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p>in /tmp/Slicer-mikolaj logs there is this (only pasting last two lines):</p>
<p>[DEBUG][Qt] 09.12.2020 21:53:34 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 09.12.2020 22:08:21 [] (unknown:0) - Python console user input: connection_file=r’/home/mikolaj/.local/share/jupyter/runtime/kernel-7a4a79ef-474e-4810-8ec7-dd86d6eaaf38.json’</p>
<p>is there any other place where I can find trace of the crash? like, linux logs?</p>

---

## Post #16 by @lassoan (2020-12-09 22:20 UTC)

<p>Yes, you can use standard linux tools to get stack trace of the crash. I don’t use linux much, so I don’t know the details. Maybe <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can help.</p>

---

## Post #17 by @coconutattitude (2020-12-10 17:55 UTC)

<p>Hi <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> could you please help me with Slicer and Jupyter bug?</p>

---

## Post #18 by @coconutattitude (2020-12-10 18:02 UTC)

<p>I checked logs in /var/log/kern.log and I saw this error:</p>
<p>Dec  9 21:44:56 machine kernel: [181247.526073] traps: SlicerApp-real[24615] trap invalid opcode ip:7f2eb59e4c6c sp:7ffeb7a186f0 error:0 in libxeus.so.1[7f2eb5982000+7b000]</p>

---

## Post #19 by @lassoan (2020-12-10 19:39 UTC)

<p>Invalid opcode means the CPU encountered an invalid instruction. It may be due to data corruption/incorrect loading, but there is a chance that your CPU actually does not recognize the instruction.</p>
<p>Do you run on a physical computer or in a virtualized environment? What is your CPU model?</p>

---

## Post #20 by @coconutattitude (2020-12-10 19:43 UTC)

<p>according to Slicer logs it’s i3-3217U CPU @ 1.80GHz, 2 cores, 4 logical processors:</p>
<p>[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Session start time …: 2020-12-09 21:53:16<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) linux-amd64 - installed release<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Operating system …: Linux / 4.15.0-126-generic / <span class="hashtag">#129-Ubuntu</span> SMP Mon Nov 23 18:53:38 UTC 2020 - 64-bit<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Memory …: 7861 MB physical, 10239 MB virtual<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i3-3217U CPU @ 1.80GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 09.12.2020 21:53:16 [] (unknown:0) - Application path …: /home/mikolaj/Downloaded_Programs/Slicer-4.11.20200930-linux-amd64/bin</p>

---

## Post #21 by @coconutattitude (2020-12-10 19:43 UTC)

<p>it’s physical laptop (Asus)</p>

---

## Post #22 by @lassoan (2020-12-10 19:53 UTC)

<aside class="quote no-group" data-username="coconutattitude" data-post="20" data-topic="14965">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coconutattitude/48/9123_2.png" class="avatar"> coconutattitude:</div>
<blockquote>
<p>Intel® Core™ i3-3217U CPU</p>
</blockquote>
</aside>
<p>This explains it all. This is a third-generation Intel CPU, released more than 8 years ago.</p>
<p>When we choose software libraries and instruction set for building the binary packages we need to balance between backward compatibility and performance. If preserve backward compatibility with older systems then we cannot use new features and the software will run slower on modern systems. If we use latest features then the software will not run at all on older systems. Therefore, we aim for preserving backward compatibility with computers that are not older than 5 years.</p>
<p>You either need to upgrade your hardware or <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html">build Slicer yourself</a> (on your system by default an older instruction set will be used that is compatible with your CPU, so you don’t need to tune any build options).</p>

---

## Post #23 by @coconutattitude (2020-12-10 19:56 UTC)

<p>Thank you! Does this also explain why the setup on docker does not work?</p>

---
