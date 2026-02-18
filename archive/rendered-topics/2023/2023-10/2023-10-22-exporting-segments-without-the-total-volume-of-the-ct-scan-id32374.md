# Exporting segments without the total volume of the CT scan

**Topic ID**: 32374
**Date**: 2023-10-22
**URL**: https://discourse.slicer.org/t/exporting-segments-without-the-total-volume-of-the-ct-scan/32374

---

## Post #1 by @orla001 (2023-10-22 20:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/738b8327e851966edafb856b7b1e3acbef3c6ae9.jpeg" data-download-href="/uploads/short-url/gu9OoJiEXxu0k9bLXq3JoFSeqpz.jpeg?dl=1" title="Screen Shot 2023-10-22 at 2.06.24 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738b8327e851966edafb856b7b1e3acbef3c6ae9_2_547x500.jpeg" alt="Screen Shot 2023-10-22 at 2.06.24 PM" data-base62-sha1="gu9OoJiEXxu0k9bLXq3JoFSeqpz" width="547" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738b8327e851966edafb856b7b1e3acbef3c6ae9_2_547x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738b8327e851966edafb856b7b1e3acbef3c6ae9_2_820x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/738b8327e851966edafb856b7b1e3acbef3c6ae9_2_1094x1000.jpeg 2x" data-dominant-color="555552"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-10-22 at 2.06.24 PM</span><span class="informations">1782×1628 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any way to export a segment without the empty space outside of that segment? When I export a segment as nrrd and convert it to a DICOM, the unsegmented/empty space of the CT scan turns into a grey background (as seen in the screenshot attached). Is there any way to remove this feature during the segmentation export?</p>

---

## Post #2 by @lassoan (2023-10-22 20:46 UTC)

<p>Probably the easiest is to crop the input volume before segmentation. This is also useful because you can then reduce the spacing (increase the resolution) of the volume, which is often desirable when you want to segment small details from a small part of the image.</p>
<p>If you have already completed the segmentation then you can modify its extent by drawing a region of interest (ROI) markup and then clicking the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options"><code>Specify geometry</code> button</a> and selecting this ROI. You might need to edit the segment (with any effect) to apply the new extents to the segment.</p>

---

## Post #3 by @orla001 (2023-10-23 15:29 UTC)

<p>Thanks for your help! Is there any way to draw an irregular ROI in 3D slicer? I do not want any background in the image.</p>

---

## Post #4 by @muratmaga (2023-10-23 15:57 UTC)

<p>Images have to be rectuangular in shape. So even if you but a spherical ROI, there will be background int the corners. By the way I suspect gray is coming from the background value of 0 you put in the maskVolume, but perhaps that’s not the lowest value, particularly if it is a signed dataset. So, perhaps try setting the background to -1024 and retry.</p>
<p>Additionally if you do want to reduce the volume to the minimum size of the segmentation (so that you want have a huge black background), you can use the SplitVolume in SegmentEditorExtraEffects instead of maskVolume</p>

---
