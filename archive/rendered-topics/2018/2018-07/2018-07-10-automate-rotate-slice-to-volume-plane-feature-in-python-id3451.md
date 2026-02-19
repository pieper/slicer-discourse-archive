---
topic_id: 3451
title: "Automate Rotate Slice To Volume Plane Feature In Python"
date: 2018-07-10
url: https://discourse.slicer.org/t/3451
---

# Automate "Rotate slice to volume plane" feature in Python

**Topic ID**: 3451
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/automate-rotate-slice-to-volume-plane-feature-in-python/3451

---

## Post #1 by @cphillips (2018-07-10 18:21 UTC)

<p>Is there anyway to automate rotating a slice window? (I.e. automate the clicking of the “rotate to volume plane” button)</p>
<p>I have tried:</p>
<p>controller = slicer.qMRMLSliceControllerWidget()<br>
controller.rotateSliceToBackground()</p>
<p>but this doesn’t seem to do anything, and I don’t know how to associate this with a particular slice window (i.e. a particular qMRMLSliceWidget)</p>

---

## Post #2 by @lassoan (2018-07-10 20:25 UTC)

<p>Examples in the script repository should help:  <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_a_Slice_View">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_a_Slice_View</a></p>

---

## Post #3 by @pieper (2018-07-11 21:49 UTC)

<aside class="quote no-group" data-username="cphillips" data-post="1" data-topic="3451">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/848f3c/48.png" class="avatar"> cphillips:</div>
<blockquote>
<p>controller = slicer.qMRMLSliceControllerWidget()<br>
controller.rotateSliceToBackground()</p>
<p>but this doesn’t seem to do anything, and I don’t know how to associate this with a particular slice window (i.e. a particular qMRMLSliceWidget)</p>
</blockquote>
</aside>
<p>That will just create an instance of a new controller widget but you want the ones that are associated with views in the layout, like this from the examples <a class="mention" href="/u/lassoan">@lassoan</a> linked:</p>
<pre><code class="lang-auto">for sliceViewName in layoutManager.sliceViewNames():
     sliceWidget = layoutManager.sliceWidget(sliceViewName)
     
     controller = sliceWidget.sliceController()
</code></pre>

---
