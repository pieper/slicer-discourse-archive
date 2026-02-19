---
topic_id: 27784
title: "Issue Displaying Color Legend In Other Slice Views"
date: 2023-02-12
url: https://discourse.slicer.org/t/27784
---

# Issue displaying color legend in other slice views

**Topic ID**: 27784
**Date**: 2023-02-12
**URL**: https://discourse.slicer.org/t/issue-displaying-color-legend-in-other-slice-views/27784

---

## Post #1 by @jamesobutler (2023-02-12 23:43 UTC)

<p>I was trying to display a color legend in some custom slice views when I noticed that it was not showing as I expected. Is there a certain set of conditions to make sure the color legend shows in the other non-standard slice views.</p>
<p>I start Slicer 5.2.1 (and latest Slicer Preview 5.3.0-2023-02-10), set layout to Four-Up, close Slicer, restart Slicer then run the below snippet</p>
<pre><code class="lang-python">slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutThreeOverThreeView)

import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()

color_legend_display_node = slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(mrHead)
color_legend_display_node.SetVisibility(True)
</code></pre>
<p>I observe the following where the color legend is showing in the Red/Yellow/Green slice views, but not in the Red+/Yellow+/Green+ slice views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee8a147b6bdb4a521e2627a7fde71e4d657d0426.jpeg" data-download-href="/uploads/short-url/y2dtkhXktaaNeE9wTFXFmECSntk.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8a147b6bdb4a521e2627a7fde71e4d657d0426_2_690x370.jpeg" alt="image" data-base62-sha1="y2dtkhXktaaNeE9wTFXFmECSntk" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8a147b6bdb4a521e2627a7fde71e4d657d0426_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8a147b6bdb4a521e2627a7fde71e4d657d0426_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee8a147b6bdb4a521e2627a7fde71e4d657d0426_2_1380x740.jpeg 2x" data-dominant-color="868685"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then if I close Slicer so that it remembers the “Three over three” layout, relaunch Slicer and run the same script I observe the following where the color legend is showing in all the slice views as I would expect:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb0ece809066c4123b7f924b6b747b8c1cd019a3.jpeg" data-download-href="/uploads/short-url/xxpVzKxhNCSRFUXC4zlOfUYxKXF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb0ece809066c4123b7f924b6b747b8c1cd019a3_2_690x370.jpeg" alt="image" data-base62-sha1="xxpVzKxhNCSRFUXC4zlOfUYxKXF" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb0ece809066c4123b7f924b6b747b8c1cd019a3_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb0ece809066c4123b7f924b6b747b8c1cd019a3_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb0ece809066c4123b7f924b6b747b8c1cd019a3_2_1380x740.jpeg 2x" data-dominant-color="878786"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jamesobutler (2023-02-12 23:45 UTC)

<p><a class="mention" href="/u/mik">@Mik</a>, since you did some of the recent color legend rework, do you know what is going on here?</p>

---

## Post #3 by @Mik (2023-02-13 12:25 UTC)

<p>Definitely a bug. SliceCompositeNode is invalid for a new slice views in color legend displayable manager.</p>
<p>For a fast fix:</p>
<ol>
<li>Enable <code>Toggle slice visibility in 3D view</code> in slice controller widget<br>
or</li>
<li>Python script below</li>
</ol>
<pre><code class="lang-python">layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutThreeOverThreeView)
import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()

for sliceViewName in layoutManager.sliceViewNames():
  view = layoutManager.sliceWidget(sliceViewName).sliceView()
  sliceNode = view.mrmlSliceNode()
  sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)
  sliceLogic.StartSliceNodeInteraction(slicer.vtkMRMLSliceNode.SliceVisibleFlag)
  sliceNode.SetSliceVisible(True)
  sliceLogic.EndSliceNodeInteraction()

color_legend_display_node = slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(mrHead)
color_legend_display_node.SetVisibility(True)

</code></pre>
<p>After that the color legends are visible and available for editing.<br>
I hope it helps.</p>

---

## Post #4 by @jamesobutler (2023-02-13 13:55 UTC)

<p>I assume then that this commit is likely the culprit for requiring slice visibility to be on?</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6550/commits/c0343f171968766c0bbfec0fe854d8efcb866709">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6550/commits/c0343f171968766c0bbfec0fe854d8efcb866709" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
    <div class="github-icon-container" title="Commit">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.5 7.75a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zm1.43.75a4.002 4.002 0 01-7.86 0H.75a.75.75 0 110-1.5h3.32a4.001 4.001 0 017.86 0h3.32a.75.75 0 110 1.5h-3.32z"></path></svg>
    </div>




  <div class="github-info-container">
      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6550/commits/c0343f171968766c0bbfec0fe854d8efcb866709" target="_blank" rel="noopener nofollow ugc">BUG: Show color legend for volumes in 3D
</a>
      </h4>

      <span>
        Commit by
        <a href="" rel="noopener">
          <img alt="" src="" class="onebox-avatar-inline" width="20" height="20">
          
        </a>
        in
        <a href="https://github.com/Slicer/Slicer/pull/6550/commits/c0343f171968766c0bbfec0fe854d8efcb866709" target="_blank" rel="noopener nofollow ugc">ENH: Color legend is to be shown for slice view, visible in the 3D view</a>
      </span>




    <div class="branches">
      <code>Slicer:main</code> ← <code>MichaelColonel:volume-cb-3d</code>
    </div>

  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Color legend is shown if color legend display is enabled for the volume, the vol<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6550" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ume is shown in a slice view, and that slice view is visible in the 3D view.

