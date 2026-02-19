---
topic_id: 806
title: "Flood Filling Segment Editor Effect Does Not Fill The Image"
date: 2017-08-02
url: https://discourse.slicer.org/t/806
---

# Flood filling segment editor effect does not fill the image

**Topic ID**: 806
**Date**: 2017-08-02
**URL**: https://discourse.slicer.org/t/flood-filling-segment-editor-effect-does-not-fill-the-image/806

---

## Post #1 by @doc-xie (2017-08-02 09:18 UTC)

<p>Hello professor!<br>
About the Flood filling,why the function can not run correctly after i paint the ROI,the image have not any reaction.<br>
For example,I paint the ROI(not sphere brush) of hemotoma on an CT scan of ICH firstly,then I choose Flood filling,click the region suround ROI( intensity tolerance 50,neighbordhood size1.0),the image have not any change,why?In addition,how to adjust the intensity tolerance and neighbordhood size?<br>
Thanks a lot!</p>

---

## Post #2 by @lassoan (2017-08-02 13:03 UTC)

<aside class="quote no-group quote-modified" data-username="docxieguoqiang" data-post="3" data-topic="104">
<div class="title">
<div class="quote-controls"></div>
<a href="https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104/3">Watershed, Fast marching, and Flood filling effects in Segment editor</a></div>
<blockquote>
<p>why the function can not run correctly</p>
</blockquote>
</aside>
<p>Click “Show details” link in the effect to see what it does.</p>
<p>For example, for Flood filling: “Fill connected voxels with similar intensity.<br>
Click in the image to add voxels that have similar intensity to the clicked voxel.” Therefore, it does not require any previous paints, you just click at any point in the image and similar-intensity regions are filled. If nothing is filled then it means you need to increase intensity tolerance or decrease neighborhood size.</p>
<p>To fill a hollow segment, use “Islands” effect’s “Add selected island” method and click in side the hole in the segment.</p>
<p>To fill many small holes at once, use “Smoothing” effect’s “Closing” method.</p>

---
