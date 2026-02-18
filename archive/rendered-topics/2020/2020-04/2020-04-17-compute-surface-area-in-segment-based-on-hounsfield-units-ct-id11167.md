# Compute surface area in segment based on Hounsfield units (CT-images)

**Topic ID**: 11167
**Date**: 2020-04-17
**URL**: https://discourse.slicer.org/t/compute-surface-area-in-segment-based-on-hounsfield-units-ct-images/11167

---

## Post #1 by @Justin (2020-04-17 19:37 UTC)

<p>Dear all,</p>
<p>I hope you guys can help. I’m relatively new to 3D slicer. I am using the 4.11 version.<br>
My goal is to compute skeletal muscle area in a single CT-slice.</p>
<p>I have loaded the CT and have created a segment using the segment editor. I manually outlined all the muscles in a single segment. If I go to the segment analysis, I can convert the segment to a model and I can calculate the surface area of this segment.</p>
<p>However, I am trying to calculate only the surface area of the pixels that have hounsfield units between -29 and +150, not the area of the entire segment. The main reason is to remove fatty tissue inside muscles from the calculation.<br>
Is there a way in 3d Slicer to achieve this?</p>
<p>Thanks a lot in advance,<br>
Best,<br>
Justin</p>

---

## Post #2 by @lassoan (2020-04-17 23:11 UTC)

<p>We developed a module for this with <a class="mention" href="/u/hherhold">@hherhold</a> some time ago, now I’ve touched it up and pushed it into <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/SegmentCrossSectionArea">Sandbox extension</a>. You can download it tomorrow in latest Slicer Preview Release. The Sandbox extension is in Examples category, after you install it, the “Segment Cross-Section Area” module should show up in Quantification category.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c011b587a9832cdf3a0bcc0a4a126e44d0e78e73.png" data-download-href="/uploads/short-url/rp7Cbwoom0Rh5sc7h8cXAzJ4k1l.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c011b587a9832cdf3a0bcc0a4a126e44d0e78e73_2_690x441.png" alt="image" data-base62-sha1="rp7Cbwoom0Rh5sc7h8cXAzJ4k1l" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c011b587a9832cdf3a0bcc0a4a126e44d0e78e73_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c011b587a9832cdf3a0bcc0a4a126e44d0e78e73_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c011b587a9832cdf3a0bcc0a4a126e44d0e78e73_2_1380x882.png 2x" data-dominant-color="BFBDB5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 860 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Justin (2020-04-18 07:16 UTC)

<p>Dear Andras,</p>
<p>Thanks very much for your quick reply and solution!<br>
Once the module is available I’ll try it out.</p>
<p>Best, Justin</p>

---

## Post #4 by @lassoan (2020-04-18 14:07 UTC)

<p>Nightly build was not successful on Windows last night but tomorrow it should be OK. If you want to try it earlier then you can download the repository from github and add the SegmentCrossSectionArea folder to the additional module paths in Slicer application settings.</p>

---

## Post #5 by @Justin (2020-04-18 20:07 UTC)

<p>Thanks very much Andras,<br>
I noticed the windows version wasn’t updated, but I was able to install the module manually with your instruction.</p>
<p>I also found out that I could filter out the relevant HU range using the section editor, so I have all I need.</p>
<p>Thanks again,<br>
Best, Justin</p>

---

## Post #6 by @lassoan (2020-04-21 15:38 UTC)

<p>A post was split to a new topic: <a href="/t/automating-thresholding-of-existing-segments/11229">Automating thresholding of existing segments</a></p>

---

## Post #7 by @Justin (2020-05-01 19:34 UTC)

<p>Can the SegmentCrossSectionArea also be reached through script?<br>
I’ve looked up the script and tried</p>
<p>areaNode = slicer.mrmlScene.AddNewNodeByClass(“SegmentCrossSectionAreaWidget(ScriptedLoadableModuleLogic)”)<br>
tableNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”, “Segment cross-section area table”)<br>
plotChartNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLPlotChartNode”, “Segment cross-section area plot”)<br>
logic = SegmentCrossSectionAreaLogic()<br>
logic.run(segmentationNode, masterVolumeNode, “slice”, tableNode, plotChartNode)<br>
logic.showChart(plotChartNode)</p>
<p>I get the error that SegmentCrossSectionAreaLogic is not defined.<br>
Unfortunately I cannot make much more of the python script to see how SegmentCrossSectionAreaLogic should be defined or how I can add the right node so that it will work.</p>
<p>Do you have a suggestion?</p>

---

## Post #8 by @lassoan (2020-05-01 20:38 UTC)

<p>The module’s automatic test serves as an example of how to use the module from a script:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/PerkLab/SlicerSandbox/blob/90320348677225ae86bb54d0dea563af55c5bcae/SegmentCrossSectionArea/SegmentCrossSectionArea.py#L494-L496" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/90320348677225ae86bb54d0dea563af55c5bcae/SegmentCrossSectionArea/SegmentCrossSectionArea.py#L494-L496" target="_blank">PerkLab/SlicerSandbox/blob/90320348677225ae86bb54d0dea563af55c5bcae/SegmentCrossSectionArea/SegmentCrossSectionArea.py#L494-L496</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="494" style="counter-reset: li-counter 493 ;">
<li>logic = SegmentCrossSectionAreaLogic()
</li>
<li>logic.run(segmentationNode, masterVolumeNode, "slice", tableNode, plotChartNode)
</li>
<li>logic.showChart(plotChartNode)
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you run the code from a different file then of course you need to import the module or the classes that you use from them. For example, you can import the logic class by calling:</p>
<pre><code class="lang-python">from SegmentCrossSectionArea import SegmentCrossSectionAreaLogic
logic = SegmentCrossSectionAreaLogic()
</code></pre>

---

## Post #9 by @Justin (2020-05-01 21:22 UTC)

<p>Thanks, I found the example but I did not know I needed to import</p>
<p>As you say, I just followed the rest of the test module to work run the model from script.</p>

---
