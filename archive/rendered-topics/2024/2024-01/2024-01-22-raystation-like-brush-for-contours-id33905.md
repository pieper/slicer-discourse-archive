---
topic_id: 33905
title: "Raystation Like Brush For Contours"
date: 2024-01-22
url: https://discourse.slicer.org/t/33905
---

# Raystation-like brush for contours

**Topic ID**: 33905
**Date**: 2024-01-22
**URL**: https://discourse.slicer.org/t/raystation-like-brush-for-contours/33905

---

## Post #1 by @strider_hunter (2024-01-22 13:33 UTC)

<p>Hi,<br>
Is it possible to edit contours like in RayStation (radiotherapy contouring and planning software).</p>
<p>It basically pushes or repulses existing contours using a circular brush</p>
<p>Find attached a video/image</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e50bc8c489f9cba5a28e4e9e9e9d89da53e61bde.mp4">
  </div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96c9f7a89fb15be19fd9908383e7f2fb0cfc6717.png" data-download-href="/uploads/short-url/lvWkGYQFCw6ATWr8MlehLjQMXY3.png?dl=1" title="RaystationContourBrush" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c9f7a89fb15be19fd9908383e7f2fb0cfc6717_2_558x500.png" alt="RaystationContourBrush" data-base62-sha1="lvWkGYQFCw6ATWr8MlehLjQMXY3" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c9f7a89fb15be19fd9908383e7f2fb0cfc6717_2_558x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c9f7a89fb15be19fd9908383e7f2fb0cfc6717_2_837x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96c9f7a89fb15be19fd9908383e7f2fb0cfc6717.png 2x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RaystationContourBrush</span><span class="informations">906×811 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><p></p>
<p><strong>Update</strong></p>
<ol>
<li>
<p>I also found that the OHIF viewer has something similar, though less intuitive in design<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d36e808960b881940ba39d608ecc8202acac806f.mp4">
  </div><p></p>
</li>
<li>
<p>And also another tool called DragonFly allow “repulsing” the contours (<a href="https://www.youtube.com/watch?v=1ta5bnuVjlo&amp;t=18s" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=1ta5bnuVjlo&amp;t=18s</a>)</p>
</li>
</ol>

---

## Post #2 by @strider_hunter (2024-01-22 14:39 UTC)

<p>When I try this with 3D Slicer 5.6.1 (using Paint/Erase tool on Closed Surface), the updates are not on-the-fly (i.e. only after I release mouse click).</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4056403fcf1163c6a1daeaeea7186a3089466bb2.mp4">
  </div><p></p>

---

## Post #3 by @pieper (2024-01-22 15:55 UTC)

<p>Try the “Color smudge” option instead of the eraser.  It changes the segmentation label based on where you first click.</p>
<p>The outline doesn’t update until you release the mouse so that you have a smooth interaction while painting independent of the complexity of the segmentation.</p>
<p>Regarding active contours there have been a lot of experiments but nothing that seems generally useful across a range of data.  Generally Grow from seeds can work well but it depends on your data.</p>

---

## Post #4 by @strider_hunter (2024-01-23 10:24 UTC)

<p>Thanks for the suggestion.</p>
<ol>
<li>
<p>When I use the “Color Smudge” option, the contour shrinks rather than expanding.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10a211bce147758f79a4bb27e9f04a0fd62c16f.mp4">
  </div><p></p>
</li>
<li>
<p>So my work generally involves editing automated contours. And clinicians prefer using editing tools that they already have experience with (in this case the brush tool of Raystation).</p>
</li>
<li>
<p>Any pointers on how to proceed with active contours? Would this involve building an extension from scratch or could I pythonically implement such a brush?</p>
</li>
</ol>

---

## Post #5 by @pieper (2024-01-23 13:36 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="4" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>When I use the “Color Smudge” option, the contour shrinks rather than expanding.</p>
</blockquote>
</aside>
<p>This depends on whether your paint stroke starts inside the segment or outside - the term ‘smudge’ is meant to be like finger painting.</p>
<p>Making new segment editor effects is a bit of work, but can certainly be done in python.  Making something efficient may be easier with some C++ code, but it’s also possible there are existing VTK or ITK classes that could be used.</p>

---

