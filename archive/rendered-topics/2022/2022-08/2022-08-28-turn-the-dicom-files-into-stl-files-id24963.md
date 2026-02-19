---
topic_id: 24963
title: "Turn The Dicom Files Into Stl Files"
date: 2022-08-28
url: https://discourse.slicer.org/t/24963
---

# Turn the Dicom files into .Stl files

**Topic ID**: 24963
**Date**: 2022-08-28
**URL**: https://discourse.slicer.org/t/turn-the-dicom-files-into-stl-files/24963

---

## Post #1 by @NativeArcher (2022-08-28 10:05 UTC)

<p>I have the Library of Congress stringed Instrument Dicom collection and want to turn the Dicom files into .Stl files and no tutorial that I have seen for this file conversion is really easy to understand.</p>
<p>Operating system:Windows 10<br>
Slicer version:5.1.0<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2022-08-28 12:22 UTC)

<p>Most likely you can create nice-quality models by simple thresholding using Segment Editor module. You can find hundreds of segmentation tutorials on youtube, such as:</p>
<ul>
<li>simple segmentation video tutorial: <a href="https://youtu.be/Uht6Fwtr9hE" class="inline-onebox">How to segment multiple vertebrae in spine CT for 3D printing - YouTube</a>
</li>
<li>lots more segmentation video tutorial, find one that uses simple thresholding: <a href="https://www.youtube.com/channel/UC8vxI0-dEWrw0_tBF-v8xGA/videos">https://www.youtube.com/channel/UC8vxI0-dEWrw0_tBF-v8xGA/videos</a>
</li>
</ul>

---

## Post #3 by @NativeArcher (2022-09-06 19:07 UTC)

<p>But all of the presets are for animal tissues,how would I do this for wood?</p>

---

## Post #4 by @lassoan (2022-09-07 03:45 UTC)

<p>Animal and plant tissues are probably quite similar in CT images. You can start from any of the presets and use the offset slider to adjust for overall density differences and then further tune the scalar opacity and color mapping.</p>
<p>If the presets don’t sem to work at all then it is most likely due to that the scanner was not calibrated (intensity is not in Hounsfield unit). This may require manual editing of the transfer function, similarly to this example:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="69XLwDxVTkE" data-video-title="Super-high-resolution CT visualization" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=69XLwDxVTkE" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/69XLwDxVTkE/maxresdefault.jpg" title="Super-high-resolution CT visualization" width="" height="">
  </a>
</div>


---
