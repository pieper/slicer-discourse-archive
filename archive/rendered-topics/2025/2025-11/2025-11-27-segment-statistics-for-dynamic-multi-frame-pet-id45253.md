# Segment Statistics for dynamic (multi frame) PET

**Topic ID**: 45253
**Date**: 2025-11-27
**URL**: https://discourse.slicer.org/t/segment-statistics-for-dynamic-multi-frame-pet/45253

---

## Post #1 by @lennart81 (2025-11-27 14:39 UTC)

<p>Hi community,</p>
<p>I am working with dynamic PET data acquired on a Siemens Quadra PET/CT (30 frames + static CT).</p>
<p>I have loaded the data and segmented several VOIs based on the CT. My goal is to extract the mean PET intensity per frame (Time Activity Curve) for these segments.</p>
<p>Currently, when I use the calculate statistics function, it seems to only calculate values for the currently displayed scalar volume (a single frame), giving me just one data point per segment.</p>
<p>My questions:</p>
<p>Do I need to load the PET data specifically as a MultiVolume to extract statistics across all time points?</p>
<p>Is there a specific module or extension recommended for batch processing these statistics across all 30 frames, or does this require a Python script?</p>
<p>Any advice on the workflow would be appreciated.</p>
<p>Thanks, Jan</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5af152f15d499a973e2e282e7cffe0d9569a6c7.jpeg" data-download-href="/uploads/short-url/z3q5MJ4yDr3DoCNabPu5okxEmrl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5af152f15d499a973e2e282e7cffe0d9569a6c7_2_690x435.jpeg" alt="image" data-base62-sha1="z3q5MJ4yDr3DoCNabPu5okxEmrl" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5af152f15d499a973e2e282e7cffe0d9569a6c7_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5af152f15d499a973e2e282e7cffe0d9569a6c7_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5af152f15d499a973e2e282e7cffe0d9569a6c7_2_1380x870.jpeg 2x" data-dominant-color="95928F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1213 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Deep_Learning (2025-12-01 01:47 UTC)

<p>Slicer uses sequences for timepoints. Take a look at that.  Never worked with your type of data, so just a guess.</p>

---

## Post #3 by @mikebind (2025-12-01 19:03 UTC)

<p>Yes, you will need to load as multivolume sequence to be able to process all the frames.  No, I don’t believe there is currently a module which calculates segment statistics across each frame of a sequence, but this is relatively straightforward to implement in a python script.</p>
<p>Also, this snippet from the script repository is concise and clear for a simple application of gathering volume from segment statistics module using python:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment" target="_blank" rel="noopener nofollow ugc">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>And this whole section will be useful for understanding working with Sequences using python: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#sequences" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>For examples of these types of things (looping over frames of a sequence, doing something on each frame, creating an output) embedded in a full module, you might find this link helpful:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/13ce1612d06887a0beec66c0fe0c66ceed7849ad/DynamicMalaciaTools/DynamicMalaciaTools.py#L4786-L4822">
  <header class="source">

      <a href="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/13ce1612d06887a0beec66c0fe0c66ceed7849ad/DynamicMalaciaTools/DynamicMalaciaTools.py#L4786-L4822" target="_blank" rel="noopener nofollow ugc">github.com/mikebind/SlicerDynamicMalaciaTools</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/13ce1612d06887a0beec66c0fe0c66ceed7849ad/DynamicMalaciaTools/DynamicMalaciaTools.py#L4786-L4822" target="_blank" rel="noopener nofollow ugc">DynamicMalaciaTools/DynamicMalaciaTools.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/13ce1612d06887a0beec66c0fe0c66ceed7849ad/DynamicMalaciaTools/DynamicMalaciaTools.py#L4786-L4822" rel="noopener nofollow ugc"><code>13ce1612d</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="4786" style="counter-reset: li-counter 4785 ;">
          <li>def getTransformSequenceFromLandmarksSequence(</li>
          <li>    landmarkSeqNode, outputTranslationTformSeq=None, addToBrowser=False</li>
          <li>):</li>
          <li>    """From carina landmarks sequence, create translation-only transforms which</li>
          <li>    align the carina points.</li>
          <li>    """</li>
          <li>    scene = slicer.mrmlScene</li>
          <li>    browserNode = getFirstBrowser(landmarkSeqNode)</li>
          <li>    # Get first landmark location (all transforms should take the landmark to</li>
          <li>    # this point)</li>
          <li>    browserNode.SetSelectedItemNumber(0)</li>
          <li>    landmarkProxy = browserNode.GetProxyNode(landmarkSeqNode)</li>
          <li>    firstLandmarkLocation = np.array(landmarkProxy.GetNthControlPointPosition(0))</li>
          <li></li>
          <li>    if outputTranslationTformSeq is None:</li>
          <li>        # Create new sequence to hold transforms</li>
          <li>        outputTranslationTformSeq = scene.AddNewNodeByClass(</li>
          <li>            "vtkMRMLSequenceNode", "TranslationTransformsSeq"</li>
          <li>        )</li>
          <li>    outputTranslationTformSeq.CopySequenceIndex(landmarkSeqNode)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/13ce1612d06887a0beec66c0fe0c66ceed7849ad/DynamicMalaciaTools/DynamicMalaciaTools.py#L4786-L4822" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Likewise, for an example of running segment statistics from python on and getting a value from it, you might find this example helpful:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/main/DynamicMalaciaTools/DynamicMalaciaTools.py#L2547">
  <header class="source">

      <a href="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/main/DynamicMalaciaTools/DynamicMalaciaTools.py#L2547" target="_blank" rel="noopener nofollow ugc">github.com/mikebind/SlicerDynamicMalaciaTools</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/main/DynamicMalaciaTools/DynamicMalaciaTools.py#L2547" target="_blank" rel="noopener nofollow ugc">DynamicMalaciaTools/DynamicMalaciaTools.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/mikebind/SlicerDynamicMalaciaTools/blob/main/DynamicMalaciaTools/DynamicMalaciaTools.py#L2547" rel="noopener nofollow ugc"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="2537" style="counter-reset: li-counter 2536 ;">
          <li>        "csaData": csaData,</li>
          <li>        "arData": arData,</li>
          <li>        "longAxisData": longAxisData,</li>
          <li>        "shortAxisData": shortAxisData,</li>
          <li>        "airwayVolMm3Data": airwayVolData,</li>
          <li>        "slicePoints": slicePoints,</li>
          <li>        "sliceNormals": sliceNormals,</li>
          <li>    }</li>
          <li>    return quantData</li>
          <li></li>
          <li class="selected">def findAirwayVolumeInBoxMm3(</li>
          <li>    self,</li>
          <li>    airwaySegID,</li>
          <li>    airSegNode,</li>
          <li>    volBoxSegID,</li>
          <li>    volBoxSegNode,</li>
          <li>    keepIntersectedSegment=True,</li>
          <li>) -&gt; float:</li>
          <li>    """Finds the volume of the intersection between two segments in mm^3.</li>
          <li>    THe first should represent an airway, and the second should have been</li>
          <li>    generated from a box ROI (for example by fillROISegment).</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
