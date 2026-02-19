---
topic_id: 4940
title: "How To Run Scripted Or Loadable Modules From Shell Scrpt Bat"
date: 2018-12-03
url: https://discourse.slicer.org/t/4940
---

# How to run Scripted or loadable Modules from Shell Scrpt (batch mode?)

**Topic ID**: 4940
**Date**: 2018-12-03
**URL**: https://discourse.slicer.org/t/how-to-run-scripted-or-loadable-modules-from-shell-scrpt-batch-mode/4940

---

## Post #1 by @MachadoL (2018-12-03 16:42 UTC)

<p>Operating system: Linux Mint 17<br>
Slicer version: 4.9<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi everyone!</p>
<p>I would like to know if it is possible to call a scripted or loadable Slicer module in a shell script giving its specific parameter and so on (is it batch mode?) (E.g. Slicer Radiomics).</p>
<p>I would like to set a “for loop” to execute that module with a list of image, lable and parameters. I gues it is possible, though, I don’t know how to do it!</p>
<p>I appreciate all your comments on that!<br>
Thank you.</p>

---

## Post #2 by @pieper (2018-12-04 13:43 UTC)

<p>Hi <a class="mention" href="/u/machadol">@MachadoL</a> -</p>
<p>For scripting radiomics over a large group of subjects, it’s probably better to run PyRadiomics directly.  You can use the same config file for either SlicerRadiomics or PyRadiomics.  Have you looked into that?</p>
<p>-Steve</p>

---

## Post #4 by @MachadoL (2018-12-04 18:32 UTC)

<p>Hey <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>thanks for your feed back. Yeah, I found out that yesterday…<br>
Surely I will use it directly through PyRadiomics.</p>
<p>Than you!</p>

---
