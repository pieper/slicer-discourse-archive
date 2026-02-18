# Module PET Tumor Segmentation

**Topic ID**: 40306
**Date**: 2024-11-21
**URL**: https://discourse.slicer.org/t/module-pet-tumor-segmentation/40306

---

## Post #1 by @imbeatriz (2024-11-21 14:20 UTC)

<p>Hi everyone,</p>
<p>I’m working on segmenting a liver lesion using the PET Tumor Segmentation module on a PET image. To assist, I followed a YouTube tutorial (<a href="https://www.youtube.com/watch?v=oYlFhqxdptE" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=oYlFhqxdptE</a>). However, when I attempt to click on the center of the lesion in any plane, nothing is selected.</p>
<p>I’ve tried alternative approaches within the module, but the tool still doesn’t seem to function as expected. For better visualization, I’m using a ct scan combined with the pet image</p>
<p>Has anyone encountered a similar issue or knows what might be causing this?</p>
<p>Thank you in advance!</p>
<p>Best regards,<br>
Beatriz</p>

---

## Post #2 by @pieper (2024-11-21 14:42 UTC)

<p>Unfortunately, I believe these PET tools haven’t been maintained since the direct funding stopped.  Maybe it’ll be easy to get them working again, but someone would need to investigate and figure out what’s not working.  You might check the error log to see if it’s something simple looking, but as I recall those are somewhat sophisticated modules.</p>

---

## Post #3 by @imbeatriz (2024-11-21 15:15 UTC)

<p>The error log says this: Python 3.9.10 (main, Apr  5 2024, 04:28:47)<br>
[GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux2</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
self.extentGrowthRatio = 0.1<br>
masterImageExtent = (0, 124, 0, 121, 0, 92)<br>
labelsEffectiveExtent = (21, 112, 13, 107, 11, 84)<br>
labelsExpandedExtent = [12, 121, 4, 116, 4, 91]<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[VTK] Warning: In vtkMRMLSegmentEditorNode.cxx, line 185<br>
[VTK] vtkMRMLSegmentEditorNode (0xe208290): qSlicerSegmentEditorAbstractEffect::GetMasterVolumeNode() method is deprecated, use GetSourceVolumeNode method instead<br>
[VTK] Warning: In vtkMRMLSegmentEditorNode.cxx, line 185<br>
[VTK] vtkMRMLSegmentEditorNode (0xe208290): qSlicerSegmentEditorAbstractEffect::GetMasterVolumeNode() method is deprecated, use GetSourceVolumeNode method instead<br>
[VTK] Warning: In vtkMRMLSegmentEditorNode.cxx, line 185<br>
[VTK] vtkMRMLSegmentEditorNode (0xe208290): qSlicerSegmentEditorAbstractEffect::GetMasterVolumeNode() method is deprecated, use GetSourceVolumeNode method instead</p>

---

## Post #4 by @pieper (2024-11-21 16:01 UTC)

<p>Hmm, those are just warnings, so not much to go on.  If you are trying on your own data, probably try with any provided sample data for the tutorial first, to see if there’s a regression.  Again, since there’s no dedicated funding for this you may need to try fixing it yourself, if you feel up to it.</p>

---

## Post #5 by @imbeatriz (2024-11-21 16:44 UTC)

<p>The tool worked perfectly on the sample data, so the issue likely lies with my images. Still, it’s strange that it functions on the sample but not with mine. As mentioned earlier, I have the CT image set as the background and the PET image overlaid on top. I’ve also adjusted the color maps to improve tumor visibility (as shown in the image).</p>
<p>Do you have any suggestions for alternative methods to segment the tumors? I’ve tried using the grow from seeds tool, but the results weren’t very good.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6305cff512d0bb4ffa58724d10527bc68972be41.png" data-download-href="/uploads/short-url/e7ZIN3VVhCXeLqG2lfXitVsrUul.png?dl=1" title="Screenshot from 2024-11-21 16-40-47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6305cff512d0bb4ffa58724d10527bc68972be41.png" alt="Screenshot from 2024-11-21 16-40-47" data-base62-sha1="e7ZIN3VVhCXeLqG2lfXitVsrUul" width="473" height="336"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-11-21 16-40-47</span><span class="informations">473×336 27.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2024-11-21 17:02 UTC)

<p>You could try the threshold and island tools in the segment editor using the pet as the source volume.</p>
<p>It’s probably worth looking into what’s different between your data and the sample.  You can look at the logs when you load the data to see if there are missing header values needed to calculate SUV.  Or maybe it’s something else.</p>

---

## Post #7 by @imbeatriz (2024-11-21 19:16 UTC)

<p>Thank you for the suggestion. I will look into the differences between my data and the sample better.</p>

---
