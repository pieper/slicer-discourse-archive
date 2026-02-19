---
topic_id: 4816
title: "Co Ordinate Transformation"
date: 2018-11-20
url: https://discourse.slicer.org/t/4816
---

# Co-Ordinate Transformation

**Topic ID**: 4816
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/co-ordinate-transformation/4816

---

## Post #1 by @Stweie (2018-11-20 15:14 UTC)

<p>I am fairly new to  3D slicer.<br>
I have a .dcm series and corresponding nifti file having lesion position. After overlaying nifti over dcm series I am trying to compute the position of lesions from the nifti label to dcm position. As shown in the below image, when I calculate the position of the red lesion, I get correct x,y,z values, with correct sign. From the 3D slicer GUI, this translated position of red lesions is in RSA.</p>
<blockquote>
<pre><code>mm_coords = nib.affines.apply_affine(roi.affine, [x,y,z])
</code></pre>
</blockquote>
<p>But when I calculate the green one, I get correct values but signs are changed for L and I values. In 3D slice all the LAI values are positive but the nibabel is giving changed signs for L and I values.<br>
What could be the possible reason? Thank you in advance.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1949082fcec3c37b9cacdfedbc0080924efa614a.png" alt="Test" data-base62-sha1="3BGpeIKYk7t7VWj8xANrAHCcbsS" width="379" height="270"></p>

---

## Post #2 by @pieper (2018-11-20 16:58 UTC)

<p>Everything in Slicer is RAS - have a look at this document and is should give you all the info you need:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @Stweie (2018-11-20 17:14 UTC)

<p>Yes, I know everything in slicer is in RAS. I have also read the link you just gave.  It says .dcm files uses LPS. On the other hand the nifti file created using slicer obviously is in RAS.  when I overlap them, and visually look at the green lesion it shows x,y,z as LAI in data probe. Also when I try to calculate from nifti x,y,z to dcm in pythoon using</p>
<blockquote>
<p>nib.affines.apply_affine(nifti_roi.affine, [x,y,z])</p>
</blockquote>
<p>I get negative signs for L and I values. But in slicer GUI all LAI values are shown positve. But that does not happen in case of red lesion. I get correct values with correct sign and shwon as RAS. I hope that clarify more my question.</p>

---

## Post #4 by @lassoan (2018-11-20 17:35 UTC)

<p>Have a closer look at the data probe: labels are changing dynamically. If a point is on the left side then you get coordinate value such as “L 12.3” (instead of “R -12.3”).</p>
<p>You should not copy-paste values from the Slicer GUI anyway. Place markups then go to Markups module and click “Copy” button to copy selected markup point coordinates to the clipboard (you can directly paste to Excel).</p>

---
