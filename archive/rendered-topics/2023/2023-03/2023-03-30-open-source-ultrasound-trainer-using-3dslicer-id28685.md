# Open-Source Ultrasound Trainer using 3DSlicer

**Topic ID**: 28685
**Date**: 2023-03-30
**URL**: https://discourse.slicer.org/t/open-source-ultrasound-trainer-using-3dslicer/28685

---

## Post #1 by @Ryan_Morrison (2023-03-30 18:37 UTC)

<p>I wanted to thank Andras Lasso for <a href="https://discourse.slicer.org/t/3d-view-lag-when-hundreds-of-models-loaded-and-openigtlinkif-running/12792">his help</a> during the development of an open-source ultrasound trainer (OSUT) for medical professionals learning ultrasound. The ultrasound trainer takes tracking data from many off-the-shelf hardware trackers and displays a virtual ultrasound transducer and 3D anatomical model at the exact location of the real ultrasound transducer in relation to the patient. We ran a randomized control trial on the device that showed it improved accuracy and speed of first year medical students learning ultrasound.</p>
<p>Full paper is available here: <a href="https://pubmed.ncbi.nlm.nih.gov/36395521/" rel="noopener nofollow ugc">https://pubmed.ncbi.nlm.nih.gov/36395521/</a></p>
<p>All source files to replicate the project are here: <a href="https://mega.nz/folder/bb4jlZqK#mI52C3hrYozXgshM0mu86A" rel="noopener nofollow ugc">https://mega.nz/folder/bb4jlZqK#mI52C3hrYozXgshM0mu86A</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e468bda44efff4861b6a16c23ea3fc154287538.jpeg" data-download-href="/uploads/short-url/baso1kMX37shwJcXzWTnpDMnUOk.jpeg?dl=1" title="Figure 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e468bda44efff4861b6a16c23ea3fc154287538.jpeg" alt="Figure 1" data-base62-sha1="baso1kMX37shwJcXzWTnpDMnUOk" width="690" height="390" data-dominant-color="A7A9AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure 1</span><span class="informations">1811×1025 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c288e3ba906717f185dbd17fa5ca4b76fab6a0b6.jpeg" data-download-href="/uploads/short-url/rKVUEGarYqYkuvbqto4b8OSiw4K.jpeg?dl=1" title="Figure 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c288e3ba906717f185dbd17fa5ca4b76fab6a0b6.jpeg" alt="Figure 2" data-base62-sha1="rKVUEGarYqYkuvbqto4b8OSiw4K" width="690" height="390" data-dominant-color="9B938C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure 2</span><span class="informations">1700×962 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342081783258f1f76e73e21a9445e88c57411361.jpeg" data-download-href="/uploads/short-url/7r8tfb7dR21gtxH1ouNpY2F7NRL.jpeg?dl=1" title="Figure 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342081783258f1f76e73e21a9445e88c57411361.jpeg" alt="Figure 3" data-base62-sha1="7r8tfb7dR21gtxH1ouNpY2F7NRL" width="690" height="390" data-dominant-color="857E79"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure 3</span><span class="informations">1707×966 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/166bc4bf69ea8b57c379eb34ddd8bda005c45e83.jpeg" data-download-href="/uploads/short-url/3cloDAbadvjXrZFU7XvEwY6rUeT.jpeg?dl=1" title="Figure 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/166bc4bf69ea8b57c379eb34ddd8bda005c45e83.jpeg" alt="Figure 4" data-base62-sha1="3cloDAbadvjXrZFU7XvEwY6rUeT" width="690" height="388" data-dominant-color="89827C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure 4</span><span class="informations">1700×956 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-30 19:29 UTC)

<p>Very nice work, thanks a lot for sharing!</p>
<p>Did you need to write any custom software for this or you could build the system from existing components by assembly and calibrations/registrations?</p>
<p>How did you register the 3D model to the live patient? Using rigid registration based on anatomical landmarks?</p>

---

## Post #3 by @Ryan_Morrison (2023-03-30 19:54 UTC)

<p>Thank you for all your work in contributing to this amazing community!</p>
<p>No custom software was written. We utilized <a href="https://plustoolkit.github.io/" rel="noopener nofollow ugc">PLUS toolkit</a> and <a href="http://openigtlink.org/" rel="noopener nofollow ugc">OpenIGTLink</a> to import the tracking data to 3DSlicer from a <a href="https://www.ndigital.com/electromagnetic-tracking-technology/3d-guidance/" rel="noopener nofollow ugc">NDI TrakStar electromagnetic tracker</a>.</p>
<p>For registration of the 3D model to the patient, we applied a linear transform (Transforms → Create New Linear Transform) to the virtual ultrasound transducer. We would place the real ultrasound transducer over an area of interest on the patient (for example the heart) and adjust the linear transform so that the virtual ultrasound transducer was correctly placed on the 3D model. While this way of registering the 3D model to the live patient wasn’t perfect, it worked well in this initial application.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bb4876e9635fb74dbf89a2059aeef4e0ec758ec.png" data-download-href="/uploads/short-url/d5gelNhZHwoItp6XnXiP4eo4ryA.png?dl=1" title="Screen Shot 2023-03-30 at 3.50.38 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bb4876e9635fb74dbf89a2059aeef4e0ec758ec.png" alt="Screen Shot 2023-03-30 at 3.50.38 PM" data-base62-sha1="d5gelNhZHwoItp6XnXiP4eo4ryA" width="379" height="500" data-dominant-color="373738"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-30 at 3.50.38 PM</span><span class="informations">958×1262 75.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0376bc3aa2638a15eb3d52cdf9e3f27ec7fbb8c.jpeg" data-download-href="/uploads/short-url/mRl8jyiu57REAr1xz4PCd1ybSIA.jpeg?dl=1" title="Screen Shot 2023-03-30 at 3.43.52 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0376bc3aa2638a15eb3d52cdf9e3f27ec7fbb8c.jpeg" alt="Screen Shot 2023-03-30 at 3.43.52 PM" data-base62-sha1="mRl8jyiu57REAr1xz4PCd1ybSIA" width="690" height="346" data-dominant-color="D6C4C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-03-30 at 3.43.52 PM</span><span class="informations">1920×963 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
