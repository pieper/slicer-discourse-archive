---
topic_id: 6692
title: "Exported Stl Files From The Segmentation Has Intersection Pe"
date: 2019-05-04
url: https://discourse.slicer.org/t/6692
---

# Exported STL files from the segmentation has intersection/penetration

**Topic ID**: 6692
**Date**: 2019-05-04
**URL**: https://discourse.slicer.org/t/exported-stl-files-from-the-segmentation-has-intersection-penetration/6692

---

## Post #1 by @Tekk_ya (2019-05-04 07:26 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1</p>
<p>Hi everyone,</p>
<p>I want to create models for mandible and teeth from a CBCT scan. After importing the DICOM file to 3Dslicer and completing the segmentation process I used segmentations/export to export the segmentations as STL models. Then I import those STL files into Meshmixer and I found out the models have intersections! (the surface of the teeth model penetrates the surface of the bone model as you can see in the image). I noticed that 3D Slicer uses the Marching Cube algorithm in order to calculate surface mesh from the label map volume, which might be the reason why the estimated surface of one segment is penetrating the other segment’s surface. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1abc452ec51c279f0b609190b1d8927b11f68be5.jpeg" data-download-href="/uploads/short-url/3OvMrABtQejjXOY4xpwH8USwxal.jpeg?dl=1" title="penetration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1abc452ec51c279f0b609190b1d8927b11f68be5_2_690x367.jpeg" alt="penetration" data-base62-sha1="3OvMrABtQejjXOY4xpwH8USwxal" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1abc452ec51c279f0b609190b1d8927b11f68be5_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1abc452ec51c279f0b609190b1d8927b11f68be5_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1abc452ec51c279f0b609190b1d8927b11f68be5_2_1380x734.jpeg 2x" data-dominant-color="55504F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">penetration</span><span class="informations">1919×1023 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>-I would like to know is there any way to solve this problem and avoiding any penetration in the exporting files?</p>
<ul>
<li>The voxel size of my data is 0.3x0.3x0.3mm. I have tried to create an empty space with 0.5mm width by shrinking the margin of the teeth segment by 0.5mm, and then exporting the models. Hopefully, my models do not have any intersection with the empty space between them. However, I am curious to know whether there is any better way to avoid such intersection problems.</li>
</ul>
<p>Thank you in advance for your help</p>

---

## Post #2 by @lassoan (2019-05-04 11:58 UTC)

<p>You can reduce chance of overlap by applying Smoothing effect with Joint smoothing method, decrease the voxel size (using Crop volume module), and/or reducing the smoothing factor (drop-down in Show 3D button).</p>

---

## Post #3 by @pieper (2019-05-04 14:36 UTC)

<p>Hi <a class="mention" href="/u/tekk_ya">@Tekk_ya</a> - please describe the exact steps you follow in Slicer that leads to this result, ideally reproducible on existing sample data, or if needed on data you can share.</p>

---

## Post #4 by @juday (2019-05-07 16:51 UTC)

<p>For segmentation, did you the old “Editor” module or the new “Segment Editor” module. If you have used the segment editor module, it is lot easier to remove intersections/overlaps using the ‘Logical operators’ tool. You the ‘subtract’ overlap regions of a segment with others.</p>

---

## Post #5 by @Tekk_ya (2019-05-08 08:41 UTC)

<p>Hi Steve,</p>
<p>I segmented the CBCT scan by using “Segment Editor” module as follow:<br>
First, I segmented the teeth by utilizing the threshold tool. Second, I modified the segmented parts by using the paint and erase/scissors tools to segment the teeth perfectly. I also used the “Island” tool to remove the small segments. Then, I segmented the bone by using level tracing without overwriting or modifying the teeth segments. I also tried the “Logical Operator” tool to subtract any possible overlapping and to avoid any intersection in the exported models. However, the problem is not in the segments that i have and they are completely separate and there isn’t any overlap between them but after exporting them as STL models I face intersection problem.</p>
<p>Could you suggest any faster method to segment the teeth from the bone? is there any extension in 3D Slicer that I can use for this type of segmentation? I have tried to go through the 3D slicer tutorials but unfortunately, none of them works for segmenting the teeth from the bone. (It is hard to segment the teeth from the outer part of the mandible as the bone is denser in those areas and the intensity of the bone is close to the intensity of the teeth which makes it difficult to segment them with automatic or semi-automatic tools.)</p>
<p>I would really happy to receive any suggestions for a better and more efficient way of segmenting the bone and the teeth since I am planning to segment many scans using Python scripts if possible.</p>

---

## Post #6 by @Tekk_ya (2019-05-08 08:46 UTC)

<p>Hi,</p>
<p>Thank you for your reply. I have tried that tool and found it really useful. but even after subtracting the segments still, I have the same problem.</p>

---

## Post #7 by @Tekk_ya (2019-05-08 09:32 UTC)

