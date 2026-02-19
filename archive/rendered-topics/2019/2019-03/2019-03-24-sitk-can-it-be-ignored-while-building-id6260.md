---
topic_id: 6260
title: "Sitk Can It Be Ignored While Building"
date: 2019-03-24
url: https://discourse.slicer.org/t/6260
---

# SITK : can it be ignored while building?

**Topic ID**: 6260
**Date**: 2019-03-24
**URL**: https://discourse.slicer.org/t/sitk-can-it-be-ignored-while-building/6260

---

## Post #1 by @chir.set (2019-03-24 10:19 UTC)

<p>I understood from comments in the forum, perhaps wrongly, that SITK can be excluded while building Slicer.</p>
<p>How far is this true ? If so, how would it impact Slicer’s usability ? What would be missing?</p>
<p>It’s just that it’s a long CPU intensive build.</p>
<p>Using Linux.</p>

---

## Post #2 by @pieper (2019-03-24 14:08 UTC)

<p>Yes, you can safely turn off Slicer_USE_SimpleITK when building to save time.  A few things won’t be available in the build, like SimpleFilters and WatershedFromMarkerEffect, but most things will work.</p>

---
