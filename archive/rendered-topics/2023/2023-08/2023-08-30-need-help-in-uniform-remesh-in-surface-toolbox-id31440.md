# Need help in Uniform remesh in Surface Toolbox

**Topic ID**: 31440
**Date**: 2023-08-30
**URL**: https://discourse.slicer.org/t/need-help-in-uniform-remesh-in-surface-toolbox/31440

---

## Post #1 by @telomere (2023-08-30 01:06 UTC)

<p>Hi.<br>
When applying undercut remove or making a base of dental model, the side walls consist of too long voxels. So I want to remesh uniformly.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23a144199245920ef00cc3597762623e2459b717.jpeg" data-download-href="/uploads/short-url/55cdMyDZ6FDO64FcW2EBWNj8vZ5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23a144199245920ef00cc3597762623e2459b717_2_690x164.jpeg" alt="image" data-base62-sha1="55cdMyDZ6FDO64FcW2EBWNj8vZ5" width="690" height="164" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23a144199245920ef00cc3597762623e2459b717_2_690x164.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23a144199245920ef00cc3597762623e2459b717_2_1035x246.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23a144199245920ef00cc3597762623e2459b717.jpeg 2x" data-dominant-color="C8C850"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1302×311 90.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The first image above is the dental model where undercut remove and base making are done with meshmixer. The uniform remesh in surface toolbox works well. You can see the long voxels got splitted fine.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3db846cbc3dc4979510bde15c9e52be6e0ea52bd.png" data-download-href="/uploads/short-url/8NZW3r3ZFlBHt6IwE7Ui7pNqhvn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3db846cbc3dc4979510bde15c9e52be6e0ea52bd_2_690x157.png" alt="image" data-base62-sha1="8NZW3r3ZFlBHt6IwE7Ui7pNqhvn" width="690" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3db846cbc3dc4979510bde15c9e52be6e0ea52bd_2_690x157.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3db846cbc3dc4979510bde15c9e52be6e0ea52bd_2_1035x235.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3db846cbc3dc4979510bde15c9e52be6e0ea52bd.png 2x" data-dominant-color="BCA270"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1309×299 93.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The second image is worked by the same(undercut remove) by blender. The method of removing undercut is different. But in this model, uniform remesh doesn’t work. You can see the long side wall voxels are just the same with before.</p>
<p>Both models are not closed model, which mean it is open surface. I first thought the open surface status is the problem so I filled the base to make it a closed model but it didn’t work.</p>
<p>What is the reason and what is the solution?<br>
Thanks always.</p>

---

## Post #2 by @tsehrhardt (2023-08-30 12:59 UTC)

<p>Did you try the Remesh tools in Meshmixer or Blender?</p>

---

## Post #3 by @telomere (2023-08-30 13:36 UTC)

<p>Yes.<br>
It works well in Meshmixer but it would be the best if it works in slicer because it will make me not have to switch to meshmixer and come back to slicer.<br>
In blender, remesh modifier doesn’t work and quadriflow remesh takes too much time like more than 6 hours…</p>

---

## Post #4 by @tsehrhardt (2023-08-30 13:57 UTC)

<p>I see. You might try the cutting tools in Slicer (Dynamic Modeler) to see if that gives you a better output than Meshmixer, then use the remeshing.</p>

---

## Post #5 by @telomere (2023-08-30 14:17 UTC)

<p>Thanks for the reply.<br>
I think you’re saying to use ‘plane cut’ in Dynamic modeler so to reduce the length of side walls.<br>
I’ve already tried but not working.<br>
Thanks anyway.</p>

---

## Post #6 by @tsehrhardt (2023-08-30 15:58 UTC)

<p>Dynamic Modeler also has curves. There is a “Combine Models” feature for Boolean operations as well if you install the Sandbox Extension. <a href="https://youtu.be/2MOAk2oNbKw?si=axRiZtOwbATdNCvI" rel="noopener nofollow ugc">https://youtu.be/2MOAk2oNbKw?si=axRiZtOwbATdNCvI</a></p>

