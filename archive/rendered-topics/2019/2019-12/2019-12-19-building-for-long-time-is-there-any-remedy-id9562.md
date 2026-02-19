---
topic_id: 9562
title: "Building For Long Time Is There Any Remedy"
date: 2019-12-19
url: https://discourse.slicer.org/t/9562
---

# building for long time, is there any remedy

**Topic ID**: 9562
**Date**: 2019-12-19
**URL**: https://discourse.slicer.org/t/building-for-long-time-is-there-any-remedy/9562

---

## Post #1 by @appollosputnik (2019-12-19 13:20 UTC)

<p>Dear All</p>
<p>I have downloaded the source of slicer 3D and building it for Windows, My CMake configuration and generation is all OK with Qt 5.10.</p>
<p>But when I am building it, it takes a long time, for Windows 10 and Laptop. Is there anything that can be done to reduce the build time. Or is it taking for first time.?</p>
<p>Please give me some suggesstions.</p>
<p>Regards<br>
sujan</p>

---

## Post #2 by @lassoan (2019-12-19 13:23 UTC)

<p>Indeed, full build time on Windows can be long (few hours on a desktop, up to 10-12 hours on a laptop). Since you only need to build it once and all further builds are incremental, this is usually not a concern. Moreover, you rarely need to build Slicer core, but most of the time you make changes and build your own extension.</p>

---

## Post #3 by @appollosputnik (2019-12-19 13:53 UTC)

<p>Thanks for your valuable answer.</p>
<p>regards</p>

---
