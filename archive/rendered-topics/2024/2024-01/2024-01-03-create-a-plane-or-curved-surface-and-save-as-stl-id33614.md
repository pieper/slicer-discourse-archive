---
topic_id: 33614
title: "Create A Plane Or Curved Surface And Save As Stl"
date: 2024-01-03
url: https://discourse.slicer.org/t/33614
---

# Create a plane or curved surface and save as STL

**Topic ID**: 33614
**Date**: 2024-01-03
**URL**: https://discourse.slicer.org/t/create-a-plane-or-curved-surface-and-save-as-stl/33614

---

## Post #1 by @johny723 (2024-01-03 22:14 UTC)

<p>How do I create a plane or a bezier surface and export it as STL? Thanks.</p>

---

## Post #2 by @muratmaga (2024-01-04 02:56 UTC)

<p>Did you look into the SurfaceMarkups extension? I think it is exactly what you want.</p>

---

## Post #3 by @johny723 (2024-01-06 00:33 UTC)

<p>I have some progress. Surprisingly, I managed to figure out how to create a grid surface. But when I saved it as an .stl file, the resulting plane is only only one point thin. Which is OK on screen, but rather impossible to 3d print.<br>
<strong>How do I increase the thickness/width of these planes?</strong><br>
Markups to Models does not seem to be the right tool. It changes a plane<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9cd0d95ab6aac43d7ce3b97ae63e4dd03b34b00.png" data-download-href="/uploads/short-url/zDQdhNtwh5rSUJCqtmVrHbdCXaE.png?dl=1" title="Snímka obrazovky 2024-01-06 012522" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9cd0d95ab6aac43d7ce3b97ae63e4dd03b34b00_2_690x440.png" alt="Snímka obrazovky 2024-01-06 012522" data-base62-sha1="zDQdhNtwh5rSUJCqtmVrHbdCXaE" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9cd0d95ab6aac43d7ce3b97ae63e4dd03b34b00_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9cd0d95ab6aac43d7ce3b97ae63e4dd03b34b00_2_1035x660.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9cd0d95ab6aac43d7ce3b97ae63e4dd03b34b00.png 2x" data-dominant-color="9B9ECE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2024-01-06 012522</span><span class="informations">1370×875 30.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
to either this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355cbc05253c1262fc5fc02f41a12ab676eed4a6.png" data-download-href="/uploads/short-url/7C3Zi7hnyTFNAmXwB55gX5o78Sa.png?dl=1" title="Snímka obrazovky 2024-01-06 012654" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355cbc05253c1262fc5fc02f41a12ab676eed4a6_2_690x437.png" alt="Snímka obrazovky 2024-01-06 012654" data-base62-sha1="7C3Zi7hnyTFNAmXwB55gX5o78Sa" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355cbc05253c1262fc5fc02f41a12ab676eed4a6_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/355cbc05253c1262fc5fc02f41a12ab676eed4a6_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/355cbc05253c1262fc5fc02f41a12ab676eed4a6.png 2x" data-dominant-color="9C9EC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2024-01-06 012654</span><span class="informations">1366×867 42.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
or this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab2c0d466519a522f49c5ba30c6acdcb2d93e6f.png" data-download-href="/uploads/short-url/vcH44cN4gdSPbglubwHZe7xwSe3.png?dl=1" title="Snímka obrazovky 2024-01-06 013154" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dab2c0d466519a522f49c5ba30c6acdcb2d93e6f_2_689x441.png" alt="Snímka obrazovky 2024-01-06 013154" data-base62-sha1="vcH44cN4gdSPbglubwHZe7xwSe3" width="689" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dab2c0d466519a522f49c5ba30c6acdcb2d93e6f_2_689x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/dab2c0d466519a522f49c5ba30c6acdcb2d93e6f_2_1033x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/dab2c0d466519a522f49c5ba30c6acdcb2d93e6f.png 2x" data-dominant-color="9EA1C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2024-01-06 013154</span><span class="informations">1371×877 35.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
. Thank you.</p>

---

## Post #4 by @muratmaga (2024-01-06 01:27 UTC)

<ol>
<li>Convert the output of the Markups2Models output to a segmentation object by right-clicking and selecting the relevant option</li>
<li>In the Segment Editor, use the WarpSurfaceSolidy effect to increase the thickness of the shell. (This is a separate extension, you need to install)</li>
<li>Re-export the segmentation as a model object.</li>
</ol>

---

## Post #5 by @johny723 (2024-01-06 11:59 UTC)

