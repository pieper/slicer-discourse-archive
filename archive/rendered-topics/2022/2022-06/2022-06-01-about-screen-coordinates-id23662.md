# About screen coordinates

**Topic ID**: 23662
**Date**: 2022-06-01
**URL**: https://discourse.slicer.org/t/about-screen-coordinates/23662

---

## Post #1 by @Changing (2022-06-01 01:26 UTC)

<p>Hello. Through the screenshot function of 3D slicer, I extracted an image from the green view. The shape of the extracted image is 634*441. The extracted image is displayed by opencv.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ca532c8e1cfd35da2d2fc415f6f855768e4e23b.png" alt="image" data-base62-sha1="ddzRw2lMloW0EnTz98qOaGZtP19" width="640" height="480"></p>
<p>The shape of the volume input to the 3D slicer is 240×240×208. Now I place markers in the green view of the 3D slicer as shown. And the IJK coordinates of the marker point is (134, 120, 143)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8a223b5d079dcbdb92bb9f76f7eedfb23152df4.png" alt="Screenshot" data-base62-sha1="qlleGlRv0FydelNrgVK6pXGWBvK" width="634" height="441"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b70d24d1b280018919b5c87238bdc2308f91c04f.png" data-download-href="/uploads/short-url/q7lxkyKo059B0KXphY6Uswlmd67.png?dl=1" title="1654006187(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b70d24d1b280018919b5c87238bdc2308f91c04f.png" alt="1654006187(1)" data-base62-sha1="q7lxkyKo059B0KXphY6Uswlmd67" width="689" height="151" data-dominant-color="858586"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1654006187(1)</span><span class="informations">1268×279 6.24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The problem is: When I convert the size and scale, the position of the marker points I draw in opencv is not the same as the position marked in the 3D slicer. The position of the marker point drawn in opencv is shown in the figure.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5184d8f51b9ba6a9ec3ec437769fa71e85215ba.png" alt="image" data-base62-sha1="nyuQN8FangIB4kPKfHkaT9T1nyq" width="640" height="480"></p>
<p>My coordinate conversion process is as follows：<br>
x = 634-(634×134/240)<br>
y = 441-(441×163/208)<br>
Is there something wrong with my coordinate conversion? I feel that there is no problem with the x coordinate, but there is a problem with the y coordinate. How can I fix this my problem.</p>
<p>And I found that the out of frame prompt appeared when I placed the marker F-3, what is the reason for this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1ba6012563a75644f7807686dc88e5dd1439824f.png" data-download-href="/uploads/short-url/3WAyo5pqAVjqPFgF0wilHtlu0lV.png?dl=1" title="1654006877(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ba6012563a75644f7807686dc88e5dd1439824f_2_690x207.png" alt="1654006877(1)" data-base62-sha1="3WAyo5pqAVjqPFgF0wilHtlu0lV" width="690" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ba6012563a75644f7807686dc88e5dd1439824f_2_690x207.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1ba6012563a75644f7807686dc88e5dd1439824f_2_1035x310.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1ba6012563a75644f7807686dc88e5dd1439824f.png 2x" data-dominant-color="7D7F81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1654006877(1)</span><span class="informations">1284×386 14.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-06-01 14:12 UTC)

<aside class="quote no-group" data-username="Changing" data-post="1" data-topic="23662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/a183cd/48.png" class="avatar"> Changing:</div>
<blockquote>
<p>screenshot function</p>
</blockquote>
</aside>
<p>Taking a screenshot means that the pixels have been scaled and translated by the view parameters.  You can learn the transformation back to source pixel space (see how it is done in the DataProbe source code) but it’s going to be awkward.  You’d be better off working with the image data as numpy arrays directly.  See the script repository for examples.</p>

---
