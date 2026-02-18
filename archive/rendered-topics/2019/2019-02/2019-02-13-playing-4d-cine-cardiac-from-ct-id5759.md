# Playing 4d cine cardiac from CT

**Topic ID**: 5759
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/playing-4d-cine-cardiac-from-ct/5759

---

## Post #1 by @sarvpriya1985 (2019-02-13 17:01 UTC)

<p>Hi all.</p>
<p>I am running into trouble playing cine of 4D cardiac data set. It did work previosuly. But now I loaded the data set into slicer as volume mode (not multivolume). When i open the data set into sequences browser to play, nothing happens. The slices sit idle and volume render does not move either. Can someone pls explain this.<br>
The green bar just moves and shows different slices, but nothing happens in the CT or volume render images.</p>
<p>Thanks,<br>
Sarv<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01718caff3c9534d0c6500294cb5fc707be8cb71.jpeg" data-download-href="/uploads/short-url/cLKT8MSfj9htsquYwkfjsK21od.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01718caff3c9534d0c6500294cb5fc707be8cb71_2_690x351.jpeg" alt="Capture" data-base62-sha1="cLKT8MSfj9htsquYwkfjsK21od" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01718caff3c9534d0c6500294cb5fc707be8cb71_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01718caff3c9534d0c6500294cb5fc707be8cb71_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/01718caff3c9534d0c6500294cb5fc707be8cb71_2_1380x702.jpeg 2x" data-dominant-color="B9B8BA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1739×885 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2019-02-13 17:36 UTC)

<p>Your proxy node for the sequence that you are trying to play is something that ends with “…sitionTime [3]”, but what you are viewing in the Slice viewers is something that ends with “…] cropped”.  I don’t think you’re actually viewing the sequence that you are playing.</p>

---

## Post #3 by @sarvpriya1985 (2019-02-13 20:10 UTC)

<p>Hi,<br>
Thank you so much for pointing out. I changed it and was able to play it. However, there are stair-step artifacts in the video. This is after I interpolate it to be same size. Also the slices are very thin. Is there a way to fix that. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1838f2828c8082ca24e0e9f6c09247e505df72b5.jpeg" data-download-href="/uploads/short-url/3sht2fFY5QJBpvlqg3RS1cOsV7v.jpeg?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1838f2828c8082ca24e0e9f6c09247e505df72b5_2_690x360.jpeg" alt="Capture1" data-base62-sha1="3sht2fFY5QJBpvlqg3RS1cOsV7v" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1838f2828c8082ca24e0e9f6c09247e505df72b5_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1838f2828c8082ca24e0e9f6c09247e505df72b5_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1838f2828c8082ca24e0e9f6c09247e505df72b5_2_1380x720.jpeg 2x" data-dominant-color="C8C4C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1739×908 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a href="https://youtu.be/_NoNpwIKoto" rel="noopener nofollow ugc">Stair-step artifacts</a></p>

---
