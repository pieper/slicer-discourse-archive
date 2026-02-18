# Export and/or retrieve a folder's hierarchy

**Topic ID**: 10906
**Date**: 2020-03-30
**URL**: https://discourse.slicer.org/t/export-and-or-retrieve-a-folders-hierarchy/10906

---

## Post #1 by @Melodicpinpon (2020-03-30 16:38 UTC)

<p>Good afternoon,</p>
<p>In the post about the 3D parts of the whole body, Andras Lasso achieved to recreate automatically the whole hierarchy and to get the names.</p>
<p>Is there a way to export a readable folder hierarchy from 3D Slicer or to get it with the script and import it inside another program?</p>
<p>Is there a way to retrieve the hierarchy of the Terminologia Anatomica 2 (TA2) in some way?</p>
<p>It would spare me much time.</p>
<p>I hope you are doing well in this particular period,</p>
<p>g.</p>

---

## Post #2 by @lassoan (2020-03-30 22:29 UTC)

<p>Here is the script that I used to convert BodyParts3D to a subject hierarchy tree: <a href="https://gist.github.com/lassoan/26e438c63e8249806958a408fb42c54a">https://gist.github.com/lassoan/26e438c63e8249806958a408fb42c54a</a></p>
<p>We have TA2-2.0.3 as a csv file, which could be used in Slicer to build hierarchies, but I’m not sure if it has been publicly released yet.</p>
<p><a class="mention" href="/u/mhalle">@mhalle</a> what is the status of this? Is the TA2 csv file allowed to be shared?</p>

---
