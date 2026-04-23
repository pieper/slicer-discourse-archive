---
topic_id: 46809
title: "Create New Cfg Error Radrenderer"
date: 2026-04-22
url: https://discourse.slicer.org/t/46809
---

# Create new cfg error RadRenderer

**Topic ID**: 46809
**Date**: 2026-04-22
**URL**: https://discourse.slicer.org/t/create-new-cfg-error-radrenderer/46809

---

## Post #1 by @Jeffrey_K_Spear (2026-04-22 17:40 UTC)

<p>Hello,</p>
<p>I am trying to create a new .cfg file. I launch Autoscoper, click ‘new file’, add the calibration files, radiographs (), and partial volumes. When I click ‘OK’ Autoscoper shuts down and the following error gets spit out into the Slicer console: “RadRenderer::rad(): Unsupported bit depth 12”.</p>
<p>I also tried creating a configuration file by scratch by taking one I knew worked and changing the information using notepad, but I get the same error when trying to load the .cfg file.</p>
<p>I am currently troubleshooting through trial and error but I thought perhaps someone might have seen this before and know what the problem is (and what I should be looking to fix)! Maybe something to do with the bit depth of my radiographs?</p>
<p>Thanks!</p>

---

## Post #2 by @John_Holtgrewe (2026-04-22 19:54 UTC)

<p>Hi Jeff,</p>
<p>We have run into this issue as well. Currently, SAM cannot read in higher bit depth images. Can you reduce the bit-depth to 8-bit and try creating/loading the .cfg file again?</p>
<p>Thanks!</p>
<p>John</p>

---

## Post #3 by @Jeffrey_K_Spear (2026-04-22 21:13 UTC)

<p>Yes, that worked perfectly, thank you!</p>

---
