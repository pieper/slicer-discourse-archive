# How to view multiple volumes in sagittal slice viewer

**Topic ID**: 39530
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/how-to-view-multiple-volumes-in-sagittal-slice-viewer/39530

---

## Post #1 by @gazeofthespark (2024-10-03 19:15 UTC)

<p>The volumes and segmentations I am working with provide a limited, localized perspective of the data when viewed one at a time. I need to be able load multiple, adjacent volumes with corresponding segmentations, and then inspect the <em>greyscale volume data</em> underneath the coloured segmentations, in the sagittal slice viewer.</p>
<p>Hopefully these images will clarify my goal:</p>
<ol>
<li>
<p>Here I have 7 segmentation mask files, and one “active” volume (the greyscale underneath) in the sagittal slice viewer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f.png" data-download-href="/uploads/short-url/bXrr2AwPdfUsO3d7CUTg8xovbeD.png?dl=1" title="Slicer_help" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_510x500.png" alt="Slicer_help" data-base62-sha1="bXrr2AwPdfUsO3d7CUTg8xovbeD" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_765x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d01417f6747efc4b8710effe397dd3384ec71f_2_1020x1000.png 2x" data-dominant-color="24221B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_help</span><span class="informations">1183×1159 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Here I’ve hidden the 5th segmentation mask to inspect the greyscale volume underneath:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932.png" data-download-href="/uploads/short-url/m4aTdeFqjSKYhgf13OBlEUgRJDQ.png?dl=1" title="Slicer_help2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_510x500.png" alt="Slicer_help2" data-base62-sha1="m4aTdeFqjSKYhgf13OBlEUgRJDQ" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_510x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_765x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9aa8a9e18686390b3e75a541b1f68b4e10916932_2_1020x1000.png 2x" data-dominant-color="24221D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_help2</span><span class="informations">1183×1159 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>To effectively  visualize the changes in the segmentation masks across a broader spatial context, I need to be able to see all 7 of the corresponding greyscale volumes at the same time as I scrub through the slice.</p>
<p>My understanding is that only one volume file can be actively displayed at a time due to the way the software manages rendering.</p>
<p>Any help is much appreciated.</p>
<p>Operating system: Linux<br>
Slicer version: 5.62</p>

---

## Post #2 by @muratmaga (2024-10-03 19:18 UTC)

<p>One slice view can display only two volume (one foreground and one background). However, you can have different volumes in different viewers. You can switch to layout (3x3 slices), and then load each volume (and segmentation) in a different slices, set them to the same plane and then link them.</p>

---

## Post #3 by @gazeofthespark (2024-10-03 20:15 UTC)

<p>When I change the layout, link slices, and try to scrub through the data only one volume is shown. Am I missing something?</p>
<p>Perhaps I need to approach this in a completely different way?<br>
The goal is to be able to compare the segmentations to the underlying, ground truth data over and increasingly larger area: 9+ volumes. As well as scrub through the changes.<br>
I wonder if rendering multiple volumes into one would work…</p>

---

## Post #4 by @muratmaga (2024-10-03 21:05 UTC)

<p>Disable the visibility of everthing in your scene and then drag and drop the volume/segmentation you want to use into each viewer one by one.</p>

---

## Post #5 by @lassoan (2024-10-03 23:52 UTC)

<p>If you want to browse many non-overlapping volumes then you can stitch them all into a single volume. You can use the <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#stitch-volumes"><code>Stitch Volume</code> module</a> in Sandbox extension for this.</p>

---

## Post #6 by @gazeofthespark (2024-10-04 04:39 UTC)

<p>This looks promising, but when I stitch the volumes together they appear cropped or something…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2e077661cebc885b5641c005bba9e9422b9e405.jpeg" data-download-href="/uploads/short-url/rNXxS2ckEKTyE95XWOfHlbRQMxT.jpeg?dl=1" title="stich_volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2e077661cebc885b5641c005bba9e9422b9e405_2_347x500.jpeg" alt="stich_volume" data-base62-sha1="rNXxS2ckEKTyE95XWOfHlbRQMxT" width="347" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2e077661cebc885b5641c005bba9e9422b9e405_2_347x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2e077661cebc885b5641c005bba9e9422b9e405_2_520x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2e077661cebc885b5641c005bba9e9422b9e405_2_694x1000.jpeg 2x" data-dominant-color="3E3E3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">stich_volume</span><span class="informations">1079×1553 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea how to solve this?</p>

---

## Post #7 by @lassoan (2024-10-17 05:05 UTC)

<p>You can try to stitch just two volumes at a time. If it still does not work as expected then you could share a minimum set of images that can be used to reproduce the behavior and <a class="mention" href="/u/mikebind">@mikebind</a> may be able to have a look at them.</p>

---

## Post #8 by @mikebind (2024-10-17 16:00 UTC)

<p>The current version of StitchVolumes assumes that supplied images are arranged along a single axis and are stitched together along that axis.  The primary imagined use case was for medical imaging where you might have multiple CT or MR images taken at different locations as the scanner bed slides along the bore of the machine along one axis.  What’s happened with your images is that the side-by-side images are competing for which one is shown, and each one wins for half the time, which results in getting the image data from one of them for the top half of the block, and from the other image in the bottom half of the block.</p>
<p>After a few different use cases came up where allowing stitching of arbitrary spatial arrangements of image volumes would be helpful, I reworked my code to allow that and improve the blending options for overlap regions.  Since it was more mature, I had planned to release it as a separate Slicer extension and drop it from the Sandbox module.  However, I didn’t finish getting through all the steps of the extension development checklist to get it really registered before I needed to turn my attention to other projects.</p>
<p>All that to say, there is a fully functioning replacement to StitchVolumes which should handle your use case available at <a href="https://github.com/mikebind/SlicerStitchImageVolumes" class="inline-onebox" rel="noopener nofollow ugc">GitHub - mikebind/SlicerStitchImageVolumes: A 3D Slicer (slicer.org) module for stitching together multiple image volumes into a single larger image volume.</a>, but it is not yet available through the Extension Manager, so you would need to download it and add it to the list of available modules yourself within Slicer (I can walk you through that process if you want to pursue it, it is straightforward but not quite as simple as using the Extension Manger).</p>
<p>Separately, looking at your images, how goes the Vesuvius Challenge? I tried to see if I could advance the scroll segmentation tasks about a year ago, but didn’t end up having enough free time to actually get anywhere.  It’s a fascinating problem though!</p>

---
