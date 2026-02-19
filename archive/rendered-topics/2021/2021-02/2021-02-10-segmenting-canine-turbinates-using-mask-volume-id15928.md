---
topic_id: 15928
title: "Segmenting Canine Turbinates Using Mask Volume"
date: 2021-02-10
url: https://discourse.slicer.org/t/15928
---

# Segmenting canine turbinates using mask volume

**Topic ID**: 15928
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/segmenting-canine-turbinates-using-mask-volume/15928

---

## Post #1 by @Dexter777 (2021-02-10 00:49 UTC)

<p>Hi everyone,<br>
I want to segment the turbinates from a canine. Turbinates are typically thin interconnected tissue/bone . I’m using the mask volume segmentation tool &amp; Paint to isolate the turbinates from the bones of the skull. My segmentation is not interconnected. Is this the correct segmentation tool to use or how would you interconnect the tissue?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a679db19382937ed855a5d34e072829d6f708e9e.jpeg" data-download-href="/uploads/short-url/nKIkLXp3hAJgDXWV9xd8eoaFZQW.jpeg?dl=1" title="Mask Volume-turbinates.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a679db19382937ed855a5d34e072829d6f708e9e_2_690x378.jpeg" alt="Mask Volume-turbinates.PNG" data-base62-sha1="nKIkLXp3hAJgDXWV9xd8eoaFZQW" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a679db19382937ed855a5d34e072829d6f708e9e_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a679db19382937ed855a5d34e072829d6f708e9e_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a679db19382937ed855a5d34e072829d6f708e9e_2_1380x756.jpeg 2x" data-dominant-color="929497"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Mask Volume-turbinates.PNG</span><span class="informations">1834×1007 425 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-10 13:20 UTC)

<p>These bones are so thin that due to partial volume effect they may be hardly distinguishable from image noise at usual CT resolutions. What is your overall goal - rendering, 3D printing, quantitative analysis, …? What are your time constraints (how many data sets do you need to process and much time you can spend with each)?</p>

---

## Post #3 by @Dexter777 (2021-02-10 14:45 UTC)

<p>My goal is to 3D print the turbinates in the skull to show the reduction of the nasal cancer from stereotactic radiation treatment.  The nasal cancer was much easier to segment/print as it was a mass filed with mucosa. I segmented that by setting the threshold values and using Paint. The turbinates are so thin, I’m thinking I will need to thicken them internally so I can print them. I will have two segmentations-the skull and turbinates. I have a week to segment the turbinates and print both sides of the skull.</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbb8ec571649745a41d27717d72b54c5be622825.jpeg" data-download-href="/uploads/short-url/qMFtX4S0NqPBM3nb1bJJ4kk6Xhb.jpeg?dl=1" title="Right side mock up_richard.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbb8ec571649745a41d27717d72b54c5be622825_2_690x439.jpeg" alt="Right side mock up_richard.PNG" data-base62-sha1="qMFtX4S0NqPBM3nb1bJJ4kk6Xhb" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbb8ec571649745a41d27717d72b54c5be622825_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbb8ec571649745a41d27717d72b54c5be622825_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bbb8ec571649745a41d27717d72b54c5be622825_2_1380x878.jpeg 2x" data-dominant-color="616055"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Right side mock up_richard.PNG</span><span class="informations">1652×1053 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2021-02-10 16:13 UTC)

<p>If you only going to do this one, and anatomical accuracy is important, I think manual segmentation is the way to go. Your initial segmentation seems to based on thresholding, and such it is a mixture of things including turbinates, cartilage, but also missing for some reason part of ethmoid plate and smaller turbinals.</p>
<p>While they are complex, the morphology changes gradually from slice to slice. If you carefully outline in a one slice using manual paint/draw options, skip a few and do the same on another, you can use the ‘fill between slices’ to interpolate skipped sections.</p>
<p>This of course doesn’t work very well, if you are going to do this routinely.<br>
Then perhaps you can play with the segmentation geometry</p>

---

## Post #5 by @lassoan (2021-02-10 17:08 UTC)

<p>I agree, if it is a one-off then the fastest solution overall is to use manual or semi-automatic methods. You could try to experiment with various preprocessing methods or developing more sophisticated workflows but that does not pay off if you only need to segment one or a few cases.</p>
<p>In addition to the Fill between slices effect, you can also try to use Paint effect with sphere option enabled (so that it paints on a couple of slices at once) with enabling “Editable intensity range” in Masking settings. You can find a good intensity range using Threshold effect (click “Use for masking” if the previewed intensity range looks good).</p>

