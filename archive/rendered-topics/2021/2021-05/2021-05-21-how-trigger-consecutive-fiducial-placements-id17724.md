---
topic_id: 17724
title: "How Trigger Consecutive Fiducial Placements"
date: 2021-05-21
url: https://discourse.slicer.org/t/17724
---

# How trigger consecutive fiducial placements?

**Topic ID**: 17724
**Date**: 2021-05-21
**URL**: https://discourse.slicer.org/t/how-trigger-consecutive-fiducial-placements/17724

---

## Post #1 by @Chintha_Siva_Prasad (2021-05-21 16:42 UTC)

<p>How to trigger the fiducial placement just after the placement of other fiducial nodes and so on?<br>
I had listened to addNode method like below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6166a883dd9653df570be7adf634e556b6e9f273.png" data-download-href="/uploads/short-url/dTEg3o1thuoX1gWBv01D2i5gsXF.png?dl=1" title="Screenshot from 2021-05-21 22-09-35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6166a883dd9653df570be7adf634e556b6e9f273_2_690x389.png" alt="Screenshot from 2021-05-21 22-09-35" data-base62-sha1="dTEg3o1thuoX1gWBv01D2i5gsXF" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/6166a883dd9653df570be7adf634e556b6e9f273_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6166a883dd9653df570be7adf634e556b6e9f273.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6166a883dd9653df570be7adf634e556b6e9f273.png 2x" data-dominant-color="F2F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2021-05-21 22-09-35</span><span class="informations">929×525 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But when I call the addNode method in the script it’s getting into an infinite loop(because of the functions calling each other probably). Even after I commented addNode method its looping for every mouse moment.</p>

---

## Post #2 by @lassoan (2021-05-21 16:57 UTC)

<p>You only need to create single markups fiducial node. You can add any number of control points to it. To keep placement mode active, enable “persistent” option.</p>
<p>I would recommend to put a <a href="http://apidocs.slicer.org/master/classqSlicerMarkupsPlaceWidget.html">qSlicerMarkupsPlaceWidget</a> widget on your module GUI to activate/deactivate point placement. It ensures that the correct markups fiducial node is selected, enables/disables placement and persistent option. You can specify persistence by adjusting <a href="http://apidocs.slicer.org/master/classqSlicerMarkupsPlaceWidget.html#ab0c8d33893da590b348b9423f13b7bf5">placeMultipleMarkups</a> property.</p>

---
