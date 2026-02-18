# PRISM Rendering Chroma Depth Perception not working

**Topic ID**: 23361
**Date**: 2022-05-10
**URL**: https://discourse.slicer.org/t/prism-rendering-chroma-depth-perception-not-working/23361

---

## Post #1 by @Connor-Bowley (2022-05-10 16:12 UTC)

<p>I am currently unable to use the Chroma Depth Perception with the sample data as per the <a href="https://githubcomets-vis-interactiveslicerprismrendering.readthedocs.io/en/latest/tutorials.html#chroma-depth-perception" rel="noopener nofollow ugc">tutorial</a>. When looking at the error log, it is saying “Shader failed to compile”.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> You were thinking it is likely an API change in a newer version of VTK? Any idea how to fix this?</p>
<p>Slicer used:<br>
OS: Windows<br>
Preview 5.1.0-2022-05-08 r30927 / 1efef1b</p>

---

## Post #2 by @lassoan (2022-05-10 23:12 UTC)

<p>Yes, there was an API change from VTK8 to VTK9 that impacted ChromaDepthShader. You need to replace <code>computeLighting(c, 0)</code> by <code>computeLighting(color, 0, 0.0)</code> to make it work with VTK9.</p>

---

## Post #3 by @rbumm (2022-05-11 12:11 UTC)

<p>Would like to add that Prism rendering does not work as expected in 5.1-2022-05-10 in terms of “Plane intersecting”:<br>
“Initialize Entry” and “Target Entry” add an ROI rather than a fiducial markup and there is no visible scissor effect in the 3D view.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99a121fdef5fdab26f452eff6d012c68111f1caf.jpeg" alt="image" data-base62-sha1="lV4hg3jWFYSy84UDJ7H5EDv7htd" width="684" height="382"></p>
<p>Closing Slicer displays:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa549527b269c97a3d44566a129e339f90b65902.png" alt="image" data-base62-sha1="zIwAh22OQCRh4IZCqXunjUVL7r4" width="403" height="270"></p>
<p>4.11 works well.</p>

---

## Post #4 by @lassoan (2022-05-11 15:08 UTC)

<p><a class="mention" href="/u/drouin-simon">@drouin-simon</a> could you have a look at these issues?</p>

---
