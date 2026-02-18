# How can I convert the saved ROI points to voxel coordinates?

**Topic ID**: 22309
**Date**: 2022-03-04
**URL**: https://discourse.slicer.org/t/how-can-i-convert-the-saved-roi-points-to-voxel-coordinates/22309

---

## Post #1 by @Toby_Chen (2022-03-04 12:42 UTC)

<p>Hi,</p>
<p>I am trying to use 3D Slicer as a 3D bounding box labeling tool. I found the feature of creating an ROI in volume rendering. I can save the adjusted ROI as AnnotationROI.acsv. However, I can’t find a way to convert the saved points to voxel coordinates which I can use to crop the ROI in the 3D volume loaded by python’s SimpleITK module.<br>
For example:<br>
The saved ROI file:</p>
<pre><code class="lang-auto"># Annotation file /Users/tobychen/Desktop/test/case1.txt
# Name = AnnotationROI_1
# textVisibility = 1
# textColor = 0.7373,0.2549,0.1098
# textSelectedColor = 0.2667,0.6745,0.3922
# textOpacity = 1
# textAmbient = 0
# textDiffuse = 1
# textSpecular = 0
# textPower = 1
# textScale = 4.5
# textColumns = type|annotation|sel|vis
# pointNumberingScheme = 0
# pointVisibility = 1
# pointColor = 0.7373,0.2549,0.1098
# pointSelectedColor = 0.2667,0.6745,0.3922
# pointOpacity = 1
# pointAmbient = 0
# pointDiffuse = 1
# pointSpecular = 0
# pointPower = 1
# pointGlyphScale = 5
# pointGlyphType = 13
# pointColumns = type|x|y|z|sel|vis
point|74.5768|-166.008|-59.192|1|1
point|6.17077|7.2896|8.46312|1|1
# lineVisibility = 1
# lineColor = 0.7373,0.2549,0.1098
# lineSelectedColor = 0.2667,0.6745,0.3922
# lineOpacity = 1
# lineAmbient = 0
# lineDiffuse = 1
# lineSpecular = 0
# linePower = 1
# lineLineThickness = 1
# lineColumns = type|startPointID|endPointID|sel|vis
line|0|1|1|1
</code></pre>
<p>The volume shape read by python’s SimpleITK:<br>
125, 512, 512<br>
After resampled to spacing 1, 1, 1:<br>
312, 283, 283</p>
<p>Thanks!</p>

---