## Post #6 by @lassoan (2024-01-23 14:46 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="4" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>When I use the “Color Smudge” option, the contour shrinks rather than expanding</p>
</blockquote>
</aside>
<p>I can see on your video that you started the segmentation from inside the segment, in which case it should expand the segmentation. However, your case was unusual/unlucky in many aspects:</p>
<ul>
<li>You switched the segmentation representation displayed in slice views to be “Closed surface”, therefore you see the 3D surface interpolation of the segmentation in slice views, which may have some subpixel differences. Since the binary labelmap representation of the segmentation is used for editing, it is probably a better choice to use that during editing.</li>
<li>Voxels in your image are very large (maybe it is some low-resolution sample data set?), therefore very small (considering voxel size) differences between various representations of the segmentation may become perceivable.</li>
<li>You happened to start the painting very close to the boundary.</li>
</ul>
<p>If you change any of these then “repulsing” will work as expected. Probably the most robust solution is to switch to display the binary labelmap representation in slice views; or start the painting from inside the structure (not that close to the boundary).</p>
<p>We could address the unexpected behavior by switching the inside/outside check to use the closed surface representation if that is shown in slice views, but it is such an edge case that it would be quite low on the priority list. If you find that after trying the described alternative solutions this is still a significant issue for you then please submit an issue at <a href="https://issues.slicer.org">https://issues.slicer.org</a> .</p>

---

## Post #7 by @strider_hunter (2024-01-23 18:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I use a scan with a 2x2x2 (mm) spacing</p>
<ol>
<li>
<p>In “<strong>Closed surface</strong>” representation, starting on the inside does not seem to work (and is also not the kind of interaction I need as seen in the video at the top of this post. Note there how it shows a + or -, depending on whether its inside or outside the contour)</p>
</li>
<li>
<p>Using the “<strong>Binary labelmap</strong>” representation makes the tool function as advertised.</p>
<ul>
<li>However, such a pixelated representation is not something that clinicians are used to and I would still need to work in the closed surface representation.</li>
<li>It does surprise me that this is considered as an edge case as other commercial tools also have this (<a href="https://www.youtube.com/watch?v=GpnOajZaZb4&amp;t=165s" rel="noopener nofollow ugc">1</a>, <a href="https://www.youtube.com/watch?v=twBXRWCOhTg&amp;t=130s" rel="noopener nofollow ugc">2</a>, <a href="https://youtu.be/lGj3uyxUdgs?si=qMnd6WVBgOOBaiYp&amp;t=2" rel="noopener nofollow ugc">3</a>, <a href="https://youtu.be/lGj3uyxUdgs?si=02dUoOoNIsput4_3&amp;t=186" rel="noopener nofollow ugc">4</a>). Some others also use the closed surface representation to draw (<a href="https://youtu.be/UBm_5FtG25U?si=2p465_GVinvmyiIT&amp;t=885" rel="noopener nofollow ugc">5</a>). Conversely, open source tools dont seem to have this option (<a href="https://www.youtube.com/watch?v=YV2ssizz9gQ&amp;t=280s" rel="noopener nofollow ugc">6</a>)</li>
<li>I will raise an issue as suggested. Thank you for the detailed response!</li>
</ul>
</li>
</ol>

---

