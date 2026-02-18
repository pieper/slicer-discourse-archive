# Zoom in linked slices gets out of sync when using right-click+drag

**Topic ID**: 21678
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/zoom-in-linked-slices-gets-out-of-sync-when-using-right-click-drag/21678

---

## Post #1 by @koeglfryderyk (2022-01-28 14:00 UTC)

<p>I linked the slice views and when I right-click+drag to change the field of view (zoom) only the field of view of the slice where my mouse is is changed.</p>
<p>When I use ctrl+scroll all the linked slice views get synced and change together.</p>
<p>I’m using version 4.13.0 revision 30566 built 2022-01-28</p>
<p>Is this a feature or a bug? (or am I doing something wrong?)</p>
<p>In version 4.11.20210226 revision 29738 built 2021-03-01 both right-click+drag and ctrl+scroll changed the field of view of all linked slices</p>

---

## Post #2 by @lassoan (2022-01-28 17:07 UTC)

<p><a class="mention" href="/u/dgmato">@dgmato</a> can you check if this is a regression related to the new slice intersections feature?</p>

---

## Post #3 by @koeglfryderyk (2022-01-29 22:19 UTC)

<p>In the next build (version 4.13.0; revision 30570; built 2022-01-29) both methods work again</p>

---
