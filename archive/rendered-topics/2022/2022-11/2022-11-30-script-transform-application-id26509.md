---
topic_id: 26509
title: "Script Transform Application"
date: 2022-11-30
url: https://discourse.slicer.org/t/26509
---

# Script transform application

**Topic ID**: 26509
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/script-transform-application/26509

---

## Post #1 by @Nicolas_Tempier (2022-11-30 13:39 UTC)

<p>Operating system: Linux Mint<br>
Slicer version: 5.0.3</p>
<p>Hi,<br>
I have a transforms file (from ANTs registration) .mat and I would like to script the application of this transform via slicer on another image. When I was using CLI modules I could get the bash code and adapt it but with the transforms module, I can’t script the application of the transform on the image I want. How to do it please?<br>
Thanks already,</p>
<p>N.</p>

---

## Post #2 by @lassoan (2022-12-01 01:52 UTC)

<p>There are CLI modules for applying transforms on an image. For example, you can use “Resample Scalar/Vector/DWI volume” - it is the <code>.../Slicer 5.0.3/bin/../lib/Slicer-5.0/cli-modules/ResampleScalarVectorDWIVolume.exe</code>.</p>
<p>You can use loadable modules via the module logic class. For example, you can use the Crop volume module for applying a transform to a volume, along with cropping and resampling as shown in this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#fit-markups-roi-to-volume">code snippet in the script repository</a>.</p>

---

## Post #3 by @Nicolas_Tempier (2022-12-07 10:13 UTC)

<p>Thanks !<br>
Sort of works <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I don’t really understand how for example the ResampleScalarVectorDWIVolume.exe module interprets<br>
the ROI to create a transform that crops but it works !</p>

---

## Post #4 by @Saima (2023-02-07 05:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26509">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>for applying a transform to a volume, along with cropping and resam</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
How to get the invert transform and then apply it onto a volume using python scripting.</p>
<p>regards,<br>
Saima</p>

---

## Post #5 by @lassoan (2023-02-07 13:39 UTC)

<p>You can invert a transform node by calling the <code>Inverse()</code> method. You can apply a transform as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#apply-a-transform-to-a-transformable-node">here</a>.</p>

---
