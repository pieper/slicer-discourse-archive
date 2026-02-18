# Expanding volume without squeezing others

**Topic ID**: 9704
**Date**: 2020-01-03
**URL**: https://discourse.slicer.org/t/expanding-volume-without-squeezing-others/9704

---

## Post #1 by @annigilus (2020-01-03 13:30 UTC)

<p>How can I expand one volume without squeezing others volumes nearby? Can I overlap volumes one to another?<br>
And hov can I combine two different volumes to the one new? (For example, I have two volumes of femoral heads named “FH_left” and “FH_right” and I need it one volume “FH_all”)</p>

---

## Post #2 by @lassoan (2020-01-03 13:36 UTC)

<p>You need to resample the volumes to have the same geometry (origin, spacing, axis directions - using “Crop volume” module or one of the image resample modules) then add them (using “Add scalar volume” module or using numpy array operations). See more details in these posts:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/landmark-registration-and-combining-intenstities-of-fixed-and-moving-volume/7106" class="inline-onebox">Landmark registration and combining intenstities of fixed and moving volume</a></li>
<li><a href="https://discourse.slicer.org/t/is-it-possible-to-view-more-than-two-image-volumes-at-the-same-time-in-slice-viewers/8738" class="inline-onebox">Is it possible to view more than two image volumes at the same time in slice viewers?</a></li>
</ul>

---
