# CBCT parameters

**Topic ID**: 35960
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/cbct-parameters/35960

---

## Post #1 by @Basel04 (2024-05-07 10:37 UTC)

<p>Dear,<br>
Is there any way to adjust the CBCT parameters: Contrast, Sharpness in a similar way done in Romexis “Histogram”?<br>
I know there is a function as I attach here, but you wont see the values.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9e732ed604816fcdd2041b282831e71c5724df8.jpeg" data-download-href="/uploads/short-url/xncAHPubzDEzUZ4sRSrpRKsbmKk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e732ed604816fcdd2041b282831e71c5724df8_2_617x500.jpeg" alt="image" data-base62-sha1="xncAHPubzDEzUZ4sRSrpRKsbmKk" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e732ed604816fcdd2041b282831e71c5724df8_2_617x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e732ed604816fcdd2041b282831e71c5724df8_2_925x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e732ed604816fcdd2041b282831e71c5724df8_2_1234x1000.jpeg 2x" data-dominant-color="413F43"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1555 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regards,<br>
Basel</p>

---

## Post #2 by @cpinter (2024-05-08 10:10 UTC)

<p>These are basic functions of Slicer. The documentation is really useful if you haven’t checked that.</p>
<p>Adjusting window-level:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#adjusting-image-window-level</a></p>
<p>Volumes module:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html</a></p>
<p>It looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8658f44c58bb0710d3e4fb4cd8b7afc7370e7ea.png" data-download-href="/uploads/short-url/qjfrAWtRoOQPN84i90ha5GDTCLU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8658f44c58bb0710d3e4fb4cd8b7afc7370e7ea_2_518x500.png" alt="image" data-base62-sha1="qjfrAWtRoOQPN84i90ha5GDTCLU" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b8658f44c58bb0710d3e4fb4cd8b7afc7370e7ea_2_518x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8658f44c58bb0710d3e4fb4cd8b7afc7370e7ea.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8658f44c58bb0710d3e4fb4cd8b7afc7370e7ea.png 2x" data-dominant-color="E4E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">548×528 36.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
