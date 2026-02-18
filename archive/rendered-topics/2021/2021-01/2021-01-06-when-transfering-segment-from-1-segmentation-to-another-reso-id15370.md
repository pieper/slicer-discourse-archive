# When transfering segment from 1 segmentation to another resolution changes

**Topic ID**: 15370
**Date**: 2021-01-06
**URL**: https://discourse.slicer.org/t/when-transfering-segment-from-1-segmentation-to-another-resolution-changes/15370

---

## Post #1 by @NoobForSlicer (2021-01-06 06:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07380c762c1872fd86e60f9d1a14746581fbea62.jpeg" data-download-href="/uploads/short-url/11RqpFqiDUcrViDBSdra9HyEIwO.jpeg?dl=1" title="weird color 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07380c762c1872fd86e60f9d1a14746581fbea62_2_483x500.jpeg" alt="weird color 1" data-base62-sha1="11RqpFqiDUcrViDBSdra9HyEIwO" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07380c762c1872fd86e60f9d1a14746581fbea62_2_483x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/07380c762c1872fd86e60f9d1a14746581fbea62_2_724x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07380c762c1872fd86e60f9d1a14746581fbea62.jpeg 2x" data-dominant-color="13301C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">weird color 1</span><span class="informations">815×843 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc209fded916406672436f221b6bb765ed117242.jpeg" data-download-href="/uploads/short-url/zYqdEu5soQJ9sUBAtSnoqx3cfMS.jpeg?dl=1" title="weird color 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc209fded916406672436f221b6bb765ed117242_2_517x500.jpeg" alt="weird color 2" data-base62-sha1="zYqdEu5soQJ9sUBAtSnoqx3cfMS" width="517" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc209fded916406672436f221b6bb765ed117242_2_517x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc209fded916406672436f221b6bb765ed117242_2_775x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc209fded916406672436f221b6bb765ed117242.jpeg 2x" data-dominant-color="112B19"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">weird color 2</span><span class="informations">907×876 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So I just move the segment from one segmentation (cropped volume long time ago ) to this new segmentation (not cropped but full volume little bit modified position)</p>
<p>This is what I end up with… I wonder why?!</p>
<p>The images show the detoriation in the resolution that happens</p>

---

## Post #2 by @NoobForSlicer (2021-01-06 07:12 UTC)

<p>I spent the entire night dealing with this… It actually happens when I am saving the file it changes it!</p>
<p>when I move the segment from one segmentation to another, everything is okay and it looks good.</p>
<p>It is only when I attempt to save it, it does this to the segmentation.</p>

---

## Post #3 by @lassoan (2021-01-06 07:21 UTC)

<p>Slicer does not immediately consolidate geometries of different segments when you just move them around between segmentations, because then each move could potentially degrade the segment.</p>
<p>However, it is necessary to bring all segments to the same grid (origin, spacing, axis directions) when you edit or save the segmentation. Make sure you set the desired geometry in the segmentation node where you finally place your segments.</p>

---

## Post #4 by @NoobForSlicer (2021-01-06 07:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="15370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Make sure you set the desired geometry in the segmentation node where you finally place your segments.</p>
</blockquote>
</aside>
<p>can you please tell me what is a “node” because I have a hard time figuring out what does a “geometry in the segmentation node refer to”.</p>
<p>What I know so far is that I can adjust the pixel size in mm in volume module. I did that and pixels match perfectly. They start and end at the same spot. The segmentation over-lapps perfectly with volume pixels when I look at them. However once saved, the segmentation degrades. IT creates giant pixels that in fact consist of 6 pixels.</p>

---

## Post #5 by @lassoan (2021-01-06 07:33 UTC)

<aside class="quote no-group" data-username="NoobForSlicer" data-post="4" data-topic="15370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar"> NoobForSlicer:</div>
<blockquote>
<p>can you please tell me what is a “node”</p>
</blockquote>
</aside>
<p>See this page: <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="inline-onebox">Image Segmentation — 3D Slicer documentation</a></p>
<aside class="quote no-group" data-username="NoobForSlicer" data-post="4" data-topic="15370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar"> NoobForSlicer:</div>
<blockquote>
<p>I have a hard time figuring out what does a “geometry in the segmentation node refer to”.</p>
</blockquote>
</aside>
<p>By this I meant geometry (origin, spacing, axis directions) of the binary labelmap representation of the segments in the segmentation node. You can change it by clicking on the “<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Specify geometry</a>” button in Segment Editor module.</p>
<aside class="quote no-group" data-username="NoobForSlicer" data-post="4" data-topic="15370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar"> NoobForSlicer:</div>
<blockquote>
<p>What I know so far is that I can adjust the pixel size in mm in volume module. I did that and pixels match perfectly. They start and end at the same spot. The segmentation over-lapps perfectly with volume pixels when I look at them. However once saved, the segmentation degrades. IT creates giant pixels that in fact consist of 6 pixels.</p>
</blockquote>
</aside>
<p>Most likely you moved your segments into a segmentation node that has large spacing. Set the desired geometry (by using Specify geometry button) for the segmentation node where you move your segments to.</p>

---

## Post #6 by @NoobForSlicer (2021-01-06 07:35 UTC)

<p>Amazing Lassoan, I will go get a drink and come back sit at my computer won’t sleep until I fix it…</p>
<p>Wish I could shake your hand sir, what Cus D’Amato was in boxing, you are in Radiology. God bless you sir</p>

---

## Post #8 by @lassoan (2021-01-06 16:04 UTC)

<p>Thanks for the kind words, it always great to get good feedback and not just error reports or questions.</p>
<p>I just want to help users with finding and effectively using what hundreds of Slicer, VTK, ITK, DCMTK, CTK (and other open-source software libraries) contributors developed over the last few decades. Credit also goes to US and Canadian taxpayers for funding most of this work and making the results freely available to all.</p>
<p>If you manage to do what you need, it would be nice if you could write a short note about it in the <a href="https://discourse.slicer.org/c/community/success-stories/29">Success stories category</a>. Such personal stories can be helpful when we need to demonstrate to funding agencies what impact our efforts make. You can also give back by reading the Slicer forum and help newcomers with any questions that you can answer.</p>

---

## Post #9 by @NoobForSlicer (2021-01-07 20:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="15370">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you manage to do what you need, it would be nice if you could write a short note about it in the <a href="https://discourse.slicer.org/c/community/success-stories/29">Success stories category</a>.</p>
</blockquote>
</aside>
<p>I will do sir, I am woorking as an intern once finished with my internship and if I pass, will post a stroy</p>

---