<p>Hi Andras,</p>
<p>Thank you for your reply. Increasing the resolution of the CBCT scan by applying the B-spline method did not help me (maybe because I am not re-segmenting the scan and I just want to export the segments that I have in a such way that they don’t have intersection)</p>
<p>I solved the intersection problem by resampling the labelmap geometry in “Segmenter Editor”. I tried to “oversample” the space by a factor of 4. It solved the intersection problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/167a5144aeae4f0121b72f09b7a311127983a171.png" data-download-href="/uploads/short-url/3cQzeuHItBMjViTMtdfVYWXnQyJ.png?dl=1" title="orig_data_resampeling" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/167a5144aeae4f0121b72f09b7a311127983a171_2_353x500.png" alt="orig_data_resampeling" data-base62-sha1="3cQzeuHItBMjViTMtdfVYWXnQyJ" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/167a5144aeae4f0121b72f09b7a311127983a171_2_353x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/167a5144aeae4f0121b72f09b7a311127983a171_2_529x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/167a5144aeae4f0121b72f09b7a311127983a171_2_706x1000.png 2x" data-dominant-color="E3E5E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">orig_data_resampeling</span><span class="informations">725×1025 68.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I wonder the reason behind this! Would you explain it based on the 3Dslicers code related to this function? or share a link related to the source code of this function. Would you explain to me how it affects the exported files? Does it increase the resolution of the labelmap and consequently the marching cube method can estimate the surface triangles more accurately?</p>
<p>Please correct me if I am wrong.</p>
<p>Best</p>

---

## Post #8 by @lassoan (2019-05-08 12:43 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="7" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>Does it increase the resolution of the labelmap and consequently the marching cube method can estimate the surface triangles more accurately?</p>
</blockquote>
</aside>
<p>Exactly. Labelmap voxels are rectangular prisms while surface mesh is a smooth surface, so a smoothing operation is needed, which may introduce gaps or overlaps the size of a fraction of a voxel. If the voxel is too large enough then this fraction of a voxel difference may matter.</p>

---

## Post #9 by @pieper (2019-05-08 14:50 UTC)

<p><a class="mention" href="/u/tekk_ya">@Tekk_ya</a> you might try a slightly different pathway to get “watertight” models.</p>
<ul>
<li>export the segmentation to a label map</li>
<li>run the ModelMaker module with the “Joint Smoothing” operation enabled</li>
</ul>
<p>what this will do is apply the same smoothing operation to matching vertices from the different segments so that no gaps are introduced.  In the example below the yellow/green surfaces use the default and the red/blue use Joint Smoothing.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I don’t see that the segmentation closed surface option exposes the same version of Joint Smoothing.  The one in ModelMaker was specifically designed by <a class="mention" href="/u/lorensen">@Lorensen</a> to generate watertight models for 3D printing.</p>
<p>HTH,<br>
Steve</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a0e55717ec4a96d171cfea04bc085eeaa0b3c0f.png" alt="image" data-base62-sha1="602LlGbbAIYkEHmy0mOCjm7FsyX" width="462" height="358"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57b378a4ebab185cee2d0af5b677fcb071002ad9.png" alt="image" data-base62-sha1="cvQ3qK3NqKdWZwwIKKg6m0MXdsR" width="452" height="356"></p>

---

## Post #10 by @cpinter (2019-05-08 15:17 UTC)

<p>Joint smoothing is available in Segment Editor too, no need to do the complex workflow with exporting and Model Maker. See screenshot below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed09804886cfa80573d7b1e65bc5d811ca0c53fe.png" alt="image" data-base62-sha1="xOVw1w1ZaoEQEehYCmRFEqr10NU" width="518" height="318"></p>

---

## Post #11 by @lassoan (2019-05-08 15:39 UTC)

<p>The only difference compared to joint smoothing in Segment Editor compared to Model maker is that joint smoothing result is converted back into labelmap representation. This makes some very little difference in the final surfaces.</p>
<p>Maybe in the joint smoothing method we could add the option of changing master representation to closed surface model. Then we could store the joint smoothing result as is, instead of recomputing it from the labelmap. Since switch to labelmap representation happens automatically when segment editor tools are used, maybe we could always switch the master representation.</p>

---

## Post #12 by @pieper (2019-05-08 15:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The only difference compared to joint smoothing in Segment Editor compared to Model maker is that joint smoothing result is converted back into labelmap representation.</p>
</blockquote>
</aside>
<p>Yes, this is the difference - if you want to export the watertight surfaces you can’t re-rasterize.</p>

---

## Post #13 by @cpinter (2019-05-08 16:15 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>if you want to export the watertight surfaces you can’t re-rasterize</p>
</blockquote>
</aside>
<p>Right. Changing the master as <a class="mention" href="/u/lassoan">@lassoan</a> suggests might e a good idea to simplify this.</p>
<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>maybe we could always switch the master representation</p>
</blockquote>
</aside>
<p>You mean change the master to closed surface when using joint smoothing without asking and then back when using another effect after that?</p>

