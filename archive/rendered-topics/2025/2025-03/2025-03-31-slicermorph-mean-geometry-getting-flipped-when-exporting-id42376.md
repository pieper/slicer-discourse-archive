# SlicerMorph Mean geometry getting flipped when exporting

**Topic ID**: 42376
**Date**: 2025-03-31
**URL**: https://discourse.slicer.org/t/slicermorph-mean-geometry-getting-flipped-when-exporting/42376

---

## Post #1 by @Windy (2025-03-31 02:07 UTC)

<p>Hi all,</p>
<p>I am using SlicerMorph’s GPA to get a mean shape from multiple geometries coming from multiple biological samples. I have registered my sample volumes to be in the same direction and then marked landmarks on them. Then I used the GPA module. I get the expected results. However, when I export the mean shape (“PCA Warped Volume”) and load it in MeshLab or Paraview along with an actual sample’s model, it is flipped (refer to the image below, yellow: an actual geometry, blue: mean geometry). I tried with “use Boas coordinates” ticked and unticked, but it didn’t help.</p>
<p>What am I doing wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/592e074b5cef16d2d9e21a308512b944e36e566c.jpeg" data-download-href="/uploads/short-url/cIV6QCoZuajmgmWnogagNsTxQD2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/592e074b5cef16d2d9e21a308512b944e36e566c_2_540x500.jpeg" alt="image" data-base62-sha1="cIV6QCoZuajmgmWnogagNsTxQD2" width="540" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/592e074b5cef16d2d9e21a308512b944e36e566c_2_540x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/592e074b5cef16d2d9e21a308512b944e36e566c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/592e074b5cef16d2d9e21a308512b944e36e566c.jpeg 2x" data-dominant-color="707974"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">784×725 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-03-31 02:28 UTC)

<aside class="quote no-group" data-username="Windy" data-post="1" data-topic="42376">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/91b2a8/48.png" class="avatar"> Windy:</div>
<blockquote>
<p>What am I doing wrong?</p>
</blockquote>
</aside>
<p>You are not doing anything wrong. This is expected. There is no reason to expect the after GPA the coordinate system will be consistent with the original reference frame. We do rotations, scaling and other operations that will definitely alter the orientation and guarantee that it will not be the same.</p>
<p>Why do you need the display your exported mean shape in the same orientation as your sample?</p>
<p>Regardless you can do this in two ways:</p>
<ol>
<li>Use SlicerMorph’s FastModelAlign to register the mean shape model to the sample of your own choosing rigidly (and optionally apply the same transformation to the LMs if you want to display them on top of the rotated mean shape model</li>
<li>Use the Fiducial registration module of Slicer to accomplish this. Set the landmarks of the sample you would like mean model to be aligned to as the <strong>Fixed Landmark</strong> and the mean model LMs as <strong>Moving</strong> and create a new Linear Transform (rigid). You can then use this transform to rotate the mean model and its landmark to the orientation you prefer.</li>
</ol>

---

## Post #3 by @Windy (2025-03-31 02:40 UTC)

<p>Thank you for the input.</p>
<p>I need it aligned because I have point data with measurements coming from the original experiments, and I want to average all the experiment data (unify) to give a holistic idea about the organ being studied. So, I was thinking of getting the mean shape and then interpolating the point data onto the mean shape and computing the mean by averaging all the interpolated data (using Paraview). I am new to the unification part, so if you have any input on it using Slicer, I would really appreciate it.</p>
<p>I originally used the Fiducial registration wizard to register all experiment volumes. I will use the same as you suggested.</p>
<p>Thank you again.</p>

---

## Post #4 by @muratmaga (2025-03-31 04:01 UTC)

<p>I am still somewhat fuzzy about what you are trying to do, but it sounds to me you might want to look into diffeomorphic deformable volumetric registration  more than landmarks based ones, if you want to map points between spaces…</p>

---

## Post #5 by @Windy (2025-03-31 21:31 UTC)

<p>Thank you once again. Really appreciate it. I’ll check on diffeomorphic deformable volumetric registration.</p>

---