---

## Post #6 by @Dexter777 (2021-02-10 17:13 UTC)

<p>Hi, thanks for your reply. I will try the “fill between slices” option. I plan to do this on multiple patients. So, I will need to find a faster way after this project.  I’ll try to slice it in multiple views so as to get a better build/connections in all directions when using fill between slices.  There is a Perk Lab video for a femur by using the mask region growing, paint, grow from seeds, I will try it as well.</p>

---

## Post #7 by @Dexter777 (2021-02-10 17:18 UTC)

<p>Great, I appreciate the help from everyone.<br>
I will try your suggestions and let you know how it goes.</p>

---

## Post #8 by @lassoan (2021-02-10 17:19 UTC)

<aside class="quote no-group" data-username="Dexter777" data-post="6" data-topic="15928">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dexter777/48/6118_2.png" class="avatar"> Dexter777:</div>
<blockquote>
<p>There is a Perk Lab video for a femur by using the mask region growing, paint, grow from seeds, I will try it as well.</p>
</blockquote>
</aside>
<p>Region growing requires the segmented structures to be at least 4-6 voxel thick. You can achieve that by Cropping and resampling the volume (resample with spacing scale of 0.2 to 0.7, crop to prevent the segmentation to consume too much memory - spacing scale of 0.5 increases memory usage and processing time by a factor of 8x).</p>

---

## Post #9 by @Dexter777 (2021-02-22 11:13 UTC)

<p>Hi Murat and Andras,<br>
I was successful in segmenting the turbinates using fill between slices.<br>
Is there a setting to reduce the volume of the fill or ratio of negative to positive space in fill between slices? I was hoping to develop the left nasal cavity with more detailed turbinate leaflets.<br>
My axial view shows this detail but fill between slices filled all the negative space. This is for 3d printing. Any suggestions? Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356e0057e66a43b5e2370120ce41bb75621d2518.png" data-download-href="/uploads/short-url/7CEYVzOe6h763vnBQW0IzNox7g4.png?dl=1" title="Transversal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/356e0057e66a43b5e2370120ce41bb75621d2518_2_469x500.png" alt="Transversal" data-base62-sha1="7CEYVzOe6h763vnBQW0IzNox7g4" width="469" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/356e0057e66a43b5e2370120ce41bb75621d2518_2_469x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356e0057e66a43b5e2370120ce41bb75621d2518.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/356e0057e66a43b5e2370120ce41bb75621d2518.png 2x" data-dominant-color="B3ACA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Transversal</span><span class="informations">550×586 316 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886298e7770501e5b9c4e6096d91c1a0bc428888.jpeg" data-download-href="/uploads/short-url/jswb8HxWXWXLVb7LTkHXuGwKJqU.jpeg?dl=1" title="Fill between slices_3.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/886298e7770501e5b9c4e6096d91c1a0bc428888_2_690x371.jpeg" alt="Fill between slices_3.PNG" data-base62-sha1="jswb8HxWXWXLVb7LTkHXuGwKJqU" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/886298e7770501e5b9c4e6096d91c1a0bc428888_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/886298e7770501e5b9c4e6096d91c1a0bc428888_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/886298e7770501e5b9c4e6096d91c1a0bc428888_2_1380x742.jpeg 2x" data-dominant-color="8D9091"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fill between slices_3.PNG</span><span class="informations">1872×1009 355 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2021-02-22 13:02 UTC)

<p>You can always a good segmentation with “Fill between slices” by reviewing the slices after clicking “Preview” (before clicking “Apply”) and if you find that on any slice the segmentation needs improvement then segment that slice, too. This will automatically recompute the segmentation, taking into account this additional input. Click “Apply” when the entire segmentation is acceptable.</p>

---

## Post #11 by @Dexter777 (2021-02-22 13:39 UTC)

<p>Thanks, I’ll give it a go.</p>

---

## Post #12 by @Dexter777 (2021-03-02 22:01 UTC)

<p>Yes, it worked well.</p>
<p>I have noticed when I exported the skull as a STL(LPS), I’m losing the varying thickness of the skull. Previously the skull thickness was visible, when cut in half ,in the STL file.<br>
Have I saved it incorrectly as a STL?</p>

---

## Post #13 by @lassoan (2021-03-02 22:34 UTC)

<p>Can you post a screenshot?</p>
<p>How did you cut the mesh in half: using Dynamic modeler module’s Plane cut tool, or simply specifying cutting planes in Models module? Capping of the cut surface is only available in Dynamic modeler.</p>

