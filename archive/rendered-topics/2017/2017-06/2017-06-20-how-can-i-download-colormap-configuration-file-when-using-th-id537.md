---
topic_id: 537
title: "How Can I Download Colormap Configuration File When Using Th"
date: 2017-06-20
url: https://discourse.slicer.org/t/537
---

# How can I download "colormap configuration file" when using the module of "ShapePopulationViewer"?

**Topic ID**: 537
**Date**: 2017-06-20
**URL**: https://discourse.slicer.org/t/how-can-i-download-colormap-configuration-file-when-using-the-module-of-shapepopulationviewer/537

---

## Post #1 by @Ramttoong (2017-06-20 13:48 UTC)

<p>And, How can I show the difference between two models as arrow shape?</p>

---

## Post #2 by @mirclem (2017-06-20 14:10 UTC)

<p>Hi,</p>
<p>There is no colormap collection available online because you can customize and create your own colormaps.<br>
<a href="http://www.nitrc.org/docman/view.php/759/2022/SPV_tutorial_PDF.pdf" rel="nofollow noopener">Here</a> is the last documentation about ShapePopulationViewer, starting at slide 18 you will see how to change colormaps and slide 40 will show you how to save and then load them.</p>
<p>To show the difference between two models, there is a module named “ModelToModelDistance” (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ModelToModelDistance" rel="nofollow noopener">doc</a>) that you can download from the Slicer Extension Manager.</p>
<p>Hope it helps,</p>

---

## Post #3 by @lassoan (2017-06-20 14:30 UTC)

<aside class="quote no-group" data-username="Ramttoong" data-post="1" data-topic="537" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/edb3f5/48.png" class="avatar"> Ramttoong:</div>
<blockquote>
<p>And, How can I show the difference between two models as arrow shape?</p>
</blockquote>
</aside>
<p>For this, you need to register the two models. Result of the registration is a transform that morphs one model to the other.</p>
<p>One option for registration is to convert the models to segments using Segmentations module (Import/export section) and then use the Segment registration extension. If you have the original image data then you probably you can compute more accurate registration from that, using an intensity based image registration.</p>

---

## Post #4 by @mirclem (2017-06-20 14:50 UTC)

<p>If you are working with 3D models, the registration can be done using the “Surface Registration” module from the “CMFReg” extension also available in the Slicer Extension Manager.<br>
We have a <a href="https://www.youtube.com/watch?v=hsZrjNsXZbs" rel="nofollow noopener">video tutorial</a> about how to use the different features and ways to register models. (registration with fiducials, Region of Interest or surface; )</p>

---

## Post #5 by @lassoan (2017-06-20 15:00 UTC)

<p>If you just need linear (rigid, similarity, affine) transforms then CMFreg should work well. However, that usually will not morph one surface to the other, it’ll just align it as much as it can, so the displacement vectors will not show where each point is moved.</p>
<p>In general, if you need a transform that maps one surface <em>exactly</em> to the other, then you need to use a non-linear warping transform (b-spline or thin-plate-spline): for surface-based registration I think only Segment Registration implements this; for landmark-based registration, you can use Fiducial registration wizard (in SlicerIGT extension).</p>

---
