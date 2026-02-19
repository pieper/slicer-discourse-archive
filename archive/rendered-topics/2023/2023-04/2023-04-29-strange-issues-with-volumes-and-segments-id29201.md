---
topic_id: 29201
title: "Strange Issues With Volumes And Segments"
date: 2023-04-29
url: https://discourse.slicer.org/t/29201
---

# Strange Issues with volumes and segments

**Topic ID**: 29201
**Date**: 2023-04-29
**URL**: https://discourse.slicer.org/t/strange-issues-with-volumes-and-segments/29201

---

## Post #1 by @rbumm (2023-04-29 03:43 UTC)

<p>Slicer 5.2.2 (5.3 same) windows desktop w GPU<br>
Loading clinical CT dataset va DICOM mechanism into slicer<br>
Saving the volume as nrdd and in a mrb file (129 MB)<br>
Do a lung segmentation and an emphysema analysis<br>
After the latter the created lung contains lung analysis segmentation as expected and the volumes seem reasonable.<br>
Problem:<br>
No way can I hide or disable any of the see lung segmentation volumes to blink between the original image and the segmented structures.<br>
They just stay as an overlay, even if I delete all segmentations in the scene.<br>
The volume is a</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10845c7bb36bb5cb9ded5707841664fce461b81.png" data-download-href="/uploads/short-url/yogNfhafCgQTla4rQchVvS3yAhP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f10845c7bb36bb5cb9ded5707841664fce461b81_2_690x423.png" alt="image" data-base62-sha1="yogNfhafCgQTla4rQchVvS3yAhP" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f10845c7bb36bb5cb9ded5707841664fce461b81_2_690x423.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f10845c7bb36bb5cb9ded5707841664fce461b81_2_1035x634.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10845c7bb36bb5cb9ded5707841664fce461b81.png 2x" data-dominant-color="AAABA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1225×751 78.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57cfbabad4c21659a67ff64b867b016977348ffa.png" data-download-href="/uploads/short-url/cwOB5gAgMb6CQQDK93LXr7Ymsl4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57cfbabad4c21659a67ff64b867b016977348ffa_2_690x392.png" alt="image" data-base62-sha1="cwOB5gAgMb6CQQDK93LXr7Ymsl4" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57cfbabad4c21659a67ff64b867b016977348ffa_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57cfbabad4c21659a67ff64b867b016977348ffa_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57cfbabad4c21659a67ff64b867b016977348ffa.png 2x" data-dominant-color="A5A6A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1225×696 71.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Workaround:<br>
I waste another hour, export the volume as NIFTI file, do all calculations again, and do not run into this blocking error.</p>
<p>The NIFTI  file is bigger (179 MB) and has</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c80b174e27d7368b195417265e97f3a9e497c1f0.png" data-download-href="/uploads/short-url/sxFfU5dbGObhB3buk23089366Fa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c80b174e27d7368b195417265e97f3a9e497c1f0_2_690x253.png" alt="image" data-base62-sha1="sxFfU5dbGObhB3buk23089366Fa" width="690" height="253" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c80b174e27d7368b195417265e97f3a9e497c1f0_2_690x253.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c80b174e27d7368b195417265e97f3a9e497c1f0_2_1035x379.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c80b174e27d7368b195417265e97f3a9e497c1f0.png 2x" data-dominant-color="81807D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1264×465 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>These are problems or bugs that I can no way explain to one of our clinicians and that hinder acceptance. of 3D Slicer in the hospital</p>

---

## Post #2 by @lassoan (2023-04-29 12:49 UTC)

<p>The user interface only shows the first display node. I suspect that there are additional display nodes in the scene. If you can share your scene file or give instructions that we can follow to reproduce the issue then we can fix it.</p>
<p>The colored image in the source views looks more like a label volume and not a segmentation. I encountered before that when you don’t display any volumes in any layer (foreground, background, label) or an empty volume is selected in a layer then the previous content of the layer is not cleared. Maybe you have run into this.</p>
<p>Either way, it should be a very simple fix, but I can see how it can be frustrating that you don’t know what is happening and why.</p>

---
