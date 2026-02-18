# Strange air pockets in segmentation editor, can't mark air pockets as apart of segmentation.

**Topic ID**: 32640
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/strange-air-pockets-in-segmentation-editor-cant-mark-air-pockets-as-apart-of-segmentation/32640

---

## Post #1 by @GunnarE (2023-11-07 13:30 UTC)

<p>Hi everyone,</p>
<p>I seem to have ran into a bug, when using segmentation editor to segment a head in MRI data, I get these air pockets that are not included in segmentation. The goal is to use this segmentation to construct a model of the head with no open air pockets.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b67cfce2e6f1a267e66e2d6fb1541dce9f92b8a7.png" data-download-href="/uploads/short-url/q2mGstH1Y9Kz4rDHXS9JRnxjVTp.png?dl=1" title="Screenshot 2023-11-06 at 4.11.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b67cfce2e6f1a267e66e2d6fb1541dce9f92b8a7_2_434x500.png" alt="Screenshot 2023-11-06 at 4.11.41 PM" data-base62-sha1="q2mGstH1Y9Kz4rDHXS9JRnxjVTp" width="434" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b67cfce2e6f1a267e66e2d6fb1541dce9f92b8a7_2_434x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b67cfce2e6f1a267e66e2d6fb1541dce9f92b8a7_2_651x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b67cfce2e6f1a267e66e2d6fb1541dce9f92b8a7.png 2x" data-dominant-color="3C4339"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-06 at 4.11.41 PM</span><span class="informations">796×916 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is an image of what I mean, you will se a dark section with no green tent. That is the undesirable air pockets. Desired output is the entire head being added to the segmentation including regions where the air pockets exist.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77f5a48e2a08c4dfda04402e77bb6226e315e81d.jpeg" data-download-href="/uploads/short-url/h7d6AoF0dEt52XZ2KQKW9NINM8l.jpeg?dl=1" title="Screenshot 2023-11-06 at 4.13.21 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77f5a48e2a08c4dfda04402e77bb6226e315e81d_2_494x500.jpeg" alt="Screenshot 2023-11-06 at 4.13.21 PM" data-base62-sha1="h7d6AoF0dEt52XZ2KQKW9NINM8l" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77f5a48e2a08c4dfda04402e77bb6226e315e81d_2_494x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77f5a48e2a08c4dfda04402e77bb6226e315e81d_2_741x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77f5a48e2a08c4dfda04402e77bb6226e315e81d_2_988x1000.jpeg 2x" data-dominant-color="6F8590"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-06 at 4.13.21 PM</span><span class="informations">1316×1330 81.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is a photo of what the segmentation looks like in 3d, As you can see there is indents where these air pockets exist.</p>
<p>I am confused on how to remove these air pockets, anything helps!</p>
<p>Thank you,<br>
Gunnar</p>

---

## Post #2 by @lassoan (2023-11-07 13:32 UTC)

<p>You have selected an intensity range in masking settings that does not include the intensity of air. You can disable “Editable intensity range” checkbox to allow painting everywhere.</p>

---

## Post #3 by @JASON (2023-11-07 18:18 UTC)

<p>Also, If you don’t want to manually paint them in, you can try the Surface Wrap Solidify extension to maintain the surface but fill the cavities<br>
<a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" rel="noopener nofollow ugc">https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify</a></p>

---
