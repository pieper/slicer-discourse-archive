# slicer.modules.DICOMWidget.browserWidget.dicomBrowser does not work in preview release

**Topic ID**: 23354
**Date**: 2022-05-10
**URL**: https://discourse.slicer.org/t/slicer-modules-dicomwidget-browserwidget-dicombrowser-does-not-work-in-preview-release/23354

---

## Post #1 by @koeglfryderyk (2022-05-10 02:41 UTC)

<p>Slicer version 5.1.0, revision 30927, built 2022-05-09, MacOS</p>
<p>I tried to follow an example for loading dicoms form the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#import-dicom-files-into-the-application-s-dicom-database" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>, however</p>
<pre><code class="lang-auto">slicer.modules.DICOMWidget.browserWidget.dicomBrowser
</code></pre>
<p>does not work, it throws only the following error:</p>
<blockquote>
<p>AttributeError: module ‘modules’ has no attribute ‘DICOMWidget’</p>
</blockquote>

---

## Post #2 by @lassoan (2022-05-10 04:17 UTC)

<p>This is how it is supposed to work: module widgets are only instantiated when they are needed (i.e., when you switch to a module the first time). That is why the script example starts with switching to the DICOM module.</p>

---
