# Color Map corresponding to Scalar Values

**Topic ID**: 3117
**Date**: 2018-06-07
**URL**: https://discourse.slicer.org/t/color-map-corresponding-to-scalar-values/3117

---

## Post #1 by @aadrienne (2018-06-07 18:51 UTC)

<p>Hello!</p>
<p>I am new to Slicer 3D and I am working on segmentation and quantification for two different MRI scans. I have been able to segment specific regions, but I wanted to know if there were any options to show the specific pixel intensity values from within those segmented regions with a corresponding color map and legend? (Is there any way to create a quantitative color map for segmented regions, or are color maps only qualitative for the time being?)</p>
<p>Thank you for any help in advance.</p>
<p>-Alex</p>

---

## Post #2 by @pieper (2018-06-07 20:05 UTC)

<p>Yes, you can segment a region and use SegmentStatistics to create a Table, from which you can plot values.</p>
<p>Or you can create a custom color table and display the scalar bar:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/Colors" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/Colors</a></p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @lassoan (2018-06-07 23:22 UTC)

<p>Segmentation module will create a color node if you export the segmentation to a labelmap node. Then, as Steve described above, You can then show the legend in slice and 3D views using the Colors module.</p>

---
