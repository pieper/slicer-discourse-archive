---
topic_id: 12453
title: "Accessing Data Probe Module From Python"
date: 2020-07-09
url: https://discourse.slicer.org/t/12453
---

# Accessing Data Probe Module from Python

**Topic ID**: 12453
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/accessing-data-probe-module-from-python/12453

---

## Post #1 by @FatihSogukpinar (2020-07-09 01:59 UTC)

<p>Hi all,</p>
<p>I am trying to access to what is displayed in the Data Probe Module. In particular, I need to access the anatomical information that is displayed there. For instance, I want to get the anatomical location corresponding to the location of the mouse tip.</p>
<p>What functions do I need to use to access that information ? I looked at the Documentation but I could not find any coding examples. etc.</p>
<p>Thank you !</p>

---

## Post #2 by @lassoan (2020-07-09 02:26 UTC)

<p>DataProbe module has no logic that other modules could use, but fortunately there is a much simpler way of getting anatomical location from the crosshair node. See complete example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view</a></p>

---

## Post #3 by @FatihSogukpinar (2020-07-09 04:06 UTC)

<p>Thanks !</p>
<p>I looked at the example, but I actually want to access to that information without using the mouse at all.<br>
For instance I want to get all the anatomical coordinates and locations corresponding to the points in the Markup Fiducials.</p>
<p>How should I modify the example code for this ?</p>
<p>Thank you…</p>

---

## Post #4 by @lassoan (2020-07-09 13:45 UTC)

<p>Markups fiducial positions are already defined in anatomical coordinates.</p>

---

## Post #5 by @FatihSogukpinar (2020-07-09 19:05 UTC)

<p>Yes but can’t I obtain the anatomical names which are displayed in the Data Probe module ?</p>

---

## Post #6 by @lassoan (2020-07-09 19:09 UTC)

<p>What do you mean by anatomical name? Can you attach a screenshot and mark the information that you would like to obtain?</p>

---

## Post #7 by @FatihSogukpinar (2020-07-09 19:40 UTC)

<p>Basically I need all the information provided by the Data Probe Module.</p>
<p>For the 1st screenshot, I need the indices which are displayed next to the coordinates.</p>
<p>For the 2nd,  I need the names which correspond to the segments (in this example Amygdala).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0d7d4f375374dd481ee2bb873d6fd38f048119f.png" data-download-href="/uploads/short-url/ymB0Eky5vjX0uGYr6PNfO5CZPB5.png?dl=1" title="Screenshot (21)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0d7d4f375374dd481ee2bb873d6fd38f048119f_2_690x388.png" alt="Screenshot (21)" data-base62-sha1="ymB0Eky5vjX0uGYr6PNfO5CZPB5" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0d7d4f375374dd481ee2bb873d6fd38f048119f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0d7d4f375374dd481ee2bb873d6fd38f048119f_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0d7d4f375374dd481ee2bb873d6fd38f048119f_2_1380x776.png 2x" data-dominant-color="908E95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (21)</span><span class="informations">1920×1080 487 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/324e926066058083ebdad33032e44a56a399e53f.png" data-download-href="/uploads/short-url/7b2dbYj5Bop5B4Fobdm5xSd2MrR.png?dl=1" title="Screenshot (23)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/324e926066058083ebdad33032e44a56a399e53f_2_690x388.png" alt="Screenshot (23)" data-base62-sha1="7b2dbYj5Bop5B4Fobdm5xSd2MrR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/324e926066058083ebdad33032e44a56a399e53f_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/324e926066058083ebdad33032e44a56a399e53f_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/324e926066058083ebdad33032e44a56a399e53f_2_1380x776.png 2x" data-dominant-color="8F8F95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (23)</span><span class="informations">1920×1080 538 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2020-07-09 19:55 UTC)

<p><strong>Indices:</strong> see above (example in the script repository), you can also have a look at the implementation in DataProbe:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/b13a49465eec642a3bd9c2d5c50b2afb57088259/Modules/Scripted/DataProbe/DataProbe.py#L233-L248" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b13a49465eec642a3bd9c2d5c50b2afb57088259/Modules/Scripted/DataProbe/DataProbe.py#L233-L248" target="_blank">Slicer/Slicer/blob/b13a49465eec642a3bd9c2d5c50b2afb57088259/Modules/Scripted/DataProbe/DataProbe.py#L233-L248</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="233" style="counter-reset: li-counter 232 ;">
<li>hasVolume = False</li>
<li>layerLogicCalls = (('L', sliceLogic.GetLabelLayer),</li>
<li>                   ('F', sliceLogic.GetForegroundLayer),</li>
<li>                   ('B', sliceLogic.GetBackgroundLayer))</li>
<li>for layer,logicCall in layerLogicCalls:</li>
<li>  layerLogic = logicCall()</li>
<li>  volumeNode = layerLogic.GetVolumeNode()</li>
<li>  ijk = [0, 0, 0]</li>
<li>  if volumeNode:</li>
<li>    hasVolume = True</li>
<li>    xyToIJK = layerLogic.GetXYToIJKTransform()</li>
<li>    ijkFloat = xyToIJK.TransformDoublePoint(xyz)</li>
<li>    ijk = [_roundInt(value) for value in ijkFloat]</li>
<li>  self.layerNames[layer].setText(self.generateLayerName(layerLogic))</li>
<li>  self.layerIJKs[layer].setText(self.generateIJKPixelDescription(ijk, layerLogic))</li>
<li>  self.layerValues[layer].setText(self.generateIJKPixelValueDescription(ijk, layerLogic))</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p><strong>Segment names:</strong> you can get them from the displayable managers, see implementation here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/b13a49465eec642a3bd9c2d5c50b2afb57088259/Modules/Scripted/DataProbe/DataProbe.py#L250-L265" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b13a49465eec642a3bd9c2d5c50b2afb57088259/Modules/Scripted/DataProbe/DataProbe.py#L250-L265" target="_blank">Slicer/Slicer/blob/b13a49465eec642a3bd9c2d5c50b2afb57088259/Modules/Scripted/DataProbe/DataProbe.py#L250-L265</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="250" style="counter-reset: li-counter 249 ;">
<li># collect information from displayable managers</li>
<li>displayableManagerCollection = vtk.vtkCollection()</li>
<li>if sliceNode:</li>
<li>  sliceView = slicer.app.layoutManager().sliceWidget(sliceNode.GetName()).sliceView()</li>
<li>  sliceView.getDisplayableManagers(displayableManagerCollection)</li>
<li>aggregatedDisplayableManagerInfo = ''</li>
<li>for index in range(displayableManagerCollection.GetNumberOfItems()):</li>
<li>  displayableManager = displayableManagerCollection.GetItemAsObject(index)</li>
<li>  infoString = displayableManager.GetDataProbeInfoStringForPosition(xyz)</li>
<li>  if infoString != "":</li>
<li>    aggregatedDisplayableManagerInfo += infoString + "&lt;br&gt;"</li>
<li>if aggregatedDisplayableManagerInfo != '':</li>
<li>  self.displayableManagerInfo.text = '&lt;html&gt;' + aggregatedDisplayableManagerInfo + '&lt;/html&gt;'</li>
<li>  self.displayableManagerInfo.show()</li>
<li>else:</li>
<li>  self.displayableManagerInfo.hide()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
