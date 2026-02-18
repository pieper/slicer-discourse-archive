# Fast marching problem ver 5.0.2

**Topic ID**: 24078
**Date**: 2022-06-28
**URL**: https://discourse.slicer.org/t/fast-marching-problem-ver-5-0-2/24078

---

## Post #1 by @Nguyen_Hieu (2022-06-28 12:44 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.0.2<br>
I use this version and install Fast Marching but this extension is not appeared in “Segment Editor”, its interface is quite different from this video <a href="https://www.youtube.com/watch?v=XPx0tStSsnA&amp;ab_channel=PerkLabResearch" class="inline-onebox" rel="noopener nofollow ugc">Fast marching segmentation in 3D Slicer - YouTube</a><br>
So how can I solve this problem?<br>
In addition, I want to measure mastoid air cells, middle ear spaces in temporal bone CT scan, any suggestions to do this? because the mastoid air cells are separated by bone septa so I think they’re difficult to measure the volume.<br>
Thanks so much for your help</p>

---

## Post #2 by @lassoan (2022-06-28 16:26 UTC)

<p>Fast marching effect works exactly the same as it is shown in the video. There was a minor change in the Segment Editor module layout in that the toolbar is now vertical, while previously it was horizontal:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7170132f8ee65782c09c4feeb78619b01a80a640.png" data-download-href="/uploads/short-url/gbw4z07XmmspMrT5ImgtIzW91Ac.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7170132f8ee65782c09c4feeb78619b01a80a640_2_496x500.png" alt="image" data-base62-sha1="gbw4z07XmmspMrT5ImgtIzW91Ac" width="496" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7170132f8ee65782c09c4feeb78619b01a80a640_2_496x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/7170132f8ee65782c09c4feeb78619b01a80a640_2_744x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7170132f8ee65782c09c4feeb78619b01a80a640.png 2x" data-dominant-color="EFF1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×800 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Note that the Fast Marching effect is provided by  SegmentEditorExtraEffects extension, so you need to install this extension to make the effect show up in Segment Editor.</p>
<p>I would recommend to create a new topic for your segmentation question, describing what you want to segment, what you have tried so far, and how it worked; illustrated by screenshots.</p>

---
