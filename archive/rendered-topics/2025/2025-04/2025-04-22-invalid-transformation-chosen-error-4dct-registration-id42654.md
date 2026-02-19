---
topic_id: 42654
title: "Invalid Transformation Chosen Error 4Dct Registration"
date: 2025-04-22
url: https://discourse.slicer.org/t/42654
---

# Invalid transformation chosen error - 4DCT registration

**Topic ID**: 42654
**Date**: 2025-04-22
**URL**: https://discourse.slicer.org/t/invalid-transformation-chosen-error-4dct-registration/42654

---

## Post #1 by @Cesar (2025-04-22 20:43 UTC)

<p>Any insights into why I’m getting this error (please see image below)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c40ed52e2ad589c021b293bac0f19f17d2e55041.jpeg" data-download-href="/uploads/short-url/rYpmw8bjtaSxamTPsp0urQHx8hr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c40ed52e2ad589c021b293bac0f19f17d2e55041_2_690x274.jpeg" alt="image" data-base62-sha1="rYpmw8bjtaSxamTPsp0urQHx8hr" width="690" height="274" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c40ed52e2ad589c021b293bac0f19f17d2e55041_2_690x274.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c40ed52e2ad589c021b293bac0f19f17d2e55041_2_1035x411.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c40ed52e2ad589c021b293bac0f19f17d2e55041_2_1380x548.jpeg 2x" data-dominant-color="4F4F58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×763 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here’s what I’ve tried and how I managed to bypass it. FYI this dataset has some motion artifact, and part of the distal radius is not visible.</p>
<ol>
<li>I placed all the models (radius, capitate, and lunate) inside the radius, and ran Hierarchical3DRegistration. It only registered the first two frames</li>
<li>I also tried placing all models inside the capitate and the lunate. In all cases, the registration only worked for the first two frames.</li>
<li>I was able to by pass the issue by not nesting any models inside others and instead registering each frame at a time.</li>
</ol>
<p>Any thoughts or suggestions would be appreciated!</p>

---

## Post #2 by @Amy_Morton (2025-08-29 15:32 UTC)

<p>Hey <a class="mention" href="/u/cesar">@Cesar</a></p>
<p>I know you know about the enhancements that were merged into 3DH to correct for this.. would you mind adding some updates to share with the community/category?</p>
<p>Thank-you!</p>

---

## Post #3 by @Cesar (2025-09-02 13:59 UTC)

<p>Hierarchical3DRegistration is doing a great job registering all bones together! Here’s what I did:</p>
<ol>
<li>
<p>Nested all bones inside the radius</p>
</li>
<li>
<p>Initialized registration by adjusting the volume rendering of the sequence for better visualization.</p>
</li>
<li>
<p>Set the initial guess and registered all bones</p>
</li>
</ol>
<p>The video below shows all the steps to register the first frame</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/350a371a6fdc494a924bafc1250fa71e1f75e0d9.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2f031a1b44711d7a117452750a594dcbdb168c8.jpeg" data-video-base62-sha1="7zdbU2WCV85Y02GRRwuBRDcFXiV.mp4">
  </div><p></p>

---
