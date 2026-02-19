---
topic_id: 14689
title: "Landmark Detection Registration Difficulties"
date: 2020-11-19
url: https://discourse.slicer.org/t/14689
---

# Landmark Detection/Registration difficulties

**Topic ID**: 14689
**Date**: 2020-11-19
**URL**: https://discourse.slicer.org/t/landmark-detection-registration-difficulties/14689

---

## Post #1 by @Cesar_Puga (2020-11-19 14:32 UTC)

<p>Dear Slicer Community,</p>
<p>During the last months i have been trying to solve a problem that i cant find a solution to, therefore i would like to kindly ask your support with ideas on how to approach it,</p>
<p>I’m trying to detect specific landmarks in “newly loaded” CT scans that will be used for needle insertion purposes,  my approach to this problem is to</p>
<ol>
<li>create a set of “atlases” which are composed by 10 different CT scans (not optimal quality)</li>
<li>create a set of landmarks (entry and target points for different organs) for every scan in this set</li>
<li>compare the “newly loaded” scan by cropping it to a region of interest and comparing it to my “atlas” set, then based on a set of features (that will allow me to know how similar a pair of CT images are)<br>
4.select which of my “atlases” is the best candidate to be registered (deformable Bspline registration) to the “newly loaded” CT scan, once i have this candidate, i perform a Bspline deformable registration to deform my “atlas” to the “newly loaded” CT scan and apply this transform to the landmark points (fiducials that were created for the “atlas”)</li>
<li>the fiducials should now be in a position appropriate to perform the needle insertion for the “newly loaded” CT scan</li>
</ol>
<p>i do this step of selecting the best candidate to avoid running into long computation times of performing multiple Bspline deformable registrations for each “atlas” candidate, i also tried segment registration of rib cages, but i have found it difficult so far to register ribcage segments using the segment registration due to the poor quality of my ct scans (thresholding seems to segment more than bones because the voxel intensity seems not to be optimal for the different structures as it is with some sample data i tried it with)</p>
<p>i would like to know if you think there is a more practical approach to the goal i want to achieve or if you know about a specific technique i am overlooking, etc, i would also like to point out that since this project is in the development phase great precision rates is not of critical importance, i would say above 80% would be totally fine<br>
all your tips/comments are greatly appreciated,thanks</p>

---