<p>Sorry, but I do not understand how to convert a model to a segmentation.</p>
<p>When I used Segment editor and its function to import models to segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e0a2c79c345290babd8f1eef3aab7e7926199f.png" data-download-href="/uploads/short-url/kXkZqByFoyuLjuUJpLt4RYCwwB9.png?dl=1" title="Snímka obrazovky 2024-01-06 131029" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92e0a2c79c345290babd8f1eef3aab7e7926199f_2_690x360.png" alt="Snímka obrazovky 2024-01-06 131029" data-base62-sha1="kXkZqByFoyuLjuUJpLt4RYCwwB9" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92e0a2c79c345290babd8f1eef3aab7e7926199f_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e0a2c79c345290babd8f1eef3aab7e7926199f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92e0a2c79c345290babd8f1eef3aab7e7926199f.png 2x" data-dominant-color="E0E4EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2024-01-06 131029</span><span class="informations">846×442 36.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
It turned the grid surface from this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abd73e7ea1fe15da090332dd04b3db03b0366643.png" data-download-href="/uploads/short-url/owaNXFNfdbOSOvFtRWjRso9bBRx.png?dl=1" title="Snímka obrazovky 2024-01-06 130713" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abd73e7ea1fe15da090332dd04b3db03b0366643_2_689x483.png" alt="Snímka obrazovky 2024-01-06 130713" data-base62-sha1="owaNXFNfdbOSOvFtRWjRso9bBRx" width="689" height="483" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abd73e7ea1fe15da090332dd04b3db03b0366643_2_689x483.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abd73e7ea1fe15da090332dd04b3db03b0366643_2_1033x724.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abd73e7ea1fe15da090332dd04b3db03b0366643.png 2x" data-dominant-color="B7B89B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2024-01-06 130713</span><span class="informations">1237×867 38.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
to this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53d58a0b8725c10deb19f33859a82a0ea66ac1e0.png" data-download-href="/uploads/short-url/bXD8pQlGkgrdCujkLB3jwiqCADK.png?dl=1" title="Snímka obrazovky 2024-01-06 130635" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d58a0b8725c10deb19f33859a82a0ea66ac1e0_2_689x467.png" alt="Snímka obrazovky 2024-01-06 130635" data-base62-sha1="bXD8pQlGkgrdCujkLB3jwiqCADK" width="689" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d58a0b8725c10deb19f33859a82a0ea66ac1e0_2_689x467.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53d58a0b8725c10deb19f33859a82a0ea66ac1e0_2_1033x700.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53d58a0b8725c10deb19f33859a82a0ea66ac1e0.png 2x" data-dominant-color="AAACAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2024-01-06 130635</span><span class="informations">1237×839 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What am I doing wrong?</p>

---

## Post #6 by @muratmaga (2024-01-06 17:28 UTC)

<aside class="quote no-group" data-username="johny723" data-post="5" data-topic="33614">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/7ea924/48.png" class="avatar"> johny723:</div>
<blockquote>
<p>When I used Segment editor and its function to import models to segmentation</p>
</blockquote>
</aside>
<p>The source volume you specified probably has a low resolution. You need to increase that. Please read the relevant sections of the documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#editing-a-segmentation-imported-from-model-surface-mesh-file" class="inline-onebox">Segmentations — 3D Slicer documentation</a></p>

---

## Post #7 by @johny723 (2024-01-07 00:10 UTC)

<p>I increased resolution the way you suggested, but it does not work. The results are the same as with normal resolution. The curved plane is broken into parts.</p>
<p>Is there any other way to make a plane or grid surface homogenously thicker and 3d printable?</p>

---

## Post #8 by @muratmaga (2024-01-07 05:28 UTC)

<p>What do you get when you right-click on the 3D surface model, and choose <strong>Convert Model to Segmentation Node</strong></p>
<p>to me, the end result seems fairly good. (yellow original model, dark red is the segmentation object)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71e66605cf4be36b740438740cfcfaf553441559.png" data-download-href="/uploads/short-url/gfBA0jmXSkRs5eIj4ggMUL08BVn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71e66605cf4be36b740438740cfcfaf553441559_2_690x379.png" alt="image" data-base62-sha1="gfBA0jmXSkRs5eIj4ggMUL08BVn" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71e66605cf4be36b740438740cfcfaf553441559_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71e66605cf4be36b740438740cfcfaf553441559_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71e66605cf4be36b740438740cfcfaf553441559_2_1380x758.png 2x" data-dominant-color="ACA8BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3088×1698 492 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @johny723 (2024-01-08 00:32 UTC)

