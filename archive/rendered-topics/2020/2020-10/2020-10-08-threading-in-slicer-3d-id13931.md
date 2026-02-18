# Threading in Slicer 3d

**Topic ID**: 13931
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/threading-in-slicer-3d/13931

---

## Post #1 by @Chintha_Siva_Prasad (2020-10-08 05:40 UTC)

<p>I am creating a progress bar in slicer. But when using threads slicer is exiting abnormally.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/183ed92fdf75208452deee30f0ce8a8c7a6ecb8a.png" data-download-href="/uploads/short-url/3su6TZ2KWxKj8cmfUgqwNx692hI.png?dl=1" title="Screenshot from 2020-10-08 11-04-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/183ed92fdf75208452deee30f0ce8a8c7a6ecb8a_2_690x125.png" alt="Screenshot from 2020-10-08 11-04-13" data-base62-sha1="3su6TZ2KWxKj8cmfUgqwNx692hI" width="690" height="125" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/183ed92fdf75208452deee30f0ce8a8c7a6ecb8a_2_690x125.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/183ed92fdf75208452deee30f0ce8a8c7a6ecb8a_2_1035x187.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/183ed92fdf75208452deee30f0ce8a8c7a6ecb8a.png 2x" data-dominant-color="320D26"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-10-08 11-04-13</span><span class="informations">1291×235 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
This the runnable I created <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bb2be313edb0edca2df9d991fde040939777c1f.png" alt="Screenshot from 2020-10-08 11-04-46" data-base62-sha1="jVPk32OD03FxNS2p4JccVPEHFH9" width="454" height="230"><br>
This is the driver code<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f16f5780b17ff256aa6b20be5e98f9d5c5ab799e.png" alt="Screenshot from 2020-10-08 11-04-26" data-base62-sha1="yrPCnOZhywasGD5qExVZhJ3EtNY" width="588" height="251"></p>
<p>Why is the slicer exiting? Can I know how to create a progress bar in slicer qt that will get progressed on a thread?</p>

---

## Post #2 by @mikebind (2020-10-08 16:57 UTC)

<p>Do you need a separate thread?  Have you tried slicer.util.createProgressDialog()?  You might find these examples helpful: <a href="https://discourse.slicer.org/t/use-progress-bar-from-python/4343" class="inline-onebox">Use progress bar from python</a></p>

---

## Post #3 by @pieper (2020-10-08 19:12 UTC)

<p>You need to be very careful with threads in vtk and python.  Another alternative is to start processes instead.  <a href="https://github.com/pieper/SlicerProcesses">Here’s a prototype implementation</a> that works well.</p>

---
