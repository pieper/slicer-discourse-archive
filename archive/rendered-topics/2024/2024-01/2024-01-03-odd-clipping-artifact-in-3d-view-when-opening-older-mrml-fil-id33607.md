---
topic_id: 33607
title: "Odd Clipping Artifact In 3D View When Opening Older Mrml Fil"
date: 2024-01-03
url: https://discourse.slicer.org/t/33607
---

# Odd clipping artifact in 3D view when opening older MRML file into 2023-12-31 preview

**Topic ID**: 33607
**Date**: 2024-01-03
**URL**: https://discourse.slicer.org/t/odd-clipping-artifact-in-3d-view-when-opening-older-mrml-file-into-2023-12-31-preview/33607

---

## Post #1 by @hherhold (2024-01-03 19:48 UTC)

<p>I have a MRML file that had been working properly in an older preview (2023-10-26) but when I loaded it into the latest preview(2023-12-31) on windows, I would get an odd foreground clip artifact in the 3D view. This clipping did <em>not</em> happen in a late October 2023 preview (2023-10-26).</p>
<p>When I manually load in the segmentation file, the volume NRRD, and the markups file I’d been working on into the 2023-12-31 nightly (i.e., not using the MRML file), the issue disappeared. It looks like there may have been some old settings/dreck/whatever in the MRML that was confusing some of the newer settings, perhaps dealing with the new shadows visibility (which looks <em>AWESOME</em>, by the way).</p>
<p>This is not necessarily a request for a fix or investigation, just a post so that if anybody runs into this using a MRML file from a previous verison, you can ditch the MRML file and load in the individual files by hand via Add Data and things will show up properly.</p>

---

## Post #2 by @pieper (2024-01-03 19:55 UTC)

<p>Thanks for reporting.  If anyone thinks it’s serious enough, making a small mrml scene that allows replicating the issue would help with possible debugging.</p>

---

## Post #3 by @hherhold (2024-01-03 20:05 UTC)

<p>Sounds good, I can throw one together if someone thinks it’s worth debugging. The workaround is pretty simple.</p>
<p>It also might be related to interactions with the Lights module, I have that loaded in the 2023-10-26 preview and I’m not sure how well those settings interact with the new Shadows Visibility. Although Lights isn’t managing any of the views, so maybe that doesn’t have anything to do with it.</p>

---
