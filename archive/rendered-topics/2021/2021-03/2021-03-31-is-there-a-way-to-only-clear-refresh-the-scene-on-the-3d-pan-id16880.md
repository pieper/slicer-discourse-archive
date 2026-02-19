---
topic_id: 16880
title: "Is There A Way To Only Clear Refresh The Scene On The 3D Pan"
date: 2021-03-31
url: https://discourse.slicer.org/t/16880
---

# Is there a way to only clear/refresh the scene on the 3D panel?

**Topic ID**: 16880
**Date**: 2021-03-31
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-only-clear-refresh-the-scene-on-the-3d-panel/16880

---

## Post #1 by @will_kim (2021-03-31 17:13 UTC)

<p>Hi, I was wondering if it is possible to clear the scene on the 3D panel without touching the other slices(red, green, yellow). Thank you.</p>

---

## Post #2 by @jamesobutler (2021-03-31 19:06 UTC)

<p>Are you looking to show/hide a volume in the 3D View that is currently shown in one of the slice views (red, green, yellow) without pressing the “eye” icon in the individual slice controller? Are you wanting to maintain the volume in these 2D slice views or are you wanting to completely remove them from the Slicer scene?</p>
<p>Are you looking for a programmatic solution using python?</p>

---

## Post #3 by @will_kim (2021-03-31 21:52 UTC)

<p>Hi, thanks for getting back. Yes, I am looking for a programmatic solution using python. I would like to keep the MRI images on the 2D slice and completely remove the scene on the 3D panel if it is possible.</p>

---

## Post #4 by @jamesobutler (2021-04-01 13:51 UTC)

<p>There is an example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">Slicer Script Repository</a> regarding how to “show slice views in 3D window”.  You can set the boolean to True to show them, or to False to hide them as you are desiring. Let us know how it works for you!</p>

---
