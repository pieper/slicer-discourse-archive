# Multiple volume renderings are not displayed correctly

**Topic ID**: 41147
**Date**: 2025-01-18
**URL**: https://discourse.slicer.org/t/multiple-volume-renderings-are-not-displayed-correctly/41147

---

## Post #1 by @Stuart (2025-01-18 23:54 UTC)

<p>My goal is to use the transforms editor to align two different volume renderings of the same skull, each rendered in a different color. No matter how I change the orientations, the gold version of the skull always shows “on top” and the red version only shows where there is miss alignment. To illustrate this, the first view is the superior view showing just a fringe of the red skull beneath, but when I rotated to reveal the inferior view the gold skull is still in front and just a bit of the red skull shows around the edges. Last is the inferior view with the gold version turned off just to demonstrate the presence of the red version. I would like to have the display show whichever view is “closer” as being in front of the other as I arbitrarily rotate the view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddebf761da6c1172aca1b8a4cccdbec59798a575.jpeg" data-download-href="/uploads/short-url/vFd4K7wltZVNnTYVSj3eJX9poih.jpeg?dl=1" title="Screenshot 2025-01-18 at 4.45.47 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddebf761da6c1172aca1b8a4cccdbec59798a575_2_690x325.jpeg" alt="Screenshot 2025-01-18 at 4.45.47 PM" data-base62-sha1="vFd4K7wltZVNnTYVSj3eJX9poih" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddebf761da6c1172aca1b8a4cccdbec59798a575_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddebf761da6c1172aca1b8a4cccdbec59798a575_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/ddebf761da6c1172aca1b8a4cccdbec59798a575_2_1380x650.jpeg 2x" data-dominant-color="432A1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-18 at 4.45.47 PM</span><span class="informations">1608×758 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for your assistance.</p>
<p>Stu</p>

---

## Post #2 by @pieper (2025-01-19 00:12 UTC)

<p>Yes, that’s a limitation of the default volume rendering method from VTK. You can change to the multi-volume option which is slower and has some other limitations but should do what you need here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a15198024260cc212ed18e2c17d3af1bba3b2b38.png" data-download-href="/uploads/short-url/n15GzmBtXhR7OdHDkaXXuZmcHK8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a15198024260cc212ed18e2c17d3af1bba3b2b38.png" alt="image" data-base62-sha1="n15GzmBtXhR7OdHDkaXXuZmcHK8" width="396" height="104"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">396×104 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>By the way you probably want to try an automated registration tool for this task.</p>

---

## Post #3 by @Stuart (2025-01-19 19:08 UTC)

<p>Thanks Steve for your suggestions. Alas, VTK Multi-Volume did not resolve the issue but at this point I’m getting into your suggestion to use an automated registration tool; specifically General Registration (BRAINS). This seems to be a better approach than the manual method I was using.</p>

---

## Post #4 by @muratmaga (2025-01-19 21:05 UTC)

<aside class="quote no-group" data-username="Stuart" data-post="3" data-topic="41147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/cab0a1/48.png" class="avatar"> Stuart:</div>
<blockquote>
<p>VTK Multi-Volume did not resolve the issue b</p>
</blockquote>
</aside>
<p>VTK Multi-volume should fix occlusion issues, and render the volumes in correct order. What version of Slicer are you using.</p>
<aside class="quote no-group" data-username="Stuart" data-post="3" data-topic="41147">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/cab0a1/48.png" class="avatar"> Stuart:</div>
<blockquote>
<p>This seems to be a better approach than the manual method I was using.</p>
</blockquote>
</aside>
<p>In general rigid registration should be faster and easier than manually aligning your volumes, if the starting positions similar to what you have shown in the screenshot.<br>
Registration methods can fail if the positions of the volumes are too dissimilar.</p>

---

## Post #5 by @Stuart (2025-01-19 22:05 UTC)

<p>I’m using 5.6.2. My start position is indeed that shown previously.</p>

---