---

## Post #14 by @lassoan (2019-05-08 18:17 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="13" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>You mean change the master to closed surface when using joint smoothing without asking and then back when using another effect after that?</p>
</blockquote>
</aside>
<p>Yes. I think the automatic switching mechanism is already implemented (triggered by activating a segment editor effect), so it may be easy to change the behavior.</p>
<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>you can’t re-rasterize</p>
</blockquote>
</aside>
<p>It works remarkably well, even with re-rasterizarion. The difference is in the range of fraction of a voxel.</p>

---

## Post #16 by @brhoom (2019-05-09 09:17 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>. I noticed that 3D Slicer uses the Marching Cube algorithm in order to calculate surface mesh from the label map volume, which might be the reason why the estimated surface of one segment is penetrating the other segment’s surface.</p>
</blockquote>
</aside>
<p>Have you tried to get better surface mesh using e.g. <a href="https://github.com/lassoan/SlicerSegmentMesher" rel="noopener nofollow ugc">SlicerMesher</a> or <a href="https://github.com/MedicalImageAnalysisTutorials/SlicerMeshing" rel="noopener nofollow ugc">SlicerMeshing</a></p>

---

## Post #17 by @pieper (2019-05-09 11:33 UTC)

<p><a class="mention" href="/u/tekk_ya">@Tekk_ya</a> it’s hard to tell what’s going on from the screenshots - can you share the data?</p>

---

## Post #18 by @lassoan (2019-05-11 19:01 UTC)

<p>For me the screenshots show that everything works great. The random pattern visible at the joint teeth/bone surface indicates that the surfaces are accurately matched. You will only have the teeth strictly on one side of the bone if you add clearance between the bone and teeth (e.g., using Margin effect). You can represent arbitrarily small distance between surfaces by decreasing the spacing in segmentation.</p>
<aside class="quote no-group quote-post-not-found" data-username="Tekk_ya" data-post="15" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>smoothing factor of 1, which erodes the teeth too much</p>
</blockquote>
</aside>
<p>You can decrease the smoothing factor to lower values, if you find that important details are removed by smoothing.</p>

---

## Post #19 by @Tekk_ya (2019-06-06 15:25 UTC)

<p>I tried your suggested solution. However, when I use the model maker with joint smoothing, although the boundary lines are similar to the red/blue one you have shown here, still sometimes they cross each other which results in segments penetration in those areas.</p>

---

## Post #20 by @lassoan (2019-06-06 15:31 UTC)

<p>There is always some amount of numerical imprecision, so if you cannot tolerate even the slightest overlap between segments then you may need to add some clearance between segments (using Margin effect), disable smoothing, or work with labelmaps instead of meshes.</p>

---

## Post #21 by @cpinter (2019-06-06 16:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>disable smoothing</p>
</blockquote>
</aside>
<p>Maybe this will be the best solution for you. This way the slice intersections will be choppy, but the vertices will coincide.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e5f87731f723625d915eaaf5b8667708d2d9864.png" alt="image" data-base62-sha1="8TMgWEa8ySFPqIaLqUrFMOixaIY" width="197" height="74"></p>

---

## Post #22 by @Tekk_ya (2019-06-07 04:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>add some clearance between segments (using Margin effect),</p>
</blockquote>
</aside>
<p>do mean to add some empty space between the segments by shrinking the margin of the segments?</p>
<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>disable smoothing</p>
</blockquote>
</aside>
<p>would you please let me know in which step I should avoid smoothing?</p>
<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>or work with labelmaps instead of meshes.</p>
</blockquote>
</aside>
<p>I need to create a volumetric mesh for these geometries, therefore, I have to work with the meshes and I have no idea how can I use the labelmap to create the volumetric mesh.</p>

---

## Post #23 by @Tekk_ya (2019-06-07 04:41 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="21" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e5f87731f723625d915eaaf5b8667708d2d9864.png" alt="image" data-base62-sha1="8TMgWEa8ySFPqIaLqUrFMOixaIY" width="197" height="74"></p>
</blockquote>
</aside>
<p>I thought that setting the smoothing factor to the zero only effects the 3D visualization and does not affect the exported geometries from the Slicer. Please correct me if I am wrong.</p>
<p>thank you in advance,</p>

---

## Post #24 by @cpinter (2019-06-07 12:32 UTC)

<p>It affects the surface model contained in the segmentation, which is both displayed, and saved to file.</p>

---

## Post #25 by @lassoan (2019-06-08 19:35 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="22" data-topic="6692">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>I need to create a volumetric mesh for these geometries</p>
</blockquote>
</aside>
<p>You can use Segment Mesher extension to create volumetric mesh directly from segments. Cleaver method generates mesh from the labelmap representation (not from surface mesh) and creates a joint, multi-material tetrahedral mesh, with guaranteed no overlap or gap between materials (segments).</p>

---
