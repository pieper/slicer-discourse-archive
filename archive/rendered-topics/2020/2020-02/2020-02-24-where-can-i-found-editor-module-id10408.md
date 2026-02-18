# Where can I found Editor module

**Topic ID**: 10408
**Date**: 2020-02-24
**URL**: https://discourse.slicer.org/t/where-can-i-found-editor-module/10408

---

## Post #1 by @pooyesh (2020-02-24 01:43 UTC)

<p>Hi<br>
I am beginner in 3D Slicer. I want to segment the Brain Corpus callosum and Cerebellum. In training movies I  found the “Editor” models that can be helpful but in latest installed version (4.10.2 r28257) and in extensions ,  I can’t find Editor module to use. Only I can see Segment Editor that seems its function is different to " Editor" model.Please help how to find and integrate “Editor” .<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2020-02-24 01:54 UTC)

<p>We have not removed Editor module yet, but we will move it out from the Slicer core soon. I know that it can be frustrating if you are forced to learn new things but this case the Segment Editor offers so much more than the old Editor that it will worth the retraining time. You can find tutorials <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">on Slicer training page</a> and if you have any specific questions then you can ask them here.</p>

---

## Post #3 by @LearningSlicerYay (2020-02-24 14:39 UTC)

<p>Andras, if it has not been removed from 4.10.2 where can the Editor module be found? I cannot find it either…</p>

---

## Post #4 by @aiden.zhu (2020-02-24 15:01 UTC)

<p>You may search it or click the all modules:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d7641ba14f2d7af8dbc5950bc05861f63c83a42.png" data-download-href="/uploads/short-url/6uaQHHGfWpdKQNWpMlzMbTb3DWy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7641ba14f2d7af8dbc5950bc05861f63c83a42_2_304x500.png" alt="image" data-base62-sha1="6uaQHHGfWpdKQNWpMlzMbTb3DWy" width="304" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7641ba14f2d7af8dbc5950bc05861f63c83a42_2_304x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7641ba14f2d7af8dbc5950bc05861f63c83a42_2_456x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d7641ba14f2d7af8dbc5950bc05861f63c83a42_2_608x1000.png 2x" data-dominant-color="F3F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">689×1133 84.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pooyesh (2020-02-24 21:55 UTC)

<p>I can’t find the Editor in 4.10.2. It  is all modules that I see in this version <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae31e21ac3e1cf6322fb357c1dc2a05af2370edd.jpeg" data-download-href="/uploads/short-url/oQZX9OtKQeiFsXCBdmn2295vuYB.jpeg?dl=1" title="a" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae31e21ac3e1cf6322fb357c1dc2a05af2370edd_2_684x500.jpeg" alt="a" data-base62-sha1="oQZX9OtKQeiFsXCBdmn2295vuYB" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae31e21ac3e1cf6322fb357c1dc2a05af2370edd_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae31e21ac3e1cf6322fb357c1dc2a05af2370edd_2_1026x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae31e21ac3e1cf6322fb357c1dc2a05af2370edd.jpeg 2x" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a</span><span class="informations">1207×882 348 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @aiden.zhu (2020-02-24 21:59 UTC)

<p>try to update to a newer version.</p>
<p>my version is 4.11.0 2019-06-23 nightly.</p>
<p>good luck.</p>

---

## Post #7 by @pieper (2020-02-24 22:10 UTC)

<p>The Editor module is in my windows 4.10.2 installation.  Doublecheck that it’s enabled in the module settings (see screenshot below) and also check the error log for clues (look under Help-&gt;Report a bug).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d67a37d947fa9e77587989b73a23539c7420366.jpeg" data-download-href="/uploads/short-url/8LdazcHs1Axdf8kSLPUbu66b78i.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d67a37d947fa9e77587989b73a23539c7420366_2_646x500.jpeg" alt="image" data-base62-sha1="8LdazcHs1Axdf8kSLPUbu66b78i" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d67a37d947fa9e77587989b73a23539c7420366_2_646x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3d67a37d947fa9e77587989b73a23539c7420366_2_969x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d67a37d947fa9e77587989b73a23539c7420366.jpeg 2x" data-dominant-color="EAEAEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">993×768 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @pooyesh (2020-02-25 16:20 UTC)

<p>Thank you Aidin<br>
I downloaded and saw the Editor but unfortunately the program stops after Dicom image importing! with this release.</p>

---

## Post #9 by @pooyesh (2020-02-25 16:22 UTC)

<p>Thanks, but I can’t still see Editor in this version.</p>

---

## Post #10 by @lassoan (2020-02-25 16:26 UTC)

<p>Editor module is not supported anymore (it was deprecated several years ago). Please use Segment Editor instead and let us know if you run into any problems or if you have any questions.</p>

---
