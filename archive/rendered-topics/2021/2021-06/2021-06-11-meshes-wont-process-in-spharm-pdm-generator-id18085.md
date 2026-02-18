# Meshes won't process in SPHARM-PDM Generator

**Topic ID**: 18085
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/meshes-wont-process-in-spharm-pdm-generator/18085

---

## Post #1 by @quan (2021-06-11 21:47 UTC)

<p>Hi!! I’m trying to run a few meshes through the SPHARM-PDM generator. My process is as follow:</p>
<ol>
<li>Import .stl files</li>
<li>Convert .stl to binary label map .nrrd</li>
<li>Input the .nrrd into the SPHARM-PDM generator pipeline</li>
<li>Change some settings (Subdivision level and SPHARM deg)</li>
<li>Run<br>
While this process works for some meshes, others just run for a long time without finishing. I have cells run for more than 5 hours with no result.</li>
</ol>
<p>The pipeline generates 3 output folders for each corresponding step: Post Processed Segmentation, Generate Mesh Parameters, and Parameters to SPHARM Mesh. I’ve observed that the folder gets filled out in the order of the step finishing. I think the software might be stuck on the “Post Processed Segmentation” step since this folder is empty for all non-working cells.</p>
<p>The meshes that cannot be processed seem to have a Y-shape or very complicated structure, seen below.</p>
<p>Any help is great! Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a19da3b934370be2b6539d5a7b9ab15b878f5b8.png" data-download-href="/uploads/short-url/1rma7Zu5rASioNKHlYTwlivVl56.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a19da3b934370be2b6539d5a7b9ab15b878f5b8_2_690x304.png" alt="image" data-base62-sha1="1rma7Zu5rASioNKHlYTwlivVl56" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0a19da3b934370be2b6539d5a7b9ab15b878f5b8_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a19da3b934370be2b6539d5a7b9ab15b878f5b8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a19da3b934370be2b6539d5a7b9ab15b878f5b8.png 2x" data-dominant-color="F9F9F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×351 28.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2b17dd194cba30520946bcfc562f48a3666cf3.png" data-download-href="/uploads/short-url/oqdYoYwg1BaJbHAqryAuOjsHa9l.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab2b17dd194cba30520946bcfc562f48a3666cf3_2_690x304.png" alt="image" data-base62-sha1="oqdYoYwg1BaJbHAqryAuOjsHa9l" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab2b17dd194cba30520946bcfc562f48a3666cf3_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2b17dd194cba30520946bcfc562f48a3666cf3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2b17dd194cba30520946bcfc562f48a3666cf3.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">795×351 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7dc05cadfeaf5c3c9149f0bcc716a67a84759e.png" data-download-href="/uploads/short-url/8lr75Wfx6aoNhJEFAFyAHisFkui.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a7dc05cadfeaf5c3c9149f0bcc716a67a84759e_2_690x304.png" alt="image" data-base62-sha1="8lr75Wfx6aoNhJEFAFyAHisFkui" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a7dc05cadfeaf5c3c9149f0bcc716a67a84759e_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7dc05cadfeaf5c3c9149f0bcc716a67a84759e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7dc05cadfeaf5c3c9149f0bcc716a67a84759e.png 2x" data-dominant-color="F0F0EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×351 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
