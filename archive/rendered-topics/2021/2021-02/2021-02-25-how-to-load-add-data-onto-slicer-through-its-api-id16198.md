---
topic_id: 16198
title: "How To Load Add Data Onto Slicer Through Its Api"
date: 2021-02-25
url: https://discourse.slicer.org/t/16198
---

# How to load/add data onto Slicer through its API?

**Topic ID**: 16198
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/how-to-load-add-data-onto-slicer-through-its-api/16198

---

## Post #1 by @will_kim (2021-02-25 03:04 UTC)

<p>Hi is there a Slicer API that loads png, jpg, or any other common file format to Slicer. I know you can go to the ‘Add data into the scene’  to do it manually, but I want to try to include this to be automatic on my python script as well.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-02-25 06:14 UTC)

<p>You can use the <code>loadVolume</code> function - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Load_volume_from_file">examples in the script repository</a>.</p>

---

## Post #3 by @will_kim (2021-02-26 21:11 UTC)

<p>Thank you. Also is there a way you can automatically display only the 3D panel?</p>

---

## Post #4 by @lassoan (2021-02-26 22:11 UTC)

<p>Yes, see examples how to switch layout in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> (search for <code>setLayout</code>).</p>

---
