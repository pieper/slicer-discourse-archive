---
topic_id: 1082
title: "Create New Segment In Python Script"
date: 2017-09-18
url: https://discourse.slicer.org/t/1082
---

# Create new segment in Python script

**Topic ID**: 1082
**Date**: 2017-09-18
**URL**: https://discourse.slicer.org/t/create-new-segment-in-python-script/1082

---

## Post #1 by @mschumaker (2017-09-18 17:47 UTC)

<p>I’m attempting to create and configure a segment within a new segmentation node via Python script. Here is what I’m attempting:</p>
<pre><code>    segNode = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(segNode)
    segNode.CreateDefaultDisplayNodes()
    segNode.SetReferenceImageGeometryParameterFromVolumeNode(self.SSFPVolumeNode)
    theSegmentation = segNode.GetSegmentation()
    theSegmentation.AddEmptySegment("test")
</code></pre>
<p>The result is an error that theSegmentation does not have a method AddEmptySegment. When I check the class type, theSegmentation is a vtkObject, rather than a vtkSegmentation. Is there a reason for this? Do I need to downcast to vtkSegmentation, or is there something I’m doing incorrectly?<br>
Thanks very much.</p>

---

## Post #2 by @cpinter (2017-09-18 18:15 UTC)

<p>You need to import vtkSegmentationCorePython, we usually do it like this:<br>
import vtkSegmentationCorePython as vtkSegmentationCore</p>
<p>It would be great if it was imported by default, similarly to all the other libraries, like vtkAddon etc.<br>
<a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> I have tried to make that happen, but it turned out to be more complicated than I thought. I’ll submit a PR shortly, I hope you can tell me what’s missing. Thanks!</p>

---

## Post #3 by @mschumaker (2017-09-18 18:55 UTC)

<p>Great, thanks! That seems to work well so far.</p>

---

## Post #4 by @cpinter (2017-09-18 18:57 UTC)

<p>This is the PR I made to make it easier for everybody to use segmentations from python<br>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/792" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/792" target="_blank">need new color nodes added to default list</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:04" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:32:04" data-timezone="UTC">10:32PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #5 by @lassoan (2017-09-18 19:23 UTC)

<p>I’ve tried to implement this before, similarly to Csaba, and failed, too.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, I think you implemented this for other libraries - what’s the trick that we missed?</p>

---

## Post #6 by @lassoan (2021-08-31 13:36 UTC)

<p>A post was split to a new topic: <a href="/t/prevent-a-segment-from-changing-when-editing-other-segments/19433">Prevent a segment from changing when editing other segments</a></p>

---
