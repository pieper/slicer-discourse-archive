---
topic_id: 1501
title: "Can We Measure Angles On The 3Dslicer"
date: 2017-11-21
url: https://discourse.slicer.org/t/1501
---

# Can we measure angles on the 3Dslicer

**Topic ID**: 1501
**Date**: 2017-11-21
**URL**: https://discourse.slicer.org/t/can-we-measure-angles-on-the-3dslicer/1501

---

## Post #1 by @patsawas (2017-11-21 20:50 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2017-11-21 21:59 UTC)

<p>There used to be an angle measurement widget in Slicer but then it had to be removed temporarily until the underlying infrastructure is cleaned up.</p>
<p>Until this widget becomes available again, you can use this module for measuring angles:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14">
  <header class="source">

      <a href="https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14" target="_blank" rel="noopener">https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14</a></h4>

  <h5>AngleMeasurement.py</h5>
  <pre><code class="Python">#
# Installation:
# - Save this file as AngleMeasurement.py to a directory on your computer
# - Add the directory to the additional module paths in the Slicer application settings:
#   - Choose in the menu: Edit / Application settings
#   - Click Modules, click &gt;&gt; next to Additional module paths
#   - Click Add, and choose the .py file's location
# - After you restart Slicer, "Angle Measurment" module should show up in Quantification category
#
</code></pre>
   This file has been truncated. <a href="https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You have to place two rulers and the module shows angle between them. You can click on “Add to table” to add the measurement to a table and remove the rulers.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b82643b300a106394847bea8808e847dae02365.png" data-download-href="/uploads/short-url/hCC5Frl4JlS4PiYWE94iC6GhAwZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b82643b300a106394847bea8808e847dae02365_2_690x469.png" alt="image" data-base62-sha1="hCC5Frl4JlS4PiYWE94iC6GhAwZ" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b82643b300a106394847bea8808e847dae02365_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b82643b300a106394847bea8808e847dae02365_2_1035x703.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b82643b300a106394847bea8808e847dae02365.png 2x" data-dominant-color="B9B7B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1075×731 98.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @stevenagl12 (2018-03-19 19:57 UTC)

<p>Has this ever gotten updated so that the widget is available?</p>

---

## Post #4 by @stevenagl12 (2018-03-19 20:15 UTC)

<p>Also, for whatever reason, any time I record an angle with this script. The rulers are cleared instantaneously, is there a way to preserve the rulers?</p>

---

## Post #5 by @stevenagl12 (2018-03-19 20:32 UTC)

<p>Not sure if the given script is working correctly either because I ran it on</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/892542e5d18472d97e62195bc15e44006134b7d4.jpeg" alt="image" data-base62-sha1="jzffdxWYTtGJNcYmKPKsRpmAJw0" width="570" height="424"></p>
<p>and it gave me an angle of 137.4.</p>

---

## Post #6 by @lassoan (2018-03-20 20:00 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="5" data-topic="1501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>it gave me an angle of 137.4.</p>
</blockquote>
</aside>
<p>Yes, that looks correct (about 45 deg less than 180 deg). Note that the order of points matter, not which endpoints you place close to each other.</p>

---

## Post #7 by @lassoan (2018-03-20 20:01 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="4" data-topic="1501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>The rulers are cleared instantaneously</p>
</blockquote>
</aside>
<p>This is a feature. This allow you to make many measurements. You can change the script to not clear previous angles.</p>
<p>I’m working on improving widgets. I’ll first add curve widget, but soon after I’ll add proper angle measurement widget. It should be available in a few months.</p>

---
