# A single JPEG image in view

**Topic ID**: 34608
**Date**: 2024-02-29
**URL**: https://discourse.slicer.org/t/a-single-jpeg-image-in-view/34608

---

## Post #1 by @bzhu (2024-02-29 00:07 UTC)

<p>I created a customized grid layout, in which most views are used to view nifti files generated from different algorithms and one view is used to display a JPEG file showing analysis/comparison result of the algorithms.<br>
This view displays a single JPEG file. Once the picture is displayed, the slider value range goes automatically to [-1, 0, 1].<br>
When scrolling any one of other views (with scroll control enabled), the JPEG file disappears with slider going to -1 or 1. (The picture can be seen when slider is at 0.)<br>
I tried to set max and min to 0 for the slider but to no avail. Is there a way to fix the JPEG file in view without being controlled by scroll.</p>
<p>Sincerely,<br>
Bing<br>
UCLA</p>

---

## Post #2 by @pieper (2024-02-29 15:20 UTC)

<p>You could try setting the jpeg image to be thick so that it spans the full range of your other data so that if you are holding shift and moving the mouse in the other windows it stays within the single slice, something like this:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; v = getNode("im1")
&gt;&gt;&gt; v.SetSpacing(1,1,200)
</code></pre>

---
