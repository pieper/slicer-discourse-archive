# How to generate a cut plane using markups

**Topic ID**: 44905
**Date**: 2025-10-28
**URL**: https://discourse.slicer.org/t/how-to-generate-a-cut-plane-using-markups/44905

---

## Post #1 by @Davi_Matos (2025-10-28 22:43 UTC)

<p>Hello, I’ve been searching for a way to generate cutting planes through curved mark up. First I’ve found two ways of generating those curved markups (1st pic is the surface markup extension and 2nd pic is the surface cut on segmentation editor). But none of those option s provide me with a cut plane. What I want is to generate a cut plane that can cut strutures above that plane, very similar to thee 3rd pic. Is there a way to do something like this on slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6047dad77749a4192560966c2df8ee7ce54f5a6.jpeg" data-download-href="/uploads/short-url/wOPrhfKJ3kAa1wVeio0QkCQ1acu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6047dad77749a4192560966c2df8ee7ce54f5a6_2_570x500.jpeg" alt="image" data-base62-sha1="wOPrhfKJ3kAa1wVeio0QkCQ1acu" width="570" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/6/e6047dad77749a4192560966c2df8ee7ce54f5a6_2_570x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6047dad77749a4192560966c2df8ee7ce54f5a6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6047dad77749a4192560966c2df8ee7ce54f5a6.jpeg 2x" data-dominant-color="998CC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">779×683 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e39f7d9405cbaf5df9a95882759461cb3e16c713.jpeg" data-download-href="/uploads/short-url/wtE5KksLsyRFVOU7dSBkat5zvuX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e39f7d9405cbaf5df9a95882759461cb3e16c713_2_690x478.jpeg" alt="image" data-base62-sha1="wtE5KksLsyRFVOU7dSBkat5zvuX" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e39f7d9405cbaf5df9a95882759461cb3e16c713_2_690x478.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e39f7d9405cbaf5df9a95882759461cb3e16c713_2_1035x717.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e39f7d9405cbaf5df9a95882759461cb3e16c713.jpeg 2x" data-dominant-color="9B91C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1043×723 66.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b9f9e4a46643775d107faa3fb521f9c6bd71c85.jpeg" data-download-href="/uploads/short-url/aMZN2rEng7nWX8xW43L4TXTNzzT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b9f9e4a46643775d107faa3fb521f9c6bd71c85_2_690x379.jpeg" alt="image" data-base62-sha1="aMZN2rEng7nWX8xW43L4TXTNzzT" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b9f9e4a46643775d107faa3fb521f9c6bd71c85_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b9f9e4a46643775d107faa3fb521f9c6bd71c85_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b9f9e4a46643775d107faa3fb521f9c6bd71c85.jpeg 2x" data-dominant-color="BABFBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×570 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Davi_Matos (2025-10-28 22:47 UTC)

<p>I know that SlicerLiver extension from <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can do something similar to this, where a markup can creat a Bezier Surface to make a ressection trajectory, but I don’t think I can apply this to this case on a mandible. At least I was not able to.</p>

---

## Post #3 by @RafaelPalomar (2025-11-18 07:04 UTC)

<p><a class="mention" href="/u/davi_matos">@Davi_Matos</a> in Slicer-Liver we do something similar, but I’m not sure you can take advantage from it directly, as it is very oriented to liver resections (one assumption is homogeneous tissue, in your fig3 there seem to be more; one requirement is having both segmentation and surface mesh). There are some discussion on the topic here: <a href="https://discourse.slicer.org/t/beginner-question-liver-volumetry/33887/9" class="inline-onebox">Beginner question: liver volumetry - #9 by RuoyanMeng</a></p>
<p>In my view, it is possible to achieve what you want using 3D Slicer, but you need to develop your own specialized tools for the task. A procedure to do this may look like this:</p>
<p>(1) Place surface markups/bezier surface in 3D space at the desired location.</p>
<p>(2) Create a temporary segmentation (copy) to work the separation</p>
<p>(3) Transfer the surface to image space by evaluating a high-resolution evaluation of if and setting the voxels intersected with a value. This will create a barrier in the segmentation.</p>
<p>(4) Apply a region growing on either of the sides, for this you typically need a seed point, but if your segmentation contains structures which are always on a certain side of the cut, you can use those. This would leave you with a mask that you can use for separation in image space, later you can reconstruct the 3D surface, if needed.</p>
<p>I hope this helps.</p>

---

## Post #4 by @cpinter (2025-11-18 11:27 UTC)

<p>The Grid Surface markup has the option to choose the output surface model:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cefcfe9562cf5d3e9839f43f9c4192bd309922f.png" data-download-href="/uploads/short-url/k6MDK8fZZyRjkm5bLM33EiKQ9zh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cefcfe9562cf5d3e9839f43f9c4192bd309922f.png" alt="image" data-base62-sha1="k6MDK8fZZyRjkm5bLM33EiKQ9zh" width="594" height="383"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">594×383 13.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then you’ll have a model node that you can use for cutting. Not sure if it solves your problem.</p>

---
