# Changing voxel size

**Topic ID**: 7804
**Date**: 2019-07-30
**URL**: https://discourse.slicer.org/t/changing-voxel-size/7804

---

## Post #1 by @Andrew_Kanawati (2019-07-30 02:24 UTC)

<p>Can you please explain the steps to change the voxel size of the models. I am finding the dimensions of printed tubes and cylinders to be smaller or larger than the planned dimension. I have tried reducing the ‘spacing scale’ in crop volume but it is not working.</p>

---

## Post #2 by @lassoan (2019-07-30 04:15 UTC)

<p>If you crop &amp; resample the volume <em>before</em> starting segmentation and use the cropped volume as master volume then the segmentation node’s internal binary labelmap representation will use this higher resolution.</p>
<p>You can also change the segmentation’s resolution any time by clicking on the “Specify geometry” button next to the master volume selector in Segment Editor.</p>

---

## Post #3 by @Andrew_Kanawati (2019-08-01 18:50 UTC)

<p>Thank you Andras.<br>
If I click on the ‘specific geometry’ button, is there a difference between changing the ‘segmentation’ resolution as opposed to the master volume?</p>

---

## Post #4 by @cpinter (2019-08-01 19:05 UTC)

<p>If you use the “Specify geometry” button, then only the labelmaps in your segments will have the specified geometry, but your anatomical image (i.e. the master volume) will stay the same.</p>
<p>If you resample the master volume, but do it after doing some segmentation, then the labelmaps in the segments will be unchanged (will have the geometry of the master volume before resampling). But if you resample the master volume before starting to segment, then both will have the resampled master volume’s geometry.</p>

---

## Post #5 by @Andrew_Kanawati (2019-08-12 15:19 UTC)

<p>Thanks very much.</p>
<p>These solutions have helped a little bit, but they slow the process of creating models and cause slicer to crash often. I image because the models are more complex and file sizes are increased.</p>
<p>However I am still having trouble when creating tubes or straight objects in slicer. I don’t have any problems with scaling or pixels when an object has been created from a dicom (such as a vertebral bone), or if I’ve created a shell model which I use to print templates.<br>
However if I am creating a tube, then creating a segment from that transform, the model becomes pixelated and the 3d print of this segment is also pixelated, and is this not accurate.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dacfcd54b88cf5f3deb898a83416a5d2e1a41e45.jpeg" data-download-href="/uploads/short-url/vdHiKBQSLEc70M0jhBCxrfdHMQl.jpeg?dl=1" title="04%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dacfcd54b88cf5f3deb898a83416a5d2e1a41e45_2_354x500.jpeg" alt="04%20AM" data-base62-sha1="vdHiKBQSLEc70M0jhBCxrfdHMQl" width="354" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dacfcd54b88cf5f3deb898a83416a5d2e1a41e45_2_354x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dacfcd54b88cf5f3deb898a83416a5d2e1a41e45_2_531x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dacfcd54b88cf5f3deb898a83416a5d2e1a41e45.jpeg 2x" data-dominant-color="84749A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04%20AM</span><span class="informations">641×904 88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/617d0430e7f4d98b786155051d36870f817c4957.jpeg" data-download-href="/uploads/short-url/dUq9YMwUNMhXevlVhisRAfCyNnh.jpeg?dl=1" title="10%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/617d0430e7f4d98b786155051d36870f817c4957_2_363x499.jpeg" alt="10%20AM" data-base62-sha1="dUq9YMwUNMhXevlVhisRAfCyNnh" width="363" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/617d0430e7f4d98b786155051d36870f817c4957_2_363x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/617d0430e7f4d98b786155051d36870f817c4957_2_544x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/617d0430e7f4d98b786155051d36870f817c4957.jpeg 2x" data-dominant-color="8683C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">10%20AM</span><span class="informations">577×794 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, if I change the oversampling factor the 3d model become very pixelated. I’m not sure what this is.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d61131adb7f745123ba7bf0229ecf58206bafba.jpeg" data-download-href="/uploads/short-url/6trsZsOCj1V0IVoNeyKF34Pvgam.jpeg?dl=1" title="11%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d61131adb7f745123ba7bf0229ecf58206bafba_2_388x500.jpeg" alt="11%20AM" data-base62-sha1="6trsZsOCj1V0IVoNeyKF34Pvgam" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d61131adb7f745123ba7bf0229ecf58206bafba_2_388x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d61131adb7f745123ba7bf0229ecf58206bafba_2_582x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d61131adb7f745123ba7bf0229ecf58206bafba.jpeg 2x" data-dominant-color="837196"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11%20AM</span><span class="informations">661×850 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
