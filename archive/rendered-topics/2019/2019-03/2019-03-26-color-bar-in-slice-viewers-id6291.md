# Color bar in slice viewers

**Topic ID**: 6291
**Date**: 2019-03-26
**URL**: https://discourse.slicer.org/t/color-bar-in-slice-viewers/6291

---

## Post #1 by @fedorov (2019-03-26 14:40 UTC)

<p>I wanted to visualize color bar in slice views today, and I was reminded how difficult it is to find this functionality. I think the only reason I was able to find it is because I knew it was possible to do that, I know who contributed that functionality, so I was able to search my email and find this PR: <a href="https://github.com/Slicer/Slicer/pull/235" class="inline-onebox">Issues with window level and threshold on the volume module, display panel · Issue #235 · Slicer/Slicer · GitHub</a>, and then I saw and remembered that this functionality is hidden in the “Data Probe” module (not to be confused with the “DataProbe” area of the interface!).</p>
<p>In case someone else needs to do this (or does not know this is possible), here’s how to enable scalar bar:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adfde48a015432390b38e05175b979acc6a15f9e.png" data-download-href="/uploads/short-url/oPcz24lNBaPc5fS0gqBQK5F3mNg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adfde48a015432390b38e05175b979acc6a15f9e_2_443x500.png" alt="image" data-base62-sha1="oPcz24lNBaPc5fS0gqBQK5F3mNg" width="443" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adfde48a015432390b38e05175b979acc6a15f9e_2_443x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adfde48a015432390b38e05175b979acc6a15f9e_2_664x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adfde48a015432390b38e05175b979acc6a15f9e.png 2x" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×788 62.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Saima (2021-09-15 06:59 UTC)

<p>Hi,<br>
it do not enable scalar bar in slice view. Am i missing some other settings.</p>
<p>Regards,<br>
Saima safdar</p>

---

## Post #3 by @Saima (2021-09-15 07:10 UTC)

<p>Hi,<br>
This is for the scalarvolume and not for the labelmapnode. I need to convert the labelmap to volume node then it displays the bar but grey scale.</p>
<p>Is it possible to directly get the bar for labelmap. how to change the color code for the scalar volume</p>

---

## Post #4 by @lassoan (2021-09-15 16:58 UTC)

<aside class="quote no-group" data-username="Saima" data-post="3" data-topic="6291">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>I need to convert the labelmap to volume node</p>
</blockquote>
</aside>
<p>You can convert between labelmap ↔ scalar volume nodes in Volumes module / Volume Information section.</p>

---

## Post #5 by @Saima (2022-03-08 21:18 UTC)

<p>How to enable disable color scalar bar in data probe using python script</p>

---

## Post #6 by @Saima (2022-03-08 21:20 UTC)

<p>Thank you I got it</p>
<p>sliceAnnotations = slicer.modules.DataProbeInstance.infoWidget.sliceAnnotations sliceAnnotations.scalarBarEnabled=False<br>
sliceAnnotations.updateSliceViewFromGUI()</p>

---

## Post #7 by @Saima (2022-03-08 22:14 UTC)

<p>Hi,<br>
I am trying to create a check box but running into error</p>
<pre><code>self.setParameterNode(self.logic.getParameterNode())
</code></pre>
<p>File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/Visualisation/Visualisation/Visualisation.py”, line 115, in setParameterNode<br>
self.updateGUIFromParameterNode()<br>
File “/home/saima/Slicer-4.11.0-2020-02-25-linux-amd64/Visualisation/Visualisation/Visualisation.py”, line 147, in updateGUIFromParameterNode<br>
self.scalarBar.checked = (self._parameterNode.GetParameter(“scalarBarLabel”) == “true”)<br>
AttributeError: ‘VisualisationWidget’ object has no attribute ‘scalarBar’</p>
<p>Please help</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #8 by @lassoan (2022-03-08 23:41 UTC)

<p>Color legend has been hugely improved in recent Slicer versions (you can show multiple color legends, for more node types, works automatically for continuous and discrete colormaps, etc.) and it is now also simpler to show/hide it. See example in the script repository: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-color-legend-for-a-volume-node" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>More information on the new color legend:</p><aside class="quote quote-modified" data-post="1" data-topic="21567">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/color-scalar-bar-reworked-and-upgraded-now-it-s-called-color-legend/21567">"Color Scalar Bar" reworked and upgraded, now it’s called "Color Legend"</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Starting from version <a href="https://github.com/Slicer/Slicer/pull/5828/commits/170a0e0edd448fd2c5d8e47ac6de591293fc8354" rel="noopener nofollow ugc">30530 build 2022-01-15</a> “Color Scalar Bar” section from “Colors” module was replaced with “Color Legend” section. 
The “Color Legend” section has been also added to the “Volume”, “Model” and “Markups” modules to control visibility and behavior of color legend. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6755ea30878f4e57abb5e25ea985518b838bea3e.jpeg" data-download-href="/uploads/short-url/eK9fz7FnRdhsnN7COOaH5Wc2NCm.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
New major features: 


More unified API. Each Volume, Model, Markups or any other displayable node now can have an individual color legend by means of <a href="https://apidocs.slicer.org/master/classvtkMRMLColorLegendDisplayNode.html" rel="noopener nofollow ugc">vtkMRMLColorLegendDisplayNode</a>. 


Displayed LUT is in sy…
  </blockquote>
</aside>


---
