---
topic_id: 11695
title: "Trouble With Data From Philips Qlab"
date: 2020-05-25
url: https://discourse.slicer.org/t/11695
---

# Trouble with data from Philips Qlab

**Topic ID**: 11695
**Date**: 2020-05-25
**URL**: https://discourse.slicer.org/t/trouble-with-data-from-philips-qlab/11695

---

## Post #1 by @MarekJedrzejek (2020-05-25 14:41 UTC)

<p>Hello,</p>
<p>I’m working on Mac. I have slicer 4.10.2. I’ve installed SlicerHeart, Sequences module. I’ve changed directory to be without any special characters. And I want to use <strong>Philips4dUsDicomPatcher</strong> I choose directory and when I click on patch and only what see: Unexpected error: No module named pydicom.</p>
<p>Thank you for any support with this trouble.</p>
<p>Mark</p>

---

## Post #2 by @lassoan (2020-05-25 14:42 UTC)

<p>Thanks for reporting this. Python package dicom was renamed to pydicom and probably we have not made all updates accordingly in Slicer-4.10. I’ll fix these but in the meantime you can use a recent Slicer-4.11 release instead.</p>

---

## Post #3 by @MarekJedrzejek (2020-05-25 14:43 UTC)

<p>Thank you. I will try it!</p>

---
