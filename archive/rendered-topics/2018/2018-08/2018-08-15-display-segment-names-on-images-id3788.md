---
topic_id: 3788
title: "Display Segment Names On Images"
date: 2018-08-15
url: https://discourse.slicer.org/t/3788
---

# Display segment names on images

**Topic ID**: 3788
**Date**: 2018-08-15
**URL**: https://discourse.slicer.org/t/display-segment-names-on-images/3788

---

## Post #1 by @Justin_Cramer (2018-08-15 18:35 UTC)

<p>Is there a way to display segment names on every slice in a way similar to annotations on e-anatomy? (see attached image) The verbiage gets confusing because “label” and “annotation” already have different meanings in Slicer, but I essentially want to annotate my segmentation for the purposes of creating an anatomy reference.</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05aafede24a753601a2dc394a20cd3273dd02a83.png" data-download-href="/uploads/short-url/O8K6JlH80WV1x9JB8KUb4DK7Wr.png?dl=1" title="label_names" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05aafede24a753601a2dc394a20cd3273dd02a83_2_690x366.png" alt="label_names" data-base62-sha1="O8K6JlH80WV1x9JB8KUb4DK7Wr" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05aafede24a753601a2dc394a20cd3273dd02a83_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05aafede24a753601a2dc394a20cd3273dd02a83_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05aafede24a753601a2dc394a20cd3273dd02a83.png 2x" data-dominant-color="313130"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">label_names</span><span class="informations">1243×660 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2018-08-28 16:22 UTC)

<p>You can use Markups module to mark points and assign a label to each point. The layout is not flexible: label is always displayed near the marked point.</p>
<p>You could write a short Python script to create markups automatically for a selected slice. For example, it could place a markup in the center of gravity of each segment. You could then move the markups manually as needed.</p>

---

## Post #3 by @rkikinis (2018-08-28 17:14 UTC)

<p>Hi,</p>
<p>Also, dependent on the look-up table that you use, you could associate anatomical names with particular labels. On mouse over those names are displayed in the - data probe area of slicer<br>
I used the brain atlas as example. It comes with its own custom look-up table.</p>
<p>Best</p>
<p>Ron</p>
<p>Download the brain atlas: <a href="http://www.spl.harvard.edu/publications/item/view/2037" rel="noopener nofollow ugc">http://www.spl.harvard.edu/publications/item/view/2037</a></p>
<p>Standalone viewer: <a href="http://openanatomy.org/" rel="noopener nofollow ugc">http://openanatomy.org/</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/d/dff0556a9f38a262cc6342ddca6c7356dc20d2d8.jpeg" data-download-href="/uploads/short-url/vX3o507Fd2fTsIEczrLXs6S4ZEQ.jpeg?dl=1" title="IMG_1090.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dff0556a9f38a262cc6342ddca6c7356dc20d2d8_2_690x465.jpeg" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dff0556a9f38a262cc6342ddca6c7356dc20d2d8_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dff0556a9f38a262cc6342ddca6c7356dc20d2d8_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dff0556a9f38a262cc6342ddca6c7356dc20d2d8_2_1380x930.jpeg 2x" data-dominant-color="7F7F7C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1090.jpg</span><span class="informations">3041×2052 1.62 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @Justin_Cramer (2018-10-08 13:39 UTC)

<p>Thanks for the suggestions. Sounds like that specific functionality isn’t available at this point. As a feature request, just a checkbox in the Segment Editor saying “Display visible segment names” would be awesome for creating educational content.</p>

---

## Post #5 by @lassoan (2018-10-08 14:17 UTC)

<aside class="quote no-group" data-username="Justin_Cramer" data-post="4" data-topic="3788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/e79b87/48.png" class="avatar"> Justin_Cramer:</div>
<blockquote>
<p>just a checkbox in the Segment Editor saying “Display visible segment names” would be awesome for creating educational content</p>
</blockquote>
</aside>
<p>This would be certainly nice to have and would be happy to help anyone who would have some time to work on this.</p>
<p>In the meantime, we are starting a project on improving Slicer’s segmentation/atlas export to <a href="http://openanatomy.org/">Open Anatomy</a>. This may make the information almost as easily accessible as static images, but offer much more flexibility.</p>

---
