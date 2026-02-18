# Create non GUI module

**Topic ID**: 19787
**Date**: 2021-09-21
**URL**: https://discourse.slicer.org/t/create-non-gui-module/19787

---

## Post #1 by @keri (2021-09-21 16:01 UTC)

<p>Hi,</p>
<p>Is it possible to create non GUI loadable module? Hide it even from module menu.<br>
I used to find some information in Intertnet but can’t do that now…</p>

---

## Post #2 by @lassoan (2021-09-21 17:53 UTC)

<p>You can set the module’s <code>hidden</code> attribute to make the module hidden:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/022a4f1a347ebb24509a50f6c8928ae26d3c5955/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L833-L834">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/022a4f1a347ebb24509a50f6c8928ae26d3c5955/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L833-L834" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/022a4f1a347ebb24509a50f6c8928ae26d3c5955/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L833-L834" target="_blank" rel="noopener">Slicer/Slicer/blob/022a4f1a347ebb24509a50f6c8928ae26d3c5955/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L833-L834</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="833" style="counter-reset: li-counter 832 ;">
          <li># don't show this module - it only appears in the DICOM module</li>
          <li>parent.hidden = True</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
