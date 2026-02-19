---
topic_id: 25002
title: "Running External Python File From"
date: 2022-08-30
url: https://discourse.slicer.org/t/25002
---

# Running external python file from

**Topic ID**: 25002
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/running-external-python-file-from/25002

---

## Post #1 by @AMK (2022-08-30 14:35 UTC)

<p>Hi,</p>
<p>I have developed a deep learning model for segmentation. For the purpose of inference, I want to run a python file from Slicer. What commands should I use for this purpose?</p>

---

## Post #2 by @pieper (2022-08-30 15:57 UTC)

<p>You might be able to install all the needed python packages into Slicer’s python using the <code>slicer.util.pip_install</code> or if  it’s an independent python installation you can use <code>slicer.util.launchConsoleProcess</code>.</p>

---
