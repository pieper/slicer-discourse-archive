# Can I export the data for multiple points at once?

**Topic ID**: 42189
**Date**: 2025-03-17
**URL**: https://discourse.slicer.org/t/can-i-export-the-data-for-multiple-points-at-once/42189

---

## Post #1 by @MIZ (2025-03-17 20:35 UTC)

<p>I am landmarking approximately 44 points in a mesh. Exporting the x,y,z coordinates into an .fcsv file is extremely laborious. Is there any way to export the data for all 44 points simultaneously? Also, it would be great if when the data is exported it would go into a single .fcsv file, but that does not seem to be possible.</p>

---

## Post #2 by @park (2025-03-19 07:13 UTC)

<p>Hi,<br>
Try this code</p>
<pre><code class="lang-auto">markupsNode = getNode("yourMarkupsNodeName")
markupsArray = slicer.util.arrayFromMarkupsControlPoints(markupsNode)
</code></pre>
<p>In here, <code>markupsArray</code> is numpy array easy to export as file</p>
<p>I hope it is help to you.</p>

---

## Post #3 by @muratmaga (2025-03-19 16:25 UTC)

<aside class="quote no-group" data-username="MIZ" data-post="1" data-topic="42189">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/miz/48/79748_2.png" class="avatar"> MIZ:</div>
<blockquote>
<p>Exporting the x,y,z coordinates into an .fcsv file is extremely laborious</p>
</blockquote>
</aside>
<p>It is a single-click. right click and export as. I don’t think it can be made any more simpler.</p>

---

## Post #4 by @MIZ (2025-03-19 22:05 UTC)

<p>I need to export multiple markups (currently 44 points), but the ‘Export to File’ feature only works for individual markups/points. This means I cannot export all of my desired .fcsv files at once. Instead, I am currently exporting 44 individual .fcsv files, one for each point. Is there a way to export all .fcsv files at once or to combine all the markups/points into a single .fcsv file?</p>
<p>(Clarifying my previous post, thank you)</p>

---

## Post #5 by @pieper (2025-03-19 22:37 UTC)

<p>You can add all the points to the same Point List and then they will all export to the same file.</p>

---

## Post #6 by @muratmaga (2025-03-20 06:42 UTC)

<aside class="quote no-group" data-username="MIZ" data-post="4" data-topic="42189">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/miz/48/79748_2.png" class="avatar"> MIZ:</div>
<blockquote>
<p>I am currently exporting 44 individual .fcsv files, one for each point.</p>
</blockquote>
</aside>
<p>Is there a reason why you are doing this? I mean pointLists can contain an arbitrary number of control points. Don’t create new pointList objects, just keep adding the points to the existing one, and you will end up with a single object to save and not need to merge things later.</p>

---

## Post #7 by @MIZ (2025-04-06 21:51 UTC)

<p>When I try to export, I can only do one point at a time, I am attaching an image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e250cb119276f99ed65a02133db198dc762beefa.png" data-download-href="/uploads/short-url/wi50r2cAGHbdhIL9LP5Z19M1bOq.png?dl=1" title="Screenshot 2025-04-06 144119" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e250cb119276f99ed65a02133db198dc762beefa_2_690x310.png" alt="Screenshot 2025-04-06 144119" data-base62-sha1="wi50r2cAGHbdhIL9LP5Z19M1bOq" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e250cb119276f99ed65a02133db198dc762beefa_2_690x310.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e250cb119276f99ed65a02133db198dc762beefa_2_1035x465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e250cb119276f99ed65a02133db198dc762beefa.png 2x" data-dominant-color="454A53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-06 144119</span><span class="informations">1359×611 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Additionally, under “Data” when I do highlight multiple points, the option to export does not populate when I right click.</p>

---

## Post #8 by @muratmaga (2025-04-06 22:37 UTC)

<p>That because you have created 5  pointList objects each of which has a single point in. I am not sure what your use case is, but I assume want to have all those 5 points in <strong>single</strong> pointList object (e.g., just F_1).</p>
<p>I think you will benefit reviewing our Markups tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Markups_1" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/Markups_1 at main · SlicerMorph/Tutorials · GitHub</a> carefully.</p>
<p>Regardless, if that’s what you want (i.e., 5 separate files with one point in each), you can use standard Save (CTRL+S) and choose which ones to save. Export to file is meant to work on one file at a time.</p>

---

## Post #9 by @MIZ (2025-07-02 01:13 UTC)

<p>Thank you! My confusion was cleared.</p>

---
