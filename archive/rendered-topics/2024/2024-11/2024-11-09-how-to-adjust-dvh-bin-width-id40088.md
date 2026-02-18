# How to adjust DVH bin width?

**Topic ID**: 40088
**Date**: 2024-11-09
**URL**: https://discourse.slicer.org/t/how-to-adjust-dvh-bin-width/40088

---

## Post #1 by @wilbysl (2024-11-09 04:24 UTC)

<p>Hello.<br>
Can anyone tell me if it’s possible to change the bin width for DVHs in v5.6.2 of Slicer3D please?<br>
Many thanks</p>

---

## Post #2 by @cpinter (2024-11-14 13:35 UTC)

<p>There is no option for this on the GUI. However, you have the possibility to change it from Python using these functions:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/Logic/vtkSlicerDoseVolumeHistogramModuleLogic.h#L125-L129">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/Logic/vtkSlicerDoseVolumeHistogramModuleLogic.h#L125-L129" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/Logic/vtkSlicerDoseVolumeHistogramModuleLogic.h#L125-L129" target="_blank" rel="noopener">SlicerRt/SlicerRT/blob/master/DoseVolumeHistogram/Logic/vtkSlicerDoseVolumeHistogramModuleLogic.h#L125-L129</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="125" style="counter-reset: li-counter 124 ;">
          <li>vtkGetMacro(StartValue, double);
</li>
          <li>vtkSetMacro(StartValue, double);
</li>
          <li>
</li>
          <li>vtkGetMacro(StepSize, double);
</li>
          <li>vtkSetMacro(StepSize, double);
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The code you need to run in the Python console is</p>
<pre><code class="lang-auto">dvhLogic = slicer.modules.dosevolumehistogram.logic()
dvhLogic.SetStartValue(0.1)
dvhLogic.SetStepSize(0.2)
</code></pre>
<p>Obviously you need to changes these values. The above numbers are the defaults.</p>
<p>If you want this to be persistent every time you start Slicer, you can add this to the <code>.slicerrc.py</code> file.</p>

---

## Post #3 by @wilbysl (2024-11-20 14:00 UTC)

<p>Thank you Csaba, that’s very helpful. I will give it a try.</p>
<p>Best wishes</p>
<p>Sarah</p>

---
