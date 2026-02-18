# Segment - Area Calculation

**Topic ID**: 14193
**Date**: 2020-10-21
**URL**: https://discourse.slicer.org/t/segment-area-calculation/14193

---

## Post #1 by @Christos_Tzerefos (2020-10-21 20:07 UTC)

<p>I am creating with the segment editor a cranial bone 3D shape. I figure out that the surface are exported to the table corresponds to the whole 3d shape. Is there any way to calculate only one of the surfaces of the 3D object (blue arrow) and not the whole surface?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c57a1ffc39ae6b2eee2b8197cf03c054489b1a6.jpeg" data-download-href="/uploads/short-url/mj4eKav5zUB2B1veHo3raCKTAvI.jpeg?dl=1" title="Inked1_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c57a1ffc39ae6b2eee2b8197cf03c054489b1a6_2_690x486.jpeg" alt="Inked1_LI" data-base62-sha1="mj4eKav5zUB2B1veHo3raCKTAvI" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c57a1ffc39ae6b2eee2b8197cf03c054489b1a6_2_690x486.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9c57a1ffc39ae6b2eee2b8197cf03c054489b1a6_2_1035x729.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c57a1ffc39ae6b2eee2b8197cf03c054489b1a6.jpeg 2x" data-dominant-color="B7BADB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Inked1_LI</span><span class="informations">1248×880 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e3f25db264e30c5169347f6ceeee209efe05cbd.png" data-download-href="/uploads/short-url/221YEwH9AnGLLTjNaUzWjJEYmjb.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e3f25db264e30c5169347f6ceeee209efe05cbd_2_690x481.png" alt="2" data-base62-sha1="221YEwH9AnGLLTjNaUzWjJEYmjb" width="690" height="481" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e3f25db264e30c5169347f6ceeee209efe05cbd_2_690x481.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e3f25db264e30c5169347f6ceeee209efe05cbd_2_1035x721.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e3f25db264e30c5169347f6ceeee209efe05cbd.png 2x" data-dominant-color="B7BADB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1252×873 43.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-10-21 20:21 UTC)

<p>Extracting “one side” of a thin structure is an extremely difficult problem. However, there are many solutions available in Slicer that can be used for particular problems.</p>
<p>For example, you can use Dynamic modeler module to draw a closed curve on one side of the surface. Create a bounding curve on the surface can be automated quite easily, by placing points around the of the boundary - closest points to points far away from the model - in 4-8 directions and connect them using a curve that prefers travelling through high-curvature points.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="nLva95ZF4ko" data-video-title="Extract one side of a closed surface mesh" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=nLva95ZF4ko" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/nLva95ZF4ko/maxresdefault.jpg" title="Extract one side of a closed surface mesh" width="" height="">
  </a>
</div>


---

## Post #3 by @Christos_Tzerefos (2020-10-21 22:14 UTC)

<p>Thank  you for your response. After I have the model of the upper surface of the initial 3D-model,  how I calculate its area in cm^2 ?</p>

---

## Post #4 by @lassoan (2020-10-21 22:27 UTC)

<p>You can find surface area of a model in Models module’s Information section.</p>

---

## Post #5 by @Christos_Tzerefos (2020-10-22 14:24 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a5180f934a7cc2fd50d5934aacf6753692b1df3.png" data-download-href="/uploads/short-url/jJCvKbbG8itwfRj7clf8jecHbi3.png?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5180f934a7cc2fd50d5934aacf6753692b1df3_2_690x247.png" alt="4" data-base62-sha1="jJCvKbbG8itwfRj7clf8jecHbi3" width="690" height="247" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5180f934a7cc2fd50d5934aacf6753692b1df3_2_690x247.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5180f934a7cc2fd50d5934aacf6753692b1df3_2_1035x370.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a5180f934a7cc2fd50d5934aacf6753692b1df3_2_1380x494.png 2x" data-dominant-color="B1AFD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1912×685 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccecdc4f00371246571bc5c315175b976e42f0da.png" data-download-href="/uploads/short-url/teQSh8f1ZBtsSe3zJVIQs7Zh0im.png?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccecdc4f00371246571bc5c315175b976e42f0da_2_690x247.png" alt="5" data-base62-sha1="teQSh8f1ZBtsSe3zJVIQs7Zh0im" width="690" height="247" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccecdc4f00371246571bc5c315175b976e42f0da_2_690x247.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccecdc4f00371246571bc5c315175b976e42f0da_2_1035x370.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccecdc4f00371246571bc5c315175b976e42f0da_2_1380x494.png 2x" data-dominant-color="B2B0D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">1907×684 88.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I managed to create this model_4 (red color), which is part of the surface of my 3d-object.<br>
The surface area calculated by the software corresponds to only one surface of Model_4 or it corresponds to both up and down??</p>

---

## Post #6 by @lassoan (2020-10-22 15:03 UTC)

<p>You already extracted the “top” part of the closed surface, so you don’t need to divide by 2.</p>
<p>Note that you can skip the Scissors step in Segment Editor and just draw the closed curve directly on the extracted complete skull.</p>

---

## Post #7 by @Christos_Tzerefos (2020-10-22 15:12 UTC)

<p>So better draw the closed curve on the skull after i create the skull-model with the threshold?<br>
The volume corresponds to what?</p>

---

## Post #8 by @lassoan (2020-10-22 16:43 UTC)

<p>Volume that Models module computes is only applicable for closed surfaces. If you have any opening on the surface then the meaning is undefined.</p>

---

## Post #9 by @Christos_Tzerefos (2020-10-23 18:34 UTC)

<p>I have two other questions a little bit irrelevant? Should I create 2 different topics ?</p>

---

## Post #10 by @lassoan (2020-10-23 18:37 UTC)

<p>Yes, please create a new forum topic for each independent question you would like to discuss.</p>

---
