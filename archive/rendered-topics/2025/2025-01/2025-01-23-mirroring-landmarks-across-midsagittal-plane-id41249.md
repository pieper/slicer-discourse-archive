---
topic_id: 41249
title: "Mirroring Landmarks Across Midsagittal Plane"
date: 2025-01-23
url: https://discourse.slicer.org/t/41249
---

# Mirroring landmarks across midsagittal plane 

**Topic ID**: 41249
**Date**: 2025-01-23
**URL**: https://discourse.slicer.org/t/mirroring-landmarks-across-midsagittal-plane/41249

---

## Post #1 by @sck84 (2025-01-23 22:33 UTC)

<p>Hello,</p>
<p>I am trying to mirror landmarks applied to one half of a skull across the midsagittal plane. Really, my aim is to landmark half of the skull, and mirror any points that are not on the midsagittal line, so as to create one complete skull.</p>
<p>Is there a way to do this in 3D slicer? If not, using my mrk.json files, is there another software that does?</p>

---

## Post #2 by @lassoan (2025-01-23 22:48 UTC)

<p>It is quite easy to do it on Slicer.</p>
<p>First, you need to get a transformation matrix that transforms the midsagittal plane to a plane that is orthogonal to the world coordinate syatem left-right axis. Probably the easiest is to use the ACPC transform module for this (provided by SlicerNeuro extension). You don’t need to apply this transform to the image.</p>
<p>Then you place your landmarks and get them as a numpy array. To get the point coordinates mirrored to the midsagittal plane:</p>
<ul>
<li>add a row of 1.0 values to the numpy array that contains each point position in a column (the result is the homogenous coordinates of the landmark points)</li>
<li>multiply this matrix from the left with the mirroring transform (4x4 matrix)</li>
</ul>
<p>You can compute the mirroring transform by a simple matrix multiplication: <code>inv(ACPC) * diag(-1,1,1,1) * ACPC</code> (where <code>ACPC</code> is the ACPC transform computed by the ACPC Transform module).</p>
<p>Probably Microsoft Copilot or ChatGPT can generate the Python script from this description. You can run the script by copying it into the Python console.</p>

---

## Post #3 by @sck84 (2025-01-28 20:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="41249">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>First, you need to get a transformation matrix that transforms the midsagittal plane to a plane that is orthogonal to the world coordinate syatem left-right axis. Probably the easiest is to use the ACPC transform module for this (provided by SlicerNeuro extension). You don’t need to apply this transform to the image.</p>
<p>Then you place your landmarks and get them as a numpy array. To get the point coordinates mirrored to the midsagittal plane:</p>
<ul>
<li>add a row of 1.0 values to the numpy array that contains each point position in a column (the result is the homogenous coordinates of the landmark points)</li>
<li>multiply this matrix from the left with the mirroring transform (4x4 matrix)</li>
</ul>
<p>You can compute the mirroring transform by a simple matrix multiplication: <code>inv(ACPC) * diag(-1,1,1,1) * ACPC</code> (where <code>ACPC</code> is the ACPC transform computed by the ACPC Transform module).</p>
<p>Probably Microsoft Copilot or ChatGPT can generate the Python script from this description. You can run the script by copying it into the Python console.</p>
</blockquote>
</aside>
<p>Wow… I was beginning to think it was impossible, but this worked. Thank you so much!!</p>

---
