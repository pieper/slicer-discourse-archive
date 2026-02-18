# Publicly available segmentations for the eye

**Topic ID**: 8723
**Date**: 2019-10-09
**URL**: https://discourse.slicer.org/t/publicly-available-segmentations-for-the-eye/8723

---

## Post #1 by @JoeCrozier (2019-10-09 16:23 UTC)

<p>I hope this falls under support, if not please point me in the right direction.</p>
<p>I’m trying to create a combination 3d printed/silicone molded surgical trainer for the eye for some of the residents I work with.  Prior to getting it into a cad program to do some of the designing, it’d be nice if I had some segmentations to work with that I know are anatomically accurate.  I can find (and have access to) mri and ct data sets that I could manually segment, but as I’m sure you know, all of the little details in the eye can be frustratingly hard to segment accurately.<br>
I found this:  <a href="https://www.slicer.org/wiki/Slicer3.4:Training" rel="nofollow noopener">https://www.slicer.org/wiki/Slicer3.4:Training</a> and it’s associated orbit segmentation tutorials, but as you can see it is a quite old version of slicer and I can’t figure out how to import everything and turn them into segmentations well.  The tutorial does me no good as everything seems to be old and fuzzy.  Also the names of the models (once loaded) make no sense as they are labelled things like “pre-gyrus”, “jake” and “peach”.</p>
<p>Ideally the models/stl’s/segmentations/etc…  I’d be working with would include the:  eye, orbital wall, lacrimal system, and either something for the skin or comes along with the dicom I can segment the flesh/skin by myself manually.   Any other muscles/features would be great but not necessary.</p>
<p>Any thoughts?  I appreciate any ideas you may have to make this task easier!</p>

---

## Post #2 by @pieper (2019-10-09 16:41 UTC)

<p>The clinical content of the old tutorial is probably good, but with the new Slicer you should supersample the segmentation to something closer to your desired resolution (for printing or whatever).  Also you can define whatever names you want.  I don’t know of any atlas data to work from, but if you do find a good way to make models please consider sharing data and an updated tutorial.</p>

---

## Post #3 by @Amine (2019-10-09 16:41 UTC)

<p>Hi, the problematic of orbital wall segmentation has already been asked <a href="https://discourse.slicer.org/t/enhancing-orbital-walls-with-unsharp-mask-filtering/8440">Here</a> and <a href="https://discourse.slicer.org/t/high-quality-segmentation-of-the-orbital-walls/2345">Here</a> for more information</p>

---

## Post #4 by @JoeCrozier (2019-10-09 16:55 UTC)

<p>Thank you both for your input.</p>
<p>As far as the orbital walls themselves, actually I’m less concerned about those.  I’m aware of where that has been answered before and I’ve also dealt with it in the past.  The holes caused by the really thins bones and stuff are easy enough to fix with “fill holes” and random other tools.  I was more concerned with the other parts.  I.e. muscles, ducts, etc…</p>
<p>What do you mean by “SuperSample”?  And yea, I figured I could change the names but I was having trouble loading both the original models and the 2d ct slices themselves at the same time so I could figure out what the heck each object was.  Here’s a screenshot of what I mean:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9428e344983f5c84f95aee134efb5752bc5e152f.png" data-download-href="/uploads/short-url/l8GgzlvwVvdGzZWIWoIlMgPzBcr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9428e344983f5c84f95aee134efb5752bc5e152f_2_690x386.png" alt="image" data-base62-sha1="l8GgzlvwVvdGzZWIWoIlMgPzBcr" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9428e344983f5c84f95aee134efb5752bc5e152f_2_690x386.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9428e344983f5c84f95aee134efb5752bc5e152f_2_1035x579.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9428e344983f5c84f95aee134efb5752bc5e152f_2_1380x772.png 2x" data-dominant-color="9897AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1706×955 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If there is a better way to load the files in so that doesn’t happen I’m all ears, but I unfortunately couldn’t figure it out from the tutorial.</p>

---

## Post #5 by @JoeCrozier (2019-10-09 16:56 UTC)

<p>P.s. I would absolutely share the models and update a tutorial if interested.  Although I must admit I’m hoping to find somebody has done the work already for me haha.</p>

---

## Post #6 by @pieper (2019-10-09 17:11 UTC)

<aside class="quote no-group" data-username="JoeCrozier" data-post="4" data-topic="8723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/c4cdca/48.png" class="avatar"> JoeCrozier:</div>
<blockquote>
<p>What do you mean by “SuperSample”?</p>
</blockquote>
</aside>
<p>I meant you can make the resolution of the segmentation higher than the source data so the models are more faithful to the underlying image data and anatomy.</p>

---

## Post #7 by @Amine (2019-10-09 18:56 UTC)

<p>-If you want to show your slices on the 3d view click on the pin icon in the top left of the slice then on the eye icon<br>
-if you want the models to show on the slice then go to models module and set slice display to visible (scroll down a bit)</p>

---

## Post #8 by @lassoan (2019-10-09 21:45 UTC)

<p>To load the original CT from the DICOM files, either use DICOM module or uncheck “single file” option in Add data window.</p>
<p>After that you’ll be able to identify which color is which muscle (and the list of colors are also listed in one of the tutorial slides).</p>
<p>You can adjust the resolution of your segmentation by clicking on the button next to the master volume selector in Segment Editor module, choosing the MR volume as reference and set an oversampling factor &gt; 1.0.</p>

---

## Post #9 by @maggievep (2022-09-22 23:08 UTC)

<p>I’m sorry, where can I find the tutorial for eyeball and eye muscle segmentation? Thank you!!</p>

---
