# Failed to fetch Sample from MONAI Label Server.

**Topic ID**: 37735
**Date**: 2024-08-06
**URL**: https://discourse.slicer.org/t/failed-to-fetch-sample-from-monai-label-server/37735

---

## Post #1 by @sowwn (2024-08-06 14:07 UTC)

<p>Hello everyone, Can you guys help me with this issue?</p>
<p>I deploy the MONAILabel server on Ubuntu, I connect to that IP on Mac.<br>
The connection is okay, but when I push on the Next Sample button, I get this error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83d635ed7cc3dbe491490c67e52196048e9c4f5d.png" data-download-href="/uploads/short-url/iOhuytHXTxDJZ8ioWg6nKxMiW8R.png?dl=1" title="Screenshot 2024-08-06 at 18.41.09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d635ed7cc3dbe491490c67e52196048e9c4f5d_2_690x300.png" alt="Screenshot 2024-08-06 at 18.41.09" data-base62-sha1="iOhuytHXTxDJZ8ioWg6nKxMiW8R" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d635ed7cc3dbe491490c67e52196048e9c4f5d_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d635ed7cc3dbe491490c67e52196048e9c4f5d_2_1035x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83d635ed7cc3dbe491490c67e52196048e9c4f5d_2_1380x600.png 2x" data-dominant-color="383937"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-08-06 at 18.41.09</span><span class="informations">1390×606 96.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The Python console show errors like this</p>
<pre><code class="lang-auto">[Python] 	Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)&gt;
[Python] Download failed (attempt 1 of 3)...
[Python] 	Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)&gt;
[Python] Download failed (attempt 2 of 3)...
[Python] 	Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)&gt;
[Python] Download failed (attempt 3 of 3)...
[Python] Failed to fetch Sample from MONAI Label Server.
[Python] 	Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)&gt;
[Python] Download failed (attempt 1 of 3)...
[Python] 	Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)&gt;
[Python] Download failed (attempt 2 of 3)...
[Python] 	Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1129)&gt;
[Python] Download failed (attempt 3 of 3)...
[Python] Failed to fetch Sample from MONAI Label Server.
</code></pre>
<p>The error is SSL but I don’t have experiments about that. Can you guys help me solve this problem?</p>
<p>Thank you!</p>

---
