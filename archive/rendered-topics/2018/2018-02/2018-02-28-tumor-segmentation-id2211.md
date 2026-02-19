---
topic_id: 2211
title: "Tumor Segmentation"
date: 2018-02-28
url: https://discourse.slicer.org/t/2211
---

# Tumor segmentation

**Topic ID**: 2211
**Date**: 2018-02-28
**URL**: https://discourse.slicer.org/t/tumor-segmentation/2211

---

## Post #1 by @nodi (2018-02-28 18:19 UTC)

<p>I tried to segment the tumor but when I save it as .nrrd, I got the whole volume with other tissues. I want to save and use JUST the tumor volume. how can I do that?</p>
<p>Do I have to use the Editor to segment the tumor or I can do something by CLI?</p>

---

## Post #2 by @lassoan (2018-02-28 19:37 UTC)

<p>Hide all segments that you don’t want to export and in advanced section of Export section, choose Visible segments only.</p>

---

## Post #3 by @nodi (2018-03-01 00:18 UTC)

<p>Thank you it works and I got (segmentation.seg.nrrd and segmentation-lable.nrrd)</p>
<p>However, since I’m new learner, I want to get the volume (segmented tumor) as an array.</p>
<p>so I loaded the “segmentation-lable.nrrd” then:</p>
<blockquote>
<blockquote>
<blockquote>
<p>o= slicer.util.array(‘segmentation-lable’)<br>
print (o)<br>
[[[0 0 0 …, 0 0 0]<br>
[0 0 0 …, 0 0 0]<br>
[0 0 0 …, 0 0 0]<br>
…</p>
</blockquote>
</blockquote>
</blockquote>
<p>I’m getting zeros<br>
Could you please guide me</p>
<p>Thank you.</p>

---

## Post #4 by @pieper (2018-03-01 01:08 UTC)

<p>It may look like zeros, but your data is probably just being shortened for display.</p>
<p>Try <code>o.max()</code> and you should see the label value you exported.</p>
<p>Also something like:</p>
<pre><code class="lang-auto">import numpy
numpy.transpose(numpy.where(o==1))
</code></pre>
<p>will give you a list of the pixel coordinates where there’s a 1 in the segmentation array.</p>
<p>HTH</p>

---

## Post #5 by @nodi (2018-03-01 01:24 UTC)

<p>now I got “None” when printing o</p>

---

## Post #6 by @lassoan (2018-03-01 02:26 UTC)

<p>You got <code>None</code> if you mistype the node name or the image is invalid.</p>
<p>I would recommend to use <code>slicer.util.arrayFromSegment()</code>. It can retrieve voxels directly from segmentation node, you don’t need to export it to labelmap.</p>

---

## Post #7 by @nodi (2018-03-01 22:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="2211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>slicer.util.arrayFromSegment()</p>
</blockquote>
</aside>
<p>now I’m getting error.<br>
Could you please give me the complete steps code maybe I did something wrong.</p>

---

## Post #8 by @lassoan (2018-03-01 23:38 UTC)

<aside class="quote no-group" data-username="nodi" data-post="7" data-topic="2211">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/57b2e6/48.png" class="avatar"> nodi:</div>
<blockquote>
<p>now I’m getting error.</p>
</blockquote>
</aside>
<p>Sorry, I need more specific information than this to be able to help.</p>
<p>You can get help on usage of any commands by using <code>help</code> command. For example: <code>help(slicer.util.arrayFromSegment)</code>.</p>
<p>See complete example here: <a href="https://discourse.slicer.org/t/area-of-segment-in-a-given-slice/1559/3" class="inline-onebox">Area of segment in a given slice? - #3 by lassoan</a></p>

---
