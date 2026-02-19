---
topic_id: 7920
title: "Get Ijk From Slice Offset After Rotate To Volume Plane"
date: 2019-08-07
url: https://discourse.slicer.org/t/7920
---

# Get IJK from Slice Offset after Rotate to Volume Plane

**Topic ID**: 7920
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/get-ijk-from-slice-offset-after-rotate-to-volume-plane/7920

---

## Post #1 by @EricM (2019-08-07 16:30 UTC)

<p>Hello Slicer Community,</p>
<p>My ultimate goal is to create a button that copies a manual segmentation from the slice below/above and copies it into the current slice (presumably axial/Red SliceView). Note that due to the problems with segmenting on oblique views, I always use the “Rotate to Volume Plane” function after loading a Volume.</p>
<p>My plan of attack was to</p>
<ul>
<li>Get the Red, Yellow, Green coordinates with</li>
</ul>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
offsets = []
for sliceViewName in ['Red','Yellow','Green']:
  sliceWidget = layoutManager.sliceWidget(sliceViewName)
  sliceWidgetLogic = sliceWidget.sliceLogic()
  offset = sliceWidgetLogic.GetSliceOffset()
  offsets.append(offset)

z,x,y = offsets
</code></pre>
<ul>
<li>Use the z (“Red”) offset and use RAS to IJK to get the slice level</li>
<li>Copy the z-1 or z+1 slice from the segment array onto the current z slice</li>
<li>Update the segment in order to finalize the “copy”</li>
</ul>
<p>However, after doing “Rotate to Volume Plane”, the slice offsets can no longer be used to get the IJK coordinates because the Direction matrix has changed.</p>
<p>There are two ways of solving my problem, but I’m not sure which one is easiest/doable in Slicer</p>
<ul>
<li>Instead of getting the slice offset, simply get the current ‘k’ slice from the Red SliceView, if this function exists. (After “Rotate to Volume Plane” all Offsets correspond to a unique z coordinate).</li>
<li>Get the transformation from “Rotate to Volume Plane” in order to transform my Red Slice Offset from the “Rotate to Volume Plane” space to the “World” space to “Voxel” space.</li>
</ul>
<p>Thank you for any tips or comments!<br>
Eric</p>

---

## Post #2 by @lassoan (2019-08-07 17:15 UTC)

<p>Copying content of previous slice is not implemented in Segment Editor because it could either cause huge bias in the segmentation (you would tend to accept the suggested contour as is) or increase segmentation time (since it usually takes much more time to fix a contour then draw it from scratch) or both.</p>
<p>Therefore, for cases when contours of a segment does not change very quickly between neighboring segments, we suggest to use “Fill between slices” effect. You can segment on as many slices as you want then review the interpolated segmentation, and make fixes (by providing complete segmentations on additional slices) and so you avoid bias and keep segmentation time at a minimum.</p>
<p>If you still want to implement copy from previous slice then you can find IJK&lt;-&gt;RAS conversion sample code in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" rel="nofollow noopener">script repository</a>. For oblique views, voxels of previous/next slice is not well defined, as some of the volume voxels are always shared between neighbor slices.</p>

---

## Post #3 by @EricM (2019-08-09 11:01 UTC)

<p>Thanks for your answer <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I completely agree with you. I’m not a huge fan of this feature, but unfortunately, it was something that was asked of me.<br>
As you point out, the IJK&lt;-&gt;RAS conversion is not simple because of the oblique views. As I tried to explain in my previous post, I think I may have found a way around this, but I would need the transformation matrix after performing “Rotate Volume to Plane”. This matrix would take me from the “Rotate Volume to Plane” space to the “Oblique” space. In other words, using the offsets from the Red, Yellow, Green once the Volume has been rotated to the plane, I could get their equivalent in the Oblique space (i.e., how the volume shows up in Slicer by default). Then, using the RAS&lt;-&gt;IJK matrix of the volumeNode, I could get the ‘k’ slice that I see when the volume is Rotated to Plane.</p>
<p>I hope this makes sense. To summarize, is there a way to get the transformation performed on the image when “Rotate Volume to Plane” has been performed?</p>

---
