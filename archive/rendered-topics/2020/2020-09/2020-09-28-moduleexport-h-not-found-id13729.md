# ModuleExport.h not found

**Topic ID**: 13729
**Date**: 2020-09-28
**URL**: https://discourse.slicer.org/t/moduleexport-h-not-found/13729

---

## Post #1 by @Anish_Basnet (2020-09-28 10:36 UTC)

<p>Hello everyone,<br>
When compiling the slicer code, I am getting an error. What could be the reason for it? Do I need to change the Cmake.lists file? I am extending a loadable module. Do I need SubjectHierarchyPlugins directory in my module? I went through some other loadable modules such as Models and Markups. They have the folder named SubjectHierarchyPlugins.</p>
<p>Any help would be much appreciated!</p>
<p>Best regards,<br>
Anish</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a404dcd8134d6962f782bfc06fa8fbbdfc9ea50.png" data-download-href="/uploads/short-url/m0ziESe7QO3txBghxzLn6CZjId2.png?dl=1" title="ERROR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a404dcd8134d6962f782bfc06fa8fbbdfc9ea50.png" alt="ERROR" data-base62-sha1="m0ziESe7QO3txBghxzLn6CZjId2" width="690" height="107" data-dominant-color="5E5B5C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ERROR</span><span class="informations">1281×199 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-09-28 15:08 UTC)

<p>Do you build latest master version and follow <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html">these instructions</a>?</p>
<p>Did you have trouble building unmodified Slicer?<br>
You should not modify Slicer source code but add your custom modules in an extension.</p>

---
