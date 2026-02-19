---
topic_id: 17350
title: "Roi On Slice Intersection"
date: 2021-04-27
url: https://discourse.slicer.org/t/17350
---

# ROI on slice intersection

**Topic ID**: 17350
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/roi-on-slice-intersection/17350

---

## Post #1 by @Vincebisca (2021-04-27 13:26 UTC)

<p>Hello, I have been trying to create a custom workflow GUI on a Slicelet used for segmentation. part of this workflow is a Crop Volume to select only a precise part of the DICOM I try to segment.</p>
<p>I managed pretty well (considering my base skills) to implement the crop function, but I have 2 small problems that I don’t manage to solve :</p>
<ol>
<li>Is there a way that when I create my ROI, I set it to be located at the Slice Intersection of the currently selected volume?</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8561fbedd272ce722bad611b60054642608e6ff0.png" data-download-href="/uploads/short-url/j1XqSuvkoP28d2fTZBK4YuiopZC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8561fbedd272ce722bad611b60054642608e6ff0_2_493x500.png" alt="image" data-base62-sha1="j1XqSuvkoP28d2fTZBK4YuiopZC" width="493" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8561fbedd272ce722bad611b60054642608e6ff0_2_493x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8561fbedd272ce722bad611b60054642608e6ff0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8561fbedd272ce722bad611b60054642608e6ff0.png 2x" data-dominant-color="8888B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">641×649 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>I have a case where the crop works overhaul but applies a sort of Grey filter on the image, which is a bit weird, any idea why?</li>
</ol>
<p>Before Crop :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b73989fd425a2eda3f8f70b34a95fb4cbf19a91d.png" alt="image" data-base62-sha1="q8SExuP78FweNGVo8WW7PUthRA9" width="335" height="335"></p>
<p>After Crop :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af46993fd11e63870aaafec1e2bcaefe596c42ba.png" alt="image" data-base62-sha1="p0yOtLEQgPbpuZHETDG1IC8ddb4" width="352" height="332"></p>
<p>In my code, the crop parameters are use are these ones :<br>
cropVolumeLogic.CropInterpolated(roi, inputVolume, outputVolume, True, 1.00, 0, 0)</p>
<p>Thanks for the hints if you have some !</p>

---

## Post #2 by @pieper (2021-04-27 18:54 UTC)

<p>For the first, you can set the ROI location to the offsets which you can get from the slice nodes (in psuedocode you get the app’s layoutManager and then iterate through the slice views to get their slide nodes from which you can get the planes which can be used to figure out the intersection.</p>
<p>For the second probably it’s a window/level auto on the cropped volume.  So you can copy the source window and level from the display node to the new cropped node’s display node.</p>
<p>Hope that gives you the hints you need.</p>

---

## Post #3 by @Vincebisca (2021-04-28 06:59 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="17350">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For the first, you can set the ROI location to the offsets which you can get from the slice nodes (in psuedocode you get the app’s layoutManager and then iterate through the slice views to get their slide nodes from which you can get the planes which can be used to figure out the intersection.</p>
</blockquote>
</aside>
<p>Okay so if I understand well, there is no way I can get the intersection coordinates, or the crossbar coordinates (since that option exists also) through a builtin function? I have to figure out a process to get it, right?</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="17350">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For the second probably it’s a window/level auto on the cropped volume. So you can copy the source window and level from the display node to the new cropped node’s display node.</p>
</blockquote>
</aside>
<p>Hmmm okay I think I get it, I’ve got to copy the level parameters from the original window right? Gotta figure out the code for that</p>

---

## Post #4 by @Vincebisca (2021-04-28 08:25 UTC)

<p>Okay, after a few trials :</p>
<ul>
<li>
<p>I manage to set the ROI location on the crosshairs location. I have to manually set the crosshair beforehand but that’s already a lot better. I used the following code :</p>
<p>crosshairNode=slicer.util.getNode(‘Crosshair’)<br>
pos = crosshairNode.GetCrosshairRAS()<br>
self.MyROI.SetXYZ(pos)</p>
</li>
<li>
<p>I managed to solve the filtering level by copying the InputVolume in the OutputVolume before doing the crop (previously, OutputVolume was a blank scalar volume node). Simply used the .Copy(inputVolume) method for this one.</p>
</li>
</ul>
<p>Edit : I modified the way I initialize my outputVolume : instead of using .Copy, I use CloneVolume (from Volumes Logic) to be able to have a different name (.Copy creates a volume with the same name which is not optimal to navigate afterwards). Here’s the code :</p>
<pre><code>  volumesLogic = slicer.modules.volumes.logic()
  outputVolume = volumesLogic.CloneVolume(slicer.mrmlScene, inputVolume, 'Cropped Volume' )
</code></pre>
<p>Thank you very much !</p>

---
