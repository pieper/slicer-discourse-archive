---
topic_id: 38521
title: "No Linux Extensions"
date: 2024-09-24
url: https://discourse.slicer.org/t/38521
---

# No Linux extensions

**Topic ID**: 38521
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/no-linux-extensions/38521

---

## Post #1 by @muratmaga (2024-09-24 16:28 UTC)

<p>Cdash doesn’t report any Linux extensions. Looks like only Mac and Windows were build.</p>
<p><a href="https://slicer.cdash.org/index.php?project=SlicerStable" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerStable</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @jcfr (2024-09-24 17:31 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Indeed, it looks like the last step of the overall build process stopped while building the <code>SegmentEditorExtraEffects</code> Preview extension.</p>
<p>We will review the build tomorrow to further investigate.</p>
<p>In the meantime, are there particular updated extensions  for Slicer 5.6 you were expecting to have published  ?</p>

---
