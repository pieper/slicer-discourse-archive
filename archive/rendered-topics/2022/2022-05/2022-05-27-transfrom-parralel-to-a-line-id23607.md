---
topic_id: 23607
title: "Transfrom Parralel To A Line"
date: 2022-05-27
url: https://discourse.slicer.org/t/23607
---

# Transfrom parralel to a line

**Topic ID**: 23607
**Date**: 2022-05-27
**URL**: https://discourse.slicer.org/t/transfrom-parralel-to-a-line/23607

---

## Post #1 by @Igor_S (2022-05-27 12:47 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.1.</p>
<p>Hello,</p>
<p>I have to orient a CT image according to two lines. So right now i manually transform-rotate image so that the image is oriented parallel to the first line in axial plane, and then I rotate the sagittal and coronal plane so that it is parallel to the other line.<br>
Is there a way to script-automate this manual procedure: automatic transform-rotate image parallel to these two lines?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2022-05-27 19:08 UTC)

<p>Could you please draw a sketch to illustrate how the new coordinate system axis directions are related to your two lines?</p>
<p>What is the clinical application? For example, if you need to compute ACPC transform then you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/acpctransform.html">ACPC transform</a> module for that.</p>

---

## Post #3 by @Igor_S (2022-05-27 20:01 UTC)

<p>It is for a very similar use.<br>
I have a CT scan of lower extremity, where I want to project measurements to a coronal plane. Because lower extremity is usually positioned suboptimaly I need to adjust it to a reference plane: in transversal plane it has to be parallel to bicondlyar line, and sagittal and coronal plane have to be parallel to the mechanical line of the foot (Mikulicz line).<br>
Original and repositioned images:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efdcda6b2010062762748a6cc3cd80b16587135f.jpeg" data-download-href="/uploads/short-url/ydVi3ue7v4XosTOX7gISNvP3wmj.jpeg?dl=1" title="original image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdcda6b2010062762748a6cc3cd80b16587135f_2_79x249.jpeg" alt="original image" data-base62-sha1="ydVi3ue7v4XosTOX7gISNvP3wmj" width="79" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdcda6b2010062762748a6cc3cd80b16587135f_2_79x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdcda6b2010062762748a6cc3cd80b16587135f_2_118x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efdcda6b2010062762748a6cc3cd80b16587135f_2_158x498.jpeg 2x" data-dominant-color="1F191C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">original image</span><span class="informations">403×1267 79.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Reference lines:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf4f81eac6e0137dcee5428cf1af1ea4076f671f.png" alt="image" data-base62-sha1="tzXbbqpIlTGU2mY1LNSqhNrMg6r" width="213" height="201"></p>
<p>From this position I project some other points and lines in the same coronal plane and make measurements in that plane. There could be an easier way to do it, but that’s what I came up with.</p>

---

## Post #4 by @chir.set (2022-05-28 10:45 UTC)

<p>Based on these assumptions :</p>
<ul>
<li>the two lines need not intersect</li>
<li>you want to rotate each slice view independently</li>
</ul>
<p>This code snippet will rotate the Yellow slice view such that the two control points of line L are visible in this slice view :</p>
<pre><code class="lang-auto">lineNode = slicer.util.getNode("L")
p1 = lineNode.GetNthControlPointPositionWorld(0)
p2 = lineNode.GetNthControlPointPositionWorld(1)
normal = [0.0] * 3
vtk.vtkMath().Cross(p1, p2, normal)
sliceNode = slicer.app.layoutManager().sliceWidget("Yellow").sliceLogic().GetSliceNode()
sliceNode.SetSliceToRASByNTP(normal[0], normal[1], normal[2], p2[0], p2[1], p2[2], p1[0], p1[1], p1[2], 0)
</code></pre>
<p>Please note that you may lose Left-Right and/or Inferior-Superior anatomical orientation, this is not predictable.</p>

---
