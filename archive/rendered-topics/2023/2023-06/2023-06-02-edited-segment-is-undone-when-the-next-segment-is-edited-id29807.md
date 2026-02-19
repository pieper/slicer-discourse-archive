---
topic_id: 29807
title: "Edited Segment Is Undone When The Next Segment Is Edited"
date: 2023-06-02
url: https://discourse.slicer.org/t/29807
---

# Edited segment is undone when the next segment is edited

**Topic ID**: 29807
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/edited-segment-is-undone-when-the-next-segment-is-edited/29807

---

## Post #1 by @ga1424 (2023-06-02 18:45 UTC)

<p>Operating system  windows 11<br>
Slicer version: 5.2.2<br>
Expected behavior:  Want to protect and preserve all segmentation edits<br>
Actual behavior:  Editing a subsequent or new segment and using an operation like fill value or a logical operation works fine for the segment being edited but the greyscale information from the previously edited segment. reappears.  My previous work is undone What is causing this?</p>

---

## Post #2 by @lassoan (2023-06-02 23:27 UTC)

<p>I’m not sure what grayscale information you are referring to. Could you clarify, maybe attach a few illustrative screenshots?</p>

---

## Post #3 by @ga1424 (2023-06-04 01:44 UTC)

<p>Hello, Andrus.</p>
<p>The volume is one which we want to segment into Air (-1000 Hu), water (0 Hu) and bone. The bone is to remain unedited.</p>
<p>I began by transforming the background and internal voids to -1000 Hu. (Air)</p>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=1ad062974e&amp;attid=0.1&amp;permmsgid=msg-a:r-4953343549178719465&amp;th=18883fd99c7fd382&amp;view=fimg&amp;fur=ip&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ-zRYsF4unbIYvteIumXrOdH5kqnv6nPo9FZvnUeGFBybPHgC9BKD2OfTIzk5vpuze6DQqxoVcDgJo78Rmz6M0HaAqdCGqV4yxA7xv2PQ9VQ7mEdNvmEWfeKt0&amp;disp=emb&amp;realattid=ii_ligpgvb90" alt="Screenshot_8.png" width="562" height="261"></p>
<p>I then turned off the segment layer and moved on to transforming the non-bone elements of the head to 0 Hu (water).</p>
<p>I bracket this process to come as close to the bone as possible and to preserve delicate, thin bones in the sinus and temporal regions.</p>
<p>The first mask is bracketed at -500 to 50 Hu.</p>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=1ad062974e&amp;attid=0.2&amp;permmsgid=msg-a:r-4953343549178719465&amp;th=18883fd99c7fd382&amp;view=fimg&amp;fur=ip&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ9oOFP0fH8U3tVN-jEleh-zqV5Wn_5K33YHg0GuaJYkb1HoUYN_Dt5kgEseEZSlWujI967gKHofL-Jfp4sDf1L8BqIjuyxy4I9WYdry9n2FGDTqm_YfSrfZqNY&amp;disp=emb&amp;realattid=ii_ligpqo7m1" alt="Crysttal Test 6-1-23 Image 3.png" width="562" height="261"></p>
<p>I next used “mask volume” to apply a “fill value” of 0 Hu inside the mask.</p>
<p>The “fill value” worked. But…</p>
<p><img src="https://mail.google.com/mail/u/0?ui=2&amp;ik=1ad062974e&amp;attid=0.4&amp;permmsgid=msg-a:r-4953343549178719465&amp;th=18883fd99c7fd382&amp;view=fimg&amp;fur=ip&amp;sz=s0-l75-ft&amp;attbid=ANGjdJ8XemYKrHqMQGtbrCtQxQvmD_D3a6prqnXKnB8cl9fIBLaXhGZrfIjRxxqyhXJjho4tMOtePkmaimSttSnA1PTXuSSJWQOMdv21umkPRKcC8nFp29TBzQ_80gU&amp;disp=emb&amp;realattid=ii_ligq3w373" alt="Crysttal Test 6-1-23 Image 5.png" width="562" height="261"></p>
<p>…the material I transformed in the previous segmentation has returned. Dang!</p>
<p>Hoping to fix the problem I went back to the first step to transform the background and voids again to -1000 Hu. And…</p>
<p>… it worked but the transformation I did inside the head in the second segmentation was undone.</p>
<p>I seem to be stuck in a loop. I would like to preserve my work in the segments segments as I go and then output the resulting edited volume in an imagestack for further editing in another application</p>
<p>Any help is appreciated. I am relatively new to Slicer and have much to learn.</p>
<p>Thanks for taking a look at this.</p>
<p>Mike</p>

---
