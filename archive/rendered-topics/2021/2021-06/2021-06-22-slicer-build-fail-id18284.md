# Slicer build fail

**Topic ID**: 18284
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/slicer-build-fail/18284

---

## Post #1 by @smallvalthoss (2021-06-22 20:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f809d0703b35e6ce8b9d4081b016b759822cfa94.png" data-download-href="/uploads/short-url/zofrfx2EM4VPfYZlCboVOBXDvy4.png?dl=1" title="Slicer errors" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f809d0703b35e6ce8b9d4081b016b759822cfa94_2_690x122.png" alt="Slicer errors" data-base62-sha1="zofrfx2EM4VPfYZlCboVOBXDvy4" width="690" height="122" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f809d0703b35e6ce8b9d4081b016b759822cfa94_2_690x122.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f809d0703b35e6ce8b9d4081b016b759822cfa94_2_1035x183.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f809d0703b35e6ce8b9d4081b016b759822cfa94_2_1380x244.png 2x" data-dominant-color="323233"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer errors</span><span class="informations">3667×650 190 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I encountered these errors when trying to build. Any help would be appreciated.</p>

---

## Post #2 by @lassoan (2021-06-22 21:59 UTC)

<p>Most likely Anaconda messes up your build environment. You need to temporarily rename your main anaconda or conda folder to something else, build Slicer, and you can then restore the original name.</p>

---

## Post #3 by @smallvalthoss (2021-06-23 15:42 UTC)

<p>Thanks! I now just have one error:</p>
<pre><code class="lang-auto">Severity	Code	Description	Project	File	Line	Suppression State
Error	MSB8066	Custom build for 'D:\D\S4R\CMakeFiles\551ca37c0026cda4fee29f0729cb6475\python-update.rule;D:\D\S4R\CMakeFiles\551ca37c0026cda4fee29f0729cb6475\python-patch.rule;D:\D\S4R\CMakeFiles\551ca37c0026cda4fee29f0729cb6475\python-configure.rule;D:\D\S4R\CMakeFiles\551ca37c0026cda4fee29f0729cb6475\python-build.rule;D:\D\S4R\CMakeFiles\551ca37c0026cda4fee29f0729cb6475\python-install.rule;D:\D\S4R\CMakeFiles\551ca37c0026cda4fee29f0729cb6475\python-configure_python_launcher.rule;D:\D\S4R\CMakeFiles\3b657cd1f5796cbed5301f0e73ca6eec\python-complete.rule;D:\D\S4R\CMakeFiles\0b4a24838f508b9d1726cbe947087ed5\python.rule' exited with code 1.	python	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
</code></pre>

---

## Post #4 by @lassoan (2021-06-23 15:57 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-create-custom-markup/18305">How to create custom markup?</a></p>

---
