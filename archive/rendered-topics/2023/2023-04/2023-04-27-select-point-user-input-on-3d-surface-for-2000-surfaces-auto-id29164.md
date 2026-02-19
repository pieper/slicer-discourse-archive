---
topic_id: 29164
title: "Select Point User Input On 3D Surface For 2000 Surfaces Auto"
date: 2023-04-27
url: https://discourse.slicer.org/t/29164
---

# Select point (user input) on 3D surface for 2000 surfaces automatically opening after user selects a point

**Topic ID**: 29164
**Date**: 2023-04-27
**URL**: https://discourse.slicer.org/t/select-point-user-input-on-3d-surface-for-2000-surfaces-automatically-opening-after-user-selects-a-point/29164

---

## Post #1 by @Saima (2023-04-27 03:45 UTC)

<p>Hi Andras,<br>
Would it be possible to select the point (x,y,z) location in a ply file, for all the ply files opening up one by one and closing once the point is selected.<br>
The point needed to be selected by the user on the model and then the next model file opens up automatically and the user selects a point on that model and will do until points in all the ply files are selected. can this process be automated.</p>
<p>Thank you</p>
<p>regards,<br>
Saima</p>

---

## Post #2 by @RafaelPalomar (2023-05-02 10:52 UTC)

<p>This could be easily done through a scripted module (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/module_overview.html#scripted-modules" class="inline-onebox" rel="noopener nofollow ugc">Module Overview — 3D Slicer documentation</a>). You could have a a user interface featuring (1) a directory selector to point to where your <code>.ply</code> files lie and (2) a “Next” button that will save the recorded data and load the next model in the dataset. In addition, you will probably want to add some other widgets to select the output file for the results, etc.</p>
<p>You can use <a href="https://github.com/RafaelPalomar/BulkLabelStatistics" class="inline-onebox" rel="noopener nofollow ugc">GitHub - RafaelPalomar/BulkLabelStatistics: Module to compute labelmap statistics in bulk</a> as inspiration for batch loading data from a folder.</p>
<p>When it comes to the selection of one point, you could use callbacks to control the workflow for placing one (and only one) point. This topic might be helpful for that: <a href="https://discourse.slicer.org/t/how-to-access-node-in-scene/27197" class="inline-onebox">How to access Node in Scene?</a>. Alternatively, I would suggest to use the Template Markups (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#creating-template-landmarks" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a>) to control the workflow and limit the point acquisition to 1.</p>

---

## Post #3 by @Saima (2023-05-09 01:45 UTC)

<p>Hi,<br>
I would not want a next button but I would want the .ply files to open one by one once the point in the .ply file is selected.<br>
is it possible?</p>
<p>regards,<br>
saima</p>

---

## Post #4 by @RafaelPalomar (2023-05-09 08:39 UTC)

<p>Yes, I think that is possible. You just need to observe the right events from the markups and manage the creation/deletion of new added markups. I believe all the links above are still relevant to make this happen.</p>

---
