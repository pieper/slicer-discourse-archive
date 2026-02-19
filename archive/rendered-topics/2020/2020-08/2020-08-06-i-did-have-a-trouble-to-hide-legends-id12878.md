---
topic_id: 12878
title: "I Did Have A Trouble To Hide Legends"
date: 2020-08-06
url: https://discourse.slicer.org/t/12878
---

# I did have a trouble to hide legends

**Topic ID**: 12878
**Date**: 2020-08-06
**URL**: https://discourse.slicer.org/t/i-did-have-a-trouble-to-hide-legends/12878

---

## Post #1 by @aiden.zhu (2020-08-06 19:09 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.0<br>
Expected behavior: Hide legends by LegendVisibilityOff()<br>
Actual behavior: can’t turn legends off via cripts</p>
<p>I used the help file via the site: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a><br>
and get chartplot there:<br>
plotChartNode_ID = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLPlotChartNode”)</p>
<p>but via running python scritps:</p>
<pre><code>   cn = slicer.util.getNodesByClass('vtkMRMLPlotChartNode')
   tt = cn[0]
   tt.LegendVisibilityOff()
</code></pre>
<p>I failed to hide legends.</p>
<p>But while I typed  exactly the same  commands inside the “Python Interactor”, it worked well to hide legends.</p>
<p>Why?  Thanks a lot.</p>

---

## Post #2 by @lassoan (2020-08-06 19:27 UTC)

<p>Probably you have several chart nodes and in the code snippet you only modify the first one, which may not be the one you are interested in. You can get the displayed chart node from the plot widget, and the widget from the layout manager.</p>

---

## Post #3 by @Alex_Vergara (2020-08-06 20:28 UTC)

<p>you can try my code at <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/Dosimetry4D/Dosimetry4D.py#L772" rel="nofollow noopener">https://gitlab.com/opendose/opendose3d/-/blob/develop/Dosimetry4D/Dosimetry4D.py#L772</a></p>

---

## Post #4 by @aiden.zhu (2020-08-06 20:43 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks a lot. Basically I understand what you mentioned.<br>
But after I did set up the visibility to be false by<br>
plotChartNode_ID.SetLegendVisibility(False) and then I checked if it was false as printed out as follows ==&gt; LegendVisibility: false. So that means, in the python scripts there, somehow, sometime the legend was set to be “false” not-shown there. But later somehow something brought it back to be “true” shown there.</p>
<p>While the legend was still shown there until I did manual commands from the “python interactor” to do again, since, checking from “python interactor”, I saw the “legendVisibility: True” there before I did manual commands.</p>
<p>printed inside scripts after I did set it to be “False”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc86d21d491b2cc3962ddb87bd006ea16fdae4d5.png" data-download-href="/uploads/short-url/tbkfSvHwhXxFYMhDkOZjUJWRIKF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc86d21d491b2cc3962ddb87bd006ea16fdae4d5.png" alt="image" data-base62-sha1="tbkfSvHwhXxFYMhDkOZjUJWRIKF" width="528" height="500" data-dominant-color="F6FAF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">858×811 18.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>in “python interactor”, before I manually changed to be “False”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886935ed357b6d3fb0b939e16e8cbe50f188fab9.png" data-download-href="/uploads/short-url/jsKlCDs6bXG5iOBxcFTOzjHUzod.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/886935ed357b6d3fb0b939e16e8cbe50f188fab9.png" alt="image" data-base62-sha1="jsKlCDs6bXG5iOBxcFTOzjHUzod" width="538" height="500" data-dominant-color="F6FAF5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">852×791 17.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So please help check if there is kind of glitch there for the legend-visibility. Thanks a lot.</p>

---

## Post #5 by @aiden.zhu (2020-08-06 20:50 UTC)

<p>thanks a lot, <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a><br>
I am trying to test your way. LOL.</p>

---

## Post #6 by @aiden.zhu (2020-08-06 22:26 UTC)

<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a><br>
I did try  applying your way. I have to say it’s kind of the same case I described. That means, while I clicked the checkbox on or off to show  or hide legends, it worked just perfectly fine. But that’s not what I need. Since I would have hundreds times of screen-shot of the plots, one time/one plot for one sample, I need try to hide legends in the plot while I capture the plot.   I am pretty sure of that there is some glitch inside something/somewhere.</p>
<p>I will try something else to see if I may skip this issue.</p>

---

## Post #7 by @aiden.zhu (2020-08-06 23:35 UTC)

<p>I think there were some extra touching parameters of legends there to get it from False to True.<br>
So right after set it as False, it’s just good there to hide legends!</p>

---
