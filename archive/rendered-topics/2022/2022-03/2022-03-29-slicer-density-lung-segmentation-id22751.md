---
topic_id: 22751
title: "Slicer Density Lung Segmentation"
date: 2022-03-29
url: https://discourse.slicer.org/t/22751
---

# Slicer Density Lung Segmentation

**Topic ID**: 22751
**Date**: 2022-03-29
**URL**: https://discourse.slicer.org/t/slicer-density-lung-segmentation/22751

---

## Post #1 by @PaoloZaffino (2022-03-29 15:59 UTC)

<p>Dear all,<br>
I would like to inform you that Slicer has a new extension: <a href="https://github.com/pzaffino/SlicerDensityLungSegmentation" rel="noopener nofollow ugc">Slicer Density Lung Segmentation</a>.<br>
In this extension, we provide a tool to classify lung tissue density on CT images.<br>
Its first use is for images of patients diagnosed with pneumonia (such as COVID19), where the algorithm is able to label voxels as “air”, “healthy parenchyma”, “ground glass”, “consolidation” and “thick tissue”.<br>
A couple of clicks are sufficient to automatically get such a piece of precious information…give it a shot!<br>
The rationale behind this extension, as well as a link to a free COVID-19 CT dataset, can be found <a href="https://www.mdpi.com/2306-5354/8/2/26" rel="noopener nofollow ugc">here</a>.</p>
<p>Do not hesitate to ask for further information or to improve the code (feedback are always welcomed)!</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pzaffino/SlicerDensityLungSegmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pzaffino/SlicerDensityLungSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/d1d6fa6d7880105a55991713f2a4506ed0fc0881438c52a408e062fc0136e740/pzaffino/SlicerDensityLungSegmentation" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pzaffino/SlicerDensityLungSegmentation" target="_blank" rel="noopener nofollow ugc">GitHub - pzaffino/SlicerDensityLungSegmentation: Extension for 3D Slicer that...</a></h3>

  <p>Extension for 3D Slicer that labels lung tissue according to density - GitHub - pzaffino/SlicerDensityLungSegmentation: Extension for 3D Slicer that labels lung tissue according to density</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @xackey (2023-04-07 05:03 UTC)

<p>Excellent extension!<br>
I want to operate this extension with python interactor.<br>
Could you tell me how to write python code?</p>

---

## Post #3 by @lassoan (2023-04-11 04:59 UTC)

<p>See how it is used in Python scripts in the module’s GUI:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pzaffino/SlicerDensityLungSegmentation/blob/cd207ded376cdac2e8bc9c3850fe3cac55024887/LungCTGMMSegmentation/LungCTGMMSegmentation.py#L136">
  <header class="source">

      <a href="https://github.com/pzaffino/SlicerDensityLungSegmentation/blob/cd207ded376cdac2e8bc9c3850fe3cac55024887/LungCTGMMSegmentation/LungCTGMMSegmentation.py#L136" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pzaffino/SlicerDensityLungSegmentation/blob/cd207ded376cdac2e8bc9c3850fe3cac55024887/LungCTGMMSegmentation/LungCTGMMSegmentation.py#L136" target="_blank" rel="noopener">pzaffino/SlicerDensityLungSegmentation/blob/cd207ded376cdac2e8bc9c3850fe3cac55024887/LungCTGMMSegmentation/LungCTGMMSegmentation.py#L136</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="126" style="counter-reset: li-counter 125 ;">
          <li>    self.onSelect()</li>
          <li>
          </li>
<li>    # Create logic object</li>
          <li>    self.logic = LungCTGMMSegmentationLogic()</li>
          <li>
          </li>
<li>  def onSelect(self):</li>
          <li>    self.applyButton.enabled = self.CTSelector.currentNode() and self.outputSelector.currentNode() and self.averagedOutputSelector.currentNode()</li>
          <li>
          </li>
<li>
          </li>
<li>  def onApplyButton(self):</li>
          <li class="selected">    self.logic.run(self.CTSelector.currentNode(), self.outputSelector.currentNode(), self.averagedOutputSelector.currentNode())</li>
          <li>#</li>
          <li># LungCTGMMSegmentationLogic</li>
          <li>#</li>
          <li>
          </li>
<li>class LungCTGMMSegmentationLogic(ScriptedLoadableModuleLogic):</li>
          <li>  """This class should implement all the actual</li>
          <li>  computation done by your module.  The interface</li>
          <li>  should be such that other python code can import</li>
          <li>  this class and make use of the functionality without</li>
          <li>  requiring an instance of the Widget.</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Daniel_Lo (2024-09-24 00:28 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e86fd454f609dd202485025bcb44f2e90c5a5507.jpeg" data-download-href="/uploads/short-url/xaemJ6YCYWrZofiZSS66xmgzZf9.jpeg?dl=1" title="Screenshot 2024-09-24 at 08.25.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e86fd454f609dd202485025bcb44f2e90c5a5507_2_690x329.jpeg" alt="Screenshot 2024-09-24 at 08.25.23" data-base62-sha1="xaemJ6YCYWrZofiZSS66xmgzZf9" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e86fd454f609dd202485025bcb44f2e90c5a5507_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e86fd454f609dd202485025bcb44f2e90c5a5507_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e86fd454f609dd202485025bcb44f2e90c5a5507_2_1380x658.jpeg 2x" data-dominant-color="A1A29F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-09-24 at 08.25.23</span><span class="informations">1920×917 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Hi, i have tried this, my system is macos, in this case, i have large green area, which was labeled as label_2, can you help me to understand this part ?</p>

---
