---
topic_id: 3831
title: "Can Oct Scans Of File Format E2E Be Uploaded Into 3D Slicer"
date: 2018-08-19
url: https://discourse.slicer.org/t/3831
---

# Can OCT scans (of file format .E2E) be uploaded into 3D slicer

**Topic ID**: 3831
**Date**: 2018-08-19
**URL**: https://discourse.slicer.org/t/can-oct-scans-of-file-format-e2e-be-uploaded-into-3d-slicer/3831

---

## Post #1 by @Ingie_Baho (2018-08-19 10:18 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-08-19 10:22 UTC)

<p>I don’t think Slicer or any of its underlying toolkits can read this format, but it might not be too difficult to add support for it. Do you have a specification and sample data sets?</p>

---

## Post #3 by @Ingie_Baho (2018-08-19 11:28 UTC)

<p>I do not have sample data sets. The file format that I would like to load into slicer is an OCT scan. Unfortunately, the file format is .e2e which is. proprietary file format of Heidelberg. I would like to know if this can be uploaded into slicer. Or if there is a way I can convert this e2e file into a dicom file</p>

---

## Post #4 by @lassoan (2018-08-20 16:06 UTC)

<p>It seems that you need to ask developers of the proprietary software for an exporter or converter to any standard file format (or ask them to give you file format specification so that you can implement a converter).</p>

---

## Post #5 by @ihnorton (2018-08-23 13:56 UTC)

<p>ImageJ is often a good place to start for the question of how to read some niche or proprietary imaging format, and indeed it looks like some people have reverse-engineered this one:</p>
<p><a href="https://imagej.nih.gov/ij/plugins/heyex/index.html" class="onebox" target="_blank" rel="noopener">https://imagej.nih.gov/ij/plugins/heyex/index.html</a></p>
<p>Keywords there quickly lead me to a C++ implementation:</p>
<p><a href="https://bitbucket.org/uocte/uocte" class="onebox" target="_blank" rel="noopener">https://bitbucket.org/uocte/uocte</a></p>
<p>HTH,<br>
Isaiah</p>

---

## Post #6 by @Oli4 (2023-03-16 10:23 UTC)

<p>You can use the <a href="https://github.com/MedVisBonn/eyepy" rel="noopener nofollow ugc">eyepy</a> Python package to read images from E2E files and then write the numpy arrays to DICOM for an import to 3D Slicer.</p>
<p>Disclaimer: I am the developer of eyepy</p>

---
