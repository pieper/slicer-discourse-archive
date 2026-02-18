# Opening ExtensionManager while running Slicer as root crashes the app

**Topic ID**: 23666
**Date**: 2022-06-01
**URL**: https://discourse.slicer.org/t/opening-extensionmanager-while-running-slicer-as-root-crashes-the-app/23666

---

## Post #1 by @fedorov (2022-06-01 03:15 UTC)

<p>I have a setup where Slicer is run as root from within a docker container. When I try to open Extension Manager, I get a crash with the latest stable Slicer. Is this expected?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c55d93dba003f17a6666e001e3c0ec140e63324.jpeg" data-download-href="/uploads/short-url/42Fix99eCbpiQXCOXyNCMTj89gg.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c55d93dba003f17a6666e001e3c0ec140e63324_2_690x189.jpeg" alt="image" data-base62-sha1="42Fix99eCbpiQXCOXyNCMTj89gg" width="690" height="189" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c55d93dba003f17a6666e001e3c0ec140e63324_2_690x189.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c55d93dba003f17a6666e001e3c0ec140e63324_2_1035x283.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c55d93dba003f17a6666e001e3c0ec140e63324.jpeg 2x" data-dominant-color="1B1B1A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1372×376 95.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-06-01 13:59 UTC)

<p>Based on the error message I would say yes, this is the expected behavior.</p>
<p><a href="https://bugs.chromium.org/p/chromium/issues/detail?id=638180" class="onebox" target="_blank" rel="noopener">https://bugs.chromium.org/p/chromium/issues/detail?id=638180</a></p>

---

## Post #3 by @pieper (2022-06-01 14:00 UTC)

<p>Since you are root you can just switch to being a normal user to run Slicer.</p>

---
