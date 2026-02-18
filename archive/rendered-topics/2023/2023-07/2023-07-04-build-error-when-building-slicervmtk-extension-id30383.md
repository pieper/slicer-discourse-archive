# Build error when building SlicerVMTK extension

**Topic ID**: 30383
**Date**: 2023-07-04
**URL**: https://discourse.slicer.org/t/build-error-when-building-slicervmtk-extension/30383

---

## Post #1 by @paul.w (2023-07-04 04:44 UTC)

<p>Build error raised when building SlicerVMTK extension <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerExtension-VMTK</a> within VS2022, the  error code shows below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4368a0a17dc11eab86de7fe91e80cf9d7dbbb7c.png" data-download-href="/uploads/short-url/nqH9BnHeDTpjYEx3HmR8fi1OJAg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4368a0a17dc11eab86de7fe91e80cf9d7dbbb7c_2_690x356.png" alt="image" data-base62-sha1="nqH9BnHeDTpjYEx3HmR8fi1OJAg" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4368a0a17dc11eab86de7fe91e80cf9d7dbbb7c_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4368a0a17dc11eab86de7fe91e80cf9d7dbbb7c_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a4368a0a17dc11eab86de7fe91e80cf9d7dbbb7c_2_1380x712.png 2x" data-dominant-color="EAEBF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1721×888 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The Slicer 5.3.0 has been successfully built with Release, thus the environment should be okay, which is Win11 64bit (Windows SDK version 10.0.22000.0 to target Windows 10.0.22621) + VS2022 Community + CMake 3.24.3 + C compiler (MSVC 19.36.32535.0)</p>

---

## Post #2 by @cpinter (2023-07-04 14:50 UTC)

<p>What commit did you use for Slicer and what commit and repo did you used for SlicerVMTK?</p>

---

## Post #3 by @paul.w (2023-07-04 14:58 UTC)

<p>Slicer is the commit 30c31182ad6587117e79af5352fa6f22f38e998b, and SlicerVMTK is the commit cac7b299fae7a1f8115a770d6d0cb57c08952145</p>

---

## Post #4 by @jamesobutler (2023-07-04 15:07 UTC)

<p>Xref</p>
<aside class="quote" data-post="2" data-topic="30355">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vmtk-extension-fails-to-build-for-preview/30355/2">VMTK extension fails to build for preview</a> <a class="badge-category__wrapper " href="/c/community/vmtk/28"><span data-category-id="28" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This is the new home of the VMTK community (moved from VMTK Google Groups)"><span class="badge-category__name">VMTK</span></span></a>
  </div>
  <blockquote>
    Thank you for reporting. We’ve noticed this, too, and working on a fix. I expect it will work again by the end of this week.
  </blockquote>
</aside>


---

## Post #5 by @paul.w (2023-07-04 15:07 UTC)

<p>I checked the build process, the error is caused by the D:\Codes\SlicerVMTK_bin\VMTK\vtkVmtk\Misc codes, if I don’t build the Misc folder by commenting in the CMakeList, the build can succeed, but when Misc is missing, VMTK will not be fully functional. Hence I assumed there are some bugs with the codes of the Misc folder.</p>

---

## Post #6 by @paul.w (2023-07-04 15:13 UTC)

<p>Thanks. How can I work with SlicerVMTK by now?</p>
<p>Should I downgrade Slicer to 4.xx version, maybe the latest Slicer can not work well with the SlicerVMTK (somewhat old).</p>

---

## Post #7 by @jamesobutler (2023-07-04 15:17 UTC)

<p>SlicerVMTK is showing no build errors with latest Slicer stable (5.2.2). You can download Slicer stable from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> and install the SlicerVMTK extension using the Extensions Manager (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions" rel="noopener nofollow ugc">instructions</a>).</p>
<p><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=VMTK</a></p>

---

## Post #8 by @paul.w (2023-07-04 15:20 UTC)

<p>Cool, I will have a try</p>

---

## Post #9 by @lassoan (2023-07-04 15:36 UTC)

<p>The VMTK extension build error has been <a href="https://github.com/vmtk/SlicerExtension-VMTK/commit/48a071a88de626dc305134a1ac6e252fe0d5bed9">fixed</a>. The VMTK extension should be available again in Slicer Preview Releases from tomorrow.</p>

---

## Post #10 by @paul.w (2023-07-04 17:35 UTC)

<p>Bravo! The build passed with Slicer 5.3.0</p>

---

## Post #11 by @paul.w (2023-07-04 17:37 UTC)

<p>With VMTK 13c270693e9a808019f37f0d2794cb90ff43b2e0</p>

---
