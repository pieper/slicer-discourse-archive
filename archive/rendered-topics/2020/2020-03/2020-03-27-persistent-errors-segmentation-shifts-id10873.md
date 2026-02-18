# persistent errors - segmentation shifts

**Topic ID**: 10873
**Date**: 2020-03-27
**URL**: https://discourse.slicer.org/t/persistent-errors-segmentation-shifts/10873

---

## Post #1 by @cepcep (2020-03-27 12:09 UTC)

<p>Hello.  I’ve been doing brain segmentation for more than a week now, my goal is to break it into three parts for 3D printing.</p>
<ol>
<li>Frontal, parental lobes, septum pellucidum+Monro(little pars talamus)</li>
<li>brain stem (with diencephalon)</li>
<li>temporal occipital lobes+cerebellum</li>
</ol>
<p>I do it in a simple and tedious way: colorize each layer in layers<br>
But at the same time, layer shifts constantly occur in the form of teeth of a comb for combing hair.  I attach an example of the picture.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1d45074ecda75aa4a3c1543b422c1644130ee36.jpeg" data-download-href="/uploads/short-url/wdMjlJOA3mr1fSpqTaRCVcSnEtE.jpeg?dl=1" title="2020-03-27_07-25-15" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1d45074ecda75aa4a3c1543b422c1644130ee36_2_639x500.jpeg" alt="2020-03-27_07-25-15" data-base62-sha1="wdMjlJOA3mr1fSpqTaRCVcSnEtE" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1d45074ecda75aa4a3c1543b422c1644130ee36_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1d45074ecda75aa4a3c1543b422c1644130ee36_2_958x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1d45074ecda75aa4a3c1543b422c1644130ee36.jpeg 2x" data-dominant-color="3F4641"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-03-27_07-25-15</span><span class="informations">1121×876 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I was tortured to constantly correct them.  Please tell me why these changes occur, and what I must do to prevent them from happening.</p>
<p>I will also be grateful if you tell me a simpler way of brain segmentation for this DICOM</p>

---

## Post #2 by @cepcep (2020-03-29 07:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4515a386b5da495afd65c6c80b8884fbd06ca4f4.png" data-download-href="/uploads/short-url/9R9iZuSzLIMMv4113l3LygA5Lpi.png?dl=1" title="2020-03-29_12-25-39" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4515a386b5da495afd65c6c80b8884fbd06ca4f4_2_690x467.png" alt="2020-03-29_12-25-39" data-base62-sha1="9R9iZuSzLIMMv4113l3LygA5Lpi" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4515a386b5da495afd65c6c80b8884fbd06ca4f4_2_690x467.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4515a386b5da495afd65c6c80b8884fbd06ca4f4_2_1035x700.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4515a386b5da495afd65c6c80b8884fbd06ca4f4_2_1380x934.png 2x" data-dominant-color="696F75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-03-29_12-25-39</span><span class="informations">1510×1024 522 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I do not <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f3f64661f042ef1b664e260cbbc38eabe712a1f.png" data-download-href="/uploads/short-url/mILJz3PsbaeswhqZiRGgLRuJTvF.png?dl=1" title="2020-03-29_12-30-43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f3f64661f042ef1b664e260cbbc38eabe712a1f_2_690x459.png" alt="2020-03-29_12-30-43" data-base62-sha1="mILJz3PsbaeswhqZiRGgLRuJTvF" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f3f64661f042ef1b664e260cbbc38eabe712a1f_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f3f64661f042ef1b664e260cbbc38eabe712a1f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f3f64661f042ef1b664e260cbbc38eabe712a1f.png 2x" data-dominant-color="678E63"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-03-29_12-30-43</span><span class="informations">691×460 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> understand where these terrible distortions of my segmentation come from, I’m tired of fixing them. They come out again and again</p>

---

## Post #3 by @lassoan (2020-03-29 15:26 UTC)

<p>Which Segment Editor effects do you use?</p>
<p>Can you reproduce the behavior with any of the data sets in Sample Data module?</p>
<p>Can you reproduce the behavior if you use latest Slicer Preview Release?</p>
<p>Have you imported the image from DICOM? Did you get any warning during DICOM import?</p>
<p>Is a transform applied to the volume (in Data module / Subject Hierarchy tab, is there a transform in the transform column of the volume’s row)?</p>
<p>It might be also possible that you are segmenting on oblique slices. See instructions here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/">https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/</a></p>

---

## Post #4 by @cepcep (2020-03-30 03:29 UTC)

<p>Hi. Thanks for your reply.<br>
As I understand it, the trouble with my segmentation is oblique layers.  At the same time, I changed the geometry - increased the resolution from .9 to .3<br>
following your link I saw a geometry button on the segmentation.  I really have it, but clicking on it - it disappears …<br>
I can `t get it.  If I change the rotation angle of volume with segmentation together in “Transform”, will this fix my problem?<br>
At the same time, I noticed that about creating new ROIs, they become oblique to the geometry of the monitor screen and 3d slicer windows.  Those.  the default geometry is oblique.</p>

---

## Post #5 by @lassoan (2020-03-30 04:38 UTC)

<aside class="quote no-group" data-username="cepcep" data-post="4" data-topic="10873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cepcep/48/6389_2.png" class="avatar"> cepcep:</div>
<blockquote>
<p>I really have it, but clicking on it - it disappears …</p>
</blockquote>
</aside>
<p>This is what the button is expected to do. When you click the icon with the warning button, each slice view gets aligned to closest volume axis, so the warning is no longer applicable.</p>
<p>Segmenting on oblique slices can be sometimes useful, but if you are not specifically interested in doing that (or have hard time ignoring the temporary stripe artifacts, which resolve on their own, as you complete your segmentation) then I would suggest to click the warning button and segment on volume-axis-aligned slices.</p>

---
