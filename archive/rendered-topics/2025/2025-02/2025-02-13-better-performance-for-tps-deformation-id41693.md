# Better performance for TPS deformation?

**Topic ID**: 41693
**Date**: 2025-02-13
**URL**: https://discourse.slicer.org/t/better-performance-for-tps-deformation/41693

---

## Post #1 by @muratmaga (2025-02-13 23:59 UTC)

<p>we use TPS to create interactive visualization of landmark based deformations, in which the user sets a slider to adjust magnitude of the deformation:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/blob/d9b1c22e0b92959929e2ceedb5d5a978cf5bd29a/GPA/GPA.py#L1846">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/d9b1c22e0b92959929e2ceedb5d5a978cf5bd29a/GPA/GPA.py#L1846" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/d9b1c22e0b92959929e2ceedb5d5a978cf5bd29a/GPA/GPA.py#L1846" target="_blank" rel="noopener nofollow ugc">GPA/GPA.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/SlicerMorph/blob/d9b1c22e0b92959929e2ceedb5d5a978cf5bd29a/GPA/GPA.py#L1846" rel="noopener nofollow ugc"><code>d9b1c22e0</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1836" style="counter-reset: li-counter 1835 ;">
          <li>  # Set up transform for PCA warping</li>
          <li>  self.transformNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode', 'PC TPS Transform')</li>
          <li>  GPANodeCollection.AddItem(self.transformNode)</li>
          <li></li>
          <li>  # Enable PCA warping and recording</li>
          <li>  self.slider1.populateComboBox(self.PCList)</li>
          <li>  self.slider2.populateComboBox(self.PCList)</li>
          <li>  self.applyEnabled = True</li>
          <li>  self.startRecordButton.enabled = True</li>
          <li></li>
          <li class="selected">def onApply(self):</li>
          <li>  pc1=self.slider1.boxValue()</li>
          <li>  pc2=self.slider2.boxValue()</li>
          <li>  pcSelected=[pc1,pc2]</li>
          <li></li>
          <li>  # get scale values for each pc.</li>
          <li>  sf1=self.slider1.sliderValue()</li>
          <li>  sf2=self.slider2.sliderValue()</li>
          <li>  scaleFactors=np.zeros(2)</li>
          <li>  scaleFactors[0]=sf1/100.0</li>
          <li>  scaleFactors[1]=sf2/100.0</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This works well (fast enough to be interactive) up to about 50-60 points. But as the number of points increase, the calculation becomes slower removing or interfering with the interactivy. What can we do to make this performant for high number of points?</p>

---

## Post #2 by @pieper (2025-02-14 18:08 UTC)

<p>If all you are doing is scaling the amount of the displacement then you shouldn’t need to recalculate every time.  You could convert to a grid transform and then scale the offsets based on the slider.</p>
<p>Something like this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerGetFEM/blob/main/Experiments/lung/lung.slicer.py#L63-L70">
  <header class="source">

      <a href="https://github.com/pieper/SlicerGetFEM/blob/main/Experiments/lung/lung.slicer.py#L63-L70" target="_blank" rel="noopener">github.com/pieper/SlicerGetFEM</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerGetFEM/blob/main/Experiments/lung/lung.slicer.py#L63-L70" target="_blank" rel="noopener">Experiments/lung/lung.slicer.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/pieper/SlicerGetFEM/blob/main/Experiments/lung/lung.slicer.py#L63-L70" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="63" style="counter-reset: li-counter 62 ;">
          <li>def onValueChanged(int):</li>
          <li>    global modelPoints, originalPositions, slider, displacement, resultMesh</li>
          <li>    global gridArray, originalGridArray, displacementGridNode</li>
          <li>    animationFactor = slider.value / slider.maximum</li>
          <li>    modelPoints[:] = originalPositions + animationFactor * displacement</li>
          <li>    gridArray[:] = animationFactor * originalGridArray</li>
          <li>    slicer.util.arrayFromModelPointsModified(resultMesh)</li>
          <li>    slicer.util.arrayFromGridTransformModified(displacementGridNode)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
