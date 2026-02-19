---
topic_id: 12197
title: "How To Change What Images Appear In Input Field Of Modules"
date: 2020-06-24
url: https://discourse.slicer.org/t/12197
---

# How to change what images appear in input field of modules

**Topic ID**: 12197
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/how-to-change-what-images-appear-in-input-field-of-modules/12197

---

## Post #1 by @Tami (2020-06-24 13:51 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: I need to erase all my previously-loaded DICOM files from wherever they are saved, so that I will not see them under the  “Input Image (or Volume)” field of the Filtering modules. I want to have control of what shows up in that list. What is its source? How do I make it show only the DICOMs that are currently loaded?<br>
Actual behavior: Even though I removed all the files in the DICOM browser (so it now looks empty) I still see all my previously-loaded dicom-files in the “Input Image/Volume” field of the Filtering modules. The problem is that many of them have duplicate names so I can’t know which to choose.<br>
I need to be able to refresh that list somehow, or control its content.<br>
I couldn’t find a clue how to do it…</p>

---

## Post #2 by @fedorov (2020-06-24 13:52 UTC)

<p>DICOM Browser shows DICOM instances that are in your DICOM database. If you empty DICOM browser, you empty your database.</p>
<p>Node selectors show nodes that are currently loaded in the scene. Emptying DICOM database does not clear the scene.</p>
<p>What you probably want to do is “File &gt; Close scene”, and then reload items one by one as needed.</p>

---

## Post #3 by @Tami (2020-06-24 14:34 UTC)

<p>Thank you very much for your quick and helpful answer!<br>
<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:"><br>
Tami</p>

---

## Post #4 by @lassoan (2020-06-24 15:22 UTC)

<p>I would strongly recommend to switch to a recent Slicer Preview Release, as DICOM support has been greatly improved. It is shown clearly what is in the DICOM database and what is loaded into scene. You can also easily load a selected patient, study, or series, by double-clicking on it in the DICOM database.</p>

---
