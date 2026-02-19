---
topic_id: 19807
title: "Re Opening Mrml Error Code Unmatched Volume Size"
date: 2021-09-22
url: https://discourse.slicer.org/t/19807
---

# Re-opening mrml error code - unmatched volume size

**Topic ID**: 19807
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/re-opening-mrml-error-code-unmatched-volume-size/19807

---

## Post #1 by @ni5h (2021-09-22 13:29 UTC)

<p>Hi,</p>
<p>We have completed a number of annotations segmenting abdominal tissue on one vertebral level. We are unable however to reopen the mrml file we have saved, there is an intermittent error appearing suggesting the load has failed. We are cropping the images to ensure our annotation remains within the required level. When we save the annotation we use the uncropped file as the reference volume. however, the size of the annotation is equal to the cropped volume instead of matching the size of the uncropped volume, this should not be the case. I have attached an image of the error code. Is there a cause to this? This issue is mostly intermittent and has affected 50% of our cases. Please offer a solution?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad48ed0b6c7faad3e1b1cc9ae6519fadc0239124.png" alt="image" data-base62-sha1="oIWQqcJvxNAjUkaPcEv1VWIcOqM" width="674" height="291"></p>

---

## Post #2 by @pieper (2021-09-22 13:59 UTC)

<p>Is your Y: drive a dropbox or google drive like folder?  There have been some reported issues saving to those.  Try using local drives for saving.  If you can replicate an error let us know the exact steps and environment.</p>

---

## Post #3 by @ni5h (2021-09-22 14:17 UTC)

<p>our processes have included saving to local devices initially and then transferring to a shared drive mainly because the time taken to save onto the shared drive directly is considerably longer…the issue has occurred saving to local devices and transferring to a shared drive. the series on the shared drive have shown this mismatch. we will try to use a locally saved series for analyses and see if it works</p>

---

## Post #4 by @lassoan (2021-09-23 01:07 UTC)

<p>You can also have a look at the application log. It may contain additional details about what exactly failed while attempting to load the image.</p>
<aside class="quote no-group" data-username="ni5h" data-post="1" data-topic="19807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>When we save the annotation we use the uncropped file as the reference volume. however, the size of the annotation is equal to the cropped volume instead of matching the size of the uncropped volume, this should not be the case.</p>
</blockquote>
</aside>
<p>This is probably unrelated to the failure to save/read a scene from virtual file systems. If you export the segmentation to a labelmap volume then the geometry of that labelmap will match the specified reference node. However, if you just save the scene, the segment geometry will still be the same (probably the cropped volume, if that was used for segmentation). If you can describe any reproducible workflow that does not work as you expect then let us know and we will look into it.</p>

---

## Post #5 by @ni5h (2021-09-23 13:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="19807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you export the segmentation to a labelmap volume then the geometry of that labelmap will match the specified reference node</p>
</blockquote>
</aside>
<p>it is quite strange, when we saved the scene 50% of the segment geometry matched what the cropped image was and 50% matched the un-cropped segment. We crop the images at the start of our annotation to our desired vertebral level. We can not work out why the geometry changes during our processes. Could we have flicked back to the uncropped images to check if the annotation remained within the crop level before we have saved? however, when we save the file we save the scene, mrml, both cropped and uncropped series and the seg.nrrd file. I dont understand.</p>
<p>Additionally, we have loading errors each time we reload the mrml back onto 3d slicer (occasionally they are critical errors) we do not know why this happens [please see attached error picture above]. We dont think it related to the geometry but I can give you a workflow of how we load, annotate and save if you wish to better understand our issue?</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2021-09-23 13:47 UTC)

<aside class="quote no-group" data-username="ni5h" data-post="5" data-topic="19807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>when we save the file we save the scene, mrml, both cropped and uncropped series and the seg.nrrd file.</p>
</blockquote>
</aside>
<p>I can understand that the behavior may be hard to follow, but it sounds like everything works as it should. What is probably not clear for users is that choosing a master volume has important consequence:</p>
<blockquote>
<p>The master volume that is selected the very first time after the segmentation is created is used to determine the segmentation’s labelmap representation geometry (extent, resolution, axis directions, origin).</p>
</blockquote>
<blockquote>
<p>Note: changing the master volume does not affect the segmentation’s labelmap representation geometry. To make changes to the geometry (make the extent larger, the resolution finer, etc.) click “Specify geometry” button next to the master volume selector, …</p>
</blockquote>
<p>See more details in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#panels-and-their-use">Segment Editor module documentation</a>.</p>
<p>The solution is to either change the geometry in your segmentations ;or export labelmaps from the segmentations, using the non-cropped volume as reference volume.</p>
<aside class="quote no-group" data-username="ni5h" data-post="5" data-topic="19807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/839c29/48.png" class="avatar"> ni5h:</div>
<blockquote>
<p>Additionally, we have loading errors each time we reload the mrml back onto 3d slicer (occasionally they are critical errors) we do not know why this happens [please see attached error picture above]. We dont think it related to the geometry but I can give you a workflow of how we load, annotate and save if you wish to better understand our issue?</p>
</blockquote>
</aside>
<p>If you share a scene with use that fails to load then we might be able to tell what went wrong when it was saved. A workflow that reproduces the issue would be great (the simplest the workflow the better), but I suspect it is simply file corruption due to problems in the virtual file system.</p>
<p>Virtual file systems provided Box and Google work well for simple bulk data copy but known to cause data corruption if you try to use it as a working directory. The issue with these network-backed virtual file systems is that they cannot handle large amount of random read/write operations on many files in quick succession - at some point they just fail, maybe they even return with an error, but these errors may happen in completely unexpected locations that it is very hard to capture and handle them properly at the application level. These virtual file systems effectively work as a faulty hard disk. It would be very expensive to harden a complex application’s all file reading/writing operations against all possible file system errors, so in practice the conclusion is to not work on these drives directly, but only for bulk copy to/from local drive.</p>
<p>Note that Dropbox and OneDrive does not have such problem, because they store the files on local disk and network synchronization happens in the background.</p>

---
