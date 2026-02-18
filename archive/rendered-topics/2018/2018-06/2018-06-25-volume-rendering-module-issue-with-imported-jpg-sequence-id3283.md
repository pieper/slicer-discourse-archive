# Volume rendering module issue with imported JPG sequence

**Topic ID**: 3283
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/volume-rendering-module-issue-with-imported-jpg-sequence/3283

---

## Post #1 by @LeviAthan (2018-06-25 16:34 UTC)

<p>Hi everyone,</p>
<p>I am trying to use the volume rendering module on a volume i imported from a sequence of grayscale JPG images. The sequences I have are thousands of microscopic slices of nerve specimens.<br>
When I try to use the volume rendering module i only get to see the top and bottom slice of the volume in the 3D volume.<br>
Please see the screenshot below. I managed to get the background transparent with the opacity settings but still i can only see the top and bottom slices. When i change the opacity settings, it shows me a solid block of slices, but i can’t manage to see only the nerve-parts of the slices in the rendering.<br>
Is this a known limitation when working with non-DICOM data or is there something I could do better?</p>
<p>Any advice is appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b50d414397f29170efcd440aac8852258466fbcd.jpeg" data-download-href="/uploads/short-url/pPEOSRyIdASlHnkzR0D3XiaSt5P.jpg?dl=1" title="Slicer-forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b50d414397f29170efcd440aac8852258466fbcd_2_690x388.jpg" alt="Slicer-forum" data-base62-sha1="pPEOSRyIdASlHnkzR0D3XiaSt5P" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b50d414397f29170efcd440aac8852258466fbcd_2_690x388.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b50d414397f29170efcd440aac8852258466fbcd_2_1035x582.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b50d414397f29170efcd440aac8852258466fbcd.jpeg 2x" data-dominant-color="BDBDC1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-forum</span><span class="informations">1280×720 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-06-25 16:38 UTC)

<p>This kind of volume rendering appearance usually indicates that your GPU is not compatible with Slicer.</p>
<p>Slicer-4.9 (nightly version of Slicer) uses new software interface, which is compatible with much wider range of GPUs, so I would recommend to switch to a recent nightly version.</p>
<p>If you do not want to switch to nightly builds then you need to select CPU volume rendering option, or upgrade your GPU.</p>

---
