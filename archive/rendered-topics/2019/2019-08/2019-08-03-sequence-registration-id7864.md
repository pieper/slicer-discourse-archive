---
topic_id: 7864
title: "Sequence Registration"
date: 2019-08-03
url: https://discourse.slicer.org/t/7864
---

# Sequence registration

**Topic ID**: 7864
**Date**: 2019-08-03
**URL**: https://discourse.slicer.org/t/sequence-registration/7864

---

## Post #1 by @sarvpriya1985 (2019-08-03 14:44 UTC)

<p>Hi,</p>
<p>Is there any change in sequence registration? Earlier, to register a 4d cardiac sequence it used to take me a minute or so (after doing cropping, isotropic spacing 1.7x), but now even after 20 minutes, it is still not completed. I amusing 4.11 version.<br>
Pls advise if something is wrong on my end.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2019-08-05 03:39 UTC)

<p>Does the registration end after a while? Does the result look good?<br>
Have you tried with the latest Preview Release?<br>
Could you attach the application log?</p>

---

## Post #3 by @sarvpriya1985 (2019-08-05 03:55 UTC)

<p>Hi Andras,</p>
<p>Sequence didn’t register. It failed after sequence 9th (out of 10th) due to bad allocation memory. So then I had to increase the spacing by 2.0x. However, i had to reduce field of view and include only heart and cut out aorta and then it worked. I guess the issue is related to memory and i am not sure how much is the minimum required for this task.</p>
<p>Thanks again,<br>
Sarv</p>

---

## Post #4 by @lassoan (2019-08-05 04:04 UTC)

<p>Yes, you need to increase memory size by installing more RAM or increasing virtual memory size (it is system setting on Windows and Linux; amount of free disk space on MacOSX), crop image or reduce image resolution, or disable saving of output transforms.</p>

---
