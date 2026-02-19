---
topic_id: 31149
title: "The New Version 5 2 2 Roi Registration In Surface Registrati"
date: 2023-08-15
url: https://discourse.slicer.org/t/31149
---

# The new version 5.2.2 ROI Registration in Surface registration cannot add online 1 landmark unlike version 4.5.0-1

**Topic ID**: 31149
**Date**: 2023-08-15
**URL**: https://discourse.slicer.org/t/the-new-version-5-2-2-roi-registration-in-surface-registration-cannot-add-online-1-landmark-unlike-version-4-5-0-1/31149

---

## Post #1 by @YOU_DDS (2023-08-15 10:51 UTC)

<p>Greeting all the professors and everyone in this community,</p>
<p>I want to do surface registration of 2 models using ROI Registration in Surface Registration in CMFreg.<br>
I have install the new version 5.2.2 of slicer, but I notice that this version cannot pick more than one landmark.</p>
<p>Is this the program problem or my problem? Is there anything I can do to solve this problem?</p>
<p>I also try to install the version 4.5.0-1 as the video tutorial and I can choose more than 1 landmark which is very convenient but the old version was very slow and do not not many useful option to do with the data.</p>
<p>Please suggest me some Idea of what should I do to be able to use surface registration of 2 model using ROI.</p>
<p>best regard<br>
YOU_DDS</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @YOU_DDS (2023-08-22 02:01 UTC)

<p>I have finally found the answer I was looking for.</p>
<p>For those who might have the same problem, you might need to create point list in markup module. Place the point one by one and go back to ROI Registration and set the size of each ROI you want from each point one by one.</p>
<p>This is what I do and it work for me.<br>
Good Luck!!!</p>

---
