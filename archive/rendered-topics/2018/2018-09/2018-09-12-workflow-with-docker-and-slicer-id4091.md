# Workflow with Docker and Slicer

**Topic ID**: 4091
**Date**: 2018-09-12
**URL**: https://discourse.slicer.org/t/workflow-with-docker-and-slicer/4091

---

## Post #1 by @darekdev (2018-09-12 19:22 UTC)

<p>Hi,</p>
<p>I’am a scientist and working with Slicer build inside a docker image but I want make some upgrade in a workflow and add SlicerJupyter extension. I have a dream that I am preparing a docker image for my friends in team. In last few days I did some research about your solution with docker but I got lost in this topic. What need I to create a dream workflow:</p>
<ul>
<li>Create docker image with build version Slicer Qt5 (always need builded version because I working with own extensions</li>
<li>Build and install to Slicer SlicerJupyter extension(this will allow me to accelerate my work considerably and simply - JUPYTER is awesome)</li>
<li>Redistribute created image.<br>
Now I have only working version with Slicer Qt4 but for this version I can’t build SlicerJupyter.</li>
</ul>
<p>Have you got some suggestion how I can improve that workflow? What image (for example from <a href="https://github.com/thewtex/SlicerDocker" rel="nofollow noopener">https://github.com/thewtex/SlicerDocker</a>) should I use? And what do if my computer has Nvidia and other ATI or Intel graphic cards? Should I install all drivers?</p>
<p>Regards,<br>
Darek</p>

---

## Post #2 by @pieper (2018-09-17 14:21 UTC)

<p>Hi Darek -</p>
<p>You can have a look at my dockerfiles.  It should be no problem to get a latest nightly build and install the jupyter extension in a dockerfile.  Then you can push the result back to dockerhub or other repository.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerDockers">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/d9a4a684e86b6008ce7ec26cedfd6d3db6ee11e025271ce0b46f82b43ba6fe4c/pieper/SlicerDockers" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub - pieper/SlicerDockers: docker config files for slicer</a></h3>

  <p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This will provide a software rendering layer with vnc access for the browser (not GPU accelerated but still typically quite usable).</p>

---

## Post #3 by @darekdev (2018-09-17 20:22 UTC)

<p>Thank you for your reply. I have got your solution before and additionaly I have installed X11 and nvidia drivers inside. Then connect to container with volume /tmp/X11 and share $DISPLAY. Works great but now I have simplier solution as I think:<br>
I get out from docker packed Slicer nightly build and packed SlicerJupyter and working on this. Then I have gave a chance for <a href="https://github.com/Slicer/SlicerBuildEnvironment:" rel="nofollow noopener">https://github.com/Slicer/SlicerBuildEnvironment:</a> build Slicer and SlicerJupyter but with this envoronment I dont know why Slicer (when I connect to SlicerJupyter) has 100% CPU usage.<br>
Well now I have working nightly Slicer from pieper/SlicerDockers extracted and I build my extension through SlicerBuildEnvironment and copy libs.</p>

---

## Post #4 by @pieper (2018-09-17 21:32 UTC)

<p>Sounds great - if you have any examples of installing nvidia drivers or running jupyter through Slicer in docker please post.</p>

---

## Post #5 by @darekdev (2018-09-18 13:02 UTC)

<p>I have been working with Docker and Slicer around 2 years and I installed packages in the docker by trial and error (I have never successfully compile Qt 4 and 5). Probably it’s nothing revealing:</p>
<ul>
<li>I use Ubuntu 16.04 image(with 18 I have compile errors),</li>
<li>Download prebuilt qt unified version,</li>
<li>Install dependencies etc <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a>, after successfully building process I test Slicer on my laptop with GTX 980m and of course in docker I have got errors. Simple solution:</li>
<li>Install nvidia drivers but carefully. I have on my host a nvidia-396 drivers and the same drivers must be installed in docker(now Slicer is running),</li>
<li>Install dependencies for SlicerJupyter:</li>
</ul>
<blockquote>
<pre><code>  sudo apt-get install libicu-dev
  sudo apt-get install uuid-dev
</code></pre>
</blockquote>
<ul>
<li>Build SlicerJupyter based on previously built Slicer,</li>
<li>Create conda environment and connect Slicer with Jupyter.<br>
I run docker with this script:</li>
</ul>
<blockquote>
<p>#!/bin/bash<br>
xhost +local:docker<br>
PATH_TO_EHDD=$1<br>
docker run\<br>
–privileged\<br>
-v $PATH_TO_EHDD/software:/home/software:rw\<br>
-v /dev:/dev/:ro\<br>
-e QT_X11_NO_MITSHM=1\<br>
-e DISPLAY=$DISPLAY\<br>
-v /tmp/.X11-unix/:/tmp/.X11-unix:ro\<br>
–user broncho\<br>
-it slicer_jupyter:nv /bin/bash</p>
</blockquote>
<p>Explanation of some parameters:<br>
-v /dev/:/dev/<br>
I need this volume because I use sensors on /dev/ttyACM*</p>
<p>-e DISPLAY=$DISPLAY\<br>
-v /tmp/.X11-unix/:/tmp/.X11-unix:ro\<br>
It allows me to run GUI programs like Slicer</p>
<p>Now as I said before I packed Slicer and SlicerJupyter and working with it outside the docker on the host. JupyterLab is my current IDE.<br>
Remember that when you are move Slicer executables(for example working on a packaged version) you need to change paths in this two files: <strong>kernel.json</strong> and <strong>AdditionalLauncherSettings.ini</strong></p>

---

## Post #6 by @lassoan (2018-09-18 20:38 UTC)

<p>It is great that you find Slicer and SlicerJupyter useful. Thanks for sharing information about how your setup works.</p>
<aside class="quote no-group" data-username="darekdev" data-post="5" data-topic="4091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e5b9ba/48.png" class="avatar"> darekdev:</div>
<blockquote>
<p>Remember that when you are move Slicer executables(for example working on a packaged version) you need to change paths in this two files: <strong>kernel.json</strong> and <strong>AdditionalLauncherSettings.ini</strong></p>
</blockquote>
</aside>
<p>Note that Slicer can install when you click “Install Slicer kernel in Jupyter” then it updates the path in the kernel file and installs it. <a href="https://github.com/Slicer/SlicerJupyter/commit/ed8aa847fcae51be98278a8d1a4e2690099449a6">I’ve updated JupyterKernel module</a> to make this feature available from Python (so that you can automate it as part of the installation process).</p>
<p>If you package the extension and install the extension from file it using the extension manager (by calling <code>slicer.app.extensionsManagerModel().installExtension()</code>) then you don’t need additional launcher settings, because all the libraries are installed into standard locations where Slicer can find them automatically.</p>
<aside class="quote no-group" data-username="darekdev" data-post="3" data-topic="4091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e5b9ba/48.png" class="avatar"> darekdev:</div>
<blockquote>
<p>with this envoronment I dont know why Slicer (when I connect to SlicerJupyter) has 100% CPU usage</p>
</blockquote>
</aside>
<p>See this issue: <a href="https://github.com/Slicer/SlicerJupyter/issues/16" class="inline-onebox">JupyterKernel uses 100% CPU when idle · Issue #16 · Slicer/SlicerJupyter · GitHub</a><br>
It would be nice if you could give it a try to solve this problem.</p>

---

## Post #7 by @darekdev (2018-09-18 21:54 UTC)

<p>Hi Andras,</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="4091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that Slicer can install when you click “Install Slicer kernel in Jupyter” then it updates the path in the kernel file and installs it. [I’ve updated JupyterKernel module</p>
</blockquote>
</aside>
<p>I always do what you wrote, but it doesn’t update kernel.json. After click “Install Slicer kernel in Jupyter” it fills the template with paths to SuperBuild/Slicer-build not to for example Slicer-2018.08.20-amd64/. Tested few times. I give a try for <code>slicer.app.extensionsManagerModel().installExtension()</code>, because can’t install builded and packed SlicerJupyter through GUI extension manager.</p>
<p>Maybe I will find some time in a break from my doctorate.</p>

---

## Post #8 by @lassoan (2018-09-19 19:48 UTC)

<aside class="quote no-group" data-username="darekdev" data-post="7" data-topic="4091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e5b9ba/48.png" class="avatar"> darekdev:</div>
<blockquote>
<p>it doesn’t update kernel.json. After click “Install Slicer kernel in Jupyter” it fills the template with paths to SuperBuild/Slicer-build not to for example Slicer-2018.08.20-amd64/</p>
</blockquote>
</aside>
<p>Could you start Slicer using Jupyter, enter these commands and let us know what you got as output?</p>
<pre><code>print slicer.app.launcherExecutableFilePath
print slicer.app.applicationFilePath()
</code></pre>
<p>Is this an installed Slicer or a custom-built Slicer run from the build tree?<br>
Is this an SlicerJupyter package installed or a custom-built SlicerJupyter left in the build tree?</p>
<aside class="quote no-group" data-username="darekdev" data-post="3" data-topic="4091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e5b9ba/48.png" class="avatar"> darekdev:</div>
<blockquote>
<p>with this envoronment I dont know why Slicer (when I connect to SlicerJupyter) has 100% CPU usage</p>
</blockquote>
</aside>
<p>I’ve updated SlicerJupyter with an option to use a timer instead of watching socket changes. This option (<a href="https://github.com/Slicer/SlicerJupyter/blob/5216ba31c2dea77357b9d3d4b74f4b815ccecb76/JupyterKernel/xSlicerServer.h#L21-L25">JUPYTER_POLL_USING_TIMER</a>) is enabled on Windows by default. Could you check if you build SlicerJupyter with this option enabled then your 100% CPU usage problem is resolved?</p>

---

## Post #9 by @darekdev (2018-09-20 08:57 UTC)

<p>Answering to kernel.json:</p>
<ol>
<li>
<p>I did something wrong with <strong>kernel-template.json</strong>(doesn’t exists). Works now.</p>
</li>
<li>
<p>I have a custom-build Slicer with built in SlicerJupyter. I used this script: <a href="https://github.com/Slicer/SlicerBuildEnvironment/issues/8" class="inline-onebox" rel="noopener nofollow ugc">DOC: Script to build qt5 image, bundling external modules. · Issue #8 · Slicer/SlicerBuildEnvironment · GitHub</a>,  because I can’t built SlicerJupyter standalone what is write here <a href="https://github.com/Slicer/SlicerBuildEnvironment#configure-build-and-package-a-slicer-extension-for-linux" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a>. I have an error:</p>
<blockquote>
<p>ninja: error: unknown target ‘package’</p>
</blockquote>
</li>
<li>
<p>Yes, I’m tracking an extension on github and I’m going answer there.</p>
</li>
</ol>

---

## Post #10 by @Saima (2023-02-03 05:32 UTC)

<p>Hi andras,<br>
I ran external python script with anaconda env using check_output through slicer scripted module. It was running fine last time but it is now not returning to slicer.</p>
<p>The external python script is running but at the end a pop up window with forcequit comes. slicer crash…</p>
<p>When I open slicer using terminal. The terminal window is showing</p>
<p>Error response from daemon: No such container: greedy_elephant<br>
Error: No such container: greedy_elephant<br>
Error response from daemon: No such container: greedy_elephant<br>
Error response from daemon: removal of container greedy_elephant is already in progress</p>
<p>Could you please help.</p>
<p>Regards,<br>
Saima</p>

---
