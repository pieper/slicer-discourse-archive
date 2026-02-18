# VMTK - Branch points coordinates

**Topic ID**: 13173
**Date**: 2020-08-26
**URL**: https://discourse.slicer.org/t/vmtk-branch-points-coordinates/13173

---

## Post #1 by @janneke_slicer (2020-08-26 12:56 UTC)

<p>Hello,</p>
<p>I am using the VMTK extension in Slicer 4.11.<br>
It works really well; however, I would like to extract the branch point coordinates of the centerline model in a fast way.<br>
I know this is possible by creating the centerline or network curves and reading the coordinates of the begin- or endpoint of these curves in the created table. However, my 3D model is pretty complex and it takes a lot of time to find the coordinates of certain branch points (for example, it is difficult to determine if the branch point I’m interested in is the begin- or end point of the curve).</p>
<p>Is it possible to get the branch points coordinates in a faster way? Ideally, I would click on a branch point and receive the coordinates of that point immediately.</p>
<p>Regards,<br>
Janneke</p>

---

## Post #2 by @lassoan (2020-08-26 21:37 UTC)

<p>Yes, it is very easy to extract point coordinates of a selected branch. Add a markups curve, place two points near the begin/end points of the path you want to extract and then in Markups module/Curve settings, choose Curve type → Shortest distance on surface and select the centerline as model node as shown in this video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="WJQexDTiRRc" data-video-title="Transform markups between original and straightened vessel" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WJQexDTiRRc" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WJQexDTiRRc/maxresdefault.jpg" title="Transform markups between original and straightened vessel" width="" height="">
  </a>
</div>

<p>You can get all curve point positions and the coordinates of first and last point in the Python console:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a=slicer.util.arrayFromMarkupsCurvePoints(slicer.util.getNode('C'))
&gt;&gt;&gt; a[0]
array([ 57.43868 , -31.754717,   0.      ], dtype=float32)
&gt;&gt;&gt; a[-1]
array([-48.099056, -14.009434,   0.      ], dtype=float32)
</code></pre>

---

## Post #3 by @janneke_slicer (2020-08-28 09:26 UTC)

<p>Thank you! This is indeed a faster method. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---
