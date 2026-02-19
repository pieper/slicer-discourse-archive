---
topic_id: 9525
title: "How To Segment All Pores And Its Connecting Paths Seperately"
date: 2019-12-17
url: https://discourse.slicer.org/t/9525
---

# How to  segment all pores and its  connecting paths seperately 

**Topic ID**: 9525
**Date**: 2019-12-17
**URL**: https://discourse.slicer.org/t/how-to-segment-all-pores-and-its-connecting-paths-seperately/9525

---

## Post #1 by @muntahi398 (2019-12-17 13:38 UTC)

<p>Dear  altruists,<br>
I am trying  to segment this 3d binary volume of having many spherical blobs connected to one another with some small path. Can you suggest me simple way of segmenting all the pores individually and seperating connection region,   so that I can get properties of each spheres which is important for my work. I have  attached an image for reference<br>
Any suggestion is appriciated.</p>

---

## Post #2 by @pieper (2019-12-17 15:01 UTC)

<p>Hi - looks like the image didn’t come through - can you try again?</p>
<aside class="quote no-group" data-username="muntahi398" data-post="1" data-topic="9525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muntahi398/48/5302_2.png" class="avatar"> muntahi398:</div>
<blockquote>
<p>Dear altruists,</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji only-emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @muntahi398 (2019-12-17 17:24 UTC)

<p>unfortunately, image was not uploaded  previously. Here is the pore 3D volume I need  to segment individually.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a07b561af44162e8dacb24916a03f24e978f5e98.png" data-download-href="/uploads/short-url/mTGDOxzPo7tQAxBbObYaWJL8JGE.png?dl=1" title="3d_slice_pore" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a07b561af44162e8dacb24916a03f24e978f5e98_2_690x399.png" alt="3d_slice_pore" data-base62-sha1="mTGDOxzPo7tQAxBbObYaWJL8JGE" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a07b561af44162e8dacb24916a03f24e978f5e98_2_690x399.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a07b561af44162e8dacb24916a03f24e978f5e98.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a07b561af44162e8dacb24916a03f24e978f5e98.png 2x" data-dominant-color="9C9A96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_slice_pore</span><span class="informations">701×406 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2019-12-17 19:27 UTC)

<p>With the Segment Editor you could definitely threshold, then shrink with the margins tool, and then use the split option in the islands operator.  That should get you most of the way.</p>

---

## Post #5 by @mikebind (2019-12-17 20:00 UTC)

<p>In the Segment Editor, assuming you can get to the segmentation in your image (e.g. via thresholding), you should be able to do a pretty good job of isolating the spherical parts via the “Smoothing” tool with the Smoothing Method set to “Opening”.  This should eliminate the small connections between spheres while only minimally modifying the spheres themselves.  Next you can use the “Islands” tool with the option to “Split islands to segments”. That should make each sphere into it’s own segment.</p>
<p>If you want the connecting paths isolated, you can use the “Logical Operations” to subtract the opened object from the original connected object.  If you want those as separate objects, you could again use the “Islands” tool and split them into individual segments.</p>

---

## Post #6 by @muntahi398 (2019-12-18 16:36 UTC)

<p>Thanks Mike for your kind suggestion.<br>
However I could not get satisfactory result out of that.<br>
I did smoothing twice consecutively by opening with 3X3X3 kernal which did not open the connections.<br>
Is there any shape based (for example spherical) object segmentor?<br>
Island labeled unconnected  object, but need segment on conencted spheres.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7954e3a15fd5fe92bc327237ba4d6adaef5a1f.png" data-download-href="/uploads/short-url/fLitm8jb5fd0IUH2L14Z4ff7CtF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7954e3a15fd5fe92bc327237ba4d6adaef5a1f_2_690x272.png" alt="image" data-base62-sha1="fLitm8jb5fd0IUH2L14Z4ff7CtF" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e7954e3a15fd5fe92bc327237ba4d6adaef5a1f_2_690x272.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7954e3a15fd5fe92bc327237ba4d6adaef5a1f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7954e3a15fd5fe92bc327237ba4d6adaef5a1f.png 2x" data-dominant-color="6F6756"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">914×361 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2019-12-18 17:15 UTC)

<p>Probably you don’t need a model-based segmentation method. Instead, you can erode massively (it is enough if a couple of voxels remain in each sphere), split to islands, and do grow from seeds (with the intensity range set to match the sphere’s intensities). If you can upload a sample data set and post the link here then we can give more specific suggestions.</p>