Co-authored-by: Andras Lasso &lt;lasso@queensu.ca&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Mik (2023-02-13 14:21 UTC)

<p>Quite possible. I haven’t tested color legends with nonstandard slice views.</p>

---

## Post #6 by @jamesobutler (2023-02-13 17:11 UTC)

<p>Issue now being tracked at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6827">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6827" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6827" target="_blank" rel="noopener nofollow ugc">Color legend display not working as expected in all slice views</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-02-13" data-time="17:11:16" data-timezone="UTC">05:11PM - 13 Feb 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

As originally mentioned at https://discourse.slicer.org/t/issue-di<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">splaying-color-legend-in-other-slice-views/27784, the color legend display is not working as expected in some of the other slice views other than Red/Yellow/Green. 

## Steps to reproduce

```python
# Start Slicer so that on startup it is the Four-Up Layout
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutThreeOverThreeView)

import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()

color_legend_display_node = slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(mrHead)
color_legend_display_node.SetVisibility(True)
```
If you start Slicer where it begins in the the Three-over-three layout, then the color legend display shows as expected. Something about the views on startup has some impact here.

## Expected behavior

The color legend display should turn on/off for the specified volume in all slice views that the volume is displayed in. It should not be tied to Slice visibility in 3D either.

## Current workaround
```python
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutThreeOverThreeView)

import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()

# Workaround - set slice view visibles before turning on color legend display
layoutManager = slicer.app.layoutManager()
for sliceViewName in layoutManager.sliceViewNames():
  view = layoutManager.sliceWidget(sliceViewName).sliceView()
  sliceNode = view.mrmlSliceNode()
  sliceNode.SetSliceVisible(True)

color_legend_display_node = slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(mrHead)
color_legend_display_node.SetVisibility(True)
```

## Environment
- Slicer version: Slicer-5.3.0-2022-02-10 and Slicer 5.2.1.
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2023-02-13 17:49 UTC)

<p><a class="mention" href="/u/mik">@Mik</a> It would be great if you could try to fix this. I’ve added a comment to the issue about potential approaches.</p>

---

## Post #8 by @Mik (2023-02-24 15:46 UTC)

<p>Fix is ready to review and tests.</p>

---

## Post #9 by @Mik (2023-04-11 16:22 UTC)

<p>Is it possible to update displayable manager data using data from other displayable manager? When we create a non standard slice view and displayable manager for that view we must somehow to get color legend actors from already displayed views (for example from <code>Red</code> slice). Since a newly created slice views don’t have such data.</p>

---

## Post #10 by @lassoan (2023-04-11 19:01 UTC)

<aside class="quote no-group" data-username="Mik" data-post="9" data-topic="27784">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>Is it possible to update displayable manager data using data from other displayable manager?</p>
</blockquote>
</aside>
<p>In general, no. Displayable managers should be kept independent to keep the overall complexity of the application manageable.</p>
<aside class="quote no-group" data-username="Mik" data-post="9" data-topic="27784">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>When we create a non standard slice view</p>
</blockquote>
</aside>
<p>What do you mean by “non-standard”?</p>
<aside class="quote no-group" data-username="Mik" data-post="9" data-topic="27784">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>displayable manager for that view we must somehow to get color legend actors from already displayed views (for example from <code>Red</code> slice)</p>
</blockquote>
</aside>
<p>Why would you need to get the color legend actors?<br>
And why would you need to get any information from other displayable managers instead of getting information directly from the MRML scene content? If there is some logic that you don’t want to repeat in multiple displayable managers then that logic can be moved to somewhere the displayable managers can all access it (in MRML display node, MRML logic classes, etc.).</p>

---

## Post #11 by @Mik (2023-04-12 14:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="27784">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you mean by “non-standard”?</p>
</blockquote>
</aside>
<p>Non-standard (initial) slice views are any slice views created after already displayed color legend.</p>
<p>For example in script</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)

import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()

clDisplayNode = slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(mrHead)
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutThreeOverThreeView)
</code></pre>
<p>Standard slice views are: <code>Red</code>, <code>Green</code>, <code>Yellow</code><br>
Non standard slice views are: <code>Red+</code>, <code>Green+</code>, <code>Yellow+</code>,</p>
<p>When we try to display a volume for a non standard slice views the color legend is invisible, because color legend display node and actors were created before these non standard slice views.</p>
<pre data-code-wrap="python"><code class="lang-python">for color in ["Red+", "Yellow+"]:
    slicer.app.layoutManager().sliceWidget(color).sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(mrHead.GetID())

</code></pre>
<p>The size of the ColorLegendActorsMap is zero for ColorLegendDisplayableManagers in these newly created slice views.</p>
<p>In order to display color legend we must iether recreate ColorLegendDisplayNode or process ColorLegendDisplayNodes from the scene in some logic or in the displayable manager itself.</p>

---
