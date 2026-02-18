# Slicer build factory speed

**Topic ID**: 45358
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/slicer-build-factory-speed/45358

---

## Post #1 by @muratmaga (2025-12-03 20:16 UTC)

<p>It is now past 12p on the west coast (meaning half of the workday in US is gone), and the builds for today’s slicers are still not finished (Macos extensions are still ongoing). I am looking at the logs and it is looking like the whole cycle is taking almost a day, about 18-20h, and in fact sometimes seems to spill over to the next day (like these three macos extension are showing up for todays dashboard but belong to the previous revision number). Given that we are expected to have daily builds, and that the number of extensions are bound to increase, it might be time to plan for a different approach.</p>
<p>What that might be (do not do daily builds, parallelize the builds, rent faster servers), I don’t know but at it seems we are at capacity.</p>

---

## Post #2 by @lassoan (2025-12-03 22:43 UTC)

<p>We talked about this at the last developer meeting. It seems that the quick-exit mechanism that are used in tests trigger macOS crash reporting. The user needs to click a button to dismiss the popup or wait for the 15-minute test timeout to elapse. There are about 40 tests like this.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> planned to look into resolving this.</p>

---