---

## Post #7 by @telomere (2023-08-30 23:36 UTC)

<p>Sorry. I don’t get your suggestion. How would Combine Models features for Boolean operation solve my problem?</p>

---

## Post #8 by @tsehrhardt (2023-08-31 01:05 UTC)

<p>Since Meshmixer and Blender are giving you a bad model after cutting (I don’t know how you’re cutting but it looks like a Boolean operation with a cylinder), rather than trying to fix the bad model, you can try something in Slicer to perform the cutting instead so maybe you won’t have a bad model that needs fixing. It might be helpful to know which cutting tools in Meshmixer and Blender you are using since there are several ways to cut a model in both programs.</p>
<p>If you are segmenting the model in Slicer to begin with, “cutting” it with tools in the Segment Editor might give better results than cutting the exported 3D model.</p>

---

## Post #9 by @tsehrhardt (2023-08-31 17:01 UTC)

<p>Actually, are you extruding after cutting? One thing you can do after you select the surface you want to extrude, is use “Modify-&gt; Smooth Boundary.” This reduces the number of vertices along the edge or at least spaces them out better, then you can extrude with density of 0 or 1. Then you can select the whole mesh and Remesh.</p>
<p>Before Smooth Boundary:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/518ce9474eef1f9747eb8d39ee7c51e05784e956.jpeg" data-download-href="/uploads/short-url/bDqzIm2axkH3ASxosu1iJZ4JouW.jpeg?dl=1" title="2023-08-31_12-58-00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/518ce9474eef1f9747eb8d39ee7c51e05784e956_2_579x500.jpeg" alt="2023-08-31_12-58-00" data-base62-sha1="bDqzIm2axkH3ASxosu1iJZ4JouW" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/518ce9474eef1f9747eb8d39ee7c51e05784e956_2_579x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/518ce9474eef1f9747eb8d39ee7c51e05784e956_2_868x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/518ce9474eef1f9747eb8d39ee7c51e05784e956_2_1158x1000.jpeg 2x" data-dominant-color="6B6865"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-08-31_12-58-00</span><span class="informations">1920×1656 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After Smooth Boundary:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d762601662b3abc9a33f1cb8a99117d52f132609.jpeg" data-download-href="/uploads/short-url/uJnqjb0SQGqBHhplbkCDEgl215f.jpeg?dl=1" title="2023-08-31_12-58-36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d762601662b3abc9a33f1cb8a99117d52f132609_2_579x500.jpeg" alt="2023-08-31_12-58-36" data-base62-sha1="uJnqjb0SQGqBHhplbkCDEgl215f" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d762601662b3abc9a33f1cb8a99117d52f132609_2_579x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d762601662b3abc9a33f1cb8a99117d52f132609_2_868x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d762601662b3abc9a33f1cb8a99117d52f132609_2_1158x1000.jpeg 2x" data-dominant-color="6A6561"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-08-31_12-58-36</span><span class="informations">1920×1656 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Extruding after Smooth Boundary:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83fcca04914700ca393472efc522e3288ed5c37a.jpeg" data-download-href="/uploads/short-url/iPC96tGAWKoMyCQSTqSyZ3jjWcO.jpeg?dl=1" title="2023-08-31_12-48-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fcca04914700ca393472efc522e3288ed5c37a_2_579x500.jpeg" alt="2023-08-31_12-48-01" data-base62-sha1="iPC96tGAWKoMyCQSTqSyZ3jjWcO" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fcca04914700ca393472efc522e3288ed5c37a_2_579x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fcca04914700ca393472efc522e3288ed5c37a_2_868x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83fcca04914700ca393472efc522e3288ed5c37a_2_1158x1000.jpeg 2x" data-dominant-color="837464"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-08-31_12-48-01</span><span class="informations">1920×1656 361 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
