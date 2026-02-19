---
topic_id: 4998
title: "How To Write A Recursive Script To Crop Volumes With Roi"
date: 2018-12-06
url: https://discourse.slicer.org/t/4998
---

# How to write a recursive script to crop volumes with ROI?

**Topic ID**: 4998
**Date**: 2018-12-06
**URL**: https://discourse.slicer.org/t/how-to-write-a-recursive-script-to-crop-volumes-with-roi/4998

---

## Post #1 by @jenaflex (2018-12-06 18:19 UTC)

<ol>
<li>
<p>How to write recursive script to run ‘crop volume’ (like attached screenshot) on all 3D volumes (3D volumes extracted from 4D nifti)? I have ‘UtBox.acsv’ ROI file already.</p>
</li>
<li>
<p>(Am I supposed to, OR, ) how to make function call ‘slicer.modules.cropvolume’ in built-in Python console to crop 3D volumes with ROI (instead of using GUI).<br>
The documentation seems to be very limited.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a7c542013a837c1dce7fcd83173c623ce683f8.png" data-download-href="/uploads/short-url/kMwG9FLbDLZzUxLc9ey0zjZWFwQ.png?dl=1" title="CropScreenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91a7c542013a837c1dce7fcd83173c623ce683f8_2_690x489.png" alt="CropScreenshot" data-base62-sha1="kMwG9FLbDLZzUxLc9ey0zjZWFwQ" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91a7c542013a837c1dce7fcd83173c623ce683f8_2_690x489.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91a7c542013a837c1dce7fcd83173c623ce683f8_2_1035x733.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91a7c542013a837c1dce7fcd83173c623ce683f8.png 2x" data-dominant-color="575758"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CropScreenshot</span><span class="informations">1131×803 33.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>Thanks!</p>

---

## Post #2 by @jenaflex (2019-02-08 00:31 UTC)

<p>Up. Please help. Thanks!</p>

---

## Post #3 by @pieper (2019-02-08 13:52 UTC)

<p>You could start by looking at the <a href="https://github.com/JoostJM/SlicerCaseIterator" rel="nofollow noopener">SlicerCaseIterator</a>.  Once you can iterate through your volumes you could add some code to do the cropping.  I agree it’s not well documented but the building blocks are there and you can see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">example scripts</a>.</p>

---

## Post #4 by @jenaflex (2019-02-08 16:34 UTC)

<p>Thanks!<br>
I think I should be able to figure out iteration method.<br>
My main concern is how to call cropvolume function with input ROI being UtBox ROI file (like the screenshot).</p>

---

## Post #5 by @simonoxen (2019-02-08 17:54 UTC)

<p>Hi, this is a part of a script I used to call cropvolume from a python script:</p>
<pre><code>parameters = slicer.vtkMRMLCropVolumeParametersNode()
slicer.mrmlScene.AddNode(parameters)

parameters.SetInputVolumeNodeID(input.GetID())
parameters.SetOutputVolumeNodeID(output.GetID())
parameters.SetROINodeID(roiNode.GetID())
slicer.modules.cropvolume.logic().Apply(parameters)</code></pre>

---

## Post #6 by @lassoan (2020-04-17 23:26 UTC)

<p>A post was merged into an existing topic: <a href="/t/volume-cropping-from-scripted-module/11169/2">Volume Cropping from Scripted Module</a></p>

---
