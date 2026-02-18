# Placing landmarks on meshs with geometric constructions

**Topic ID**: 31789
**Date**: 2023-09-19
**URL**: https://discourse.slicer.org/t/placing-landmarks-on-meshs-with-geometric-constructions/31789

---

## Post #1 by @Saggittaman (2023-09-19 13:41 UTC)

<p>Dear all,</p>
<p>I’m working in 3D Slicer to place landmarks on 3D meshs.<br>
I would like to apply something like the figure 1. A of <a href="https://www.publish.csiro.au/MF/pdf/MF15052" rel="noopener nofollow ugc">this paper</a> in 3D, involving projection and landmark as a geometric construction. What is the best way to display a grid for placing landmarks accurately?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @muratmaga (2023-09-19 15:53 UTC)

<p>These types of geometrically constructed landmarks are more tricky to do in 3D. In 2D you standardize the orientation prior to taking the picture and then you lay the grid.</p>
<p>Standardizing the orientation in 3D usually requires a template and registration.</p>
<p>Regardless of the challenges you should be able to do all of those in Slicer with little bit python scripting. I didn’t read the paper in detail, but if you have reference LMs that define those lines, you would being with placing those. Of course in 3D part line connecting those pair of landmarks might end up inside the mesh, so you might have to project onto the axis where you want to create the semi-landmark.</p>
<p>You should start by reviewing the script examples of Markups modules. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>ps. Did you try the semi/pseudoLMing tools in SlicerMorph?</p>

---

## Post #3 by @Saggittaman (2023-09-19 16:10 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a></p>
<p>Indeed - this is easier to standardize in 2D.</p>
<p>We are trying both fewer points (like the hereabove cited study) and high density patches by subsampling the surface with pseudolandmarks then backtransfer them to other meshes as semilandmarks with the R software. We only rely on 3D slicer for ‘standard’ points position and to ‘register’ specimens in R.<br>
I had a look to SlicerMorph module earlier but we build an alternative efficient way in R.</p>
<p>The only problem is to standardize then the grid I want to have as a reference to geometrically link the points… Maybe there’s a way to show a grid on the surface mesh than I can locally align with the most accurate orientation or something alike.</p>
<p>Thank you so much.<br>
Best.</p>

---

## Post #4 by @muratmaga (2023-09-19 16:31 UTC)

<p>You can lay an arbitrary 3D grid on any object using Transform module of slicer (in this screen shot spacing of grid lines is 20mm).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9effcfbd60811ad14c02b8536ebb0268b1667404.jpeg" data-download-href="/uploads/short-url/mGzvRsiKkLZWgIylVmSO6xN3ObW.jpeg?dl=1" title="Screen Shot 2023-09-19 at 9.29.52 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9effcfbd60811ad14c02b8536ebb0268b1667404_2_690x396.jpeg" alt="Screen Shot 2023-09-19 at 9.29.52 AM" data-base62-sha1="mGzvRsiKkLZWgIylVmSO6xN3ObW" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9effcfbd60811ad14c02b8536ebb0268b1667404_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9effcfbd60811ad14c02b8536ebb0268b1667404_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9effcfbd60811ad14c02b8536ebb0268b1667404_2_1380x792.jpeg 2x" data-dominant-color="9E9CB3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-09-19 at 9.29.52 AM</span><span class="informations">3864×2218 1.59 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Saggittaman (2023-09-20 09:08 UTC)

<p>Thank you so much.<br>
It’s working. However, the grid minimal spacing is 1 mm and some of our models are about 2-3 mm and we would like to have something like 0.5-0.2 µm.<br>
Is it feasible ?<br>
Sorry if it is too basic…<br>
Best.</p>

---

## Post #6 by @Saggittaman (2023-09-20 09:09 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ff108520b14bb1af4634d8258351e29c92db2d.png" data-download-href="/uploads/short-url/w6pqrVbMbToleKxNc6cdk31btRb.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ff108520b14bb1af4634d8258351e29c92db2d_2_345x182.png" alt="1" data-base62-sha1="w6pqrVbMbToleKxNc6cdk31btRb" width="345" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ff108520b14bb1af4634d8258351e29c92db2d_2_345x182.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ff108520b14bb1af4634d8258351e29c92db2d_2_517x273.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ff108520b14bb1af4634d8258351e29c92db2d_2_690x364.png 2x" data-dominant-color="7B7F98"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1919×1016 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56de2c0b128d9d50bb32f61f5bd516693323c450.png" data-download-href="/uploads/short-url/cot3XvpweVxmrhoFPWGsYFC1TKo.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56de2c0b128d9d50bb32f61f5bd516693323c450_2_345x176.png" alt="2" data-base62-sha1="cot3XvpweVxmrhoFPWGsYFC1TKo" width="345" height="176" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56de2c0b128d9d50bb32f61f5bd516693323c450_2_345x176.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56de2c0b128d9d50bb32f61f5bd516693323c450_2_517x264.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56de2c0b128d9d50bb32f61f5bd516693323c450_2_690x352.png 2x" data-dominant-color="797EA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×984 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2023-09-20 14:48 UTC)

<p>Yes, I noticed that too for small models.</p>
<p>You can use a trick, first create scaling transform in which diagonals are like 100 100 100 (meaning all axes are scaled by 100). Then create an empty pointList markup up object. Place both markup object and your model under this scaling transform.</p>
<p>Then proceed as before. Once you are done, take model and pointList object out of transform, and the coordinates should be now in the original scale.</p>

---