## Post #8 by @lassoan (2024-01-23 21:10 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="7" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>Note there how it shows a + or -, depending on whether its inside or outside the contour</p>
</blockquote>
</aside>
<p>Slicer allows not just adding/removing but moving boundaries between any two segments. Limiting it to editing the currently selected segment could be possible, but that would feel more like a limitation than a feature. Also, if you want to just paint/erase the currently selected segment then you switch between them using the space key (after clicking on the paint and erase effects, as space key toggles between the last two active effects).</p>
<aside class="quote no-group" data-username="strider_hunter" data-post="7" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>However, such a pixelated representation is not something that clinicians are used to and I would still need to work in the closed surface representation.</p>
</blockquote>
</aside>
<p>By default, the resolution of the segmentation is the same as the resolution of the source image. 2mm voxel size indeed means quite low resolution, and so the voxel size of the segmentation can be quite visible.</p>
<p>A simple solution would be to set finer resolution for the segmentation using <code>Specify geometry</code> as <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">described in the Segment Editor documentation</a>.</p>
<p>It could be useful to discuss with the clinicians what their accuracy requirements are. They may not realize just how crude these 2x2x2mm images are and that the resulting contours can have several-millimeter errors. Maybe this error size is acceptable, but then they should have no problem with using this resolution for representing segmentations, too.</p>
<aside class="quote no-group" data-username="strider_hunter" data-post="7" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>It does surprise me that this is considered as an edge case as other commercial tools also have this (<a href="https://www.youtube.com/watch?v=GpnOajZaZb4&amp;t=165s">1</a>, <a href="https://www.youtube.com/watch?v=twBXRWCOhTg&amp;t=130s">2</a>, <a href="https://youtu.be/lGj3uyxUdgs?si=qMnd6WVBgOOBaiYp&amp;t=2">3</a>, <a href="https://youtu.be/lGj3uyxUdgs?si=02dUoOoNIsput4_3&amp;t=186">4</a>). Some others also use the closed surface representation to draw (<a href="https://youtu.be/UBm_5FtG25U?si=2p465_GVinvmyiIT&amp;t=885">5</a>). Conversely, open source tools dont seem to have this option (<a href="https://www.youtube.com/watch?v=YV2ssizz9gQ&amp;t=280s">6</a>)</p>
</blockquote>
</aside>
<p>It is an edge case because you need to use low-resolution input volume + use closed surface representation + click close to the boundary (in 3D, so in the slice view it may seem you are far from the edge, but you may be actually very close).</p>
<p>The labelmap representation is objectively better for representing 3D shapes than planar contour sets, and generally labelmap representation is used by most modern tools for storing segmentation.</p>
<p>There are a number of exceptions in the field of radiation treatment planning, as medical physicists decades ago made the unfortunate decision to use planar contour representation for storing segmentation results in DICOM. This kind of forced commercial treatment planning systems to work with planar contours and changing that would be enormous cost and risk for them.</p>
<details>
<summary>
Note on microscopy</summary>
<p>Since you have included some videos of microscopy software, I would add that of course contour representation is an attractive option in this field, because:</p>
<ol>
<li>Data sets are mostly just 2D, so you don’t need to worry about reconstructing a 3D shape from contours, and</li>
<li>They need to operate on a very wide range of scale, which is trivial if you use a contour representation but quite complex if you use a multi-resolution labelmap representation.</li>
</ol>
<p>However, these don’t apply to radiology images, which are 3D and not super-high-resolution.</p>
</details>
<p>3D Slicer is exceptional in that it can work with multiple representations (binary labelmap, fractional labelmap, closed surface, planar contours, ribbons), each representation can be stored losslessly, without having to convert to some hardcoded representation, you can also choose what representations are used for visualization and quantification. Representations are computed automatically from the soruce representation as needed, and the user has even control over what methods are used and with what parameters (and developers can add their own custom conversion methods and representation types). As a result, Slicer can import, process/edit, visualize, and export data in a wide range of formats, in a variety of workflows. This extreme flexibility also means that the user may be exposed to more information than usual and may need to make more decisions that have further consequences (e.g., if you choose to switch from the default binary labelmap representation then you may also need to consider adjusting the internal labelmap resolution if the source image had low resolution). In clinical software, there is no flexibility because only routine clinical workflows need to be supported; and in most research projects there is just no capacity to develop and maintain such level of flexibility.</p>

---

## Post #9 by @strider_hunter (2024-01-24 10:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, your case was unusual/unlucky in many aspects:</p>
</blockquote>
</aside>
<p>I tested the Color Smudge option on another scan with a xy resolution of 0.9mm and the feature worked as advertised. So I see why you call it an edge case.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe this error size is acceptable, but then they should have no problem with using this resolution for representing segmentations, too.</p>
</blockquote>
</aside>
<p>The CT I have used is actually paired with a PET scan, which in general have low resolution. So the clinicians are aware of the low resolution. But I think the issue is with getting them to use tools (in this case 3D Slicer) which do not conform with their daily clinical experience.</p>
<p>Of course, as a researcher, 3D Slicer suits my purpose, since I can extend it with deep learning based auto-contouring extensions. But I also do not wish to add a learning curve for clinicians, as that can be an additional factor affecting my experiments.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The labelmap representation is objectively better for representing 3D shapes than planar contour sets, and generally labelmap representation is used by most modern tools for storing segmentation.</p>
</blockquote>
</aside>
<p>I agree with you, but with a slight modification. I believe labelmaps are better for storing 3D shapes (as they then align with the same discretization of the scan they are associated with). However, visualization/editing is just more pleasing with their smoothed versions (i.e., contour points). I guess this where I fundamentally disagree with the approach taken by slicer in the Segment Editor extension. Looks like similar concerns have been raised on this forum before (<a href="https://discourse.slicer.org/t/editing-of-planar-contours-without-converting-to-binary-label-map/9475">1</a>, <a href="https://discourse.slicer.org/t/planar-contours-and-binary-label-maps/3778">2</a>). Nevertheless, I am still an advocate of slicer at my lab and really find the tool very convenient to use for exploring 3D data.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A simple solution would be to set finer resolution for the segmentation using <code>Specify geometry</code> as <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough" rel="noopener nofollow ugc">described in the Segment Editor documentation </a>.</p>
</blockquote>
</aside>
<p>This is indeed a simple solution to my issue. I tried doing this and was able to edit existing masks with a higher resolution. However, I was unable to create additional masks on other slices. Even when I switch off the “Color Smudge” option. Is this an error or am I incorrectly using this? Please see the video below.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/859fc9067e23544f32ead73187cf2288dd18ae2a.mp4">
  </div><p></p>
