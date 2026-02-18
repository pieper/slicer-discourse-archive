# Getting a 2D binary mask from a 3D Binary Volume

**Topic ID**: 13422
**Date**: 2020-09-10
**URL**: https://discourse.slicer.org/t/getting-a-2d-binary-mask-from-a-3d-binary-volume/13422

---

## Post #1 by @evanakm (2020-09-10 13:36 UTC)

<p>My segmentation is a 3D binary volume (shown in green in the screenshot) imported from a RTSS file. I need to do two things:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/0944533c22c86c5def188721e61f28468a2a5b60.jpeg" data-download-href="/uploads/short-url/1jYGm507RgzdcVsAi9JY39EtkVa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0944533c22c86c5def188721e61f28468a2a5b60_2_690x257.jpeg" alt="image" data-base62-sha1="1jYGm507RgzdcVsAi9JY39EtkVa" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0944533c22c86c5def188721e61f28468a2a5b60_2_690x257.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0944533c22c86c5def188721e61f28468a2a5b60_2_1035x385.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0944533c22c86c5def188721e61f28468a2a5b60_2_1380x514.jpeg 2x" data-dominant-color="A4A4B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×716 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol>
<li>Extract the 2D mask in all three planar directions (the specific voxels that are shown in all three slices)</li>
<li>Convert this 2D region to a contour. (There are algorithms for doing that, so I essentially just need to extract the mask from part 1)</li>
</ol>
<p>I’ve figured out that slicer.util.getNode(‘1: RTSTRUCT: AutoSS’) will return a vthMRMLSegmentationNode, but I can’t figure out how to traverse it to get the segmentation. Is there an easy way to just export the 3d array of zeros and ones using python?</p>

---

## Post #2 by @lassoan (2020-09-10 13:41 UTC)

<aside class="quote no-group" data-username="evanakm" data-post="1" data-topic="13422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evanakm/48/6725_2.png" class="avatar"> evanakm:</div>
<blockquote>
<p>Is there an easy way to just export the 3d array of zeros and ones using python?</p>
</blockquote>
</aside>
<p>Of course! Probably the easiest way is to <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node">export to labelmap</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_value_of_a_volume_at_specific_voxel_coordinates">get voxels as numpy array</a>.</p>

---

## Post #3 by @evanakm (2020-09-10 13:50 UTC)

<p>Thanks a lot. I just tried it and I’m getting an error when I try running ExportAllSegmentsToLabelmapNode…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff272b80d8049c819ad8b6a6f7a9681d46bd164f.png" data-download-href="/uploads/short-url/ApbFVauP2bWlO8rI9JUCby6N6k7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff272b80d8049c819ad8b6a6f7a9681d46bd164f.png" alt="image" data-base62-sha1="ApbFVauP2bWlO8rI9JUCby6N6k7" width="690" height="67" data-dominant-color="F6F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1331×131 7.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(I’m using Slicer 4.10.2)</p>

---

## Post #4 by @lassoan (2020-09-10 13:52 UTC)

<p>Examples in the “Nightly” script repository page work with the latest Slicer Preview Release (which I would highly recommend to use, as latest stable is very old now and we added tons of features and fixes since then).</p>

---

## Post #5 by @evanakm (2020-09-10 14:24 UTC)

<p>Great. It seems to work in 4.11. Thank you. Just one question though. When I show the Labelmap as well as the segments, they don’t seem to match up completely. (the green segment in the Yellow and Green slices appear much more blocky)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e756683c4a634aad9460192174f1f58c67567aa0.jpeg" data-download-href="/uploads/short-url/x0vqaRGRpbW9H8VY9OxfwY1cebe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e756683c4a634aad9460192174f1f58c67567aa0_2_690x281.jpeg" alt="image" data-base62-sha1="x0vqaRGRpbW9H8VY9OxfwY1cebe" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e756683c4a634aad9460192174f1f58c67567aa0_2_690x281.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e756683c4a634aad9460192174f1f58c67567aa0_2_1035x421.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e756683c4a634aad9460192174f1f58c67567aa0_2_1380x562.jpeg 2x" data-dominant-color="9A9DAE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1921×784 320 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is this just a case of changing the resolution when I export to a Labelmap?</p>

---

## Post #6 by @lassoan (2020-09-10 14:54 UTC)

<p>You see two different representations of the same segmentation (closed surface and binary labelmap). The higher the resolution is in the reference geometry (or higher the oversampling factor is) the labelmap, the closer is the match between the two representations. See more information about representations in segmentations here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>

---

## Post #7 by @evanakm (2020-09-10 17:59 UTC)

<p>I believe I understand. Is there an easy way to extract the contour representation from Python? When it exports as a DICOM RT file, I believe this is what gets output as the contour data field (tag 3006,0050). I’m sure it’s another function under segmentations.logic(), but I can’t find anything obvious in the API docs.</p>
<p>I will be doing a transform on the data, and want to extract the contour along a specific plane, in the same format (i.e. a sequence of points) that would be exported to a Dicom RT file.</p>

---

## Post #8 by @lassoan (2020-09-10 18:10 UTC)

<aside class="quote no-group" data-username="evanakm" data-post="7" data-topic="13422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evanakm/48/6725_2.png" class="avatar"> evanakm:</div>
<blockquote>
<p>Is there an easy way to extract the contour representation from Python?</p>
</blockquote>
</aside>
<p>Yes, see examples in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Segmentations" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #9 by @evanakm (2020-09-10 18:27 UTC)

<p>On that page, I only see how to extract two representations, binary label map and closed surface. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eabc4e0dfc6d5e676795faba29acfd6b3d2f91ed.png" data-download-href="/uploads/short-url/xuzavsy1xYMcGqcFCy9gh1CJaYB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eabc4e0dfc6d5e676795faba29acfd6b3d2f91ed.png" alt="image" data-base62-sha1="xuzavsy1xYMcGqcFCy9gh1CJaYB" width="690" height="310" data-dominant-color="F3F4F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1359×612 23.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t see a way to extract the contours. Does this have to be done by exporting the closed surface and using a function in the vtk library?</p>

---

## Post #10 by @lassoan (2020-09-10 18:35 UTC)

<p>These are convenience functions for the most useful representations. Most likely you actually want the closed surface representation and not the contours (that is the one you see on screen).</p>
<p>Parallel contours representation is really, really bad way to store a 3D shape, but if you are curious how you can access it: you can do it via segmentation node -&gt; GetSegmentation -&gt; GetSegment-&gt; <a href="http://apidocs.slicer.org/master/classvtkSegment.html#a9a890bc95ebdd9b035d655b9075689cd">GetRepresentation</a>.</p>

---
