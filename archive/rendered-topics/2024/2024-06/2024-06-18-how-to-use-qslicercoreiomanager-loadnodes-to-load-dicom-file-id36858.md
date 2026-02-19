---
topic_id: 36858
title: "How To Use Qslicercoreiomanager Loadnodes To Load Dicom File"
date: 2024-06-18
url: https://discourse.slicer.org/t/36858
---

# How to use qSlicerCoreIOManager::loadNodes to load dicom files by cpp

**Topic ID**: 36858
**Date**: 2024-06-18
**URL**: https://discourse.slicer.org/t/how-to-use-qslicercoreiomanager-loadnodes-to-load-dicom-files-by-cpp/36858

---

## Post #1 by @fqzhice (2024-06-18 08:06 UTC)

<p>To load  dicom series “.dcm” file, code is as below</p>
<pre><code class="lang-auto">    qSlicerCoreIOManager* ioManager = qSlicerCoreApplication::application()-&gt;coreIOManager();
    properties["fileName"] = file; // the first file in series
    ioManager-&gt;loadNodes("VolumeFile", properties );
</code></pre>
<p>some dicom files can be loaded as single volume, some generates multiple series for every dicom file</p>
<p>How can i solve this?</p>

---

## Post #2 by @lassoan (2024-06-18 19:23 UTC)

<p>DICOM files have to be loaded with the DICOM module. The IO plugin for the IO manager just calls the DICOM module to import the image, too.</p>
<p>There are often several different interpretations of a set of DICOM files, so you have to ask the user or make assumptions.</p>

---

## Post #3 by @fqzhice (2024-06-19 00:44 UTC)

<p>Thanks for your replay.<br>
Does that mean the first arguments should not only ‘VolumeFile’  and change according to some dicom feature?</p>

---

## Post #4 by @lassoan (2024-06-19 00:59 UTC)

<p>Specifying <code>VolumeFile</code> would use ITK library’s DICOM reader, which only loads some images correctly. It loads some images incorrectly or not at all, and it cannot read any other information objects. Therefore, I would recommend to always use the DICOM module for loading DICOM data. First you need to import the data, then examine, select what you want to load, and finally load them. You can find examples in the script repository. You can execute Python commands in C++ using the Python manager object.</p>

---

## Post #5 by @fqzhice (2024-06-19 01:02 UTC)

<p>yeah<br>
very appreciated！</p>

---
