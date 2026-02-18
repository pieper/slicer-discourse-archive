# Do you know how to exactly extract brain tumor using NVIDIA module?

**Topic ID**: 24153
**Date**: 2022-07-02
**URL**: https://discourse.slicer.org/t/do-you-know-how-to-exactly-extract-brain-tumor-using-nvidia-module/24153

---

## Post #1 by @platanus (2022-07-02 07:48 UTC)

<p>Hello. All members of 3D-Slicer</p>
<p>I have a question regarding NVIDIA module.</p>
<p>I’m extracting brain tumor using NVIDIA AIAA effect in Segment Editor module.</p>
<p>When I used sample DICOM data of brain tumor provided in 3d-slicer, brain tumor extracted well as following options.</p>
<ol>
<li>Auto-Segmentation</li>
<li>Segment from boundary pint(DExtr3D)<br>
But I didn’t deal with option of DeepGrow because I don’t know how to use DeepGrow option.</li>
</ol>
<p>Unfortunately,  when I used option of Auto-Segmentation and Segment from boundary point(DExtr3D) in NVIDIA AIAA effect in Segment Editor module with real clinical dicom, brain tumor didn’t extract well such as bottom image. It only extracted the part of tumor.</p>
<p>First image is to use option of Auto-Segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4747eb1c8d593655a1f8394be019be18bc792f7.png" data-download-href="/uploads/short-url/pKnx68fQQUXmpbjriRuYmNM6OoL.png?dl=1" title="problem of auto_tumor_boundary_point" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4747eb1c8d593655a1f8394be019be18bc792f7_2_690x374.png" alt="problem of auto_tumor_boundary_point" data-base62-sha1="pKnx68fQQUXmpbjriRuYmNM6OoL" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4747eb1c8d593655a1f8394be019be18bc792f7_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4747eb1c8d593655a1f8394be019be18bc792f7_2_1035x561.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4747eb1c8d593655a1f8394be019be18bc792f7.png 2x" data-dominant-color="5E656C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem of auto_tumor_boundary_point</span><span class="informations">1071×581 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Second image is to use option of Segment from boundary point(DExtr3D).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/763ccad7a49050cdcff8b2bf5f6e05ae54026e44.png" data-download-href="/uploads/short-url/gRYAuiOFTkEwYEFfUhot7s0jbc8.png?dl=1" title="problem of tumor_boundary_point" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763ccad7a49050cdcff8b2bf5f6e05ae54026e44_2_689x328.png" alt="problem of tumor_boundary_point" data-base62-sha1="gRYAuiOFTkEwYEFfUhot7s0jbc8" width="689" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763ccad7a49050cdcff8b2bf5f6e05ae54026e44_2_689x328.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/763ccad7a49050cdcff8b2bf5f6e05ae54026e44_2_1033x492.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/763ccad7a49050cdcff8b2bf5f6e05ae54026e44.png 2x" data-dominant-color="575957"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem of tumor_boundary_point</span><span class="informations">1374×655 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’d like to exactly extract whole of tumor, but It is not easy.</p>
<p>May I add a number of boundary point(more 4 boundary points)?</p>
<p>Let me know how to exactly extract whole of brain tumor using option of Auto-Segmentation and Segment from boundary point(DExtr3D) in NVIDIA AIAA effect in Segment Editor module.</p>
<p>If there is different solution regarding extraction of whole of tumor, let me know that too.</p>
<p>Thank you for reading my question.</p>

---

## Post #2 by @pieper (2022-07-02 14:30 UTC)

<p>It’s expected that not all cases will work with existing tools as everything is experimental and evolving.  For brain tumors you can look at the <a href="http://braintumorsegmentation.org/">BraTS experience</a> to see the state of the art.  <a href="https://github.com/Project-MONAI/MONAILabel">MONAI Label</a> is also being adapted for brain tumors but there is still work to be done and perhaps you could contribute to progress there.</p>

---

## Post #3 by @lassoan (2022-07-03 00:34 UTC)

<p>The control specify a region of interest, so they need to be slightly (at least a couple of millimeters) away from the tumor. That said, if a tumor looks very different than all the rumors that the model was trained to recognize then it may not be segmented well.</p>
<p>You can use classic semi-automatic segmentation methods, such as <a href="https://youtu.be/cybL5A0w3hw">“Grow from seeds”, to segment the tumor with a few minutes of manual effort</a>.</p>
<p>As <a class="mention" href="/u/pieper">@pieper</a> suggested above, these additional manual/semi-automatic segmentations can be used to train or refine models using MONAILabel.</p>

---

## Post #5 by @platanus (2022-07-05 01:35 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> Thank you for answering my question. I’ll try modeling with reference your answer as you advice me.</p>

---
