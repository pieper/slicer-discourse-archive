# Change default location for screenshots

**Topic ID**: 31805
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/change-default-location-for-screenshots/31805

---

## Post #1 by @mohammed_alshakhas (2023-09-20 15:27 UTC)

<p>I wish it is  possible to select the location of the screenshot instead of the default parent folder and change the default location for screenshots.<br>
at least if I change it, it stays as changed but unfortunately, I have to change it every time I save a screenshot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6356e865b6a251010eb6b9716eb043e102c1319.jpeg" data-download-href="/uploads/short-url/shr0ZXz1GMNgtv5FuIPbHwRYhFT.jpeg?dl=1" title="Screenshot 2023-09-20 at 18.21.56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6356e865b6a251010eb6b9716eb043e102c1319_2_690x388.jpeg" alt="Screenshot 2023-09-20 at 18.21.56" data-base62-sha1="shr0ZXz1GMNgtv5FuIPbHwRYhFT" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6356e865b6a251010eb6b9716eb043e102c1319_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6356e865b6a251010eb6b9716eb043e102c1319_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6356e865b6a251010eb6b9716eb043e102c1319_2_1380x776.jpeg 2x" data-dominant-color="29282B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-20 at 18.21.56</span><span class="informations">1920×1080 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-09-20 20:50 UTC)

<p>This would be a good first issue for a new developer.  It shouldn’t be hard to save the path in the settings file.</p>

---

## Post #3 by @lassoan (2023-09-21 20:18 UTC)

<p>The Screen Capture module can take screenshots and animations (slicing through a volume, rotating a 3D view, replaying a time sequence, etc.) of views, directly to a selected folder.</p>
<p><strong>What do you think about updating the screen capture toolbar to use the Screen Capture module to save screenshots directly to a folder?</strong> For the user not much would need to be changed, but it would allow us to simplify the application design (we could completely deprecate the annotation module, because annotation snapshot is the last node type that the module still can create and save).</p>
<p>Note that you can also copy the content of any view as an image using the right-click menu; and the Animator module of SlicerMorph extension offers some additional animation options, such as blowing-up models or cropping a volume.</p>

---
