# Clip the closed surface

**Topic ID**: 2653
**Date**: 2018-04-21
**URL**: https://discourse.slicer.org/t/clip-the-closed-surface/2653

---

## Post #1 by @wpgao (2018-04-21 09:56 UTC)

<p>Operating system: win7<br>
Slicer version:4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi guys,</p>
<p>How to clip the closed surface?<br>
Thanks</p>

---

## Post #2 by @lassoan (2018-04-21 14:16 UTC)

<p>There are many ways, but probably these two stand out:</p>
<ol>
<li>For free-form, rectangular, or circular cutting of closed surfaces probably the most versatile method is <strong>Scissors effect in Segment Editor</strong>. You need to import the model into a segmentation and when you go to Segment Editor, you need to choose a volume with arbitrary content that defines resolution.</li>
</ol>
<div class="lazyYT" data-youtube-id="m4zTj8i4tCA" data-youtube-title='New "scissors" editing tool in 3D Slicer for 3D cropping' data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=9"></div>
<ol start="2">
<li>For cutting with a plane, you can use <strong>EasyClip</strong> extension. The advantage of this extension compared to the Scissors tool is that Easy Clip is simpler and does not use the intermediate step of resampling the surface on a voxel grid.</li>
</ol>

---

## Post #3 by @wpgao (2018-04-23 01:14 UTC)

<p>Hi Lasso,</p>
<p>Thanks for your help!</p>

---
