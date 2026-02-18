# Vessel tree centerline branch extraction using VMTK

**Topic ID**: 11867
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/vessel-tree-centerline-branch-extraction-using-vmtk/11867

---

## Post #1 by @szhang (2020-06-04 19:49 UTC)

<p>Hello<br>
In order to utilize some of vmtk functionalities (branch splitting is the one of interest, i.e. vmtkbranchextractor), is it possible to import their libraries?<br>
However, a simple “import vmtk” does not seem to succeed, any pointers?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-06-04 20:34 UTC)

<p>You need to import specific VMTK packages as it is done in existing VMTK modules in Slicer:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L69-L73" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L69-L73" target="_blank">vmtk/SlicerExtension-VMTK/blob/master/VesselnessFiltering/VesselnessFiltering.py#L69-L73</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="69" style="counter-reset: li-counter 68 ;">
<li>try:</li>
<li>  import vtkvmtkSegmentationPython as vtkvmtkSegmentation</li>
<li>except ImportError:</li>
<li>  self.layout.addWidget(qt.QLabel("Failed to load VMTK libraries"))</li>
<li>  return</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @szhang (2020-06-04 21:00 UTC)

<p>I see, thank you.<br>
Correct, “import vtkvmtkSegmentationPython” is possible, but “import vmtkbranchextractor” or "“import vtkvmtkbranchextractor” is not possible, what am I missing?</p>
<p>Thanks again!</p>

---

## Post #4 by @lassoan (2020-06-04 21:06 UTC)

<p>You need to follow the exact same format (note the capitalization and “Python” at the end). Probably you need something like this:</p>
<pre><code class="lang-python">import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
extractor = vtkvmtkComputationalGeometry.vtkvmtkCenterlineBranchExtractor()
</code></pre>

---

## Post #5 by @lassoan (2020-06-04 21:09 UTC)

<p>If you manage to implement some new features it would be great if you could contribute back to SlicerVMTK extension (add to one of the existing modules or add a new module). We can help polishing things and adding to the extension.</p>

---

## Post #6 by @lassoan (2020-06-05 16:28 UTC)

<p>FYI, I’ve <a href="https://github.com/vmtk/SlicerExtension-VMTK/commit/10caf98d22dcbfc776c5861d1806d4079c32fc83">added a simple function to VMTK Slicer extension</a> to allow showing the extracted centerlines as a hierarchy of markups curves (it uses centerline branch extractor and merger):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86c98ac974bbb4249221f9783e7eeb91385c06e4.png" data-download-href="/uploads/short-url/jenMy8XRrXBq8JQ4BQNHBJRVK28.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86c98ac974bbb4249221f9783e7eeb91385c06e4_2_690x418.png" alt="image" data-base62-sha1="jenMy8XRrXBq8JQ4BQNHBJRVK28" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86c98ac974bbb4249221f9783e7eeb91385c06e4_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86c98ac974bbb4249221f9783e7eeb91385c06e4_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/86c98ac974bbb4249221f9783e7eeb91385c06e4_2_1380x836.png 2x" data-dominant-color="CACBE4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1369 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This allows you to remove branches, assign names, show/hide sections, measure lengths, get parent/children branches easily.</p>

---

## Post #7 by @szhang (2020-06-05 19:51 UTC)

<p>Great, thank you for extending the extension! Some follow-up questions:</p>
<ol>
<li>What’s the reason this function cannot be used on the stable version 4.10?</li>
<li>I modified 411 to 410 in the code, and tried it on 4.10.2, while “Curve tree root” is stuck at “None”, as clicking “Create New Node” or “Delete current node” does not lead anywhere.</li>
<li>It will be great if you could create a quick tutorial video to explain how to use this function.</li>
</ol>

---

## Post #8 by @jamesobutler (2020-06-05 21:47 UTC)

<p><a class="mention" href="/u/szhang">@szhang</a> The function can’t be used in Slicer 4.10 because the actual curve object being used (vtkMRMLMarkupsCurveNode) is only available in Slicer 4.11. It is parts of the Markups module which had a major overhaul after Slicer 4.10 was released.</p>

---

## Post #9 by @lassoan (2020-06-06 04:38 UTC)

<p>I’ve uploaded a short video that shows how to segment and extract centerline of vessels:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="caEuwJ7pCWs" data-video-title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=caEuwJ7pCWs" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/caEuwJ7pCWs/maxresdefault.jpg" title="Vessel segmentation and centerline extraction using 3D Slicer and VMTK" width="" height="">
  </a>
</div>


---

## Post #10 by @szhang (2020-06-08 10:46 UTC)

<p>Excellent, thank you very much! The decimation is a good step to learn.<br>
The tree branches look slightly off from the centerlines if I am not mistaken.</p>

---

## Post #11 by @lassoan (2020-06-08 14:32 UTC)

