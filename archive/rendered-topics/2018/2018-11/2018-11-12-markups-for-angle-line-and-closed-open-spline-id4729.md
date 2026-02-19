---
topic_id: 4729
title: "Markups For Angle Line And Closed Open Spline"
date: 2018-11-12
url: https://discourse.slicer.org/t/4729
---

# Markups for angle, line and closed/open spline

**Topic ID**: 4729
**Date**: 2018-11-12
**URL**: https://discourse.slicer.org/t/markups-for-angle-line-and-closed-open-spline/4729

---

## Post #1 by @Davide_Punzo (2018-11-12 09:31 UTC)

<p>Hi all,</p>
<p>I am starting to work on VTK widgets / Slicer Markups for:</p>
<ol>
<li>Adding middle/right/double clicks vtk events / Slicer Markups signals</li>
<li>Few customization to the VTK widgets (e.g., display a centroid point for closed spline)</li>
<li>Adding Markups MRML nodes and widgets for angle, lines and closed/open spline</li>
</ol>
<p>The general idea is to incorporate the vtkContourWidget, vtkLineWidget2 and vtkAngleWidget in Slicer as Markups.</p>
<p>I have a couple of questions:</p>
<ol>
<li>Is anyone actively working on Markups related projects? If yes, it will be nice to coordinates the devs.</li>
<li>
<a class="mention" href="/u/johan_andruejol">@Johan_Andruejol</a> you have implemented Markups for curve and plane in <a href="https://github.com/Slicer/Slicer/pull/1010" rel="nofollow noopener">Slicer/Slicer#1010</a>. I still have to look at the implementation, but may you notify what is the status of this? Thanks!</li>
</ol>
<p>Cheers,<br>
Davide.</p>

---

## Post #2 by @muratmaga (2019-01-03 20:29 UTC)

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a></p>
<p>As discussed in the long thread <a href="https://discourse.slicer.org/t/a-users-proposal-for-markups-module-enhancements/3362" class="inline-onebox">A user's proposal for Markups Module enhancements</a>, we have some interest in markups module improvement. One of our requested features is the ability to use a template that defines landmark labels and their description and have the user selectively populate this. I think the PW would be good time to coordinate these efforts.</p>
<p>I won’t be attending but <a class="mention" href="/u/smrolfe">@smrolfe</a> is. I am not sure where to provide this, but I am attaching a video which shows the landmarking behavior we would like to emulate in Slicer. Sorry there is no audio.<br>
<a href="https://bit.ly/fiducials" class="onebox" target="_blank" rel="nofollow noopener">https://bit.ly/fiducials</a></p>
<p>Basically user loads a file that contains the fiducials descriptions and by clicking on one of them and then clicking on the 3D renderer, it records its 3D coordinate. Landmarking doesn’t have to go in a sequence, but simply initiated by user clicking on a landmark on the list. Selecting an existing landmark with a coordinate a second time and clicking on 3D viewer updates its the coordinates with the new values.</p>

---

## Post #3 by @lassoan (2019-01-04 02:48 UTC)

<p>We’ve already planned for such features. Currently we are working on lower-level infrastructure. I’ll be at the project week and work with <a class="mention" href="/u/smrolfe">@smrolfe</a> on this.</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> Could you please add a project page <a href="https://na-mic.github.io/ProjectWeek/PW30_2019_GranCanaria/" rel="nofollow noopener">here</a>?</p>

---

## Post #4 by @smrolfe (2019-01-04 19:32 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, I will update soon with the project page.</p>

---

## Post #5 by @lassoan (2019-01-11 17:28 UTC)

<p>I’ve created the project page: <a href="https://github.com/NA-MIC/ProjectWeek/blob/master/PW30_2019_GranCanaria/Projects/MarkupsRedesign/README.md" rel="nofollow noopener">https://github.com/NA-MIC/ProjectWeek/blob/master/PW30_2019_GranCanaria/Projects/MarkupsRedesign/README.md</a></p>

---

## Post #6 by @smrolfe (2019-01-11 20:19 UTC)

<p>Thanks for your help <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
