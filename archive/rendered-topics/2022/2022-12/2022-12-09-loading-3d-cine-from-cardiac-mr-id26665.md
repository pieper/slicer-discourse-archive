---
topic_id: 26665
title: "Loading 3D Cine From Cardiac Mr"
date: 2022-12-09
url: https://discourse.slicer.org/t/26665
---

# Loading 3d cine from cardiac MR

**Topic ID**: 26665
**Date**: 2022-12-09
**URL**: https://discourse.slicer.org/t/loading-3d-cine-from-cardiac-mr/26665

---

## Post #1 by @RGhosh (2022-12-09 16:45 UTC)

<p>I am having trouble loading a 3d cine from cardiac MR, specifically one obtained using a Phillips scanner. Despite choosing “volume sequence” in Edit–&gt;settings–&gt;DICOM, it does not load properly. Instead of each “instance number” representing a phase of the cardiac cycle, each “instance number” represents the position of each slice in the acquisition. (see the two screenshots below).</p>
<p>I have not had this problem when loading in 3D cines from cardiac CT or from cardiac MRs obtained from a Siemens scanner.</p>
<p>Any advice?<br>
Thank you,<br>
Reena</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bb4998ed3e4c6607c35999f61a8934568f292d4.jpeg" data-download-href="/uploads/short-url/d5gnKV8pNJNBH9jLOrAamksbULG.jpeg?dl=1" title="slicer3dcine screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bb4998ed3e4c6607c35999f61a8934568f292d4_2_690x484.jpeg" alt="slicer3dcine screenshot" data-base62-sha1="d5gnKV8pNJNBH9jLOrAamksbULG" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bb4998ed3e4c6607c35999f61a8934568f292d4_2_690x484.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bb4998ed3e4c6607c35999f61a8934568f292d4_2_1035x726.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bb4998ed3e4c6607c35999f61a8934568f292d4_2_1380x968.jpeg 2x" data-dominant-color="393A40"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3dcine screenshot</span><span class="informations">1920×1348 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41915aa7ebb6cd49bdb49694d463f4e35d854f70.jpeg" data-download-href="/uploads/short-url/9m2senUaNuAFSQuWLGDnWlWlD20.jpeg?dl=1" title="slicer3dcinescreenshot2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41915aa7ebb6cd49bdb49694d463f4e35d854f70_2_690x401.jpeg" alt="slicer3dcinescreenshot2" data-base62-sha1="9m2senUaNuAFSQuWLGDnWlWlD20" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41915aa7ebb6cd49bdb49694d463f4e35d854f70_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41915aa7ebb6cd49bdb49694d463f4e35d854f70_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41915aa7ebb6cd49bdb49694d463f4e35d854f70_2_1380x802.jpeg 2x" data-dominant-color="36373D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer3dcinescreenshot2</span><span class="informations">1920×1116 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-12-09 17:33 UTC)

<p>Probably we didn’t have an example datasets from Philips.  If you can share something (anoymized or a phantom) it’s probably debuggable <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMPlugins/DICOMImageSequencePlugin.py">here</a>.  Maybe you can have a look yourself at the logic for splitting up a series into a volume sequence.  Usually it’s just finding the right tag pattern, sometimes a private tag unfortunately.</p>

---

## Post #3 by @lassoan (2022-12-09 19:14 UTC)

<aside class="quote no-group" data-username="RGhosh" data-post="1" data-topic="26665">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/ce73a5/48.png" class="avatar"> RGhosh:</div>
<blockquote>
<p>I am having trouble loading a 3d cine from cardiac MR</p>
</blockquote>
</aside>
<p>What do you expect to have in the image?</p>
<p>From the screenshots it looks like this is a 2D+t cine MRI.</p>
<p>If the image plane is static, then you can see the image in the sagittal plane updating when you click play.</p>
<p>If it is a rotational acquisition then when you start playing then the slice may turn into a line in all views and you should see it rotating. You can set up Volume Reslice Driver module in SlicerIGT extension to keep rotating the slice view along with the moving image, or you can reconstruct a 3D volume from it using <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/Reconstruct4DCineMRI.md">Reconstruct 4D cine MRI</a> module in SlicerHeart extension.</p>
<p>If you can provide a sample data set as <a class="mention" href="/u/pieper">@pieper</a> suggested then we can test if it is interpreted correctly. Unfortunately, the DICOM standard does not specify how to group slices into spatial and temporal groups, so the only way to ensure time sequences are loaded optimally is via some vendor-specific heuristics in the DICOM importer.</p>

---
