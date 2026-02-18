# Why neighboured slices got overlaid in the Red-Slice-view after I get into the module of Screen-Capture?

**Topic ID**: 8066
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/why-neighboured-slices-got-overlaid-in-the-red-slice-view-after-i-get-into-the-module-of-screen-capture/8066

---

## Post #1 by @aiden.zhu (2019-08-16 22:07 UTC)

<p>Hi all and <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I happened to get a funny case as follows:<br>
A. I load a 20-slice 3D image data. The first and the second slice look just like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5506bb6406d1a8411e486d38e685619ab1c526e3.jpeg" data-download-href="/uploads/short-url/c8b0vBisn4xodbDf8nFpivucuMH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5506bb6406d1a8411e486d38e685619ab1c526e3_2_468x500.jpeg" alt="image" data-base62-sha1="c8b0vBisn4xodbDf8nFpivucuMH" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5506bb6406d1a8411e486d38e685619ab1c526e3_2_468x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5506bb6406d1a8411e486d38e685619ab1c526e3.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5506bb6406d1a8411e486d38e685619ab1c526e3.jpeg 2x" data-dominant-color="5C5858"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">499×532 61.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>  and <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7977ef42872d0c6d94837a283382066c0e0b6fda.jpeg" data-download-href="/uploads/short-url/hkyJqgl0p3hIcqEUQzCp1iSnFt8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7977ef42872d0c6d94837a283382066c0e0b6fda_2_468x500.jpeg" alt="image" data-base62-sha1="hkyJqgl0p3hIcqEUQzCp1iSnFt8" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7977ef42872d0c6d94837a283382066c0e0b6fda_2_468x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7977ef42872d0c6d94837a283382066c0e0b6fda.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7977ef42872d0c6d94837a283382066c0e0b6fda.jpeg 2x" data-dominant-color="656262"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">498×532 64.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So everything looks so cool there so far. and then<br>
B. I go to Screen-Capture and then I click to change the “Start sweep offset” to be 0.5. I got the slices changed as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55ac005332959e30c975a2c44c068aa705e0e062.jpeg" data-download-href="/uploads/short-url/cdT5X3vXpKEWEOUignvpbLGRmzU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55ac005332959e30c975a2c44c068aa705e0e062_2_532x500.jpeg" alt="image" data-base62-sha1="cdT5X3vXpKEWEOUignvpbLGRmzU" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/55ac005332959e30c975a2c44c068aa705e0e062_2_532x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55ac005332959e30c975a2c44c068aa705e0e062.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55ac005332959e30c975a2c44c068aa705e0e062.jpeg 2x" data-dominant-color="565352"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">667×626 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>  and <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6aa2db9546e37ac594b2eda442b2157d2d0de9.jpeg" data-download-href="/uploads/short-url/rjlF9zI5cHS4r8WA5UFJA3wuLoJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf6aa2db9546e37ac594b2eda442b2157d2d0de9_2_536x500.jpeg" alt="image" data-base62-sha1="rjlF9zI5cHS4r8WA5UFJA3wuLoJ" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bf6aa2db9546e37ac594b2eda442b2157d2d0de9_2_536x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6aa2db9546e37ac594b2eda442b2157d2d0de9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6aa2db9546e37ac594b2eda442b2157d2d0de9.jpeg 2x" data-dominant-color="635F5F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">672×626 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
You see the second slice right now has been reset (changed?) to a overlaid.</p>
<p>So do I miss something? or any refresh on some slicenodes?</p>
<p>Any comments are welcome and Thank you!</p>

---

## Post #2 by @lassoan (2019-08-17 19:40 UTC)

<p>Have a look at the slice position. As you can see, you are halfway between two slices, so the image that you see is a 50-50% mix of these two slices. Normally neighbor slices are similar, so you want this interpolated view, but in such extremely sparse image as yours (distance between slices is magnitudes larger than inplane spacing), you might want to disable interpolated display (click the pushpin icon in the top left corner of the slice view, then click button next to the volume selector in the slice view controller).</p>

---

## Post #3 by @aiden.zhu (2019-08-19 12:41 UTC)

<p>Thanks a lot for pointing out the interpolated display. Great! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
