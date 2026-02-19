---
topic_id: 31840
title: "How Can I Ignore Popup"
date: 2023-09-22
url: https://discourse.slicer.org/t/31840
---

# How can i ignore popup

**Topic ID**: 31840
**Date**: 2023-09-22
**URL**: https://discourse.slicer.org/t/how-can-i-ignore-popup/31840

---

## Post #1 by @FWSU (2023-09-22 07:55 UTC)

<p>I’m studying an auto-segmentation project on Jupyter.<br>
Is there a way to prevent notification pop-ups or confirmation pop-ups from appearing?<br>
For example, after segmentation, when trying to save a label, a completion and log pop-up appears. Also, when trying to view another file during work, an OK/Cancel confirmation pop-up appears. I want it to proceed as if it’s okay without any pop-ups</p>

---

## Post #2 by @lassoan (2023-09-22 18:33 UTC)

<p>You can avoid these popups if you automate the workflow by using logic classes without using any GUI classes. For example, do not launch a Slicer function by simulating button clicks but call those logic methods that the button click triggers (and skip the display of the confirmation popup).</p>

---

## Post #3 by @FWSU (2023-09-25 00:54 UTC)

<p>Are there any relevant documents or tutorials available?</p>

---

## Post #4 by @lassoan (2023-09-26 12:49 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab Bootcamp Slicer programming tutorial</a> is a good starting point.</p>
<p>You can find Python code snippets for all the commonly needed operations in Slicer in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>. If you cannot find something and Bing Chat / ChatGPT cannot provide useful hints either then you can ask here and we’ll help.</p>

---
