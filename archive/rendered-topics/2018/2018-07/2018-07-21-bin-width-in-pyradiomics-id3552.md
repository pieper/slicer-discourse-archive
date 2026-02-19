---
topic_id: 3552
title: "Bin Width In Pyradiomics"
date: 2018-07-21
url: https://discourse.slicer.org/t/3552
---

# Bin width in Pyradiomics 

**Topic ID**: 3552
**Date**: 2018-07-21
**URL**: https://discourse.slicer.org/t/bin-width-in-pyradiomics/3552

---

## Post #1 by @mnchyy (2018-07-21 14:17 UTC)

<p>Hello<br>
I’m working on Pyradiomics in 3D Slicer and I found that I can only adjust bin width up to only 100. Is there any possible way to change the bin width more than 100?</p>
<p>many thanks</p>

---

## Post #2 by @pieper (2018-07-23 23:05 UTC)

<p>That’s a kind of arbitrary hard coded upper limit - if you want to change it you can edit this line:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L276" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L276" target="_blank">Radiomics/SlicerRadiomics/blob/master/SlicerRadiomics/SlicerRadiomics.py#L276</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="266" style="counter-reset: li-counter 265 ;">
<li>manualCustomizationFormLayout.addWidget(settingsCollapsibleButton)</li>
<li>
</li>
<li># Layout within the dummy collapsible button</li>
<li>settingsFormLayout = qt.QFormLayout(settingsCollapsibleButton)</li>
<li>
</li>
<li># bin width, defaults to 25</li>
<li>self.binWidthSliderWidget = ctk.ctkSliderWidget()</li>
<li>self.binWidthSliderWidget.singleStep = 1</li>
<li>self.binWidthSliderWidget.decimals = 2</li>
<li>self.binWidthSliderWidget.minimum = 0.01</li>
<li class="selected">self.binWidthSliderWidget.maximum = 100</li>
<li>self.binWidthSliderWidget.value = 25</li>
<li>self.binWidthSliderWidget.toolTip = 'Set the bin width'</li>
<li>settingsFormLayout.addRow('Bin Width', self.binWidthSliderWidget)</li>
<li>
</li>
<li># symmetricalGLCM flag, defaults to false</li>
<li>self.symmetricalGLCMCheckBox = qt.QCheckBox()</li>
<li>self.symmetricalGLCMCheckBox.checked = 1</li>
<li>self.symmetricalGLCMCheckBox.toolTip = 'Use a symmetrical GLCM matrix'</li>
<li>settingsFormLayout.addRow('Enforce Symmetrical GLCM', self.symmetricalGLCMCheckBox)</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>(you need to find this file in the extension installation, edit it, and restart Slicer).</p>
<p>But a better approach would be to use the latest nightly preview of Slicer and the corresponding SlicerRadiomics extension and from there you can specify your own parameter file with whatever settings you want.as described here:</p>
<p><a href="https://pyradiomics.readthedocs.io/en/latest/customization.html#parameter-file" class="onebox" target="_blank">https://pyradiomics.readthedocs.io/en/latest/customization.html#parameter-file</a></p>
<p>If you want to suggest a better default min and max for bin width, you could file a feature request here <a href="https://github.com/Radiomics/SlicerRadiomics/issues">https://github.com/Radiomics/SlicerRadiomics/issues</a></p>

---
