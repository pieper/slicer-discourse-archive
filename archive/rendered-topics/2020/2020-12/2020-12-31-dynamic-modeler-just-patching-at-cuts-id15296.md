# Dynamic Modeler just patching at cuts

**Topic ID**: 15296
**Date**: 2020-12-31
**URL**: https://discourse.slicer.org/t/dynamic-modeler-just-patching-at-cuts/15296

---

## Post #1 by @tsehrhardt (2020-12-31 02:10 UTC)

<p>I was cutting models using Dynamic Modeler to prepare for 3D printing and noticed that the cut surfaces are filled in with “patches,” resulting in a multi-part mesh rather than a finished one-part mesh.</p>
<p>Is this what it is supposed to do? I have normally used the EasyClip module and that produces a finished mesh.</p>
<p>Screenshots show the cut surface of a skull in Slicer 4.11.20200930 and the filled in patches in Meshmixer that I separated using Edit → Separate Shells (I made shell 2 invisible). The patched surfaces also have the normals flipped inward.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8e5e85d1702ea659c862a3d7d779d787255122.jpeg" data-download-href="/uploads/short-url/zTmRVjLthCmcfqsC1IC7z63sBMu.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb8e5e85d1702ea659c862a3d7d779d787255122_2_599x500.jpeg" alt="Screenshot" data-base62-sha1="zTmRVjLthCmcfqsC1IC7z63sBMu" width="599" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb8e5e85d1702ea659c862a3d7d779d787255122_2_599x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb8e5e85d1702ea659c862a3d7d779d787255122_2_898x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb8e5e85d1702ea659c862a3d7d779d787255122.jpeg 2x" data-dominant-color="A2A1A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1182×986 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d34d2a3fae681682cf791274bf17929ba977aabd.jpeg" data-download-href="/uploads/short-url/u9g4rbr4E7P1hrWffFaxzz0oiCx.jpeg?dl=1" title="2020-12-30_20-56-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34d2a3fae681682cf791274bf17929ba977aabd_2_654x500.jpeg" alt="2020-12-30_20-56-23" data-base62-sha1="u9g4rbr4E7P1hrWffFaxzz0oiCx" width="654" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34d2a3fae681682cf791274bf17929ba977aabd_2_654x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34d2a3fae681682cf791274bf17929ba977aabd_2_981x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34d2a3fae681682cf791274bf17929ba977aabd_2_1308x1000.jpeg 2x" data-dominant-color="696767"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-12-30_20-56-23</span><span class="informations">1336×1020 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-12-31 03:55 UTC)

<p>Good point, only positive side of the plane cut output has correctly oriented cap. I’ve submitted an <a href="https://github.com/Slicer/Slicer/issues/5359">issue</a> to fix orientation of the negative side.</p>
<p>Not merging points of the caps with the cut model is a feature. It makes normal computation very robust, allows separation of caps from the original surface, and allows plane cut operation be a tiny bit faster. You can always easily merge points if that is preferred for any reason, but once you merged the points, it is much harder to separate them.</p>
<p>You can use Surface Toolbox to post-process the model to get a model with consistently oriented normals an non-separable parts:</p>
<ul>
<li>If you want to merge points of the cut model with the caps (so that MeshMixer cannot separate the parts anymore), enable “Clean” operation.</li>
<li>To make surface normal consistently face outwards, enable “Normals” operation with “Auto-orient normals” and “Splitting” options enabled (maybe also “Flip normals”). Use result of a previously “Clean”-ed (merged) operation as an input and also enable “Clean” for the output as well.</li>
</ul>

---

## Post #3 by @tsehrhardt (2020-12-31 15:49 UTC)

<p>Ok so when I use the “Clean” operation, the parts get merged although the normals are still flipped on the patches. However, when I apply “Auto-orient normals” and “Splitting”, the normals are flipped the wrong way but also the mesh gets chopped into multiple parts (blue edges) so the Cleaning step gets undone. When I input the cleaned model and check “auto-orient normals”, “splitting”, and “flip normals”, the normals are all flipped correctly, but the mesh still gets chopped into multiple parts–Meshlab is showing 1777 components and 8702 unreferenced vertices.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1eb246d1c0a111d7ccc5e1b53e69f261598dcaa.jpeg" data-download-href="/uploads/short-url/rFtWoohSvA9RTt4d5D7GJ2KQzZo.jpeg?dl=1" title="2020-12-31_9-25-38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb246d1c0a111d7ccc5e1b53e69f261598dcaa_2_524x500.jpeg" alt="2020-12-31_9-25-38" data-base62-sha1="rFtWoohSvA9RTt4d5D7GJ2KQzZo" width="524" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb246d1c0a111d7ccc5e1b53e69f261598dcaa_2_524x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb246d1c0a111d7ccc5e1b53e69f261598dcaa_2_786x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1eb246d1c0a111d7ccc5e1b53e69f261598dcaa_2_1048x1000.jpeg 2x" data-dominant-color="615A5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-12-31_9-25-38</span><span class="informations">1602×1526 302 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-12-31 16:50 UTC)

<p>Maybe the instructions above were a bit confusing. By this</p>
<blockquote>
<p>Use result of a previously “Clean”-ed (merged) operation as an input and also enable “Clean” for the output as well.</p>
</blockquote>
<p>I meant that you need to clean both before and after recomputing the normals. I’ve tested it with MeshMixer and it worked well.</p>
<p>After <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> fixes the capping plane normal direction (or you keep the positive side of the cut model) then all you need is a simple clean operation to merge all coincident points.</p>

---

## Post #5 by @tsehrhardt (2020-12-31 18:47 UTC)