<aside class="quote no-group" data-username="szhang" data-post="10" data-topic="11867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> szhang:</div>
<blockquote>
<p>The tree branches look slightly off from the centerlines if I am not mistaken.</p>
</blockquote>
</aside>
<p>Preview puts result of network extraction (vtkvmtkPolyDataNetworkExtraction) into the output model node.</p>
<p>Full computation puts result of network+centerline extraction (vtkvmtkPolyDataNetworkExtraction+vtkvmtkPolyDataCenterlines) into the output model node, and result of additional branch extraction + merging is saved into curve nodes.</p>
<p>These are somewhat arbitrary. If you have better suggestions about what outputs to save then let me know. For example, we could save the result of branch extraction and merge into the output model node instead (or in addition).</p>

---

## Post #12 by @szhang (2020-06-08 19:19 UTC)

<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="8" data-topic="11867" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><a class="mention" href="/u/szhang">@szhang</a> the actual curve object being used (vtkMRMLMarkupsCurveNode) is only available in Slicer 4.11.</p>
</blockquote>
</aside>
<p>Hello, a quick question here, do you suggest any work-around of the nightly built latest&amp;greatest Markups module? i.e. if I still want to stick with the stable version 4.10.2?</p>
<p>Thank you!!</p>

---

## Post #13 by @jamesobutler (2020-06-08 19:29 UTC)

<p>What is your motivation for continuing to stick with Slicer 4.10.2? Is there something in the Slicer nightly that doesn’t work/work well for you that is working in Slicer 4.10.2?</p>

---

## Post #14 by @szhang (2020-06-08 23:24 UTC)

<p>Well, since not all modules are available to download from extension manager in the nightly version, and by simple copy-paste of the extension folder it doesn’t get the modules running (apparently). If the markup module was overhauled before python 3 migration and ITK upgrades to 5, is there such a nightly build to download?<br>
To be back to the question of work-around in 4.10, if centerlines were already displayed, then branching is like highlighting portion of the lines, right?</p>
<p>Thank you!</p>

---

## Post #15 by @lassoan (2020-06-08 23:38 UTC)

<aside class="quote no-group" data-username="szhang" data-post="14" data-topic="11867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> szhang:</div>
<blockquote>
<p>Well, since not all modules are available to download from extension manager in the nightly version,</p>
</blockquote>
</aside>
<p>Which modules you have trouble finding?</p>
<aside class="quote no-group" data-username="szhang" data-post="14" data-topic="11867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> szhang:</div>
<blockquote>
<p>simple copy-paste of the extension folder it doesn’t get the modules running (apparently)</p>
</blockquote>
</aside>
<p>There is no difference in this between Slicer-4.10 and Slicer-4.11.</p>
<aside class="quote no-group" data-username="szhang" data-post="14" data-topic="11867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> szhang:</div>
<blockquote>
<p>To be back to the question of work-around in 4.10, if centerlines were already displayed, then branching is like highlighting portion of the lines, right?</p>
</blockquote>
</aside>
<p>I don’t understand the question and cannot afford to spend time with thinking about workarounds for Slicer-4.10. However, I can help to make sure that you can do everything with latest Preview Release that you could do with Slicer-4.10.</p>

---

## Post #17 by @szhang (2020-06-10 10:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="11867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Which modules you have trouble finding?</p>
</blockquote>
</aside>
<p>The module AirwaySegmentationCLI cannot be found in the Preview Release.</p>
<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="11867" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I can help to make sure that you can do everything with latest Preview Release that you could do with Slicer-4.10.</p>
</blockquote>
</aside>
<p>Really appreciate your help!</p>

---

## Post #18 by @lassoan (2020-06-10 17:26 UTC)

<aside class="quote no-group" data-username="szhang" data-post="17" data-topic="11867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bc8723/48.png" class="avatar"> szhang:</div>
<blockquote>
<p>The module AirwaySegmentationCLI cannot be found in the Preview Release.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> has fixed it this week. Download today’s Slicer Preview Release - the Chest Imaging Platform extension is already available for it.</p>

---

## Post #19 by @qubalee (2021-01-03 06:51 UTC)

<p>Hi there!</p>
<p>I have just installed the VMTK extension but I could not find the “Centerline Computation”. Where can I find it?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4415f31bea92c31c527f0468f0f1e9b009d84329.jpeg" alt="Capture.PNG" data-base62-sha1="9IjuGlxotM5NbUNeSP0070lGNDP" width="509" height="228"></p>

---

## Post #20 by @lassoan (2021-01-03 16:47 UTC)

<p>Use latest Slicer Stable or Preview Release and install SlicerVMTK extension.</p>

---

## Post #21 by @qubalee (2021-01-09 09:48 UTC)

