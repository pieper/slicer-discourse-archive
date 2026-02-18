# Process Node attributes to convert it into SlicerRT dose node

**Topic ID**: 8709
**Date**: 2019-10-08
**URL**: https://discourse.slicer.org/t/process-node-attributes-to-convert-it-into-slicerrt-dose-node/8709

---

## Post #1 by @Alex_Vergara (2019-10-08 14:53 UTC)

<p>What are the attributes that SlicerRT expects for a dose node to have? I can’t find a description of these.</p>
<p>Basically I want to be able to use my own produced dose matrix into SlicerRT.</p>

---

## Post #2 by @cpinter (2019-10-08 14:57 UTC)

<p>These two attributes in the parent study item:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/SlicerRtCommon/vtkSlicerRtCommon.cxx#L66-L67" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/SlicerRtCommon/vtkSlicerRtCommon.cxx#L66-L67" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT/blob/master/SlicerRtCommon/vtkSlicerRtCommon.cxx#L66-L67</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="66" style="counter-reset: li-counter 65 ;">
<li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_UNIT_NAME_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "DoseUnitName";
</li>
<li>const std::string vtkSlicerRtCommon::DICOMRTIMPORT_DOSE_UNIT_VALUE_ATTRIBUTE_NAME = vtkSlicerRtCommon::DICOMRTIMPORT_ATTRIBUTE_PREFIX + "DoseUnitValue";
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>If you move the volume under a study that is under a patient, and choose Convert into dose volume in the right-click menu, then you can do it from the UI. Otherwise you need to set it up yourself.</p>

---

## Post #3 by @Alex_Vergara (2019-10-08 15:01 UTC)

<p>So, the dose nodes must be inside a study and this study is the one that needs to have these attributes?</p>
<p>Is not important to have the modality as <code>RTDOSE</code> then?</p>

---

## Post #4 by @cpinter (2019-10-08 15:13 UTC)

<p>Exactly. The DICOM attributes in SH are populated when importing from DICOM, and when exporting to DICOM, for easier identification, but are not used in this case.</p>

---
