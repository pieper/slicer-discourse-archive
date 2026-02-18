# Extract centerlines irregularities

**Topic ID**: 44584
**Date**: 2025-09-25
**URL**: https://discourse.slicer.org/t/extract-centerlines-irregularities/44584

---

## Post #1 by @bserrano (2025-09-25 13:07 UTC)

<p>Hi everyone,</p>
<p>I’m using the <strong>Extract Centerline</strong> module and I’m experiencing some irregularities in the extracted curve (see attached image). I’m not sure why this is happening. The problem becomes more evident when I use <strong>Cross-section analysis</strong> to compute the vessel area.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fcccd07d4226d09bebda31e2cb796d3c6e5677e.jpeg" data-download-href="/uploads/short-url/2fLWEhqT2vWsEwpEbbaE8eKzV2m.jpeg?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcccd07d4226d09bebda31e2cb796d3c6e5677e_2_483x500.jpeg" alt="imagen" data-base62-sha1="2fLWEhqT2vWsEwpEbbaE8eKzV2m" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcccd07d4226d09bebda31e2cb796d3c6e5677e_2_483x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0fcccd07d4226d09bebda31e2cb796d3c6e5677e_2_724x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0fcccd07d4226d09bebda31e2cb796d3c6e5677e.jpeg 2x" data-dominant-color="D1C5C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">781×808 51.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8d31d0dcaab2c661db3c50de83b25d563618013.png" data-download-href="/uploads/short-url/zvcIIrZIq82zEmA64o2WXFUcFYD.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d31d0dcaab2c661db3c50de83b25d563618013_2_690x359.png" alt="imagen" data-base62-sha1="zvcIIrZIq82zEmA64o2WXFUcFYD" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8d31d0dcaab2c661db3c50de83b25d563618013_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8d31d0dcaab2c661db3c50de83b25d563618013.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8d31d0dcaab2c661db3c50de83b25d563618013.png 2x" data-dominant-color="FAF9F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">999×521 69.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any possibility of adjusting parameters or applying some automatic smoothing to improve the result?</p>
<p>Thanks a lot for your help!</p>

---

## Post #2 by @chir.set (2025-09-25 13:28 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="44584">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>automatic smoothing</p>
</blockquote>
</aside>
<p>Since all smoothing methods of the <code>segment editor</code> require input variables, smoothing cannot be automatic. <code>Extract centerline</code> works on a surface as it is. So you should prepare the surface beforehand. <code>CrossSectionAnalysis</code> is downstream, it works on the input surface and the input centerline as they are.</p>

---

## Post #3 by @mikebind (2025-09-25 18:48 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="44584">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>I’m not sure why this is happening.</p>
</blockquote>
</aside>
<p>It’s worth learning and thinking about how ExtractCenterline is really working: <a href="http://www.vmtk.org/tutorials/Centerlines.html" class="inline-onebox" rel="noopener nofollow ugc">Computing Centerlines | vmtk - the Vascular Modelling Toolkit</a></p>
<p>The most important conceptual idea is</p>
<blockquote>
<p>Briefly, centerlines are determined as weighted shortest paths traced between two extremal points. In order to ensure that the final lines are in fact central, the paths cannot lie anywhere in space, but are bound to run on the Voronoi diagram of the vessel model. There’s a huge literature on Voronoi diagrams, however, as a first approximation, you can consider it as the place where the centers of maximal inscribed spheres are defined. A sphere inscribed in an object is said to be maximal when there’s no other inscribed sphere that contains it. So, for every point belonging to the Voronoi diagram, there’s a sphere centered in that point that is a maximal inscribed sphere (the information relative to the radius is therefore defined everywhere on the Voronoi diagram).</p>
</blockquote>
<p>The jagged centerline you get comes from the centerline deviating to a path where locally larger maximally inscribed spheres are because such paths are lower weight.  Because your model is lumpy, the locally largest inscribed sphere is bouncing around along the length of this section of the model. The centerline is forced to be continuous, so the actual optimization is more complicated than just jumping to largest inscribed sphere locations, but the cost function is based on that.  The usual suggestion is to find the centerline based on an aggressively smoothed version of your model.  The centerline one wants is usually only minimally perturbed by smoothing the outer boundary, and it can help smooth out undesirable centerline wiggles.</p>

---
