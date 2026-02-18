# How to Modify the Default Threshold Values in Segment Editor for Custom Segmentation?

**Topic ID**: 40727
**Date**: 2024-12-17
**URL**: https://discourse.slicer.org/t/how-to-modify-the-default-threshold-values-in-segment-editor-for-custom-segmentation/40727

---

## Post #1 by @VirOrange (2024-12-17 11:54 UTC)

<p>Operating system:win11<br>
Slicer version:5.6.2</p>
<p>Hello everyone,</p>
<p>I’m working on developing a custom module in Slicer and started by modifying existing components. In the <strong>Segment Editor</strong> module, I would like to modify the <strong>Threshold adjustment</strong> functionality to set a specific default threshold range, such as for <strong>skull segmentation</strong>.</p>
<p>Specifically, I want to set the default threshold values (e.g., Hounsfield unit range for the skull) so that when performing segmentation, the values are pre-set and there’s no need to manually adjust them every time. This way, the default values can be used directly for segmentation tasks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84fd59f023d517dbd974269094459362c0a5cca0.jpeg" data-download-href="/uploads/short-url/iYtPnUg73NtFvcYDgR7o18JMMGA.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84fd59f023d517dbd974269094459362c0a5cca0_2_689x366.jpeg" alt="image" data-base62-sha1="iYtPnUg73NtFvcYDgR7o18JMMGA" width="689" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84fd59f023d517dbd974269094459362c0a5cca0_2_689x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84fd59f023d517dbd974269094459362c0a5cca0_2_1033x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84fd59f023d517dbd974269094459362c0a5cca0.jpeg 2x" data-dominant-color="46464B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1106×588 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My questions are:</p>
<ol>
<li>Is this modification possible?</li>
<li>Do I need to re-engineer the whole Slicer software, or can this be done by modifying the relevant Python scripts or configuration files?</li>
</ol>

---

## Post #2 by @cpinter (2024-12-18 15:29 UTC)

<p>I think you can do this all from Python (<code>.slicerrc.py</code> or in your own module’s initialization).</p>
<p>Each Segment Editor has its own effects, and each effect has their parameters. Look at here for example to see how a parameter can be changed:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-keyboard-shortcut-for-toggling-sphere-brush-for-paint-and-erase-effects" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-keyboard-shortcut-for-toggling-sphere-brush-for-paint-and-erase-effects</a><br>
And you can see which parameters to set here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py#L371-L372">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py#L371-L372" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py#L371-L372" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorEffects/SegmentEditorThresholdEffect.py#L371-L372</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="371" style="counter-reset: li-counter 370 ;">
          <li>self.scriptedEffect.setParameterDefault("MinimumThreshold", 0.0)</li>
          <li>self.scriptedEffect.setParameterDefault("MaximumThreshold", 0)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @VirOrange (2024-12-25 00:28 UTC)

<p>if i modify the maximum thresold, does it means i need to compile slicer again?</p>

---

## Post #4 by @VirOrange (2024-12-25 02:40 UTC)

<p>I tried compiling again, and it worked. Thank you so much for your quick response; it was really helpful. Thank you!!!</p>

---