---

## Post #8 by @mikebind (2019-12-18 18:39 UTC)

<p>Using a larger opening kernel should work well for cases where there is a thin connecting path between the large spheres. You just need a kernel larger than the connections, and the larger objects should be only minimally modified.  Cases where the connections are really two spheres touching (rather than linked via a thin connector) might end up reconnected when the spheres are restored.</p>
<p>Because of that, Andras’s suggestion of eroding (Margin =&gt; Shrink), separating (Islands =&gt; Split), followed by Grow from seeds with a threshold applied may work better for you. If you are left with small connector paths that you don’t want, applying morphological opening (Smoothing =&gt; Opening) to your final objects should get rid of any small projections off the sphere surfaces that you don’t want.</p>
<p>This reference gives a quick overview of morphological image processing: <a href="https://www.cs.auckland.ac.nz/courses/compsci773s1c/lectures/ImageProcessing-html/topic4.htm" rel="nofollow noopener">https://www.cs.auckland.ac.nz/courses/compsci773s1c/lectures/ImageProcessing-html/topic4.htm</a>.  Erode and Dilate operations are available via the Margin tool, and Open and Close are available via the Smoothing tool.</p>

---

## Post #9 by @muntahi398 (2019-12-19 08:59 UTC)

<p>Thanks everyone for their suggestion, I will try to  apply those.</p>
<p>This page is not letting tiff file to be uploded, so sharing this link of sample object<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1d9IUSWRwDZkX-0IkpgV0OsPZgC_ZGyO9/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:128/67;"><img src="https://lh5.googleusercontent.com/jCH2-UzV_RtjK-QLFpTfuw_UJ2B3OW_DwLZAPBj72H6EGlP4pClVc6JeXis=w1200-h630-p" class="thumbnail" width="128" height="67"></div>

<h3><a href="https://drive.google.com/file/d/1d9IUSWRwDZkX-0IkpgV0OsPZgC_ZGyO9/view?usp=sharing" target="_blank" rel="nofollow noopener">connected_spheres.tif</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Here is a sample segment of  3D stacked binary image (.tiff) file which can be loaded as a volume in slicer.</p>

---

## Post #10 by @lassoan (2019-12-19 16:40 UTC)

<p>I’ve gave it a try and the workflow we described above works quite well, except that certain operations takes minutes to complete. They can be automated, though, so if you have to run this analysis on many images then you don’t need to click and wait, just start the script and you get all the results at the end.</p>
<p>Workflow:</p>
<ul>
<li>Go to Segment editor module, add segment</li>
<li>Threshold effect: <em>Apply</em> (to add all bright areas to the segment)</li>
<li>Margin effect: margin size = 3.0mm, operation = shrink, <em>Apply</em> 2 times (maybe 3x, to separate blobs)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bfc2c5746560f6d080974666aa601b6abd851b94.png" alt="image" data-base62-sha1="rmoux0k9br69nsug6yK4AJAxQd6" width="408" height="445"></li>
<li>Island effect: Split islands to segments, minimum size = 30 voxels (it takes a few minutes, creates a separate segment from each blob)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9626f33c6a59107d348c53632f06adf0cc2b2a3d.png" alt="image" data-base62-sha1="lqj4onCPYRxW79nWp3aPdUWepJ3" width="406" height="443"></li>
<li>Threshold effect: <em>Use for masking</em> (to make sure segments will remain inside bright areas)</li>
<li>Grow from seeds effect: seed locality = 1.0, click Initialize, then Apply (takes 10-20 minutes, we’ll have to investigate why, we should be able to fix it so that it completes within 1-2 minutes)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c93ed3a6942103eb370c7f9e1b9457c633c84bf2.png" alt="image" data-base62-sha1="sIizN2xn6bfmQZB02GAWoTR3WIa" width="670" height="442"></li>
<li>If you need to remove clipped segments at the boundary: this can be automated with some Python scripting but you can do it manually, too: select Paint effect, enable “Color smudge”, then for each segment: click on the segment in the image (this will select the segment), then click Remove to delete the segment</li>
<li>Compute statistics using Segment Statistics module</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b086459c4edccf902bb395cf079ba64836ec050.png" data-download-href="/uploads/short-url/1zBenzZnD8ZOInZuy74uyj4GsV2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b086459c4edccf902bb395cf079ba64836ec050_2_690x474.png" alt="image" data-base62-sha1="1zBenzZnD8ZOInZuy74uyj4GsV2" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b086459c4edccf902bb395cf079ba64836ec050_2_690x474.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b086459c4edccf902bb395cf079ba64836ec050_2_1035x711.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b086459c4edccf902bb395cf079ba64836ec050.png 2x" data-dominant-color="818180"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1345×925 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @muntahi398 (2019-12-30 10:17 UTC)

