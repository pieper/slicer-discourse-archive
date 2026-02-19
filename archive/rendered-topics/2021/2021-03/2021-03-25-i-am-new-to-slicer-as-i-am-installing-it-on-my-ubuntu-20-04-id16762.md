---
topic_id: 16762
title: "I Am New To Slicer As I Am Installing It On My Ubuntu 20 04"
date: 2021-03-25
url: https://discourse.slicer.org/t/16762
---

# I am new to slicer,as I am installing it on my ubuntu 20.04 system after installation it crashes immediately and shows error as follows:

**Topic ID**: 16762
**Date**: 2021-03-25
**URL**: https://discourse.slicer.org/t/i-am-new-to-slicer-as-i-am-installing-it-on-my-ubuntu-20-04-system-after-installation-it-crashes-immediately-and-shows-error-as-follows/16762

---

## Post #1 by @Bhagyashri_Ghode (2021-03-25 13:25 UTC)

<p>Operating system: Ubuntu 20.04<br>
Slicer version:4.11<br>
Expected behavior: Work well<br>
Actual behavior: Gives error<br>
error: [/root/Bhagyashri/Slicer-4.11.20210226-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.</p>

---

## Post #2 by @pieper (2021-03-25 19:09 UTC)

<p>Be sure the prerequisites are installed: <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#debian-ubuntu" class="inline-onebox">Getting Started — 3D Slicer documentation</a></p>

---

## Post #3 by @Bhagyashri_Ghode (2021-03-26 08:28 UTC)

<p>Thanks Steve Pieper… I installed the prerequisites. Although there is error. Please help me</p>

---

## Post #4 by @pieper (2021-03-26 13:51 UTC)

<p>I use 20.04 with no problem, so it’s probably something with your <code>LD_LIBRARY_PATH</code> or other config.  You can try running <code>Slicer --launch xterm</code> and then run <code>SlicerApp-real</code> in the new window to see if there is more diagnostic info.  Also inside that window you can try <code>ldd $(which SlicerApp-real)</code> to see if any of the core slicer or python libraries are pointing outside of your install tree.</p>

---

## Post #5 by @Bhagyashri_Ghode (2021-03-26 14:33 UTC)

<p>Thanks pieper…I have error with SliperApp -real as below:<br>
icer<br>
Switch to module:  “Welcome”<br>
error: [/root/Bhagyashri/Slicer-4.11.20210226-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.<br>
which version of qt you are using</p>

---

## Post #6 by @Bhagyashri_Ghode (2021-03-26 15:50 UTC)

<p>No module named sysconfigdata–linux X86-64–linux-gnu</p>

---

## Post #7 by @Bhagyashri_Ghode (2021-03-26 18:21 UTC)

<p>I removed this error  No module named sysconfigdata–linux X86-64–linux-gnu…althrough there is same problem .I tried many different versions of qt…but slicer crashes with SlicerApp real…please help me</p>

---

## Post #8 by @jcfr (2021-03-26 18:46 UTC)

<aside class="quote no-group" data-username="Bhagyashri_Ghode" data-post="7" data-topic="16762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bhagyashri_ghode/48/10422_2.png" class="avatar"> Bhagyashri_Ghode:</div>
<blockquote>
<p>I tried many different versions of qt</p>
</blockquote>
</aside>
<p>Qt libraries, along with all required dependencies are distributed. You should  not have to install Qt.</p>

---

## Post #9 by @jcfr (2021-03-26 18:49 UTC)

<aside class="quote no-group" data-username="Bhagyashri_Ghode" data-post="5" data-topic="16762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bhagyashri_ghode/48/10422_2.png" class="avatar"> Bhagyashri_Ghode:</div>
<blockquote>
<p>Switch to module: “Welcome”</p>
</blockquote>
</aside>
<p>This seems to indicate the application  started but it crashed once the Welcome module is loaded.</p>
<p>Could you try:</p>
<pre><code class="lang-auto">./Slicer --modules-to-ignore Welcome
</code></pre>
<p>Does the application start ? Are you able to select other modules ?</p>

---

## Post #10 by @muratmaga (2021-03-26 19:14 UTC)

<aside class="quote no-group" data-username="Bhagyashri_Ghode" data-post="5" data-topic="16762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bhagyashri_ghode/48/10422_2.png" class="avatar"> Bhagyashri_Ghode:</div>
<blockquote>
<p>/root/Bhagyashri/Slicer-4.11.20210226-linux-amd64/</p>
</blockquote>
</aside>
<p>This may not be the issue, but is there a reason why you install this in root? Are you running the application as root?</p>

---

## Post #11 by @Bhagyashri_Ghode (2021-03-27 05:42 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="9" data-topic="16762">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><code>./Slicer --modules-to-ignore Welcome</code></p>
</blockquote>
</aside>
<p>tried it same problem exists…application does not start immediately crashes after installation</p>

---

## Post #12 by @Bhagyashri_Ghode (2021-03-27 05:43 UTC)

<p>I tried not in root but same problem is there</p>

---
