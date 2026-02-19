---
topic_id: 22539
title: "Slicer Docker For Gui Via Browser"
date: 2022-03-16
url: https://discourse.slicer.org/t/22539
---

# Slicer Docker for GUI via browser

**Topic ID**: 22539
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/slicer-docker-for-gui-via-browser/22539

---

## Post #1 by @Nadya_Shusharina (2022-03-16 13:44 UTC)

<p>I would like to use a web browser to access the Slicer GUI for a slicer instance running in a docker container.</p>
<p>SlicerDocker/slicer-notebook includes a Dockerfile to expose a Jupyter notebook attached to the slicer kernel, and some code related to GUI exposure: VNCPORT in Dockerfile, commented out  x11vnc in run.sh. Is there an example configuration to access Slicer GUI via a web browser?</p>
<p>Thank you,<br>
Nadya</p>

---

## Post #2 by @pieper (2022-03-16 13:48 UTC)

<p>Hi Nadya -</p>
<p>Here are some dockerfiles that set up vnc access via x11vnc and noVNC for web browser access:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerDockers">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/e42da38450c5cf0cbf3159948e0f8e38f95cb20baed466fb8bda61f28c64f1a1/pieper/SlicerDockers" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub - pieper/SlicerDockers: docker config files for slicer</a></h3>

  <p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>-Steve</p>

---

## Post #3 by @Nadya_Shusharina (2022-03-16 13:50 UTC)

<p>Thanks Steve, will check it out.<br>
Nadya</p>

---

## Post #4 by @Nadya_Shusharina (2022-03-17 02:25 UTC)

<p>I’ve got the SlicerDockers/slicer container to build (needs a different bitstream code to download Slicer 4.11.20200930 now, and curl -k to skip certificate check). The container runs fine, and shows the X environment in the browser. When I click the Slicer icon, only Slicer splash screen briefly flashes. If I open xterm and issue /opt/slicer/Slicer, I get an error:<br>
<code>qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.</code><br>
I am running this docker container on Ubuntu 18, 6Gb RAM. What could be wrong here?</p>

---

## Post #5 by @pieper (2022-03-17 12:44 UTC)

<p>Sounds like you are close.  You are probably running into this issue:</p>
<aside class="quote quote-modified" data-post="1" data-topic="14029">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/cant-start-latest-stable-on-ubuntu-20-04/14029">Can't start latest stable on ubuntu 20.04</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Due to the issues we had with Centos 7 and latest stable, I  just recently installed Ubuntu 20.04 on a spare machine. This is just a default install, and nothing more (or less). Latest stable doesn’t start with this error: 
&gt; maga@magalab-ubuntu:~/Downloads/Slicer-4.11.20200930-linux-amd64$ ./Slicer 
&gt; qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
&gt; This application failed to start because no Qt platform plugin could be initialized. Reinstalling the a…
  </blockquote>
</aside>


---

## Post #6 by @Nadya_Shusharina (2022-03-17 23:43 UTC)

<p>Thank you - it works if the following patch is applied to <a href="https://github.com/pieper/SlicerDockers/blob/master/slicer/Dockerfile" class="inline-onebox" rel="noopener nofollow ugc">SlicerDockers/Dockerfile at master · pieper/SlicerDockers · GitHub</a></p>
<pre><code class="lang-auto">11d10
&lt; RUN apt-get install -y --reinstall libxcb-xinerama0
12a12,13
&gt; RUN apt-get install -y libxcb-shape0 libxcb-xinerama0 libxcb-xinerama0-dev
&gt; RUN apt-get install -y libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-randr0 libxcb-xkb-dev libxkbcommon-x11-dev
20,21c21,22
&lt; RUN SLICER_URL="http://download.slicer.org/bitstream/1341035" &amp;&amp; \
&lt;   curl -v -s -L $SLICER_URL | tar xz -C /tmp &amp;&amp; \
---
&gt; RUN SLICER_URL="https://download.slicer.org/bitstream/60add70fae4540bf6a89bfb4" &amp;&amp; \
&gt;   curl -k -v -s -L $SLICER_URL | tar xz -C /tmp &amp;&amp; \
</code></pre>

---

## Post #7 by @pieper (2022-03-18 12:57 UTC)

<p>That’s great Nadya.  Would you be willing to put that in the form of a pull request to the repository?</p>

---

## Post #8 by @Nadya_Shusharina (2022-03-18 15:08 UTC)

<p>Yes, sure. Please advise which way.</p>

---

## Post #9 by @pieper (2022-03-18 19:52 UTC)

<p>You can make a fork of the <a href="https://github.com/pieper/SlicerDockers/blob/master/slicer/Dockerfile">repository</a> and apply your changes either directly in the github web page or in a local checkout that you push back to the fork.  Then you create <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">a pull request</a> proposing the changes and we can discuss as needed or I’ll just go ahead and merge.  I know these are small edits and I could make them myself but it’s nice for you to get credit in the history for this fix and also you can get practice for maybe bigger changes to this or other code in the future.</p>

---

## Post #10 by @Nadya_Shusharina (2022-03-23 15:06 UTC)

<p>Thank you. This is done.</p>

---

## Post #11 by @Francis_Chemorion (2024-03-24 12:27 UTC)

<p>Just in case there is anyone else looking for Docker Slicer GUI, I also have one based on Ubuntu Desktop, could not rebuild Steve’s Image</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/kchemorion/slicerGUI">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/kchemorion/slicerGUI" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/f77711e53e30ea2ae322861c250569c6e1a002c1290d6b29a9c83b58ee0b5afa/kchemorion/slicerGUI" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/kchemorion/slicerGUI" target="_blank" rel="noopener nofollow ugc">GitHub - kchemorion/slicerGUI</a></h3>

  <p>Contribute to kchemorion/slicerGUI development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Only change I made is to download and extract Slicer first, then place it in the folder with the dockerfile, and I also modify slicerrc.py to enable me copy and load files directly to the container so that it is open with the needed files.</p>
<p>I also create volumes for sending files in and reading files out.</p>
<p>Let me know if you are able to have fun with this.</p>

---
