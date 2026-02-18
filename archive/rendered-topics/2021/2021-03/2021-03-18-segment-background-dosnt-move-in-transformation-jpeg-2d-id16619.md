# segment background dosn't move in transformation (JPEG - 2D) +++

**Topic ID**: 16619
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/segment-background-dosnt-move-in-transformation-jpeg-2d/16619

---

## Post #1 by @Freshairfanatic (2021-03-18 14:51 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.11<br>
Expected behavior:<br>
For simmulating an orthognathic operation (here: forewarddisplacement of the mandible (lower jaw))<br>
mark points - create a segment  (Scissors = just outline) - move segment (points in the segment follow along) - rotation of the segment around amanually asigned point - coordinates of the markups acualisize to the new position automatically</p>
<p>Actual behavior:<br>
I did:</p>
<ul>
<li>load an JPEG (2D)</li>
<li>place some markups</li>
<li>create an segement (unfortunately &gt;Paint&lt; because &gt;Scissors&lt; will not work)</li>
<li>transform the segment and the markups in the desired direction</li>
</ul>
<p>Problems that occured (ordered by importance (1th = most important)</p>
<ol>
<li>the background X-ray area under the segment does not move with the segment (green area)</li>
<li>coordinates of the markups in the description (R, A Value) do not change according to the change of position</li>
<li>rotation seems to happen arround the upper left corner of the picture, not where I want it</li>
<li>markups have to be added to the transformed segment manually - they don’t follow automatically (if inside the segment / selection)</li>
</ol>
<p>I am grateful for any help, but problems 1 and 2 are crucial…<br>
Th<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e6b9ed4ef3de79e33bc1f4413430e53ad3a8969.jpeg" data-download-href="/uploads/short-url/bbJOJZHS9aKCZLciXna8n8vqYiZ.jpeg?dl=1" title="Ausgang" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e6b9ed4ef3de79e33bc1f4413430e53ad3a8969_2_690x353.jpeg" alt="Ausgang" data-base62-sha1="bbJOJZHS9aKCZLciXna8n8vqYiZ" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e6b9ed4ef3de79e33bc1f4413430e53ad3a8969_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e6b9ed4ef3de79e33bc1f4413430e53ad3a8969_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e6b9ed4ef3de79e33bc1f4413430e53ad3a8969_2_1380x706.jpeg 2x" data-dominant-color="7D7D7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ausgang</span><span class="informations">2036×1042 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72cdb8fcb992906e2df58aff6fe2e0d4eb0563ae.jpeg" data-download-href="/uploads/short-url/gnBbNrCouKJORJYLoXbrUEZdp5I.jpeg?dl=1" title="Verlagert" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72cdb8fcb992906e2df58aff6fe2e0d4eb0563ae_2_690x374.jpeg" alt="Verlagert" data-base62-sha1="gnBbNrCouKJORJYLoXbrUEZdp5I" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72cdb8fcb992906e2df58aff6fe2e0d4eb0563ae_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72cdb8fcb992906e2df58aff6fe2e0d4eb0563ae_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72cdb8fcb992906e2df58aff6fe2e0d4eb0563ae_2_1380x748.jpeg 2x" data-dominant-color="7C7C7C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Verlagert</span><span class="informations">1918×1040 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> anks a lot in advance</p>
<p>Johannes</p>

---

## Post #2 by @lassoan (2021-03-18 16:23 UTC)

<aside class="quote no-group" data-username="Freshairfanatic" data-post="1" data-topic="16619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e47774/48.png" class="avatar"> Freshairfanatic:</div>
<blockquote>
<p>create an segement (unfortunately &gt;Paint&lt; because &gt;Scissors&lt; will not work)</p>
</blockquote>
</aside>
<p>By default Scissors is in Erase mode. You can set it to fill mode if you want to fill regions with it.</p>
<aside class="quote no-group" data-username="Freshairfanatic" data-post="1" data-topic="16619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e47774/48.png" class="avatar"> Freshairfanatic:</div>
<blockquote>
<p>the background X-ray area under the segment does not move with the segment (green area)</p>
</blockquote>
</aside>
<p>Apply the same transform to both the segmentation, image, and markups.</p>
<aside class="quote no-group" data-username="Freshairfanatic" data-post="1" data-topic="16619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e47774/48.png" class="avatar"> Freshairfanatic:</div>
<blockquote>
<p>coordinates of the markups in the description (R, A Value) do not change according to the change of position</p>
</blockquote>
</aside>
<p>You can choose to see the coordinates in world or local coordinate system (“Transformed” checkbox).</p>
<aside class="quote no-group" data-username="Freshairfanatic" data-post="1" data-topic="16619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e47774/48.png" class="avatar"> Freshairfanatic:</div>
<blockquote>
<p>rotation seems to happen arround the upper left corner of the picture, not where I want it</p>
</blockquote>
</aside>
<p>You can use Fiducial registration wizard (in SlicerIGT extension) to rotate/align objects. If you want to rotate with a slider then you can set up a center of rotation point or rotation axis line as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point">examples in the script repository</a>.</p>
<aside class="quote no-group" data-username="Freshairfanatic" data-post="1" data-topic="16619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/e47774/48.png" class="avatar"> Freshairfanatic:</div>
<blockquote>
<p>markups have to be added to the transformed segment manually - they don’t follow automatically (if inside the segment / selection)</p>
</blockquote>
</aside>
<p>Please clarify. Adding an annotated screenshot can help.</p>
<p>General advice: You can figure out the workflow by using Slicer core modules, and once you know what to do, it is usually worth to create a small Python scripted module to automate the workflow. In the GUI of your module everything is available in one place, you only show the necessary options, and automate everything as much as possible.</p>

---

## Post #3 by @lili-yu22 (2024-06-15 00:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16619">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can choose to see the coordinates in world or local coordinate system (“Transformed” checkbox).</p>
</blockquote>
</aside>
<p>please guide me how can i get the transformed checkbox，being deeply grateful.</p>

---

## Post #4 by @lassoan (2024-06-15 05:21 UTC)

<p>It is in Control Points section in Markups module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/338c91b07210be501563ab8f4508d32d1772008c.png" data-download-href="/uploads/short-url/7m1waDQlkfiuNP0otUrMbPNEXCY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/338c91b07210be501563ab8f4508d32d1772008c_2_595x500.png" alt="image" data-base62-sha1="7m1waDQlkfiuNP0otUrMbPNEXCY" width="595" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/338c91b07210be501563ab8f4508d32d1772008c_2_595x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/338c91b07210be501563ab8f4508d32d1772008c_2_892x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/338c91b07210be501563ab8f4508d32d1772008c_2_1190x1000.png 2x" data-dominant-color="3D444A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1477×1241 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lili-yu22 (2024-06-15 09:35 UTC)

<p>thank you very muchfor your reply</p>

---
