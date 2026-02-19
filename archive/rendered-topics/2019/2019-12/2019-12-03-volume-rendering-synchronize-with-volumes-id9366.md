---
topic_id: 9366
title: "Volume Rendering Synchronize With Volumes"
date: 2019-12-03
url: https://discourse.slicer.org/t/9366
---

# Volume rendering synchronize with volumes

**Topic ID**: 9366
**Date**: 2019-12-03
**URL**: https://discourse.slicer.org/t/volume-rendering-synchronize-with-volumes/9366

---

## Post #1 by @fbordignon (2019-12-03 13:35 UTC)

<p>Problem report for Slicer 4.11.0-2019-11-21 win-amd64.<br>
Hi, I would like to report a behavior that, if it is not a bug, it is really unhelpful and confusing.<br>
When I check the synchronize with volumes module at the advanced tab of the volumes rendering module, if the checkbox is not grayed, the synchronization does not work. i.e.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f662e38fcc407c7f94ba313871ff7eb51727a6f.png" alt="slicervolumerendering" data-base62-sha1="mK6PZIg9BlKzO0OQdlHP69n8MzB" width="405" height="365"></p>
<p>With this state, the box is with a white background, the synchronization does not work. If I uncheck and check again the checkbox (or click the label), the box is then grayed and the sync works.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c57c57fd4dd123d9691a7ae7e99c7471f91e4c60.png" alt="slicervolumerendering_gray" data-base62-sha1="sb2sWyu8ewEXTKaCCuyKWtDxagg" width="406" height="333"></p>
<p>I’ve clicked the label of the checkbox a number of times and seeing the checkbox checked, I figured it was supposed to sync with the volumes module, went over the volumes module and it was not.<br>
Can we send a signal to uncheck the checkbox if the label is clicked while the checkbox is checked?<br>
I believe this will end this confusion once and for all. I see the utility in clicking the label and making it sync once with the volumes module and keep it unsynched.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2019-12-03 14:29 UTC)

<p>Thanks a lot for the feedback. I agree that the behavior is confusing. We have added automatic pushing of the button a few places but we will implement this behavior in the widget itself so that it is applied everywhere. Added an issue in the bugtracker to track this: <a href="https://issues.slicer.org/view.php?id=4717">https://issues.slicer.org/view.php?id=4717</a></p>

---
