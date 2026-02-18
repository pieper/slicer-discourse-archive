# Unable to install extension - "Incompatible with Slicer r30110"

**Topic ID**: 19158
**Date**: 2021-08-11
**URL**: https://discourse.slicer.org/t/unable-to-install-extension-incompatible-with-slicer-r30110/19158

---

## Post #1 by @fedorov (2021-08-11 18:14 UTC)

<p>I tried and failed to install SlicerRadiomics extension with the current Slicer preview. Is it expected? Sorry if I missed announcements and migration guidelines. I searched, but not sure where I should search - the error is not particularly helpful in informing about how the issue can be remedied.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15acb080d5c1fd2f5e3122a97d397c27e52d6d8c.png" data-download-href="/uploads/short-url/35K0LuejXxF7Qf2itVZGSDNMxo8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15acb080d5c1fd2f5e3122a97d397c27e52d6d8c_2_690x284.png" alt="image" data-base62-sha1="35K0LuejXxF7Qf2itVZGSDNMxo8" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/15acb080d5c1fd2f5e3122a97d397c27e52d6d8c_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15acb080d5c1fd2f5e3122a97d397c27e52d6d8c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/15acb080d5c1fd2f5e3122a97d397c27e52d6d8c.png 2x" data-dominant-color="E9EBEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">996×410 67.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jcfr (2021-08-11 18:20 UTC)

<p>Thanks for the report, it is a side effect of <a href="https://discourse.slicer.org/t/upcoming-downtime-for-download-slicer-org-and-extension-manager-due-to-package-server-transition/17444/3" class="inline-onebox">Upcoming downtime for download.slicer.org and extension manager due to package server transition - #3 by jcfr</a>, issue has been identified earlier today and I am currently working on this.</p>
<p>For reference, this is now tracked in <a href="https://github.com/Slicer/Slicer/issues/5786" class="inline-onebox">Installed extensions are not loaded · Issue #5786 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @jcfr (2021-08-13 08:03 UTC)

<p>To follow up, issue has been fixed by the following pull-requests (Slicer &gt;= <code>r30117</code>):</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/5790" class="inline-onebox">BUG: Fix loading of extension installed using "Girder_v1" serverAPI by jcfr · Pull Request #5790 · Slicer/Slic</a></li>
<li><a href="https://github.com/Slicer/Slicer/pull/5791" class="inline-onebox">Fix extensions manager issues associated with "Girder_v1" server API integration by jcfr · Pull Request #5791</a></li>
</ul>

---
