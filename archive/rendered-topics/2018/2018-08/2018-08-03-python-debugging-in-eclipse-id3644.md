# Python debugging in Eclipse

**Topic ID**: 3644
**Date**: 2018-08-03
**URL**: https://discourse.slicer.org/t/python-debugging-in-eclipse/3644

---

## Post #1 by @Saima (2018-08-03 03:45 UTC)

<p>Dear Andras,<br>
Can you help me with setup IDE liclipse with slicer. I did all the steps. The slicer is connected but when I debug it gives me error.<br>
Please see the screen shot below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4aac54dd76223b97caedbe841d472ecd859fd45b.png" data-download-href="/uploads/short-url/aEAybq6vpo7jgHcddBsmot2914D.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4aac54dd76223b97caedbe841d472ecd859fd45b_2_690x388.png" alt="image" data-base62-sha1="aEAybq6vpo7jgHcddBsmot2914D" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4aac54dd76223b97caedbe841d472ecd859fd45b_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4aac54dd76223b97caedbe841d472ecd859fd45b_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4aac54dd76223b97caedbe841d472ecd859fd45b_2_1380x776.png 2x" data-dominant-color="E8E9EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 306 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I dont know what I am doing wrong.<br>
Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2018-08-03 09:38 UTC)

<p>You need to start remote debugger, not try to run the module from Eclipse.</p>
<p>You may be able to get auto-complete, documentation, etc. If you set PythonSlicer.exe as Python interpreter in Eclipse.</p>

---
