---
topic_id: 40585
title: "Problem Debugging Slicervirtualreality Extension"
date: 2024-12-09
url: https://discourse.slicer.org/t/40585
---

# Problem debugging SlicerVirtualReality extension

**Topic ID**: 40585
**Date**: 2024-12-09
**URL**: https://discourse.slicer.org/t/problem-debugging-slicervirtualreality-extension/40585

---

## Post #1 by @petr.raunigr (2024-12-09 15:43 UTC)

<p>Hello,</p>
<p>I need help with debugging process of the SlicerVirtualReality extension. First things first… what I managed to do:</p>
<ol>
<li>Cloned 3D Slicer repo and built it (debug).</li>
<li>Tried running 3D Slicer which was ok.</li>
<li>Tried to debug it and it was also ok.</li>
<li>Then I cloned the SlicerVirtualReality repo and built it (debug).</li>
<li>Tried SlicerWithSlicerVirtualReality.exe and it works fine.</li>
<li>Created a BAT file containing this: D:\Slicer3D_git\build_debug\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings D:/Slicer_plugins/SlicerVirtualReality/build_debug/inner-build/AdditionalLauncherSettings.ini  D:/Slicer_plugins/SlicerVirtualReality/build_debug/inner-build/SlicerVirtualReality.sln</li>
<li><strong>Run the BAT file, VS project opens, set the slicer-real.exe path as a command in debugging project settings, start project debug which opens up the 3D Slicer app BUT without the SlicerVirtualReality extension present.</strong></li>
</ol>
<p><em><strong>Can anyone guess what am I missing? Maybe something in CMake?</strong></em></p>
<p>I was following this official tutorial: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html" class="inline-onebox" rel="noopener nofollow ugc">C++ debugging on Windows — 3D Slicer documentation</a><br>
I also tried this forum post response: <a href="https://discourse.slicer.org/t/debug-slicer-and-slicerrt-together/26955/6" class="inline-onebox">Debug Slicer and SlicerRT Together - #6 by cpinter</a></p>
<p>I searched on this forum and found several posts more or less talking about extensions, debugging etc., but non of them yielded a correct solution.</p>

---

## Post #2 by @cpinter (2024-12-09 15:48 UTC)

<p>Do you see anything in Application Settings / Modules / Additional module paths?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f6f1a9dd6fd4f32deb19fb1f030230916e880b4.png" data-download-href="/uploads/short-url/93a7qvgEFsBsxGya4ma63h5VlpG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f6f1a9dd6fd4f32deb19fb1f030230916e880b4.png" alt="image" data-base62-sha1="93a7qvgEFsBsxGya4ma63h5VlpG" width="669" height="297"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">669×297 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If not, maybe you need to add here the <code>qt-loadable-modules/Debug</code> folder.</p>
<p>Is there any error in the Python console or the Error log right after startup?</p>

---

## Post #3 by @petr.raunigr (2024-12-10 08:14 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33990d487a9a2350d83f0fa8d9b70cba8e913fce.png" data-download-href="/uploads/short-url/7msgjxKsfwg4nPEBoaRsBebjfci.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33990d487a9a2350d83f0fa8d9b70cba8e913fce_2_690x417.png" alt="image" data-base62-sha1="7msgjxKsfwg4nPEBoaRsBebjfci" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33990d487a9a2350d83f0fa8d9b70cba8e913fce_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33990d487a9a2350d83f0fa8d9b70cba8e913fce_2_1035x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33990d487a9a2350d83f0fa8d9b70cba8e913fce_2_1380x834.png 2x" data-dominant-color="CAC9CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1162 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That’s how the 3D Slicer settings looks like when I open it up using SlicerWithSlicerVirtualReality.exe file. You can see that the extension is there (icons on top left corner + Virtual Reality module which is selected) but no modules folders added.</p>
<p>There is also one error in the Python console.</p>
<p>Starting the debug session in VS project (SlicerVIrtualReality) opens up 3D Slicer with the same python console error but without the extension</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91837e61cad20a5938da20b7081c4809834e6aa0.png" data-download-href="/uploads/short-url/kLgXlbA1hNc8w83jQc7dl84rb1e.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91837e61cad20a5938da20b7081c4809834e6aa0_2_690x417.png" alt="image" data-base62-sha1="kLgXlbA1hNc8w83jQc7dl84rb1e" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91837e61cad20a5938da20b7081c4809834e6aa0_2_690x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91837e61cad20a5938da20b7081c4809834e6aa0_2_1035x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91837e61cad20a5938da20b7081c4809834e6aa0_2_1380x834.png 2x" data-dominant-color="C5C4C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1161 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Python error</strong><br>
QWindowsWindow::setGeometry: Unable to set geometry 675x623+2543+312 (frame: 691x662+2535+281) on QWidgetWindow/“ctkSettingsDialogWindow” on “\.\DISPLAY2”. Resulting geometry: 675x633+2543+312 (frame: 691x672+2535+281) margins: 8, 31, 8, 8 minimum size: 675x623 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=691,662 maxtrack=0,0)</p>
<p>BUT…</p>
<p><strong>I tried your advice to add the Debug folder and it worked actually. Thanks a lot!</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/646bccdb100700c3986eaf23994cdb920a669f37.png" data-download-href="/uploads/short-url/ekmHTllVDEmxa3RoiUyLPJyrvV5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646bccdb100700c3986eaf23994cdb920a669f37_2_690x416.png" alt="image" data-base62-sha1="ekmHTllVDEmxa3RoiUyLPJyrvV5" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646bccdb100700c3986eaf23994cdb920a669f37_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646bccdb100700c3986eaf23994cdb920a669f37_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/646bccdb100700c3986eaf23994cdb920a669f37_2_1380x832.png 2x" data-dominant-color="C7C6CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Even a second problem with breakpoints not being able to be hit due to no symbols loaded for extensions code is gone.</p>
<p>It’s weird a bit since I tried it already once and it didn’t work the first time. I added it based on following extension building tutorial (option: it is build - Option B)<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#windows</a></p>

---

## Post #4 by @cpinter (2024-12-10 10:25 UTC)

<aside class="quote no-group" data-username="petr.raunigr" data-post="3" data-topic="40585">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/2acd7d/48.png" class="avatar"> petr.raunigr:</div>
<blockquote>
<p>There is also one error in the Python console.</p>
</blockquote>
</aside>
<p>This error also appears for me using the latest revisions.</p>
<aside class="quote no-group" data-username="petr.raunigr" data-post="3" data-topic="40585">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/2acd7d/48.png" class="avatar"> petr.raunigr:</div>
<blockquote>
<p>using SlicerWithSlicerVirtualReality.exe file. You can see that the extension is there</p>
</blockquote>
</aside>
<p>That executable adds the necessary paths to include the extension. However, when you debug you need to use the <code>SlicerApp-real.exe</code>, which is not a launcher, so it does not add any paths. So you need to make sure the application loads the extension.</p>
<p>You do use the launcher when you start Visual Studio, but that is the basic Slicer launcher. Maybe you can use the <code>SlicerWithSlicerVirtualReality.exe</code> for starting VS and then not add the module directories, bue I haven’t tried that personally.</p>

---
