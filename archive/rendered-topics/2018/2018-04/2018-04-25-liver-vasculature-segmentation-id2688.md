---
topic_id: 2688
title: "Liver Vasculature Segmentation"
date: 2018-04-25
url: https://discourse.slicer.org/t/2688
---

# Liver vasculature segmentation

**Topic ID**: 2688
**Date**: 2018-04-25
**URL**: https://discourse.slicer.org/t/liver-vasculature-segmentation/2688

---

## Post #1 by @Serg (2018-04-25 16:37 UTC)

<p>Hello, 3D Slicer team!<br>
We want to use 3D Slicer in a project where it is necessary to make a reconstruction of liver, tumor, and arteries similar to your recent manuscript (<a href="https://www.ncbi.nlm.nih.gov/pubmed/28822820" class="inline-onebox" rel="noopener nofollow ugc">Utility of 3D Reconstruction of 2D Liver Computed Tomography/Magnetic Resonance Images as a Surgical Planning Tool for Residents in Liver Resection Surgery - PubMed</a> ). Unfortunately, the paper doesn’t explain any segmentation and reconstruction steps.<br>
I used high contrast 0.625 mm arterial and venous angio CTs and followed Slicer’s tutorials - Heart segmentation (<a href="https://www.youtube.com/watch?v=BJoIexIvtGo&amp;feature=youtu.be" class="inline-onebox" rel="noopener nofollow ugc">Whole heart segmentation from cardiac CT in 10 minutes - YouTube</a>) and segmentation for 3D printing (<a href="https://discourse.slicer.org/t/new-video-tutorial-for-segment-editor-lumbar-spine-segmentation-for-3d-printing/700" class="inline-onebox">New video tutorial for Segment editor - lumbar spine segmentation for 3D printing</a>). Thanks to tutorials - the liver and tumor were efficiently segmented and reconstructed (liver_SceneView.jpg). However, the segmentation of the vasculature is far away from perfection showing in the manuscript (MasterSceneView.jpg).<br>
Would be possible to explain in steps how you reconstructed vessels from the arterial and venous angio CTs? Did you use SlicerVMTK module? By the way, Slicer 4.8.1 contains extension SlicerVMTK module, but this extension is absent in Slicer 4.9.0 latest nightly build (2018-04-23).<br>
Also, did you use ITK in 3D Slicer to reconstruct liver vasculatures? If so, how ITK was connected to 3D slicer? Via what extension?<br>
Would be possible to create a tutorial video specifically for vessels reconstruction? Or, is it already exist?<br>
Thanks a lot for your help!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddbfe8bfec89d2dafe98ec4ce0d6c3d9a49cc53b.jpeg" data-download-href="/uploads/short-url/vDGGraEet0jvZ7ekxTRIUOT6VKP.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddbfe8bfec89d2dafe98ec4ce0d6c3d9a49cc53b_2_690x492.jpg" alt="image" data-base62-sha1="vDGGraEet0jvZ7ekxTRIUOT6VKP" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddbfe8bfec89d2dafe98ec4ce0d6c3d9a49cc53b_2_690x492.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddbfe8bfec89d2dafe98ec4ce0d6c3d9a49cc53b_2_1035x738.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ddbfe8bfec89d2dafe98ec4ce0d6c3d9a49cc53b_2_1380x984.jpg 2x" data-dominant-color="8A8198"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1726×1233 695 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b717fd7316452e3763bc779a406fc97978c6ca5.jpeg" data-download-href="/uploads/short-url/8tRlcQjA1f8TpNzmEeUkWYOCvWJ.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b717fd7316452e3763bc779a406fc97978c6ca5_2_690x492.jpg" alt="image" data-base62-sha1="8tRlcQjA1f8TpNzmEeUkWYOCvWJ" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b717fd7316452e3763bc779a406fc97978c6ca5_2_690x492.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b717fd7316452e3763bc779a406fc97978c6ca5_2_1035x738.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b717fd7316452e3763bc779a406fc97978c6ca5_2_1380x984.jpg 2x" data-dominant-color="928EAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1726×1233 685 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-05-01 23:39 UTC)

<blockquote>
<p>Would be possible to explain in steps how you reconstructed vessels from the arterial and venous angio CTs?</p>
</blockquote>
<p>It was a mostly manual process, using threshold paint, followed up manual touch-ups and smoothing. In the new Segment editor module there are some more advanced tools (Grow from seeds; Fast marching - in SegmentEditorExtraEffects extension) that may make the process a bit easier.</p>
<blockquote>
<p>Did you use SlicerVMTK module?</p>
</blockquote>
<p>We did not use it (at that time it was not available) but at least the vesselness filtering part might be able to help making vessels more distinguishable from background. I would recommend to <a href="https://groups.google.com/forum/#!forum/vmtk-users">contact VMTK developers directly</a> in asking advice about what VMTK tools may be used for your images.</p>
<blockquote>
<p>By the way, Slicer 4.8.1 contains extension SlicerVMTK module, but this extension is absent in Slicer 4.9.0 latest nightly build (2018-04-23).</p>
</blockquote>
<p>Both Slicer and VMTK has been going through large overhauls recently. Probably it’ll take at least a couple of weeks until we can get back VMTK in the extension manager. Until then you can use Slicer 4.8.1 or use VMTK processing tools directly, outside of Slicer.</p>
<blockquote>
<p>Also, did you use ITK in 3D Slicer to reconstruct liver vasculatures? If so, how ITK was connected to 3D slicer? Via what extension?</p>
</blockquote>
<p>We did not use any ITK filters. You have access to hundreds of ITK filters through Simple Filters module (included in Slicer core).</p>
<blockquote>
<p>Would be possible to create a tutorial video specifically for vessels reconstruction? Or, is it already exist?</p>
</blockquote>
<p>Suitable method for vessel segmentation depends entirely on what vessels in which organ need to be segmented, what imaging modality, imaging protocol, contrast agent are used. If we segment vessels again then we may create a tutorial about how we do it exactly, for that particular study.</p>

---
