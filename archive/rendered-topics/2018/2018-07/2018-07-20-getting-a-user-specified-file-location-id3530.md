---
topic_id: 3530
title: "Getting A User Specified File Location"
date: 2018-07-20
url: https://discourse.slicer.org/t/3530
---

# Getting a user specified file location

**Topic ID**: 3530
**Date**: 2018-07-20
**URL**: https://discourse.slicer.org/t/getting-a-user-specified-file-location/3530

---

## Post #1 by @Troy (2018-07-20 04:03 UTC)

<p>So I’m writing a program that uploads and reads a file format from the Seimans format (not DICOM), and I need to write a way to have the user find the file location, and then save that location as a string. Pretty much the equivalent of the general “upload” button. However, everywhere I look, the only way I can find to do this (and how I’ve done it in the past) is using TKinter’s filedialogue command, and tkinter isn’t available in the slicer libraries.</p>
<p>Is there any way to do this using slicer’s libraries?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2018-07-20 05:06 UTC)

<p>There are many widgets that you can use to ask file path from the user. I prefer <code>ctk.ctkPathLineEdit()</code>, as it allows you to copy-paste, select using a dialog (if you click … button), and can also save most recent selections. There are also several Qt widgets that can be used.</p>

---
