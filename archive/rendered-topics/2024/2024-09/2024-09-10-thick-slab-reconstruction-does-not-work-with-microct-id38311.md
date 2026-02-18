# Thick slab reconstruction does not work with MicroCT

**Topic ID**: 38311
**Date**: 2024-09-10
**URL**: https://discourse.slicer.org/t/thick-slab-reconstruction-does-not-work-with-microct/38311

---

## Post #1 by @cpinter (2024-09-10 12:28 UTC)

<p>Hi all,</p>
<p>I noticed when working with MicroCT data that the thick slab reconstruction is not really meant for this modality. The minimum thickness is set to 1mm, which makes it basically unusable for volumes with very small voxel spacings.</p>
<p>Here’s a video illustrating this:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20bb20a69de3270738de57b6ad07a2766bc91476.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38d980250eceac01719754cb509ea99854fbe542.jpeg">
  </div><p></p>
<p>Here’s the volume I was using for this test:<br>
<a href="https://1drv.ms/u/s!Ao_a-dPPX98Zh-lE2xThOTUH53A4RA?e=3KtOHG">microbumps_FDK cropped.nrrd</a></p>
<p>And here’s the line that I think would be the simplest place to fix this:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/c28ce0c16593fd6c494ceef4f65e3e4ee2d4d65c/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L1612">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/c28ce0c16593fd6c494ceef4f65e3e4ee2d4d65c/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L1612" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/c28ce0c16593fd6c494ceef4f65e3e4ee2d4d65c/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L1612" target="_blank" rel="noopener">Slicer/Slicer/blob/c28ce0c16593fd6c494ceef4f65e3e4ee2d4d65c/Libs/MRML/Widgets/qMRMLSliceControllerWidget.cxx#L1612</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1602" style="counter-reset: li-counter 1601 ;">
          <li>// Make thick slab lines interactive</li>
          <li>this-&gt;SlabReconstructionMenu-&gt;addAction(this-&gt;actionSlabReconstructionInteractive);</li>
          <li></li>
          <li>this-&gt;SlabReconstructionMenu-&gt;addSeparator();</li>
          <li></li>
          <li>// Slab Reconstruction Thickness</li>
          <li>QMenu* slabReconstructionThicknessMenu = new QMenu(tr("Slab thickness"), this-&gt;EnableSlabReconstructionButton);</li>
          <li>slabReconstructionThicknessMenu-&gt;setObjectName("slicerSpacingManualMode");</li>
          <li>this-&gt;SlabReconstructionThicknessSpinBox = new ctkDoubleSpinBox(slabReconstructionThicknessMenu);</li>
          <li>this-&gt;SliceSpacingSpinBox-&gt;setDecimals(3);</li>
          <li class="selected">this-&gt;SlabReconstructionThicknessSpinBox-&gt;setRange(1., VTK_FLOAT_MAX);</li>
          <li>this-&gt;SlabReconstructionThicknessSpinBox-&gt;setSingleStep(0.1);</li>
          <li>this-&gt;SlabReconstructionThicknessSpinBox-&gt;setValue(1.);</li>
          <li>QObject::connect(this-&gt;SlabReconstructionThicknessSpinBox, SIGNAL(valueChanged(double)),</li>
          <li>                 q, SLOT(setSlabReconstructionThickness(double)));</li>
          <li>QWidgetAction* slabReconstructionThicknessAction = new QWidgetAction(slabReconstructionThicknessMenu);</li>
          <li>slabReconstructionThicknessAction-&gt;setDefaultWidget(this-&gt;SlabReconstructionThicknessSpinBox);</li>
          <li>slabReconstructionThicknessMenu-&gt;addAction(slabReconstructionThicknessAction);</li>
          <li>this-&gt;SlabReconstructionMenu-&gt;addMenu(slabReconstructionThicknessMenu);</li>
          <li>this-&gt;SlabReconstructionThicknessMenu = slabReconstructionThicknessMenu;</li>
          <li></li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, simply decreasing this would not be the best solution, because then we’d need to also decrease the single step value, which would make it unusable on normal patient volumes. (I also did not look into any similar limitation on the logic level, I just assumed that the constraint comes from this single place.)</p>
<p>What could be a good solution for this?</p>

---

## Post #2 by @pieper (2024-09-10 12:50 UTC)

<p>It sounds like the step size and range should adapt to the geometry of the volumes in the view.  If it’s not possible to do this automatically, perhaps a menu item to select a reference volume to use for determining the values.</p>

---

## Post #3 by @lassoan (2024-09-11 21:27 UTC)

<p>First of all, it should not be a <code>ctkDoubleSpinBox</code> but a <code>qMRMLSpinBox</code>, with unit set to <code>length</code>. That would display the unit correctly, and could use application defaults for precision and user could hit Ctrl - + to see more digits.</p>
<p>Minimum of the range can be set to 0.</p>
<p>Computing the step size dynamically from the spacing as <a class="mention" href="/u/pieper">@pieper</a> suggested would be nice (similarly to how the slider’s step size is computed from the volume spacing), but it should be acceptable to have a hardcoded value there, as user can still type any number or drag-and-dropping the handles in slice view to adjust the value.</p>

---
