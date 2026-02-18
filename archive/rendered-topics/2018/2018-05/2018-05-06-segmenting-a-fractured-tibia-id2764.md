# Segmenting a fractured tibia

**Topic ID**: 2764
**Date**: 2018-05-06
**URL**: https://discourse.slicer.org/t/segmenting-a-fractured-tibia/2764

---

## Post #1 by @Itamartz (2018-05-06 15:08 UTC)

<p>Operating system- Windows 10<br>
Slicer version- 4.8.1</p>
<p>Hello friends,</p>
<p>I am trying to segment a fractured tibia for pre-surgical planning.</p>
<p>I have been trying the manipulations suggested in previous discussions:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/bone-segmentation-to-create-3d-printable-stl/960" class="inline-onebox">Bone segmentation to create 3D-printable STL</a></li>
<li><a href="https://discourse.slicer.org/t/fill-holes-after-threshold-based-bone-segmentation-in-ct/2478" class="inline-onebox">Fill holes after threshold-based bone segmentation in CT</a></li>
</ul>
<p>I used threshold segmentation instead of seeding, since the fractured made the manual seeding complex.</p>
<p>The fractures boarders are blurry, and there are still holes in the models.<br>
Can you think of a better way to do this segmentation?<br>
What is the best way to segment a fractured bone?</p>
<p>Attached pictures-</p>
<ul>
<li>Beige= only threshold segmentation</li>
<li>Green= manipulations as suggested in previous post (Cast Scalar Volume etc…)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/442fbf75c8b1a99f106bce048ebbee1c0a2dbb48.jpeg" data-download-href="/uploads/short-url/9JcLzMZxS2zwpWdbj0HmJRRhdUs.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/442fbf75c8b1a99f106bce048ebbee1c0a2dbb48_2_335x500.jpg" alt="image" data-base62-sha1="9JcLzMZxS2zwpWdbj0HmJRRhdUs" width="335" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/442fbf75c8b1a99f106bce048ebbee1c0a2dbb48_2_335x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/442fbf75c8b1a99f106bce048ebbee1c0a2dbb48.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/442fbf75c8b1a99f106bce048ebbee1c0a2dbb48.jpeg 2x" data-dominant-color="6FA38E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">458×682 80.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed1ae9dcba74c89b7e4491d5212585e9757e0389.jpeg" data-download-href="/uploads/short-url/xPwOZwmBJIBrPWTjBqXjeJ3vd33.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed1ae9dcba74c89b7e4491d5212585e9757e0389_2_331x500.jpg" alt="image" data-base62-sha1="xPwOZwmBJIBrPWTjBqXjeJ3vd33" width="331" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed1ae9dcba74c89b7e4491d5212585e9757e0389_2_331x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed1ae9dcba74c89b7e4491d5212585e9757e0389.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed1ae9dcba74c89b7e4491d5212585e9757e0389.jpeg 2x" data-dominant-color="A19DB6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">346×522 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I’ll be glad for your insights,<br>
Itamar</p>

---

## Post #2 by @lassoan (2018-05-09 04:29 UTC)

<p>The segmentation looks OK. Can you attach a screenshot where we can see the image slices as well? Why holes in the models are a problem? Would you like to 3D print it and not sure if it is printable? What accuracy do you need?</p>
<p>You might want visualize or 3D print fractured pieces separately. For that, grow from seeds effect should work very nicely (use a different seed color for each piece; and one more for the background).</p>
<p>You can use various methods in Smoothing effect to remove holes. You may also use the thresholded and shrunk bone segment as seed for “grow from seeds”, or maybe Watershed or Fast marching effects (available if installed SegmentEditorExtraEffects extension).</p>

---

## Post #3 by @Itamartz (2018-06-14 07:09 UTC)

