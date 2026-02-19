---
topic_id: 25677
title: "How To Measure The Mandibular Condyle Morphological Changes"
date: 2022-10-13
url: https://discourse.slicer.org/t/25677
---

# How to measure the mandibular condyle morphological changes between two time different points CT?

**Topic ID**: 25677
**Date**: 2022-10-13
**URL**: https://discourse.slicer.org/t/how-to-measure-the-mandibular-condyle-morphological-changes-between-two-time-different-points-ct/25677

---

## Post #1 by @wael_telha (2022-10-13 11:44 UTC)

<p>Hi 3D Slicer users,<br>
I am currently conducting a research to measure the mandibular condyle morphological changes between two time-different points CT:<br>
I tried to use SPHARM-PDM to achieve this goal but it is not working as immediately “terminated with error” message appeared!<br>
So, is there any other module in the program that can be used to measure this?<br>
If any one used SPHARM before please to share his/her experience</p>

---

## Post #2 by @SAO (2022-11-01 06:05 UTC)

<p>Hi <a class="mention" href="/u/wael_telha">@wael_telha</a></p>
<p>Listed below direct link to the SlicerSALT tutorial (modules 1 to 4):<br>
          <iframe class="vimeo-onebox" src="https://player.vimeo.com/video/412300712?h=b9de710cae&amp;app_id=122963" data-original-href="https://vimeo.com/412300712" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
<br>
          <iframe class="vimeo-onebox" src="https://player.vimeo.com/video/412356243?h=2a56b19bde&amp;app_id=122963" data-original-href="https://vimeo.com/412356243" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
<br>
          <iframe class="vimeo-onebox" src="https://player.vimeo.com/video/412373481?h=e19a2ccf66&amp;app_id=122963" data-original-href="https://vimeo.com/412373481" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
<br>
          <iframe class="vimeo-onebox" src="https://player.vimeo.com/video/412382491?h=047b0deaf5&amp;app_id=122963" data-original-href="https://vimeo.com/412382491" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>
<p>These were helpful when dealing with SHARPM-PDM pipelines, and SlicetSALT in general.</p>
<p>All the best.<br>
Sultan</p>

---

## Post #3 by @wael_telha (2022-11-14 13:15 UTC)

<p>thanks a million . i appreciate your help and support</p>

---

## Post #4 by @SAO (2022-11-14 14:53 UTC)

<p>You are welcome <a class="mention" href="/u/wael_telha">@wael_telha</a></p>

---

## Post #5 by @wael_telha (2022-11-23 11:36 UTC)

<p>Dear Sultan ,<br>
hi<br>
Once again I need your help regarding the method to quantification of  the changes using a color map<br>
I am using Slicer 4.11</p>

---

## Post #7 by @SAO (2023-01-18 07:51 UTC)

<p>Dear <a class="mention" href="/u/wael_telha">@wael_telha</a> ,<br>
Sorry for the late response - for some reason I did not get any notification regarding your message.</p>
<p><em>Normally - we do the following:</em></p>
<ol>
<li>Establish correspondence-between the models (of all groups), then</li>
<li>Generate a mean for each group (using principal-component analysis module), then</li>
<li>Compare the means of each group (with the same color map) - through the model-to-model distance module.</li>
</ol>
<p>I am always happy to share my knowledge regarding this.<br>
<strong>Please specify the issue you are facing, and the aim.</strong></p>
<p>Try to use the latest release of <a href="https://discourse.slicer.org/t/slicersalt-4-0-1-summary-highlights-and-changelog/26197">SlicerSALT 4.0.1</a></p>
<p>Regards,<br>
Sultan</p>

---

## Post #8 by @anasmh101 (2025-07-12 13:58 UTC)

<p>Hello, I have a question I couldn’t find an answer for in the videos:<br>
When performing PCA, which SPHARM-PDM output VTK files should be used to generate the CSV file — the <code>_pp_surf_SPHARM.vtk</code> files or the <code>_pp_surf_SPHARM_ellalign.vtk</code> files?</p>

---
