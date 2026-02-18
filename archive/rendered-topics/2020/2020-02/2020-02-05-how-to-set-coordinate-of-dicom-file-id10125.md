# How to set coordinate of Dicom file?

**Topic ID**: 10125
**Date**: 2020-02-05
**URL**: https://discourse.slicer.org/t/how-to-set-coordinate-of-dicom-file/10125

---

## Post #1 by @tbuikr (2020-02-05 13:05 UTC)

<p>Hello all, I have a dicom file. I open it on ITK-snap with the coordinate is <code>0</code><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01a5a56f2e14df313d905da4f49333c10b942038.png" alt="Screenshot from 2020-02-05 19-57-36" data-base62-sha1="ezn7kVGPRefRMu9NiZXdyI5bJe" width="420" height="304"></p>
<p>Then, I open it on Slicer, and create an ROI on the image.</p>
<pre><code class="lang-auto">    # Create ROI
    roiNode = slicer.vtkMRMLAnnotationROINode()
    roiNode.SetXYZ(0, 0, 0)
    roiNode.SetRadiusXYZ(25,40,65)
    roiNode.Initialize(slicer.mrmlScene)
</code></pre>
<p>However, the center point locates on an unexpected location (not the center of the image as the figure below). If I want the center of the ROI locates on center of the image, How can I do it? Thanks<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90e05765c17e00ce653a7740076cd26d6bb7c4b3.png" alt="Screenshot from 2020-02-05 20-04-59" data-base62-sha1="kFDp6HDjiXnEsKaEI6ySaq9pz8L" width="630" height="295"></p>

---

## Post #2 by @fbordignon (2020-02-05 14:29 UTC)

<p>The origin is the starting point of your dicom image slices. My guess is that the roi origin is at the right place. If you need to calculate the midpoint of your volume, take its dimensions and divide by 2.</p>
<p>I would use something like</p>
<pre><code>roiNode.SetXYZ(400, 300, 34)</code></pre>

---

## Post #3 by @tbuikr (2020-02-06 02:31 UTC)

<blockquote>
<p>roiNode.SetXYZ(400, 300, 34)</p>
</blockquote>
<p>Thanks for your suggestion. It should be change to <code>roiNode.SetXYZ(-400, -300, 34)</code> instead of <code>roiNode.SetXYZ(400, 300, 34)</code></p>

---
