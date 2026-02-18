# Is it possible to view more than two image volumes at the same time in slice viewers?

**Topic ID**: 8738
**Date**: 2019-10-10
**URL**: https://discourse.slicer.org/t/is-it-possible-to-view-more-than-two-image-volumes-at-the-same-time-in-slice-viewers/8738

---

## Post #1 by @Jason_West (2019-10-10 23:12 UTC)

<p>Hello,<br>
I am new here so I would first like to express my gratitude to all of you that are putting in such hard work to make this awesome tool available <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>So I know how to set the foreground and background images which works nicely for registrations and viewing a single dose wash over a CT however I have the need to view more than 2 volume nodes of differing opacity simultaneously.  These volumes would have the same dimensions however I need to be able to control window, level and thresholds separately otherwise I suppose it may be easiest to just combine them into one volume node.</p>
<p>Is there a mechanism currently that can support this?<br>
If not any thoughts on the best way to implement this?</p>
<p>Thanx! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2019-10-11 00:10 UTC)

<p>It is very hard to make out details even when only two volumes are blended, therefore there is no option on the GUI to blend more volumes.</p>
<p>You can easily combine any number of volumes, especially if they have the same geometry (image extents, origin, spacing, axis directions), using numpy. See this example in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Combine_multiple_volumes_into_one" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Combine_multiple_volumes_into_one</a></p>

---
