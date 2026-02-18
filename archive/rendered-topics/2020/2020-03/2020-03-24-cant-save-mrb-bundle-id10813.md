# Can't save mrb bundle

**Topic ID**: 10813
**Date**: 2020-03-24
**URL**: https://discourse.slicer.org/t/cant-save-mrb-bundle/10813

---

## Post #1 by @PalkoD (2020-03-24 11:54 UTC)

<p>Operating system: macOS Catalina 10.15.2<br>
Slicer version: 4.11.0<br>
Expected behavior: Save the scene<br>
Actual behavior: Error saying could not make temp directory</p>
<p>Hi!<br>
I’m new to slicer and just scratching the surface. I have a problem. Whenever I want to save in mrb format, an error code pops up and says, that “Could not make temp directory” and "Cannot write scene file, regardless of the selected directory. However when I save all the files separately saving works just fine.<br>
The .log file is not visible in the report bug window and when I open the error log window, the software freezes and the only way to close it is to force quit.<br>
Is there any solution to this.<br>
Thank you for the help in advance!</p>
<p>Greetings: Daniel</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34a6607ec9c937bd359a73db1ff12b256c9fc562.png" data-download-href="/uploads/short-url/7vLhWsyC5h1DgEGOu9meBY9ytUu.png?dl=1" title="Screen Shot 2020-03-24 at 11.34.26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34a6607ec9c937bd359a73db1ff12b256c9fc562_2_690x417.png" alt="Screen Shot 2020-03-24 at 11.34.26" data-base62-sha1="7vLhWsyC5h1DgEGOu9meBY9ytUu" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34a6607ec9c937bd359a73db1ff12b256c9fc562_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34a6607ec9c937bd359a73db1ff12b256c9fc562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34a6607ec9c937bd359a73db1ff12b256c9fc562.png 2x" data-dominant-color="DEE2EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-03-24 at 11.34.26</span><span class="informations">763×462 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-03-24 12:00 UTC)

<p>As the error message shows, the problem is that your temporary directory is not writeable. Choose a writeable directory in menu: Edit / Application settings / Modules / Temporary directory.</p>

---

## Post #3 by @PalkoD (2020-03-25 11:15 UTC)

<p>Thank you very much it works now.</p>

---
