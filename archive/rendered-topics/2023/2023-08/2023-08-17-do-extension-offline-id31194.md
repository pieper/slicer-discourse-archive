# Do extension offline

**Topic ID**: 31194
**Date**: 2023-08-17
**URL**: https://discourse.slicer.org/t/do-extension-offline/31194

---

## Post #1 by @Kening_Zhang (2023-08-17 07:58 UTC)

<p>Dear developers,<br>
I want to make and test the extension written by myself, the extension was coded with python so I think it does not needed to be built but I am confused which step I should move to.<br>
I use extension Wizard to create it,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57f6a82b71a3746bd3e3e02b0605a09bfff7b1dc.jpeg" data-download-href="/uploads/short-url/cy9ZZIM4BH1P2qZQgFLzJoiXJFO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57f6a82b71a3746bd3e3e02b0605a09bfff7b1dc_2_690x239.jpeg" alt="image" data-base62-sha1="cy9ZZIM4BH1P2qZQgFLzJoiXJFO" width="690" height="239" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57f6a82b71a3746bd3e3e02b0605a09bfff7b1dc_2_690x239.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57f6a82b71a3746bd3e3e02b0605a09bfff7b1dc_2_1035x358.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57f6a82b71a3746bd3e3e02b0605a09bfff7b1dc_2_1380x478.jpeg 2x" data-dominant-color="F4F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1934×670 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Should I move to this step?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74246a633c1f326975223b2439b12aa597f325cf.png" data-download-href="/uploads/short-url/gzrpcUFN9s9HoWaFxdRtlmpiQsT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74246a633c1f326975223b2439b12aa597f325cf_2_690x325.png" alt="image" data-base62-sha1="gzrpcUFN9s9HoWaFxdRtlmpiQsT" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74246a633c1f326975223b2439b12aa597f325cf_2_690x325.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74246a633c1f326975223b2439b12aa597f325cf_2_1035x487.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74246a633c1f326975223b2439b12aa597f325cf.png 2x" data-dominant-color="EDF5DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1068×504 36.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However I think I dont have path of Slicer-SuperBuild-Release cause I did not build anything.<br>
Best wishes,<br>
Joshua</p>

---

## Post #2 by @lassoan (2023-08-17 13:06 UTC)

<p>A Python-scripted module does not require building to run it.</p>
<p>For testing, you can click the “Reload and test” button in the module GUI.</p>
<p>For packaging (create an extension package file) you currently need to build Slicer application and your extension. Packaging of extensions that only contain Python-scripted modules is mostly just gathering some version metadata and copying source files to appropriate locations. Therefore, it would not be too hard to make it work even without a build tree, but currently this is not supported. You can create a topic in the feature request category and if it gets enough votes then we’ll work on it.</p>

---

## Post #3 by @Kening_Zhang (2023-08-17 13:14 UTC)

<p>Actually I run it successfully already, but I want to try it for further download in extension manager, to be honest this topic is existed called WMA, maybe I should build Slicer app to test. Thanks a lot.</p>

---
