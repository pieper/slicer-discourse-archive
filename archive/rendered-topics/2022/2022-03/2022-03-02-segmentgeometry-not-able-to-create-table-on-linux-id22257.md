---
topic_id: 22257
title: "Segmentgeometry Not Able To Create Table On Linux"
date: 2022-03-02
url: https://discourse.slicer.org/t/22257
---

# SegmentGeometry not able to create table on Linux

**Topic ID**: 22257
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/segmentgeometry-not-able-to-create-table-on-linux/22257

---

## Post #1 by @Michel_Atieh (2022-03-02 10:31 UTC)

<p>Hello, whenever I am trying to create a table to get the data of the segments I have drawn on the image I get this error.<br>
I am only getting this problem on Linux.<br>
Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42a73ba547e7cd072b495b742840fd2441004173.jpeg" data-download-href="/uploads/short-url/9vDO6g3o2kdjN3Q6hz9pdNsrWRJ.jpeg?dl=1" title="Screenshot from 2022-03-02 11-24-19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42a73ba547e7cd072b495b742840fd2441004173_2_690x387.jpeg" alt="Screenshot from 2022-03-02 11-24-19" data-base62-sha1="9vDO6g3o2kdjN3Q6hz9pdNsrWRJ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42a73ba547e7cd072b495b742840fd2441004173_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/42a73ba547e7cd072b495b742840fd2441004173_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42a73ba547e7cd072b495b742840fd2441004173.jpeg 2x" data-dominant-color="30302E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-03-02 11-24-19</span><span class="informations">1366×768 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2022-03-02 12:19 UTC)

<p>That is a known issue with Slicer stable 4.11.20210226 on the Linux platform specifically.</p>
<p>You can use latest Slicer Preview as mentioned here:</p>
<aside class="quote" data-post="3" data-topic="20501">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/error-loading-gpa-module-slicermorph/20501/3">Error loading GPA module (Slicermorph)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This was resolved in <a href="https://github.com/Slicer/Slicer/commit/fef09b54bd55a5b6bd5870f6f05cde988f8691e3" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix import of python modules on Linux selectively stripping libr… · Slicer/Slicer@fef09b5 · GitHub</a>. It shouldn’t be a problem if you use latest Slicer Preview as that commit came a few days after the latest Stable release back in February.
  </blockquote>
</aside>

<p>You can also uninstall and install Scipy again as mentioned here:</p>
<aside class="quote" data-post="2" data-topic="20501">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/error-loading-gpa-module-slicermorph/20501/2">Error loading GPA module (Slicermorph)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have seen this error, not sure why it happens,as we do not install scipy. But this should fix: 

Open a fresh slicer,
go to python window and type
pip_uninstall("scipy")
pip_install("scipy")
restart your slicer and try gpa again.
  </blockquote>
</aside>


---

## Post #3 by @jamesobutler (2022-03-02 12:25 UTC)

<p>And it appears you have already posted about issue with Scipy on Linux before so you should be in good shape to use the same solution as you did before.</p>
<aside class="quote" data-post="1" data-topic="20953">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michel_atieh/48/11133_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/opendose-3d-extension/20953">OpenDose 3D Extension</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hello, I have installed the extension OpenDose3D. On windows it has all the features, however, on ubuntu there were missing features. I was able to solve the problem by updating the scipy library thorugh the Python interactor by typing pip_install(‘scipy -U’). 
Just to let you know that there is this problem. 
Thank you and kind regards.
  </blockquote>
</aside>


---

## Post #4 by @Michel_Atieh (2022-03-02 13:13 UTC)

<p>Hello James, thank you for your answer. I had forgotten the issue of scipy with this version of Slicer. The problem was resolved by uninstalling and installing the scipy library.<br>
Have a nice day.</p>

---
