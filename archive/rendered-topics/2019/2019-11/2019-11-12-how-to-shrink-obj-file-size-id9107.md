# How to shrink OBJ file size?

**Topic ID**: 9107
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/how-to-shrink-obj-file-size/9107

---

## Post #1 by @Coloradoultrasound (2019-11-12 00:11 UTC)

<p>Hello, I am trying to figure out how to reduce file size of an OBJ from the segment editor. Is there a way to easily do this?</p>

---

## Post #2 by @lassoan (2019-11-12 00:44 UTC)

<p>Mesh decimation is available in Segment Editor - see detailed instructions <a href="https://discourse.slicer.org/t/size-of-stl-obj-files-too-many-triangles/5137/2">here</a>.</p>

---

## Post #3 by @Coloradoultrasound (2019-11-12 23:40 UTC)

<p>Hello, is there a way to trim or edit the volume before using threshold to paint it? I’d like to be able to trim the volume before painting to improve clarity? It would be nice to be able to remove some of the noise beforehand. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58757772bfd6d198add8ad98eef7c9ed4401f6a.png" data-download-href="/uploads/short-url/nCkKy4b48Eq2657htEQTDFSv1fY.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a58757772bfd6d198add8ad98eef7c9ed4401f6a_2_690x422.png" alt="Picture1" data-base62-sha1="nCkKy4b48Eq2657htEQTDFSv1fY" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a58757772bfd6d198add8ad98eef7c9ed4401f6a_2_690x422.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58757772bfd6d198add8ad98eef7c9ed4401f6a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a58757772bfd6d198add8ad98eef7c9ed4401f6a.png 2x" data-dominant-color="8A8E90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">974×597 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Coloradoultrasound (2019-11-12 23:41 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c9c902113bfd3df0e6eafc8ca3bb479d26f83da.png" data-download-href="/uploads/short-url/aVJIN4O1amsFdW8IRnhJMjL51km.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c9c902113bfd3df0e6eafc8ca3bb479d26f83da_2_530x500.png" alt="Picture1" data-base62-sha1="aVJIN4O1amsFdW8IRnhJMjL51km" width="530" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c9c902113bfd3df0e6eafc8ca3bb479d26f83da_2_530x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c9c902113bfd3df0e6eafc8ca3bb479d26f83da_2_795x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c9c902113bfd3df0e6eafc8ca3bb479d26f83da.png 2x" data-dominant-color="4A484E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">974×918 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Coloradoultrasound (2019-11-13 19:34 UTC)

<p>Hello again,</p>
<p>I am also running into an issue where using the scissors to cut the segment are not cutting out the small particles as shown here. Why would there be any particles remaining after Erasing all outside?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a047d07c39daa1c6dd4aca8125eca844a67bff4.png" data-download-href="/uploads/short-url/lYv96iPX5sAN6WppDQsA88HHqxS.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a047d07c39daa1c6dd4aca8125eca844a67bff4_2_690x383.png" alt="Picture1" data-base62-sha1="lYv96iPX5sAN6WppDQsA88HHqxS" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a047d07c39daa1c6dd4aca8125eca844a67bff4_2_690x383.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a047d07c39daa1c6dd4aca8125eca844a67bff4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a047d07c39daa1c6dd4aca8125eca844a67bff4.png 2x" data-dominant-color="898D8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">974×541 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Sunderlandkyl (2019-11-13 21:21 UTC)

<p>You can trim the volume beforehand using the “Crop Volume” module.</p>
<p>Probably the reason there are small particles is that they are outside the editable intensity range. Try unchecking the editable intensity range in the masking options.</p>

---
