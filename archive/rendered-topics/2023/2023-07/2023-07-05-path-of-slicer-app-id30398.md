---
topic_id: 30398
title: "Path Of Slicer App"
date: 2023-07-05
url: https://discourse.slicer.org/t/30398
---

# Path of slicer app

**Topic ID**: 30398
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/path-of-slicer-app/30398

---

## Post #1 by @Kening_Zhang (2023-07-05 02:22 UTC)

<p>Dear developer,<br>
I want to design a package which need the path of the slicer installed on user’s computer, is there some command that can find  the path of the slicer location automatically?<br>
Best wishes,<br>
Joshua</p>

---

## Post #2 by @rbumm (2023-07-05 05:30 UTC)

<pre><code class="lang-auto"># all nodes are saved relative to this path
slicer.mrmlScene.GetRootDirectory() 
# write-able folder, you can use this to store any temporary data
slicer.app.temporaryPath 
# Slicer core binary folder
slicer.app.slicerHome 
# Slicer extensions folder
slicer.app.extensionsInstallPath 
# path of a scripted module (in this example: Sample Data module SampleData.py)
slicer.modules.sampledata.path 
</code></pre>

---

## Post #3 by @Kening_Zhang (2023-07-07 05:48 UTC)

<p>sorry, but I mean the launcher of slicer,<br>
such as /Applications/Slicer.app/Contents/MacOS/Slicer<br>
Best,<br>
Joshua</p>

---

## Post #4 by @rbumm (2023-07-07 06:13 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="2" data-topic="30398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<pre><code class="lang-auto"># Slicer core binary folder
slicer.app.slicerHome 
</code></pre>
</blockquote>
</aside>
<p>Sorry I am not on a Mac, but what do you get with this call?</p>

---

## Post #5 by @Kening_Zhang (2023-07-07 06:14 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a7934388791c929a40726db2489bdd90c80ae7.png" alt="image" data-base62-sha1="ucnM1uc6wJvOXNMHcioeiyxRpZl" width="580" height="64"><br>
I think it is incomplete?<br>
Thank you,<br>
Joshua</p>

---

## Post #6 by @rbumm (2023-07-07 06:27 UTC)

<aside class="quote no-group" data-username="Kening_Zhang" data-post="1" data-topic="30398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kening_zhang/48/65641_2.png" class="avatar"> Kening_Zhang:</div>
<blockquote>
<p>I want to design a package which need the path of the slicer installed on user’s computer, is there some command that can find the path of the slicer location automatically?</p>
</blockquote>
</aside>
<p>If Slicer is in the Applications directory of a Mac, you should be able to use</p>
<pre><code class="lang-auto">which Slicer
</code></pre>
<p>from bash.</p>

---

## Post #7 by @pieper (2023-07-07 13:37 UTC)

<aside class="quote no-group" data-username="Kening_Zhang" data-post="5" data-topic="30398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kening_zhang/48/65641_2.png" class="avatar"> Kening_Zhang:</div>
<blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3a7934388791c929a40726db2489bdd90c80ae7.png" alt="image" data-base62-sha1="ucnM1uc6wJvOXNMHcioeiyxRpZl" width="580" height="64"><br>
I think it is incomplete?</p>
</blockquote>
</aside>
<p>That looks correct to me.  Just ignore the /Contents part and that is the mac application folder.</p>

---
