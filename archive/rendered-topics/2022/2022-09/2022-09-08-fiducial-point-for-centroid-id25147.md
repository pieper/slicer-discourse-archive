# Fiducial/point for centroid

**Topic ID**: 25147
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/fiducial-point-for-centroid/25147

---

## Post #1 by @lsprs (2022-09-08 03:18 UTC)

<p>Hello,</p>
<p>I’ve segmented the attached brain from CT data and used SegmentStatistics to calculate the volume and centroid coordinates. I have 2 questions.</p>
<p>1- How can I place a fiducial/point to illustrate the centroid of the object below?</p>
<p>2- How can I convert the centroid coordinates (in this case 7.31849, 136.127, -103.381) to tangible measurements (such as cm)?</p>
<p>I am new to the slicer community and specific details would be very helpful! Thank you!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77a7e347dc248273859b9a74a251c927b45a4cae.png" alt="Screen Shot 2022-09-07 at 5.17.45 PM" data-base62-sha1="h4ww3e75szOOXLvsBoELLVtlKjk" width="454" height="338"></p>

---

## Post #2 by @muratmaga (2022-09-08 19:16 UTC)

<aside class="quote no-group" data-username="lsprs" data-post="1" data-topic="25147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7feea3/48.png" class="avatar"> lsprs:</div>
<blockquote>
<p>How can I place a fiducial/point to illustrate the centroid of the object below?</p>
</blockquote>
</aside>
<p>If you already know the coordinates of the centroid, go to Markups tool, create a new PointList object and simply type the coordinates or copy/paste the values.</p>
<aside class="quote no-group" data-username="lsprs" data-post="1" data-topic="25147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7feea3/48.png" class="avatar"> lsprs:</div>
<blockquote>
<p>How can I convert the centroid coordinates (in this case 7.31849, 136.127, -103.381) to tangible measurements (such as cm)?</p>
</blockquote>
</aside>
<p>A single point itself is not going to give you measurements. If you create other landmarks on the surface of the brain (by adding to the PointList), you can easily calculate the linear distance between any pair, by highlighting it in the Control Points table and right clicking on them. The units in Slicer are in millimeters (by default). So the reported measurements will also be in millimeters.</p>

---

## Post #3 by @lsprs (2022-09-10 14:48 UTC)

<p>Thank you for your help! I was able to follow those instructions almost completely. How would you recommend obtaining the precise coordinates in mm for the centroid point attached?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aed4dfeffaf8cc99f8e8e3ab944c0f6fe49318cc.jpeg" data-download-href="/uploads/short-url/oWDa2pI4nF0JsHPp9rOwAPGmdJy.jpeg?dl=1" title="Screen Shot 2022-09-10 at 10.47.20 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed4dfeffaf8cc99f8e8e3ab944c0f6fe49318cc_2_690x325.jpeg" alt="Screen Shot 2022-09-10 at 10.47.20 AM" data-base62-sha1="oWDa2pI4nF0JsHPp9rOwAPGmdJy" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed4dfeffaf8cc99f8e8e3ab944c0f6fe49318cc_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed4dfeffaf8cc99f8e8e3ab944c0f6fe49318cc_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aed4dfeffaf8cc99f8e8e3ab944c0f6fe49318cc_2_1380x650.jpeg 2x" data-dominant-color="8A8A8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-09-10 at 10.47.20 AM</span><span class="informations">1920×905 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lsprs (2022-09-13 19:01 UTC)

<p>Just bumping this thread! Thank you to all who are able to help.</p>

---

## Post #5 by @pieper (2022-09-13 19:02 UTC)

<p>It’s not clear to me what you are asking - it looks like you already have the centroid of the segment in the statistics table.</p>

---

## Post #6 by @lsprs (2022-09-13 19:10 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="25147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If you create other landmarks on the surface of the brain (by adding to the PointList), you can easily calculate the linear distance between any pair, by highlighting it in the Control Points table and right clicking on them. The units in Slicer are in millimeters (by default). So the reported measurements will also be in millimeters.</p>
</blockquote>
</aside>
<p>Thank you for your response, Steve. I agree I was not very clear. I generated the coordinates of the centroid, however I’m interested in better understanding how these coordinates can be understood in mm. It sounds the only way to understand this is the distance of the centroid relative to other structures (ie, placing points at these structures and measuring the distance between).</p>
<p>If so, what is the best way to place a point at a precise location (e.g. the euryon) on the brain above?</p>
<p>Thank you.</p>

---

## Post #7 by @pieper (2022-09-13 19:24 UTC)

<p>Ah, okay, well if you know the points you want you can just click on them and make markups points.  There are tools for pre-populating lists, marking missing points, etc. and tools in SlicerMorph to analyze populations.  If you want to get the points from an atlas via a form of registration you can also do that</p>

---

## Post #8 by @muratmaga (2022-09-14 04:59 UTC)

<aside class="quote no-group" data-username="lsprs" data-post="6" data-topic="25147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7feea3/48.png" class="avatar"> lsprs:</div>
<blockquote>
<p>e.g. the euryon)</p>
</blockquote>
</aside>
<p>Euryon is a very poor choice of landmark. First it is a skull landmark (ie., you need the skull to measure it), and is defined as the pair of points that gives you the largest diameter of the skull. If you are using a caliper and working with an actual skull sitting on a table, you can empirically get the diameter fairly consistently doing few retakes, but the 3D coordinates of the L/R euryon can vary at cm scale. So be warned.</p>
<p>If you are insistent on using it, what you need is to use the line tool and draw a bunch of lines and take the one that gives you the largest mediolateral diameter. Then you can look at the coodinates of the two control points as your left and right euryon.</p>
<p>Doing this ‘virtually’ in 3D data is more challenging than doing physically, as the measurement will be susceptible to the orientation of the data. That’s why I believe neuroimaging folks defined a bunch of brain specific coordinate system, including stereotaxic ones so that measurements are consistent. For that you will have to register your data to one of those atlases and then transfer the points.</p>
<aside class="quote no-group" data-username="lsprs" data-post="6" data-topic="25147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/7feea3/48.png" class="avatar"> lsprs:</div>
<blockquote>
<p>however I’m interested in better understanding how these coordinates can be understood in mm.</p>
</blockquote>
</aside>
<p>To repeat, there is nothing to be understood from individual coordinates; they are just points in space. You can either do a multi-dimensional geometric (shape) analysis that directly uses the coordinates themselves or you can convert the coordinates to distances and use the distances to understand the shape of the brain. There are many papers that covers both approaches.</p>
<p>What is your goal?</p>

---

## Post #9 by @lsprs (2022-09-26 16:23 UTC)

<p>Apologies for my delay! Your response was very helpful.</p>

---
