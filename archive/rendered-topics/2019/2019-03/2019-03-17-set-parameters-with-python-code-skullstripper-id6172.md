---
topic_id: 6172
title: "Set Parameters With Python Code Skullstripper"
date: 2019-03-17
url: https://discourse.slicer.org/t/6172
---

# Set parameters with python code. Skullstripper

**Topic ID**: 6172
**Date**: 2019-03-17
**URL**: https://discourse.slicer.org/t/set-parameters-with-python-code-skullstripper/6172

---

## Post #1 by @skagsoset (2019-03-17 12:04 UTC)

<p>Hey!<br>
Does someone know how to set the parrameters of the skullstripper extension with the use of python code?</p>
<p>skullWidget = slicer.modules.Skullstripper.widgetRepresentation()<br>
— need to set the inputs here first<br>
skullWidget.appry()</p>
<p>I know like Segment editor you can write something like this;<br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
slicer.mrmlScene.AddNode(segmentEditorNode)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setMasterVolumeNode(some_volume)</p>
<p>I cant understand how to reach this for skullstripping.</p>
<p>All help is appreciate <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @lassoan (2019-03-18 05:28 UTC)

<p>This is a CLI module that you can run from Python as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>
<p>Give <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper" rel="nofollow noopener">SwissSkullStripper extension</a> a try, too. It may work better.</p>

---

## Post #3 by @skagsoset (2019-03-18 14:45 UTC)

<p>Thanks for the tip, found a way <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Here is a part of my code:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e8b11a3a84f985b80bd42f378e7650c8ad2e80e.png" data-download-href="/uploads/short-url/fLUttPbnpEnRgxtlKCIcOUGO8CG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e8b11a3a84f985b80bd42f378e7650c8ad2e80e.png" alt="image" data-base62-sha1="fLUttPbnpEnRgxtlKCIcOUGO8CG" width="690" height="238" data-dominant-color="292828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">725×251 14.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-03-18 17:24 UTC)

<p>Thanks for the update and sharing the end result.</p>
<p>Please always include source code as text instead of screenshot, because others will not be able to easily copy-paste this code snippet picture and images also take thousand times more storage space. You can add triple ` character before and after the text to display it as source code.</p>

---
