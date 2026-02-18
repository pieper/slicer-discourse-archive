# Fail to open saved scene

**Topic ID**: 24284
**Date**: 2022-07-12
**URL**: https://discourse.slicer.org/t/fail-to-open-saved-scene/24284

---

## Post #1 by @SeaErhard (2022-07-12 12:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef7d2c223237615570672a39b000074a294a84f.png" data-download-href="/uploads/short-url/fPFtNGnA2OQVXf4hrESZUoyFkDR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef7d2c223237615570672a39b000074a294a84f.png" alt="image" data-base62-sha1="fPFtNGnA2OQVXf4hrESZUoyFkDR" width="690" height="420" data-dominant-color="F6F6F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">753×459 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hi all,<br>
After I installed 3D slicer version 5 in addition to 4.11 on my laptop, the saved scene could not be open.<br>
It only opens the 3D slicer as blank, when I double-click at the saved scene MRML file.<br>
I attached the error log from capturing the screen from the blank 3D slicer.<br>
Hope someone could help me.<br>
Thank you very much in advance.<br>
Best regards,<br>
Sea</p>

---

## Post #2 by @lassoan (2022-07-12 19:46 UTC)

<p>We aim for preserving backward compatibility with Slicer versions one major version before, so Slicer-4.x scenes should be Loadable in Slicer-5.x. If you can share a scene that reproduces the issue then we can investigate.</p>
<p>Note that you can always unzip a .mrb file (or save the scene as a .mrml file + data files) and load individual data files in a more recent Slicer version. Data file formats very rarely if ever change, so you can archive them for indefinitely long time and load in any Slicer versions (older or newer than the current version). Only the scene file (.mrml) requires specific Slicer version to load.</p>

---

## Post #3 by @SeaErhard (2022-07-13 15:00 UTC)

<p>Thank you very much for your kind reply and advice.<br>
It seems to work now. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I was just told that I had to drag and drop the scene on the slicer instead of double click on the scene.</p>

---