<p>Finally, thank for explaining your design reasons. Its been interesting to get the inside scoop on what motivated the features of these tools.</p>

---

## Post #10 by @pieper (2024-01-24 15:26 UTC)

<aside class="quote no-group" data-username="strider_hunter" data-post="9" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>unable to create additional masks on other slices</p>
</blockquote>
</aside>
<p>Thanks for pointing this out, yes, it’s a limitation of the smudge tool.  Since you click on a place with no segmentation it gets set to erase mode.  Maybe we should take this into account somehow, like if the slice changes then smudge mode ignores a click on an empty segment and instead uses the most recent segment value.  There might be cases where that’s confusing too, but at least this case would be okay.</p>

---

## Post #11 by @strider_hunter (2024-01-25 12:05 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Since you click on a place with no segmentation it gets set to erase mode</p>
</blockquote>
</aside>
<p>A suggestion to deal with this could be that when the smudge tool is in a place with no segmentation, a shortcut (e.g. the Alt button), could make the smudge tool goes into paint mode.</p>
<p>I made a video showcasing how it could be done.<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/eff7d99facb196635bde3b72744cf51b93bd1d8f.mp4">
  </div><p></p>
<p>I’ve also found out that this contour repulsion feature is available in other dicom visualization tools like osirix.</p>

---

## Post #12 by @lassoan (2024-01-25 14:31 UTC)

<p>Would it help if we added a shortcut to enable the smudge option, i.e., if you hold down Alt key when painting then it would switch to the segment under the mouse pointer before making the paintstroke? We could similarly add shortcut for erasing, i.e., holding down Shift while using the paint tool would always erase.</p>
<p>The +/- hint does not make much sense to me for smudge mode, as it assumes that you work with a single segment. Very often you want to adjust the contours between two segments, so you would need a hint (change color, display text, etc.) that can tell the segment name that will be painted there.</p>
<p>However, overall I’m not sure how much “segmentation touch up” is a common need. If you create ground truth segmentations for AI training then you don’t want to introduce a bias by starting from some poor contours. For clinical work, it is hard to imagine that requiring manual touchup of segmentation using paintbrush is a viable strategy (quick broad cuts using Scissors, yet, but it is really hard to imagine someone doing meticulous slice-by-slice painting in day-to-day clinical work).</p>
<p><a class="mention" href="/u/strider_hunter">@strider_hunter</a> What is your use case? AI training data set generation or clinical work? What are your time constraints and accuracy requirements?</p>

---

## Post #13 by @strider_hunter (2024-01-29 15:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Would it help if we added a shortcut to enable the smudge option, i.e., if you hold down Alt key when painting then it would switch to the segment under the mouse pointer before making the paintstroke? We could similarly add shortcut for erasing, i.e., holding down Shift while using the paint tool would always erase.</p>
</blockquote>
</aside>
<p>In my limited experience observing clinicians, they work with just one organ/tumor type at a time, and also use a single tool for painting/erasing (with shortcuts associated with that tool). So I can only comment on such a scenario.</p>
<p>Thus, having chosen a particular organ/tumor (and the paint tool with smudge option), my use case is to allow the clinician to edit an existing AI segmentation so that it can be improved to clinical quality. So then they add/erase parts of the segmentation. In areas where the segmentation does not exist, I think the Alt keypress to add segmentation would be useful (see the video above this post).</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, overall I’m not sure how much “segmentation touch up” is a common need. If you create ground truth segmentations for AI training then you don’t want to introduce a bias by starting from some poor contours. For clinical work, it is hard to imagine that requiring manual touchup of segmentation using paintbrush is a viable strategy (quick broad cuts using Scissors, yet, but it is really hard to imagine someone doing meticulous slice-by-slice painting in day-to-day clinical work).</p>
</blockquote>
</aside>
<p>I believe the field of auto-segmentation is moving towards the “edit-and-QA” direction instead of “drawing-from-scratch” anymore. Given the maturity of deep learning models, large datasets, and the software ecosystem, it seems natural for this to be the next step. Check <a href="https://www.youtube.com/watch?v=Wxmo7MVc7hI&amp;t=115s" rel="noopener nofollow ugc">this video</a> for example (<em>they dont edit segmentations though</em>).</p>
<aside class="quote no-group" data-username="strider_hunter" data-post="9" data-topic="33905">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/strider_hunter/48/8253_2.png" class="avatar"> strider_hunter:</div>
<blockquote>
<p>However, visualization/editing is just more pleasing with their smoothed versions (i.e., contour points).</p>
</blockquote>
</aside>
<p>To summarize this really long thread, this is my main requirement (<em>smoothed=Closed surface</em>). But it seems that this requirement is not the direction that Slicer will take due to all the reasons cited in the comments above.</p>

---
