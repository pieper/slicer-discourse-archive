# Mesh to mesh intersection 3D Slicer

**Topic ID**: 5676
**Date**: 2019-02-07
**URL**: https://discourse.slicer.org/t/mesh-to-mesh-intersection-3d-slicer/5676

---

## Post #1 by @nish91 (2019-02-07 12:52 UTC)

<p>Dear developers,<br>
I have two VTK mesh models in 3D Slicer as shown in the figure. One of them is the brain model of the MRI data which is rendered using the Marching Cubes algorithm while the other model in color is the model generated within the intraoperative trepanation boundary  which is the exposed brain surface during the surgery. As you see, the intraoperative model is slightly above  the brain surface. This is because the intraoperative points were acquired from the skull surface and not brain surface. Now I just want the points of the intersection of intraoperative model and the brain surface something like shown in the second figure. Could anyone let me know how I can achieve this in 3D Slicer? Thanks!</p>
<p><a href="/uploads/short-url/1BpAt3EjVza62hZG5IQISLn569y.png">Selection_052|508x500</a> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e2c3ab7e7ea17ba035832eab93a3fdd1d4a777.jpeg" data-download-href="/uploads/short-url/ze3itOuXmdBAJZPak5tU0tAmxRJ.jpeg?dl=1" title="Projection" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e2c3ab7e7ea17ba035832eab93a3fdd1d4a777_2_690x459.jpeg" alt="Projection" data-base62-sha1="ze3itOuXmdBAJZPak5tU0tAmxRJ" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e2c3ab7e7ea17ba035832eab93a3fdd1d4a777_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6e2c3ab7e7ea17ba035832eab93a3fdd1d4a777_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6e2c3ab7e7ea17ba035832eab93a3fdd1d4a777.jpeg 2x" data-dominant-color="605967"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Projection</span><span class="informations">1310×872 421 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-02-07 13:56 UTC)

<p>You can import both meshes into a Segmentation node, then use Logical operators effect in Segment Editor to compute intersection. You can use Margin effect on the intraoperative model if you want to increase the amount of overlap between the segments.</p>

---

## Post #3 by @nish91 (2019-02-07 15:25 UTC)

<p>Thanks for your reply. Actually I tried using segment editor with the intersect option in Logical operator however I cannot get the image as shown in my question post. I think I missed my first figure in my previous post. The image below is what I have currently but I want to compute the intersection of the both model and just get the surface surrounding it. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b3cd57a795537c17079b9dcb83c9adc5865e250.png" data-download-href="/uploads/short-url/1BpAt3EjVza62hZG5IQISLn569y.png?dl=1" title="Selection_052" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b3cd57a795537c17079b9dcb83c9adc5865e250_2_508x500.png" alt="Selection_052" data-base62-sha1="1BpAt3EjVza62hZG5IQISLn569y" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b3cd57a795537c17079b9dcb83c9adc5865e250_2_508x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b3cd57a795537c17079b9dcb83c9adc5865e250_2_762x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b3cd57a795537c17079b9dcb83c9adc5865e250.png 2x" data-dominant-color="9093C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Selection_052</span><span class="informations">946×931 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-02-07 16:27 UTC)

<aside class="quote no-group" data-username="nish91" data-post="3" data-topic="5676">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/da6949/48.png" class="avatar"> nish91:</div>
<blockquote>
<p>want to compute the intersection of the both model</p>
</blockquote>
</aside>
<p>What is the “both model”?</p>
<aside class="quote no-group" data-username="nish91" data-post="3" data-topic="5676">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/da6949/48.png" class="avatar"> nish91:</div>
<blockquote>
<p>and just get the surface surrounding it.</p>
</blockquote>
</aside>
<p>What do you mean by “surface surrounding it”? Segments are represented as surfaces as well and you can export segment to surface model using Export/Import section in Segmentations module.</p>
<p>Maybe you could attach a few more screenshots of what you would like to have as an end result (from different views, with different display settings) because from the ones above it is not yet clear.</p>

---

## Post #5 by @nish91 (2019-02-08 10:18 UTC)

<p>Dear Andras Lasso,<br>
Sorry for not making myself clear. Let me try to explain the problem in a simpler manner:</p>
<ol>
<li>
<p>Well as you see in the left side of the below figure, I have an intraoperative mesh model which is orange in color and brain mesh model which is showcased in green. After using the Intersect + Smoothing operations of Segment editor, I was successfully able to extract the intersection of the models giving me a new intraoperative model as shown in the right figure. As you see, the new intraoperative model goes till the tip of the cone starting from the surface of the brain model. However, I would like to extract only the vertices of the intraoperative model which is at the surface of the brain model.</p>
</li>
<li>
<p>Secondly, after I have extracted vertices at the surface of the brain model, I would like to find out the MRI intensities at those vertices so that I could interpolate those intensities on a 2D image grid.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aed38a74adb7e3287e20f3e8cc90aec667b8b87.png" data-download-href="/uploads/short-url/67KitJ3rpbaVYfKDBNiFvMUROaX.png?dl=1" title="Selection_058" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aed38a74adb7e3287e20f3e8cc90aec667b8b87_2_690x188.png" alt="Selection_058" data-base62-sha1="67KitJ3rpbaVYfKDBNiFvMUROaX" width="690" height="188" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aed38a74adb7e3287e20f3e8cc90aec667b8b87_2_690x188.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2aed38a74adb7e3287e20f3e8cc90aec667b8b87_2_1035x282.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2aed38a74adb7e3287e20f3e8cc90aec667b8b87.png 2x" data-dominant-color="B5B0B4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Selection_058</span><span class="informations">1154×316 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2019-02-08 14:51 UTC)

<p>You may use Mask volume effect (provided by SegmentEditorExtraEffects extension) to set MRI intensities to -1000 outside the resection region, then use “Probe volume with model” module on the masked volume with the full brain surface model to get image intensities of the brain surface. You can set up display of probe volume output in Modules module to hide very low intensities (so the regions that were set to -1000 will be cut away).</p>

---
