---
topic_id: 14070
title: "Paint Mode In Segment Editor Works Incorrect"
date: 2020-10-16
url: https://discourse.slicer.org/t/14070
---

# Paint mode in segment editor works incorrect

**Topic ID**: 14070
**Date**: 2020-10-16
**URL**: https://discourse.slicer.org/t/paint-mode-in-segment-editor-works-incorrect/14070

---

## Post #1 by @jarrik (2020-10-16 06:09 UTC)

<p>Hello!<br>
I work with Slicer 4.11.0 , win10<br>
The problem is: In Segment Editor Paint mode modify several slices together (see photo). If it is not an error, I would like to know, how to deny such modifications. In my work I need to modify only one slice simultaneously, and then use Fill between Slices mode.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bb7694d0bc1742380e7a92b55260d89b04400d8.jpeg" data-download-href="/uploads/short-url/1FEcXWctI9ohzH1xLQEanjVMdlu.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bb7694d0bc1742380e7a92b55260d89b04400d8_2_690x308.jpeg" alt="1" data-base62-sha1="1FEcXWctI9ohzH1xLQEanjVMdlu" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bb7694d0bc1742380e7a92b55260d89b04400d8_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bb7694d0bc1742380e7a92b55260d89b04400d8_2_1035x462.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bb7694d0bc1742380e7a92b55260d89b04400d8_2_1380x616.jpeg 2x" data-dominant-color="4D4D4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1903×852 91.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8215592a8c9906bf0a5c84252f50ef472b34b26.jpeg" data-download-href="/uploads/short-url/qgTgV2QK1fuAZ2M5D4VOz350v42.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8215592a8c9906bf0a5c84252f50ef472b34b26_2_690x302.jpeg" alt="2" data-base62-sha1="qgTgV2QK1fuAZ2M5D4VOz350v42" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8215592a8c9906bf0a5c84252f50ef472b34b26_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8215592a8c9906bf0a5c84252f50ef472b34b26_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8215592a8c9906bf0a5c84252f50ef472b34b26_2_1380x604.jpeg 2x" data-dominant-color="4C4D4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1916×841 88.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6337e7ba4abe374b004001f82095853c17d80c9d.jpeg" data-download-href="/uploads/short-url/e9J2QnofzVG9bzBn9CbMXu6yGHX.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6337e7ba4abe374b004001f82095853c17d80c9d_2_690x304.jpeg" alt="3" data-base62-sha1="e9J2QnofzVG9bzBn9CbMXu6yGHX" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6337e7ba4abe374b004001f82095853c17d80c9d_2_690x304.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6337e7ba4abe374b004001f82095853c17d80c9d_2_1035x456.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6337e7ba4abe374b004001f82095853c17d80c9d_2_1380x608.jpeg 2x" data-dominant-color="4C4D4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1913×845 89.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa99086b1127d39863bcf18ed62f6e9ed3c237e.jpeg" data-download-href="/uploads/short-url/AtH2OjQnUx3RVyBvEArOAMeQEHQ.jpeg?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa99086b1127d39863bcf18ed62f6e9ed3c237e_2_690x307.jpeg" alt="4" data-base62-sha1="AtH2OjQnUx3RVyBvEArOAMeQEHQ" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa99086b1127d39863bcf18ed62f6e9ed3c237e_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa99086b1127d39863bcf18ed62f6e9ed3c237e_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa99086b1127d39863bcf18ed62f6e9ed3c237e_2_1380x614.jpeg 2x" data-dominant-color="4C4D4D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1915×853 91.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @JanWitowski (2020-10-16 07:03 UTC)

<p>This looks like the effect of a “Sphere brush” option in your Paint tool. Can you verify if it’s turned on?</p>
<p>If not, please provide details what kind of image you are working on.</p>

---

## Post #3 by @jarrik (2020-10-16 10:55 UTC)

<p>You are right. That was “Sphere brush” option turned on.<br>
Thank you!</p>

---