<blockquote>
<h2>Centerline Computation module (legacy)</h2>
<p><em>This module is replaced by the much improved, faster and more robust “Extract Centerline” module in current Slicer versions (Slicer-4.11 and later).</em></p>
<p>This module determines centerlines in a vessel tree from an input model node. Click “Preview” button for a quick validation of the input model and approximate centerline computation. Click “Start” button for full network analysis and computation of all outputs.</p>
<p>Required inputs:</p>
<ul>
<li>Vessel tree model: this can be any tree structure (not just vascular tree but airways, etc.), either created in Segment Editor module or using Level Set Segmentation module. If Segment Editor is used then segmentation node must be exported to model node by right-clicking on the segmentation in Data module and selecting “Export visible segments to models”.</li>
<li>Start point: a markups fiducial node containing a single point, this should be placed at the branch of the tree</li>
</ul>
<p>Outputs:</p>
<ul>
<li>Centerline model: network extraction results (without branch extraction and merging). Points contain centerline points, and “Radius” point data contains maximum inscribed sphere radius at each point.</li>
<li>Centerline endpoints: Coordinates of found start point and all detected branch endpoints.</li>
<li>Voronoi model (optional): medial surface of the input model (medial surface contains points that are qat equal distance from nearest surface points)</li>
<li>Curve tree rool (optional): if a markups curve node is selected then a hierarchy of curve nodes are created from extracted and merged branches. CellId of each branch is saved into the node’s name (and also as node attribute), which can be used for cross-referencing with CellId column of centerline properties table.</li>
<li>Centerline properties (optional): if a table node is selected then branch length, average radius, curvature, torsion, and tortuosity is computed for all the extracted and merged branches.</li>
</ul>
</blockquote>

---

## Post #22 by @fuentesdt (2021-03-09 16:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="11867">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Preview puts result of network extraction (vtkvmtkPolyDataNetworkExtraction) into the output model node.</p>
</blockquote>
</aside>
<p>Hi, the output of this (a) “Preview” button network extraction seems to be a more robust and comprehensive representation of the vessel data than when we run the (b) full computation.<br>
The full computation is very sensitive to the seed points and I cannot find a combination of seed points that recovers the result from the “Preview” functionality. Is there any functionality to enforce similar results for the “Preview” and “Start” full computation (Using Slicer 4.10.2 still)? Otherwise is there a general rule of thumb to debug these differences ? I think I saw on a tutorial that some points on the Voronoi Model are better than other?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cb257dac32bb3f5dd9c6c98510b45c52a6656b3.png" data-download-href="/uploads/short-url/6np6E5Qm2nsuwUJ840KzewMAgPV.png?dl=1" title="previewvsfull" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cb257dac32bb3f5dd9c6c98510b45c52a6656b3_2_690x281.png" alt="previewvsfull" data-base62-sha1="6np6E5Qm2nsuwUJ840KzewMAgPV" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2cb257dac32bb3f5dd9c6c98510b45c52a6656b3_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cb257dac32bb3f5dd9c6c98510b45c52a6656b3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cb257dac32bb3f5dd9c6c98510b45c52a6656b3.png 2x" data-dominant-color="F7F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">previewvsfull</span><span class="informations">962×392 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @lassoan (2021-03-09 17:48 UTC)

<p>You see the straight lines if path cannot be found to a point. It is almost always happens because the endpoint is on the surface mesh, while the full centerline extraction searches along the Voronoi diagram, which is inside the mesh.</p>
<p>You can fix the error easily by moving the endpoints inside the mesh. It would be easy to automate this by snapping the endpoint to the closest point on the Voronoi surface. It would be great if you could implement this and send a pull request.</p>

---

## Post #24 by @szhang (2021-03-29 10:28 UTC)

<p>Since I do see these straightened centerline segments often, could you please elaborate on how to move endpoints into the mesh?<br>
In this example I see the connecting lines are not even passing through the endpoints<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/306b10ced93c1de9c5c66085e37557fa8ffd62dd.jpeg" data-download-href="/uploads/short-url/6UkiX50aANPkdTwezVuMLHyvM6x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/306b10ced93c1de9c5c66085e37557fa8ffd62dd_2_412x499.jpeg" alt="image" data-base62-sha1="6UkiX50aANPkdTwezVuMLHyvM6x" width="412" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/306b10ced93c1de9c5c66085e37557fa8ffd62dd_2_412x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/306b10ced93c1de9c5c66085e37557fa8ffd62dd_2_618x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/306b10ced93c1de9c5c66085e37557fa8ffd62dd.jpeg 2x" data-dominant-color="929DAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×901 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you.</p>

---

## Post #25 by @szhang (2021-04-12 21:55 UTC)

<p>Hi <a class="mention" href="/u/fuentesdt">@fuentesdt</a><br>
I felt the same pain as you did.<br>
Now here’s my work-around: basically I converted the model to segmentation, then use “Margin” to grow the segmentation by 1 pixel (remember, 1 is enough), so the segmentation will look fuller. Additional step could be to use “Island” to keep largest island. Then use this grown segmentation in the “Extract Centerline” module as input, followed by automatic Endpoint identification, etc. So far in my case, it has been performing wonder (i.e. no more weird centerlines)!</p>
<p>Hope it helps!</p>

---
