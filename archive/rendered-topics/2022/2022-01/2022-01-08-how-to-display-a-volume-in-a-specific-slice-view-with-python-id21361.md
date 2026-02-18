# How to display a volume in a specific slice view with Python

**Topic ID**: 21361
**Date**: 2022-01-08
**URL**: https://discourse.slicer.org/t/how-to-display-a-volume-in-a-specific-slice-view-with-python/21361

---

## Post #1 by @lauralatorre (2022-01-08 16:32 UTC)

<p>Hi,</p>
<p>I am trying to display 3 different volumes in a Three by three slice layout after pressing an Apply button in my module. I was wondering how can I set the slice views where to display each volume (for instance, I want to display volume3 in the 7,8 and 9 slice views). <code>slicer.util.loadVolume()</code> has no input arguments for that, so I was looking for a function similar to <code>slicer.util.setSliceViewerLayers()</code> that allows to set the volume displayed in each slice view. My aim is to avoid using the View Controllers module for that.</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2022-01-08 17:47 UTC)

<p>You should be able to use CompareVolumes for that, or if needed tweak the code.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/CompareVolumes" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/CompareVolumes</a></p>

---

## Post #3 by @lauralatorre (2022-01-09 12:20 UTC)

<p>That’s what I was looking for, thank you <a class="mention" href="/u/pieper">@pieper</a>!</p>

---
