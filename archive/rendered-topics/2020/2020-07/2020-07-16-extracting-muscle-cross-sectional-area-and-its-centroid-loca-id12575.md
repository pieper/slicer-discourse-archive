---
topic_id: 12575
title: "Extracting Muscle Cross Sectional Area And Its Centroid Loca"
date: 2020-07-16
url: https://discourse.slicer.org/t/12575
---

# Extracting muscle cross-sectional area and its centroid locatation from MRI/CT scans

**Topic ID**: 12575
**Date**: 2020-07-16
**URL**: https://discourse.slicer.org/t/extracting-muscle-cross-sectional-area-and-its-centroid-locatation-from-mri-ct-scans/12575

---

## Post #1 by @StefSchmidPhD (2020-07-16 12:53 UTC)

<p>Hi everyone</p>
<p>I’m looking for a simple option to extract paraspinal muscle cross-sectional area (CSA) and its centroid location from MRI/CT scans (horizontal vertebral mid-planes). Is there already a feature/an extension available for this?</p>
<p>Thanks a lot and all the best<br>
-Stefan</p>

---

## Post #2 by @lassoan (2020-07-16 13:25 UTC)

<p>You can segment muscles using Segment Editor module and then use “Segment Cross-Section Area” module (provided by “Sandbox” extension in “Examples” category in Extension manager):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="G8wZl9mLWtU" data-video-title="Cross-sectional area computation in segmented image" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=G8wZl9mLWtU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/G8wZl9mLWtU/maxresdefault.jpg" title="Cross-sectional area computation in segmented image" width="" height="">
  </a>
</div>


---

## Post #3 by @StefSchmidPhD (2020-07-16 14:08 UTC)

<p>Hi Andras</p>
<p>Thank you very much for your reply!</p>
<p>I installed the Sandbox Extension…<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/699cc2a279b9d322c3d5520e3c1bcff71a9dcda5.png" alt="grafik" data-base62-sha1="f4hZuniNf6xWBC8l7GBtmoz7dad" width="434" height="126"></p>
<p>…and restarted the program, but cannot find the “Segment Cross-Section Area” module as indicated in the YouTube video:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01b68d0bacb40280f6433f84ccf6fcd767f8127b.png" data-download-href="/uploads/short-url/f9AEb02ZPXusys6Kg1UAyQlQGD.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01b68d0bacb40280f6433f84ccf6fcd767f8127b_2_589x499.png" alt="grafik" data-base62-sha1="f9AEb02ZPXusys6Kg1UAyQlQGD" width="589" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01b68d0bacb40280f6433f84ccf6fcd767f8127b_2_589x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01b68d0bacb40280f6433f84ccf6fcd767f8127b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01b68d0bacb40280f6433f84ccf6fcd767f8127b.png 2x" data-dominant-color="C9CBCC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">832×706 97.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Am I missing something?</p>
<p>Thanks and best<br>
-Stefan</p>

---

## Post #4 by @lassoan (2020-07-16 14:55 UTC)

<p>This feature was added to Sandbox extension not too long ago and so it is only available for recent Slicer Preview Releases.</p>

---

## Post #5 by @StefSchmidPhD (2020-07-16 15:25 UTC)

<p>Ok thanks! I installed the latest version and can see it now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @muratmaga (2020-07-16 20:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="12575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>then use “Segment Cross-Section Area”</p>
</blockquote>
</aside>
<p>I have a follow-up question on this. I am writing a tutorial for this, and I am wondering if the requirement is that we should have isotropic data for correct estimation. Here is why I am asking this:</p>
<p>If I paint a 10mm diameter circle on the MRhead and calculate the area I get 243mm2, which is incorrect. If I resample the MRhead to be isotropic via CropVolume and paint the same area with the same diameter in a new segmentation, I get 309mm2 which is within measurement error. You get approximately 243mm2, if you scale the correct measurement by the slice spacing (1.3mm) which is different from XY spacing (1mm) in this dataset.</p>
<p>I attached the screenshots of the both segments (red from isotropic MRhead, and yellow is the original data).</p>
<p>I also suggest replacing row, column, and slice wording with the usual axial, coronal, sagittal.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bfe1ce112aef43e09549fb153d88debce99166d.png" alt="image" data-base62-sha1="8yIBvo2QDH0jWbo9mQ0HPYNhrMp" width="333" height="351"></p>

---

## Post #7 by @lassoan (2020-07-17 05:43 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="12575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I have a follow-up question on this. I am writing a tutorial for this, and I am wondering if the requirement is that we should have isotropic data for correct estimation</p>
</blockquote>
</aside>
<p>Good catch. Isotropic spacing was not a requirement at all, this was just a bug that the automatic test did not reveal as it only checked computation along one axis. The issue is <a href="https://github.com/PerkLab/SlicerSandbox/commit/a6353e3cad4ba4df9c9a43d4d23f6b7173fc6d78">fixed</a> now.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="12575">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I also suggest replacing row, column, and slice wording with the usual axial, coronal, sagittal.</p>
</blockquote>
</aside>
<p>Measurement currently does not happen along anatomical axis but along an image IJK axis, so we cannot use anatomical terms. Row, column, slice can be mapped to any anatomical axis or oblique directions. We could change the axis names from row, column, slice to I, J, K but I don’t think it would be much better.</p>
<p>Measuring along anatomical axes would require resampling of the volume along the chosen axis. I’ve added an issue to keep track of this idea: <a href="https://github.com/PerkLab/SlicerSandbox/issues/6" class="inline-onebox">Add Cross-sectional area measurement computation along any physical axis · Issue #6 · PerkLab/SlicerSandbox · GitHub</a>.</p>

---

## Post #8 by @StefSchmidPhD (2020-07-17 09:16 UTC)

<p>Hi Andras</p>
<p>Another follow-up question just to make sure… Do the values in column B in the CSA output table (see below) represent the location of the centroid of the respective CSA?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c965387b2473beee42ca59cb3ebd9c1db06479c5.jpeg" data-download-href="/uploads/short-url/sJCPOEt52gX2fAb8CnWGp2b234x.jpeg?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c965387b2473beee42ca59cb3ebd9c1db06479c5_2_190x500.jpeg" alt="grafik" data-base62-sha1="sJCPOEt52gX2fAb8CnWGp2b234x" width="190" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c965387b2473beee42ca59cb3ebd9c1db06479c5_2_190x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c965387b2473beee42ca59cb3ebd9c1db06479c5_2_285x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c965387b2473beee42ca59cb3ebd9c1db06479c5_2_380x1000.jpeg 2x" data-dominant-color="737270"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">500×1310 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks and best<br>
-Stefan</p>

---

## Post #9 by @StefSchmidPhD (2020-07-17 13:53 UTC)

<p>Actually I just realized that these values do not represent the centroids of the CSAs. Is it possible to get those somehow out?</p>

---

## Post #10 by @lassoan (2020-07-17 14:49 UTC)

<p>You can hover the moues pointer over any column and wait for a few seconds without moving it then a tooltip appears that tells what that column contains. “Position” column contain slice center positions in RAS coordinate system.</p>
<p>You can get detailed statistics about each segment, such as centroid, oriented bounding box, etc. using Segment Statistics module.</p>

---

## Post #11 by @StefSchmidPhD (2020-07-17 15:08 UTC)

<p>Perfect! Again, thanks so much Andras!</p>

---