<p>Dear Dr Lasson,<br>
Thanks and much appreciated.<br>
I have tried according to your previos suggestions last week and could get segmention on most spheres. I had to use more than 21mm karnel shrink to seperate adjecent spheres.<br>
Below here, you can see some sphere belonging to same island/segment that needs to be separated. Here it is small portion so manually I can split by cutting tool but my original data is much bigger and splitting manually will be difficult.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17d2fe919f22abdcc1306d274f2cfe831682d022.png" alt="image" data-base62-sha1="3oL2bwVU6euhvmPGwz2BWJF6rwS" width="690" height="244"><br>
Any suggestion on making this segmentation better?</p>
<p>One more thing, from segment statistics I can get surface area, volume and (radius considering sphere), but is there a way of equivalent major axis, minor axis measurement for ellipsoid fitting?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ea318ab38f48b47caad6f7f9b8b9cfc34978bcf.png" alt="image" data-base62-sha1="fMJX9xvoGiWZQbAaD7JzQuHqF6n" width="690" height="260"></p>

---

## Post #13 by @lassoan (2019-12-30 16:34 UTC)

<aside class="quote no-group" data-username="muntahi398" data-post="12" data-topic="9525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muntahi398/48/5302_2.png" class="avatar"> muntahi398:</div>
<blockquote>
<p>I can split by cutting tool but my original data is much bigger and splitting manually will be difficult.</p>
</blockquote>
</aside>
<p>You can increase the kernel size even further. If you find that a large enough kernel size completely erases smaller spheres than you can apply additional shrinking operations for only large islands.</p>
<aside class="quote no-group" data-username="muntahi398" data-post="12" data-topic="9525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muntahi398/48/5302_2.png" class="avatar"> muntahi398:</div>
<blockquote>
<p>from segment statistics I can get surface area, volume and (radius considering sphere), but is there a way of equivalent major axis, minor axis measurement for ellipsoid fitting?</p>
</blockquote>
</aside>
<p>Oriented bounding box size <a href="https://discourse.itk.org/t/problem-calculating-oriented-bounding-box-itk-shapelabelobject/455">can be computed by ITK</a> and we <a href="https://github.com/Sunderlandkyl/Slicer/tree/vtkITKLabelShapeStatistics">started to look into making it available in Segment Statistics</a> - <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> may be able to give an estimate about when it could be ready.</p>

---

## Post #14 by @Sunderlandkyl (2019-12-30 16:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="9525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Oriented bounding box size <a href="https://discourse.itk.org/t/problem-calculating-oriented-bounding-box-itk-shapelabelobject/455" rel="noopener nofollow ugc">can be computed by ITK</a> and we <a href="https://github.com/Sunderlandkyl/Slicer/tree/vtkITKLabelShapeStatistics" rel="noopener nofollow ugc">started to look into making it available in Segment Statistics</a> - <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> may be able to give an estimate about when it could be ready.</p>
</blockquote>
</aside>
<p>There’s only a small amount left to do. It should be available early next week.</p>

---

## Post #15 by @muntahi398 (2020-01-02 13:41 UTC)

<p>Thanks for the idea. Previosly did not nitice multiple  segment editing or visualisation control option was there.</p>

---

## Post #16 by @muntahi398 (2020-01-02 13:43 UTC)

<p>Thanks, Bounding box  would  be nice  to have in Segment Statistics.<br>
Is it going to provide segment centroid coordinates?<br>
That would  be  important for calculating 3d dstribution inside.</p>

---

## Post #17 by @Sunderlandkyl (2020-01-03 19:32 UTC)

<aside class="quote no-group" data-username="muntahi398" data-post="16" data-topic="9525">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muntahi398/48/5302_2.png" class="avatar"> muntahi398:</div>
<blockquote>
<p>Is it going to provide segment centroid coordinates?</p>
</blockquote>
</aside>
<p>Yes, it will provide centroid coordinates as well.</p>

---