<p>Sorry for the long absence.<br>
I used the following workflow to make a hollow model in Blender (Shrinkwrap operation).</p>
<p>Link for Embodi3d tutorial: <a href="https://www.embodi3d.com/blogs/entry/129-3d-printing-of-bones-from-ct-scans-a-tutorial-on-quickly-correcting-extensive-mesh-errors-using-blender-and-meshmixer/" class="inline-onebox" rel="noopener nofollow ugc">3D Printing of Bones from CT Scans: A Tutorial on Quickly Correcting Extensive Mesh Errors using Blender and MeshMixer - 3D Printing in Medicine - embodi3D.com</a></p>
<p>By doing so, we managed to reduce printing time from 26hr to 13hr (using uPrint SE plus).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67c86f0dcfbaa7c037dea9df85aa7d1ffabbbfe7.jpeg" data-download-href="/uploads/short-url/eO6BCVIcf93RfHoBuMFXst9DXIr.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67c86f0dcfbaa7c037dea9df85aa7d1ffabbbfe7_2_573x500.jpg" alt="image" data-base62-sha1="eO6BCVIcf93RfHoBuMFXst9DXIr" width="573" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67c86f0dcfbaa7c037dea9df85aa7d1ffabbbfe7_2_573x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67c86f0dcfbaa7c037dea9df85aa7d1ffabbbfe7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67c86f0dcfbaa7c037dea9df85aa7d1ffabbbfe7.jpeg 2x" data-dominant-color="676564"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">608×530 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b1b2463b00f9f902728856dc38187c36835838e.jpeg" data-download-href="/uploads/short-url/8qSjZPruiC0zHvDIT3Ewz25CC5w.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b1b2463b00f9f902728856dc38187c36835838e_2_458x500.jpg" alt="image" data-base62-sha1="8qSjZPruiC0zHvDIT3Ewz25CC5w" width="458" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b1b2463b00f9f902728856dc38187c36835838e_2_458x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b1b2463b00f9f902728856dc38187c36835838e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b1b2463b00f9f902728856dc38187c36835838e.jpeg 2x" data-dominant-color="C8C8C8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×719 51.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-06-14 13:08 UTC)

<p>Thanks for the update.</p>
<p>Note that since our last discussion, we’ve added “Hollow” effect to Segment editor, which serves a similar purpose as Shrinkwrap in Blender. Hollow effect is more robust, as it performs the operation on the binary labelmap representation, so there is no risk of creating invalid meshes, while Blender’s Shrinkwrap may create intersecting mesh elements at high-curvature areas.</p>
<p>Also note that if the goal is to improve printing time and save material then you may get much better results by adjusting your 3D printer’s infill settings rather than modifying your model. You can make internals of the model less dense (instead of completely hollow), which greatly increases model strength and allows you to have a thinner shell; so overall the printed object may be stronger and lighter.</p>

---

## Post #5 by @timeanddoctor (2018-06-14 13:39 UTC)

<p>The stl file created from slicer is so big even after a “reduce” in surface tool.</p>

---

## Post #6 by @Itamartz (2018-06-14 14:17 UTC)

<p>Lovely!<br>
I will most certainly try it</p>

---

## Post #7 by @lassoan (2018-06-14 21:14 UTC)

<aside class="quote no-group" data-username="timeanddoctor" data-post="5" data-topic="2764" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/timeanddoctor/48/5839_2.png" class="avatar"> timeanddoctor:</div>
<blockquote>
<p>The stl file created from slicer is so big even after a “reduce” in surface tool.</p>
</blockquote>
</aside>
<p>If decimation cannot reduce the size of your mesh then it means that the shape is actually so complex/detailed that you cannot reduce the number of elements any further without losing details. To reduce the size, you need to apply smoothing, which creates smooth/flat regions that further decimation operation can simplify and reduce in size.</p>

---

## Post #8 by @timeanddoctor (2018-06-15 10:40 UTC)

<p>I agree with you. It is very diffcult to find a balence between size and the actural detail. And the stl exported from slicer still can be decimation in blender or 3-Matic of Mimics suit software.</p>

---