<p>Yes, but is the object created from the curved plane uniformly thick? Or does it have areas of thicker parts where the curvature was higher, and thinner parts, where the curve was more flat and straight ? Because that is all I always get. I need a resulting plane to be of the same thickness in curves as it is in areas where it is flat and straight, but it seems impossible for me.</p>
<p>I would like to make 3d printed models and highlight segments segments in parenchymatous organs by creating dividing planes within the organs. Thats why I need those “planes” to be of the same thickness.</p>
<p>I hope you understand what I am trying to say.</p>
<p>I am sure it is not difficult in 3d slicer, but so far I have been too stupid to figure it out…</p>
<p>I would love to see Markups to models offering not only a closed surfaces and curves, but also curved planes. Or some tool in segment editor or somewhere else to make a planar segment of a uniform thickness according to model from the grid surface.</p>

---

## Post #10 by @muratmaga (2024-01-08 00:53 UTC)

<aside class="quote no-group" data-username="johny723" data-post="9" data-topic="33614">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/7ea924/48.png" class="avatar"> johny723:</div>
<blockquote>
<p>Yes, but is the object created from the curved plane uniformly thick?</p>
</blockquote>
</aside>
<p>I don’t know anything about 3D printing, so take my comments with a grain of salt.</p>
<p>I think you are almost there, just run this segmentation with the <code>SurfaceWrapSolidy</code> (search the extension manager), which let’s you extract a "shell’ with specified thickness. I believe that’s what you want.</p>
<p>To do that, you do need a Source Volume, which you can easily create by right-clicking the segmentation you generated from the surface, and by choosing the “export the segmentation as a labelmap”. In the segment editor, set this newly created labelmap as your source volume, and then play with the various parameters of the SurfaceWrapSolidy effect in the segment editor (after you install the extension).</p>

---

## Post #11 by @muratmaga (2024-01-08 01:10 UTC)

<p>Something like this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9e60069a5a02b39867d39501b1d7d7897bf3079.jpeg" data-download-href="/uploads/short-url/sO4KmjIgknzkFBLREsxjS7J77vz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9e60069a5a02b39867d39501b1d7d7897bf3079_2_690x323.jpeg" alt="image" data-base62-sha1="sO4KmjIgknzkFBLREsxjS7J77vz" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9e60069a5a02b39867d39501b1d7d7897bf3079_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9e60069a5a02b39867d39501b1d7d7897bf3079_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9e60069a5a02b39867d39501b1d7d7897bf3079_2_1380x646.jpeg 2x" data-dominant-color="9898BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1998×938 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @johny723 (2024-01-08 20:51 UTC)

<p>Yes. Something like that. The rough surface and uneven edges can be smoothed, but my point is to create not just a single point thin plane, but an object with a defined uniform thicknessbased on that plane. What did you do to achieve this result? Thanks</p>

---

## Post #13 by @muratmaga (2024-01-08 20:55 UTC)

<p>I used the same procedure I described above,</p>
<ol>
<li>Use the SurfaceMarkups to cut a surface from a 3D model. This is like an egg-shell, there is no thickness.</li>
<li>Convert this model to a segmentaiton object</li>
<li>Adjust the geometry of the segmentation object (increase the resolution)</li>
<li>Use the SurfaceWrapSolidy effect to extract a model with thickness (in this case 0.25mm)</li>
</ol>

---

## Post #14 by @johny723 (2024-01-08 21:11 UTC)

<p>Which oversampling factor do you use? My pc 3d slicer keeps crashing when increasing the resolution.</p>

---

## Post #15 by @muratmaga (2024-01-08 21:39 UTC)

<p>In my case, I actually undersampled (0.5). It was a very high-resolution model, and I wanted things go fast.</p>
<p>If Slicer is crashing you might be running out of memory. What was the original reported segmentation geometry and what oversampling did you use? Remember memory usage increases with the cubic size of oversampling factor.</p>

---

## Post #16 by @mau_igna_06 (2024-01-09 00:41 UTC)

<p>Maybe use one of the Dynamic modeler tools to extrude our your surface</p>
<p>Hope it helps</p>

---

## Post #17 by @lassoan (2024-01-19 16:39 UTC)

<p>Suggestion of <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> should be a good solution for you.</p>
<p>I would just mention that in cases when you want to start your warped surface from a boundary curve then you can use <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/BafflePlanner.md">Baffle Planner module</a> in SlicerHeart extension to create the model. You can specify a thickness if you want to 3D print it.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="AigTwMYRI1Y" data-video-title="Design surface patches using new Baffle Planner module" data-video-start-time="15s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=AigTwMYRI1Y&amp;t=15s" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/AigTwMYRI1Y/maxresdefault.jpg" title="Design surface patches using new Baffle Planner module" width="" height="">
  </a>
</div>


---

## Post #18 by @johny723 (2024-01-24 20:40 UTC)

<p>Guys, you are awesome! Thank you, it finally works!</p>

---
