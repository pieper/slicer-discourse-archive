# SegmentComparison for nii.gz image

**Topic ID**: 8825
**Date**: 2019-10-18
**URL**: https://discourse.slicer.org/t/segmentcomparison-for-nii-gz-image/8825

---

## Post #1 by @vietlebao (2019-10-18 00:52 UTC)

<p>Hello everyone.<br>
I am comparing two structures of nii.gz image by using SegmentComparison. However, I cannot select the inputs (red circle), as attached, there is no segments to select.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7deca12e36fe01841f7aea9072cecd24803d0659.png" data-download-href="/uploads/short-url/hXYEWCj3GMYiWmPgrcLY4sJ06ZH.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7deca12e36fe01841f7aea9072cecd24803d0659_2_690x409.png" alt="Capture" data-base62-sha1="hXYEWCj3GMYiWmPgrcLY4sJ06ZH" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7deca12e36fe01841f7aea9072cecd24803d0659_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7deca12e36fe01841f7aea9072cecd24803d0659_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7deca12e36fe01841f7aea9072cecd24803d0659.png 2x" data-dominant-color="8F8F95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1039×616 39 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks.</p>

---

## Post #2 by @Sunderlandkyl (2019-10-18 01:59 UTC)

<p>You’ll need to create a segmentation from the volume.</p>
<p>Import or convert the nii.gz to a labelmap node as described here:</p><aside class="quote" data-post="4" data-topic="1081">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-convert-volume-to-segmentation/1081/4">How to convert volume to segmentation?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You can only import labelmap volumes. You have two options for having your volume interpreted as labelmap: 

Option A: Load your volume as a labelmap: in the Add data dialog click on Show options and check “LabelMap”.
Option B: Convert your grayscale volume to labelmap in the Volumes module, Volume information section, Convert to label map row.
  </blockquote>
</aside>

<p>Then, in the Segmentations module, import the labelmap node to a Segmentation. The option should be under the “Export/import models and labelmaps” section.</p>

---

## Post #3 by @vietlebao (2019-10-18 03:50 UTC)

<p>Many thanks Kyle…I got it</p>

---

## Post #4 by @lassoan (2019-10-18 17:48 UTC)

<p>In most recent Slicer Preview Release (since 1-2 days ago) you can load a nrrd labelmap volume file directly as a Segmentation node (select “Segmentation” in description column in “Add data” dialog).</p>
<p><a class="mention" href="/u/vietlebao">@vietlebao</a> is there a specific reason you use nifti (nii.gz) file format instead of nrrd?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you have a look into supporting reading 3D nii.gz files directly as segmentation nodes? No need to allow saving into nifti (as adding custom metadata to nifti files is very complicated).</p>

---

## Post #5 by @Fernando (2019-10-23 16:47 UTC)

<p>I have done many times [Load nifti / more options / label / Segmentations / create / import from labelmap].</p>
<p>+1 to the option of reading NIfTI as Segmentation nodes!</p>

---

## Post #6 by @lassoan (2019-10-23 17:38 UTC)

<p>Do you have any reason to use nifti format for storing segmentation?</p>
<p>Importing a plain labelmap volume is fine, but it is complicated to save custom metadata in a nifti file, so we probably won’t support saving segmentation into nifti files anytime soon (unless there is a commonly used standard emerges that allows storage of essential segmentation metadata, such as segment names and colors).</p>

---

## Post #7 by @Fernando (2019-10-24 09:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="8825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you have any reason to use nifti format for storing segmentation?</p>
</blockquote>
</aside>
<p>Nothing specific. The labs where I’ve worked only use nifti, maybe because I’ve mostly done neuroimage. I’ve never seen anyone using nrrd, just myself whenever I’m handling Slicer segmentations.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="8825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Importing a plain labelmap volume is fine, but it is complicated to save custom metadata in a nifti file, so we probably won’t support saving segmentation into nifti files anytime soon</p>
</blockquote>
</aside>
<p>Usually, I just save any segmentations as label maps, so that’s ok.</p>

---

## Post #8 by @pieper (2019-10-24 12:30 UTC)

<aside class="quote no-group" data-username="Fernando" data-post="7" data-topic="8825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar"> Fernando:</div>
<blockquote>
<p>The labs where I’ve worked only use nifti, maybe because I’ve mostly done neuroimage.</p>
</blockquote>
</aside>
<p>It’s true, this is very common practice.  The problem is that it’s also very common. for people to use a variety of ad hoc methods to track segment numbers, colors, etc. and it’s held the field back IMO.  I think that’s why there’s a big push for <a href="https://bids.neuroimaging.io/">bids</a>, and perhaps it’s time for a SlicerBIDS extension.</p>

---

## Post #9 by @lassoan (2019-10-24 15:15 UTC)

<p>I like that anybody can easily create a BIDS data set just by converting DICOM to nifti and adding text files to describe them. This is what most people end up doing before starting to analyze their data anyway and using common conventions for this helps.</p>
<p>However, simplicity stops here. BIDS standard is already probably well over hundred of printed pages long and in BIDS you cannot even store a CT image in standard way yet (it is not in the standard, they are looking for volunteers to work on the extension specification). <a href="https://bids-specification.readthedocs.io/en/stable/06-extensions.html" rel="nofollow noopener">BIDS extensions</a> page contain links to hundreds of pages of additional documentation awaiting to be added to the standard. To me, BIDS specification seem just as long and complex as corresponding sections in the DICOM standard. BIDS usage of filenames and folders to group and cross-reference information is nice and simple and suitable for certain use cases, but DICOM’s UID-based system is much more robust and flexible. You can already see many cracks showing in <a href="https://docs.google.com/document/d/1LEgsMiisGDe1Gv-hBp1EcLmoz7AlKj6VYULUgDD3Zdw" rel="nofollow noopener">BIDS 2.0 ideas document</a> caused by fixed folder structure and others.</p>
<p>Overall, BIDS is a nice format to follow for brain imaging researchers, but it does not seem to be scalable to a general medical image computing standard. It would be nice to somehow channel the enthusiasm about BIDS to improve DICOM standard and toolkits to make DICOM directly usable for research.</p>

---

## Post #10 by @pieper (2019-10-24 19:44 UTC)

<p>Ah, well, of course many people know that my preference is DICOM too!</p>
<p>My point about a SlicerBIDS is that if there is a community who uses it, then some of the developers in that community might also be willing to promote interoperability with tools that rely on BIDS.</p>

---
