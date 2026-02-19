---
topic_id: 17251
title: "Convert Nrrd To Dicom"
date: 2021-04-22
url: https://discourse.slicer.org/t/17251
---

# Convert NRRD to DICOM

**Topic ID**: 17251
**Date**: 2021-04-22
**URL**: https://discourse.slicer.org/t/convert-nrrd-to-dicom/17251

---

## Post #1 by @Lily (2021-04-22 12:08 UTC)

<p>Hello there!</p>
<p>I’m new to 3D slicer and I was wondering if there’s an easy way to convert thousands of nrrd images to dicom, I have already tried create a dicom series module but for that I will have to select the input volume one by one for over a thousand time.</p>
<p>Thank you for your time</p>

---

## Post #2 by @pieper (2021-04-22 14:33 UTC)

<p>Yes, you can do that but you need to write a python script.  It would be a pretty simple one.</p>

---

## Post #3 by @Lily (2021-04-22 18:01 UTC)

<p>Thank you! I was able to find how to load the images using python but I can’t find the function that converts them to dicom</p>

---

## Post #4 by @pieper (2021-04-22 19:45 UTC)

<p>The module to create a dicom series is a Command Line Interface (CLI) that you can run as described in the link below.  You can provide the parameters as you would when using the GUI.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python</a></p>

---

## Post #5 by @Lily (2021-04-22 20:45 UTC)

<p>Thank you very much, this has solved my problem! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=9" title=":smile:" class="emoji" alt=":smile:"></p>

---
