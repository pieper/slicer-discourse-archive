---
topic_id: 3617
title: "How To Read Nested Dicom Metadata"
date: 2018-07-31
url: https://discourse.slicer.org/t/3617
---

# How to read nested DICOM metadata

**Topic ID**: 3617
**Date**: 2018-07-31
**URL**: https://discourse.slicer.org/t/how-to-read-nested-dicom-metadata/3617

---

## Post #1 by @dominicrushforth (2018-07-31 10:20 UTC)

<p>I’m new to slicer and python. Currently I’m trying to write an extension that involves reading nested dicom files. I can read normal files using this code…</p>
<pre><code class="lang-auto">instUids=dicomData.split()
filename=slicer.dicomDatabase.fileForInstance(instUids[0])
aquisitionModality[volumeNumber] = slicer.dicomDatabase.fileValue(filename,'0008,0060')
</code></pre>
<p>but I have been unable to read nested tags such as (0008,1032) (fffe,e000) (0008,0104) - where the tags are labelled in this order in the DICOM File Metadata display. I’m sure I must be missing something very simple…</p>

---

## Post #2 by @lassoan (2018-07-31 10:45 UTC)

<p>To access DICOM tags within sequence (SQ) tags, you can get the DICOM filename as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2">here</a>, then use <a href="https://pydicom.github.io/pydicom/0.9/getting_started.html">pydicom</a> (bundled with Slicer) to read the file and retrieve any values.</p>

---

## Post #3 by @Alex_Vergara (2019-02-15 15:17 UTC)

<p>this has no direct answer but here it is how to do it using pydicom</p>
<pre><code class="lang-python">import dicom
instUids=dicomData.split()
filename=slicer.dicomDatabase.fileForInstance(instUids[0])
plan = dicom.read_file(filename)
aquisitionModality[volumeNumber] = float(plan[0x08,0x1032][0][0x08,0x0104].value)
</code></pre>
<p>You have to nest the tags, the (fffe,e000)  accounts for the list so unravel using [0]</p>

---
