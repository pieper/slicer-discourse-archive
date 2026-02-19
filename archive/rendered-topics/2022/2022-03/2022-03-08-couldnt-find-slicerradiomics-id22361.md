---
topic_id: 22361
title: "Couldnt Find Slicerradiomics"
date: 2022-03-08
url: https://discourse.slicer.org/t/22361
---

# Couldn't find SlicerRadiomics

**Topic ID**: 22361
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/couldnt-find-slicerradiomics/22361

---

## Post #1 by @xackey (2022-03-08 05:32 UTC)

<p>I couldn’t find SlicerRadiomics in the extension manager of the latest 3D Slicer (preview release).<br>
Could you tell me how to install the extension?</p>

---

## Post #2 by @pieper (2022-03-08 21:24 UTC)

<p>It’s not currently building in the preview release.  Probably best to use the stable for now until someone has a chance to look into the build errors.</p>

---

## Post #3 by @jamesobutler (2022-03-08 22:07 UTC)

<p>The specifics of the issue are found at the linked thread below. Currently, the issue hasn’t been looked into further.</p>
<aside class="quote quote-modified" data-post="1" data-topic="21935">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/factory-build-of-python-extensions-conflicting-with-each-other/21935">Factory build of python extensions conflicting with each other</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I noticed an issue occurring during the factory build of python extensions where an extension may be installing new python packages which results in Slicer core python packages having their installed version modified. This may be with general tools like pip, setuptools, etc. 
When this happens if impacts all extensions built afterwards which have to use modified versions of these packages. This makes it difficult to make sure a Slicer extension that includes additional python packages is going t…
  </blockquote>
</aside>


---
