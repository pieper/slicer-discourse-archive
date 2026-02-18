# Joint smoothing can create spurious bridges between separate parts of anatomy (in same segment)

**Topic ID**: 20765
**Date**: 2021-11-24
**URL**: https://discourse.slicer.org/t/joint-smoothing-can-create-spurious-bridges-between-separate-parts-of-anatomy-in-same-segment/20765

---

## Post #1 by @DIV (2021-11-24 07:19 UTC)

<p>In the <em>Segment Editor</em> module there are various options for <code>Smoothing</code> in the <em>Effects</em> panel.<br>
One favourable choice is <code>Joint smoothing</code>, which brings up the note:  “smoothes multiple segments at once, preserving watertight interface between them”.</p>
<p>I had in mind (from a little experience) that <code>Joint smoothing</code> would not tend to create (spurious) ‘bridges’ between different parts of an individual segment, nor would it delete (real) ‘bridges’.<br>
For instance, if the unsmoothed segment looked like the letter “<strong>H</strong>” (or the symbol “<strong>≭</strong>”), it wouldn’t delete the (possibly narrow) crossbar, but if the unsmoothed segment looked like “<strong>II</strong>” (double uppercase “i”), it wouldn’t merge these, and if the unsmoothed segment looked like Greek letter “<strong>Ω</strong>”, it wouldn’t create any crossbar to bridge across the base.<br>
Certainly the other built-in smoothing options seem more prone to create those artefacts in the case of small gaps or thin segments.</p>
<p>However, I may have oversimplified what the algorithm does.  (Or there may be some small implementational quirks, per <a href="https://discourse.slicer.org/t/exported-stl-files-from-the-segmentation-has-intersection-penetration/6692/11" class="inline-onebox">Exported STL files from the segmentation has intersection/penetration - #11 by lassoan</a> ?)</p>
<p>I found that actually it may create spurious bridges.<br>
In the screenshots below the green is the original segment (with a narrow gap created with the <code>Scissors</code> effect), and the brown is after applying the <code>Joint smoothing</code> effect, with <code>Smoothing factor</code> equal to 0.5.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d53ec0b5c4f510ec843b09b25b6da1cbf914d3c6.jpeg" data-download-href="/uploads/short-url/uqs9csAiJsAb6JmuMMQmkepqSVw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d53ec0b5c4f510ec843b09b25b6da1cbf914d3c6_2_690x373.jpeg" alt="image" data-base62-sha1="uqs9csAiJsAb6JmuMMQmkepqSVw" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d53ec0b5c4f510ec843b09b25b6da1cbf914d3c6_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d53ec0b5c4f510ec843b09b25b6da1cbf914d3c6_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d53ec0b5c4f510ec843b09b25b6da1cbf914d3c6_2_1380x746.jpeg 2x" data-dominant-color="9CABA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53f82104fdfa21dbc0db2214f0d7a358ae40b992.jpeg" data-download-href="/uploads/short-url/bYPf7HOnjjOBoB0BsfWuCEv49cS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53f82104fdfa21dbc0db2214f0d7a358ae40b992_2_690x373.jpeg" alt="image" data-base62-sha1="bYPf7HOnjjOBoB0BsfWuCEv49cS" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53f82104fdfa21dbc0db2214f0d7a358ae40b992_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53f82104fdfa21dbc0db2214f0d7a358ae40b992_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53f82104fdfa21dbc0db2214f0d7a358ae40b992_2_1380x746.jpeg 2x" data-dominant-color="AA9A9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Other than this the smoothing looks good.</p>
<p>If this is expected behaviour, is there a recommendation to avoid it?  For example, would applying joint smoothing five times with <code>Smoothing factor</code> equal to 0.1 be theoretically equivalent?  (I guess it wouldn’t.)</p>

---

## Post #2 by @mau_igna_06 (2021-11-24 10:36 UTC)

<p>Did you try creating a segment that selects all the volume except your region of interest with boolean fill and boolean difference?</p>
<p>Then with your original segment and the newly created segment visible execute joint smoothing and the bridges should not appear.</p>
<p>That could work I think. I’m not sure.</p>

---

## Post #3 by @pieper (2021-11-24 15:20 UTC)

<p>We’ve been discussing this for quite a while and I’m still thinking there’s a difference between the Joint Smoothing exposed by the current Segmentations and the Joint Smoothing originally provided by <a class="mention" href="/u/lorensen">@Lorensen</a>.  As <a href="https://discourse.slicer.org/t/exported-stl-files-from-the-segmentation-has-intersection-penetration/6692/9">dicussed</a>, <a class="mention" href="/u/lorensen">@Lorensen</a>’s algorithm maintained watertight boundaries by explicitly moving the corresponding vertices where to models abut such that they have the exact same location in the algorithm output (e.g. two STL files would have exact watertight fit).  Last I checked, as in the screenshots linked above, the current implementation can still leave some (small) gaps.</p>
<p>Also <a class="mention" href="/u/lorensen">@Lorensen</a>’s algorithm should never change the topology, since it works by first building surfaces that exactly follow the voxel edges (a ‘cuberile’ model) and then only smooths by moving the vertex points.</p>

---

## Post #4 by @lassoan (2021-11-24 16:52 UTC)

<p>The “bridges” in the image above are probably simply due to converting the smoothed result back to a binary labelmap. If you have the same voxel value in two adjacent voxels in a labelmap (without a gap or different segment between them) then the two voxels are considered connected (fused).</p>
<p>You have several options to address this. The most obvious one is to only smooth the mesh, not the labelmap. You can control mesh smoothness using “Smoothing factor” in the dropdown menu of “Show 3D” button. If you want to smooth the labelmap then you may need to increase the resolution of the segmentation so that you can reliably represent a very narrow gap.</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Also <a class="mention" href="/u/lorensen">@Lorensen</a>’s algorithm should never change the topology, since it works by first building surfaces that exactly follow the voxel edges (a ‘cuberile’ model) and then only smooths by moving the vertex points.</p>
</blockquote>
</aside>
<p>This method is only applicable when segments do not overlap and all the labels are in a single volume.</p>
<p>Until a few years ago, segmentations module stored each segment in a separate labelmap, therefore the method was not feasible (due to potentially overlapping segments); and if segments did not overlap, merging the segments after each segment update would have been just too slow.</p>
<p>After <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> implemented shared labelmap support in Segmentations, he added the “Joint smoothing” option to the closed surface generation method. Since then you can use the exact same method as the original “Model maker” module used for smoothing the output models. If the option is enabled, then segments in the same layer are smoothed jointly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3bcdfafc1f5e25a200feb220eec73200080317.png" data-download-href="/uploads/short-url/aSopWSkjdtyjP8ZJ0Xv4sIRrOyr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bcdfafc1f5e25a200feb220eec73200080317_2_596x500.png" alt="image" data-base62-sha1="aSopWSkjdtyjP8ZJ0Xv4sIRrOyr" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bcdfafc1f5e25a200feb220eec73200080317_2_596x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bcdfafc1f5e25a200feb220eec73200080317_2_894x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3bcdfafc1f5e25a200feb220eec73200080317_2_1192x1000.png 2x" data-dominant-color="ECEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1482×1242 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the labelmap is isotropic and smoothing is only used for removing staircase artifacts (and not to smooth out some valid details of the mesh) then joint smoothing should not make a difference, though.</p>

---

## Post #5 by @pieper (2021-11-24 17:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This method is only applicable when segments do not overlap and all the labels are in a single volume.</p>
</blockquote>
</aside>
<p>Yes, and this is a very common use case - in fact, required if watertightness is the goal.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If the option is enabled, then segments in the same layer are smoothed jointly.</p>
</blockquote>
</aside>
<p>How about making this <code>true</code> by default but changing the definition to “Joint smoothing unless  segments overlap”.</p>

---

## Post #6 by @DIV (2021-11-25 06:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You have several options to address this. The most obvious one is to only smooth the mesh, not the labelmap. You can control mesh smoothness using “Smoothing factor” in the dropdown menu of “Show 3D” button.</p>
</blockquote>
</aside>
<p>First of all it’s good to be able to build a more detailed understanding of the difference between the smoothing under the <code>Show 3D</code> button and the joint smoothing algorithm applied under the <code>Smoothing</code> effect.  I suppose that implicitly I had an idea that the former smooths <strong>the surface representing the boundary of the segmented voxels</strong> (which you call the <strong>mesh</strong>), while the latter smooths <strong>the segment</strong> by adding or removing voxels (which you call the <strong>labelmap</strong>).  Thank-you for additional clarification.</p>
<p>For the record (as some of you would already have realised), the above screenshots were taken without any mesh smoothing.  I presented the geometry in this way so that the source of the artefacts would be more immediately obvious.</p>
<p>If I apply mesh smoothing to the above two segments, with <code>Smoothing factor</code> equal to 0.5, then the results are as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fec39f670d96e59ff7f475e934e0b0dfc9616d6e.jpeg" data-download-href="/uploads/short-url/AlKoCxDM9DWo09BziQqfgi5A2wS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fec39f670d96e59ff7f475e934e0b0dfc9616d6e_2_690x367.jpeg" alt="image" data-base62-sha1="AlKoCxDM9DWo09BziQqfgi5A2wS" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fec39f670d96e59ff7f475e934e0b0dfc9616d6e_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fec39f670d96e59ff7f475e934e0b0dfc9616d6e_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fec39f670d96e59ff7f475e934e0b0dfc9616d6e.jpeg 2x" data-dominant-color="AEBBB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d94b6d22c0fda3bc259fb991e01f1db83ed2e31e.jpeg" data-download-href="/uploads/short-url/v0hd5UmG1bJO2W59rdRF8lcg0kC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d94b6d22c0fda3bc259fb991e01f1db83ed2e31e_2_690x367.jpeg" alt="image" data-base62-sha1="v0hd5UmG1bJO2W59rdRF8lcg0kC" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d94b6d22c0fda3bc259fb991e01f1db83ed2e31e_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d94b6d22c0fda3bc259fb991e01f1db83ed2e31e_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d94b6d22c0fda3bc259fb991e01f1db83ed2e31e.jpeg 2x" data-dominant-color="B9AEB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbcd81f0aec32a1f5723f1a8f5577f28d6f4b1da.jpeg" data-download-href="/uploads/short-url/qNnAgtp2K9jckgu0lyVdBhOa2me.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbcd81f0aec32a1f5723f1a8f5577f28d6f4b1da_2_690x367.jpeg" alt="image" data-base62-sha1="qNnAgtp2K9jckgu0lyVdBhOa2me" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbcd81f0aec32a1f5723f1a8f5577f28d6f4b1da_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbcd81f0aec32a1f5723f1a8f5577f28d6f4b1da_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbcd81f0aec32a1f5723f1a8f5577f28d6f4b1da.jpeg 2x" data-dominant-color="B4B4B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So indeed the gap is preserved by smoothing the mesh, rather than the labelmap.<br>
However, aside from the bridging artefacts, I prefer the smoothing obtained by smoothing the labelmap first and then smoothing the mesh.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to smooth the labelmap then you may need to increase the resolution of the segmentation so that you can reliably represent a very narrow gap.</p>
</blockquote>
</aside>
<p>While this is a logical suggestion, there may be a couple of potential issues.</p>
<p>Firstly, I have already increased the resolution by a minimum of fourfold in each orthogonal direction by isotropic cropping in the <strong>Crop Volume</strong> module.<br>
I’m reluctant to increase the resolution of the cropped volume much more than that, because it may create massive 3D rasters that would be (I think) slower to process.  Especially so if I go through slice-by-slice to manually amend the initial results (obtained by thresholding or grow-from-seeds, say).</p>
<p>I’m also not sure that it’d be suitable to increase the resolution of the labelmap only.<br>
Presumably this would be done through the <strong>Segmentation geometry</strong> dialogue, per the screenshot below.  [<em>DIGRESSION:  we’ve had <a href="https://discourse.slicer.org/t/how-can-i-configure-slicer-to-open-automatically-with-my-preferred-settings-for-the-view-controllers-module/20233/10">a little discussion of this topic</a> before. Incidentally, it seems a little inconsistent that in this dialogue a factor &gt;1 is needed to increase resolution, whereas in the Crop Volume module a factor &lt;1 is needed to increase resolution.</em>]<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a1deb311019967a94c4f7c8a2b75c1939703778.png" data-download-href="/uploads/short-url/lZnD7AhN6yQ9iYX9PufjjvBVF7W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a1deb311019967a94c4f7c8a2b75c1939703778_2_517x269.png" alt="image" data-base62-sha1="lZnD7AhN6yQ9iYX9PufjjvBVF7W" width="517" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a1deb311019967a94c4f7c8a2b75c1939703778_2_517x269.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a1deb311019967a94c4f7c8a2b75c1939703778_2_775x403.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a1deb311019967a94c4f7c8a2b75c1939703778.png 2x" data-dominant-color="E4DEE2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">853×444 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The additional issue I anticipate is that then the smoothing would end up being highly localised (or ‘small scale’).  Suppose I have two 5-millimetre objects separated by a small gap (say 0.2 mm).  If I use a resolution of, say, 0.05 mm, then most likely the gap will be preserved, but I may end up with smooth medium-sized artefacts (0.5–1 mm bumps, say) on the larger objects that I’m unable to smooth away.  Or, to put it another way, I imagine that the smoothing kernel (or some equivalent) will be smaller if the resolution is increased.</p>
<p>In the end I think the results look best if I manually erase the erroneous voxels, as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95bb6470dbca77eedc6fd9f5d4efd4bc44ed9fbf.jpeg" data-download-href="/uploads/short-url/lmAD1dsRohB22aRMGYHo11JE4ZV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95bb6470dbca77eedc6fd9f5d4efd4bc44ed9fbf_2_690x367.jpeg" alt="image" data-base62-sha1="lmAD1dsRohB22aRMGYHo11JE4ZV" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95bb6470dbca77eedc6fd9f5d4efd4bc44ed9fbf_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95bb6470dbca77eedc6fd9f5d4efd4bc44ed9fbf_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95bb6470dbca77eedc6fd9f5d4efd4bc44ed9fbf.jpeg 2x" data-dominant-color="AABDCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×728 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>—DIV</p>

---

## Post #7 by @DIV (2021-11-25 06:48 UTC)

<aside class="quote no-group quote-modified" data-username="pieper" data-post="5" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This method is only applicable when segments do not overlap and all the labels are in a single volume.</p>
</blockquote>
</aside>
<p>Yes, and this is a very common use case - in fact, required if watertightness is the goal.</p>
</blockquote>
</aside>
<p>That is, I think, what I have:  all of the voxels of interest are in a single segment — and it is the only segment being smoothed.</p>
<p>I expect that the bridges would definitely not appear if I cut the existing segment into two parts (one on each side of the narrow gap).  But that could create a different problem later when I would have to try to rejoin them (because the final objective is a single segment).</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="2" data-topic="20765">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Did you try creating a segment that selects all the volume except your region of interest with boolean fill and boolean difference?</p>
<p>Then with your original segment and the newly created segment visible execute joint smoothing and the bridges should not appear.</p>
</blockquote>
</aside>
<p>Thank-you for the suggestion, Mauro.<br>
I made a tiny adjustment to your method, which was to create the complementary segment using the logical operations of <code>Copy</code> and <code>Invert</code>.</p>
<p>I then tried the joint smoothing (of the labelmap) again in two different situations:  (i) with the inverted segment listed first in the segments table, with the result shown in purple below;  and (ii) with the inverted segment listed last in the segments table, with the result shown in reddish-brown below.  As you can see, the spurious bridges are still created.<br>
The order of segments in the segments table made no difference at all.  The results are very slightly different to the original results I obtained.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44f902ea63134b04f90c629c217f62e3bb56fe9b.jpeg" data-download-href="/uploads/short-url/9Q9Yi1vzIFkpLKycyasiV75uGpB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44f902ea63134b04f90c629c217f62e3bb56fe9b_2_323x250.jpeg" alt="image" data-base62-sha1="9Q9Yi1vzIFkpLKycyasiV75uGpB" width="323" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44f902ea63134b04f90c629c217f62e3bb56fe9b_2_323x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44f902ea63134b04f90c629c217f62e3bb56fe9b_2_484x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/44f902ea63134b04f90c629c217f62e3bb56fe9b_2_646x500.jpeg 2x" data-dominant-color="8E4179"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">791×612 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68f6f7ff457d7607f4078ccf4e4be161cab82607.jpeg" data-download-href="/uploads/short-url/eYyMFzJl0faeCbNCbHmT4anXRCD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68f6f7ff457d7607f4078ccf4e4be161cab82607.jpeg" alt="image" data-base62-sha1="eYyMFzJl0faeCbNCbHmT4anXRCD" width="646" height="500" data-dominant-color="802EB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">791×612 31 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1743628da49faf3285fcd6c97e32aeec839c5958.jpeg" data-download-href="/uploads/short-url/3jNlUHCtG5jhW5RBVjJLuQ8m8c0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1743628da49faf3285fcd6c97e32aeec839c5958.jpeg" alt="image" data-base62-sha1="3jNlUHCtG5jhW5RBVjJLuQ8m8c0" width="646" height="500" data-dominant-color="8B6168"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">791×612 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