---

## Post #14 by @Dexter777 (2021-03-03 01:25 UTC)

<p>I cut the mesh in Rhino3d with a cutting plane that I can control points to shape the cutting plane or I use a straight plane, then I bring in a 3dm file of a knuckle joint to do a Boolean union to the two half’s of the skull. It sounds like I can cut the skull &amp; turbinates with a straight plane in Slicer? Can I do a Boolean union?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c62a7280b50d87053294e1b4483496c6bf00539.png" data-download-href="/uploads/short-url/fsOVE6PfvWUlWI8pQYj9F14gxCx.png?dl=1" title="Dex Screen shot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c62a7280b50d87053294e1b4483496c6bf00539_2_690x361.png" alt="Dex Screen shot" data-base62-sha1="fsOVE6PfvWUlWI8pQYj9F14gxCx" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c62a7280b50d87053294e1b4483496c6bf00539_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c62a7280b50d87053294e1b4483496c6bf00539_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c62a7280b50d87053294e1b4483496c6bf00539_2_1380x722.png 2x" data-dominant-color="ADB7B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Dex Screen shot</span><span class="informations">1885×987 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @Dexter777 (2021-03-03 01:46 UTC)

<p>I found the community comments regarding using the dynamic modeler. I will pursue using it and some of the other means mentioned from the community.</p>
<p>Thanks.</p>

---

## Post #16 by @lassoan (2021-03-03 02:36 UTC)

<p>STL can only store a surface mesh. If the surface is closed then it appears from outside as a solid object, but it is really just an infinitely thin shell.</p>
<p>If Rhino3d can interpret the imported STL file as a solid then when you cut it, the cut surfaces will be capped to it will appear that it has thickness. However, if Rhino3d interprets the imported STL file as a surface mesh then when you cut it, then you will see that the mesh is just an infinitely thin shell.</p>
<p>In Slicer, you can cut a model and cap the cut surface using Dynamic modeler module’s “Plane cut” tool, which will keep the surface closed (thereby preserving the solid-like appearance). You can do Boolean operations on models (union, intersection, difference) using the new experimental module in Sandbox extension: <a href="https://discourse.slicer.org/t/new-experimental-feature-boolean-operations-union-intersection-difference-on-meshes/16048" class="inline-onebox">New experimental feature: Boolean operations (union, intersection, difference) on meshes</a></p>

---

## Post #17 by @Dexter777 (2021-03-03 11:48 UTC)

<p>Thank you. I found a Perk Lab video 3D Slicer: Dynamic Modeler - Parametric Surface Editing for Biomedical Applications that will be helpful as well. And I installed the Sandbox extension. This should streamline our process. I’ll let you know how it works. Thanks.</p>

---

## Post #18 by @Dexter777 (2021-03-03 17:04 UTC)

<p>Sorry for asking probably a very basic question but how do I declare the skull as a Model Node in the selection panel?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922ddd4f0c150ad4336bcc9c384af869e7b82c0d.png" data-download-href="/uploads/short-url/kR9YrvazOXHMJttwirqAxrjO7H7.png?dl=1" title="Capture5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/922ddd4f0c150ad4336bcc9c384af869e7b82c0d_2_690x364.png" alt="Capture5" data-base62-sha1="kR9YrvazOXHMJttwirqAxrjO7H7" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/922ddd4f0c150ad4336bcc9c384af869e7b82c0d_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/922ddd4f0c150ad4336bcc9c384af869e7b82c0d_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922ddd4f0c150ad4336bcc9c384af869e7b82c0d.png 2x" data-dominant-color="6C6C73"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture5</span><span class="informations">1072×566 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @muratmaga (2021-03-03 19:16 UTC)

<aside class="quote no-group" data-username="Dexter777" data-post="18" data-topic="15928">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dexter777/48/6118_2.png" class="avatar"> Dexter777:</div>
<blockquote>
<p>I declare the skull as a Model Node</p>
</blockquote>
</aside>
<p>Have you exported the segmentation back as 3D model? Sometimes it is easy to overlook that step.</p>

---

## Post #20 by @lassoan (2021-03-03 19:22 UTC)

<p><a class="mention" href="/u/dexter777">@Dexter777</a> I’ve also noticed that you use a Slicer version that is months old. We make fixes and improvements and add features almost every day, so during all this time you missed out on a lot of things. I would recommend to update to the latest Slicer Stable Release.</p>

---
