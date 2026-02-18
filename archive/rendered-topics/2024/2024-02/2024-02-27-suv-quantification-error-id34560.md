# SUV quantification error

**Topic ID**: 34560
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/suv-quantification-error/34560

---

## Post #1 by @david.gulis (2024-02-27 03:59 UTC)

<p>Hi all,</p>
<p>I am trying to quantify SUVs in segmented areas of a mouse PET/CT study, and it results in a blank table and the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec7f8dc357e0c6cf9dc851e23af7dc4a399731ad.png" data-download-href="/uploads/short-url/xK9XS9uqg48d0IuyHjLca4CIodD.png?dl=1" title="Slc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec7f8dc357e0c6cf9dc851e23af7dc4a399731ad_2_393x500.png" alt="Slc" data-base62-sha1="xK9XS9uqg48d0IuyHjLca4CIodD" width="393" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec7f8dc357e0c6cf9dc851e23af7dc4a399731ad_2_393x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec7f8dc357e0c6cf9dc851e23af7dc4a399731ad_2_589x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec7f8dc357e0c6cf9dc851e23af7dc4a399731ad.png 2x" data-dominant-color="F2F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slc</span><span class="informations">693×880 34.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have tried modifying the metadata but I could not find some of the tags with the parameter names mentioned in this error message. And I am not sure what MODULE_INIT_NO_VALUE means.</p>
<p>Any help appreciated. Thanks</p>

---

## Post #2 by @pieper (2024-02-27 19:49 UTC)

<p>These comments should help:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L47">
  <header class="source">

      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L47" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L47" target="_blank" rel="noopener">QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx#L47</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="37" style="counter-reset: li-counter 36 ;">
          <li>#include "vtkSUVFactorCalculatorVersionConfigure.h"</li>
          <li></li>
          <li>// helpers</li>
          <li>#include "dcmHelpersCommon.h"</li>
          <li>#include "dcmUnitsConversionHelper.h"</li>
          <li></li>
          <li>// ...</li>
          <li>// ...............................................................................................</li>
          <li>// ...</li>
          <li>/*</li>
          <li class="selected">SOME NOTES on SUV and parameters of interest:</li>
          <li></li>
          <li>This is the first-pass implementation we'll make:</li>
          <li></li>
          <li>Standardized uptake value, SUV, (also referred to as the dose uptake ratio,</li>
          <li>DUR) is a widely used, simple PET quantifier, calculated as a ratio of tissue</li>
          <li>radioactivity concentration (e.g. in units kBq/ml) at time T, CPET(T) and</li>
          <li>injected dose (e.g. in units MBq) at the time of injection divided by body</li>
          <li>weight (e.g. in units kg).</li>
          <li></li>
          <li>SUVbw = CPET(T) / (Injected dose / Patient's weight)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