<p>Thank you for the clarification Andras. Applying the Cleaner and fixing the normals at the same time worked–Meshlab found unreferenced vertices but it was a single closed mesh.</p>
<p>It might be nice if the Dynamic Modeler gave the option to leave the mesh open or not after plane cutting (like Meshmixer)–if somebody did want to leave the edges open to append to other objects, then they would have to separate the patches from the cut mesh. Also, if the cut mesh has open edges, then the Surface Toolbox (or Meshmixer) could be used to just fill holes rather than cleaning, flipping normals and cleaning again.</p>

---

## Post #6 by @lassoan (2020-12-31 19:09 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="5" data-topic="15296">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>It might be nice if the Dynamic Modeler gave the option to leave the mesh open or not after plane cutting (like Meshmixer)–if somebody did want to leave the edges open to append to other objects, then they would have to separate the patches from the cut mesh</p>
</blockquote>
</aside>
<p>Capping of cut surfaces in Dynamic Modeler’s Plane cut tool is optional - controlled by “Cap surface” checkbox. Do you mean some additional open/closed option would need to be added?</p>
<aside class="quote no-group" data-username="tsehrhardt" data-post="5" data-topic="15296">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>Meshlab found unreferenced vertices but it was a single closed mesh</p>
</blockquote>
</aside>
<p>“Clean” operation removes all unreferenced points. If you can provide an example file that MeshMixer reports to have unreferenced points then send it and I can have a look.</p>
<aside class="quote no-group" data-username="tsehrhardt" data-post="5" data-topic="15296">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>Also, if the cut mesh has open edges, then the Surface Toolbox (or Meshmixer) could be used to just fill holes rather than cleaning, flipping normals and cleaning again.</p>
</blockquote>
</aside>
<p>Hole filling relies on heuristics - it is not guaranteed to provide correct results. So, it is better to cap the cut surface while you still know where exactly the cut plane was.</p>
<p>You don’t need manual normal computation if you use a recent Slicer Preview Release and use the positive side of the cut plane, but you just need is a simple clean operation using Surface Toolbox (4-5 clicks in total).</p>
<p>We could add coincident point merging as an option to plane cut tool, but for that we would need to have a good reason (otherwise we would just clutter the GUI with it). Can you tell why is this a problem that coincident points are not merged?</p>
<p>Note that coincident point merging is a trivial operation that is available in all mesh processing software. In MeshMixer it is called “Close Cracks” (in Edit menu). So, if you don’t want to merge the points in Slicer then you can easily do it in MeshMixer, too.</p>

---

## Post #7 by @tsehrhardt (2020-12-31 19:55 UTC)

<p>I found the Cap Surfaces box–sorry I missed that! The mesh with unreferenced vertices had a floating piece so that was it. The positive side worked fine.</p>
<blockquote>
<p>We could add coincident point merging as an option to plane cut tool, but for that we would need to have a good reason (otherwise we would just clutter the GUI with it). Can you tell why is this a problem that coincident points are not merged?</p>
</blockquote>
<p>I am used to using the EasyClip module for plane cuts which automatically produces a closed finished mesh, so I assumed that Dynamic Modeler might incorporate the same feature. Ultimately, I would like to not have to use Meshmixer or Meshlab to finish a model.<br>
Thanks Andras!</p>

---

## Post #8 by @lassoan (2020-12-31 21:37 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="7" data-topic="15296">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>automatically produces a closed finished mesh, so I assumed that Dynamic Modeler might incorporate the same feature</p>
</blockquote>
</aside>
<p>There are several reasons merging coincident points after surface cutting should not be done:</p>
<ol>
<li>Breaks surface normal computation</li>
</ol>
<p>Surface normals are computed at mesh points and surface normal is computed by interpolating between these points. This means that at sharp edges you will not have nice, clean cut edges if the points are shared between neighbor cells.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66f7bcdd2d647f70fed557df3e72aa95768a1092.jpeg" data-download-href="/uploads/short-url/eGTtC9qO2UQb6VqtRlCXFSlnbwe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f7bcdd2d647f70fed557df3e72aa95768a1092_2_689x315.jpeg" alt="image" data-base62-sha1="eGTtC9qO2UQb6VqtRlCXFSlnbwe" width="689" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f7bcdd2d647f70fed557df3e72aa95768a1092_2_689x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f7bcdd2d647f70fed557df3e72aa95768a1092_2_1033x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/66f7bcdd2d647f70fed557df3e72aa95768a1092_2_1378x630.jpeg 2x" data-dominant-color="86864C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2365×1083 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can split the edges (e.g., by using a fixed feature angle), but all these splitting methods rely on heuristics, so you will never get back your original cutting planes exactly.</p>
<ol start="2">
<li>It makes more difficult to separate surface patches</li>
</ol>
<p>Often you want to render the cut surface with a different color from the original surface. By having disjoint surface patches it is easier to separate the cut surfaces and assign different color or rendering style.</p>
<ol start="3">
<li>It takes time</li>
</ol>
<p>Usually point merging is quick but for large meshes it may take significant amount of time.</p>
<ol start="4">
<li>It is an irreversible operation</li>
</ol>
<p>All mesh processing software can easily merge coincident points, but once you merged the points, there is no way to separate the cut surface from the caps again.</p>
<hr>
<p>Overall, it is probably better not to offer point merging as an option to plane cut tool, as it would encourage users to do it, causing potential complications for further visualization and processing steps. Any algorithms that is sensitive to coincident points can start with point merging step to avoid problems; and users can merge points anytime as needed anyway.</p>

---
