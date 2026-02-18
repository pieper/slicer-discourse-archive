# Implementation of Pivot and Spin Calibration

**Topic ID**: 44533
**Date**: 2025-09-19
**URL**: https://discourse.slicer.org/t/implementation-of-pivot-and-spin-calibration/44533

---

## Post #1 by @echisato (2025-09-19 19:31 UTC)

<p>Hello,</p>
<p>I am trying to implement pivot and spin calibration for a stylus, exactly how it is done in IGT &gt; Pivot Calibration (in order to prevent a user from having to navigate away from a custom module and back again, as well as preventing the need to manually choose the input/output transforms).</p>
<p>I am computing pivot calibration, getting the pivot RMSE, and getting the error text. I am then updating my output node with GetToolTipToToolMatrix and similarly running spin calibration. When I do pivot &gt; spin I get error values about one order of magnitude greater than what I get when I do it in the built-in module. If I do spin &gt; pivot, my pivot error blows up extremely high. Are the error values for pivot/spin related at all, or do they represent separate errors for the individual calibrations?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2025-09-19 21:44 UTC)

<p>SlicerIGT modules are designed to be used from other modules, because this is how we implement all the Slicer-based applications that can be used very efficiently in the operating room, under time pressure, with simple graphical user interface.</p>
<p>One openly available clinical application is LumpNav, which intraoperative ultrasound segmentation and resection guidance using tracked ultrasound. It includes needle calibration, so you can just copy-paste the relevant code pieces from there:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerIGT/LumpNav">
  <header class="source">

      <a href="https://github.com/SlicerIGT/LumpNav" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/d44774043d20bb5ebada9d831f8998c8/SlicerIGT/LumpNav" class="thumbnail">

  <h3><a href="https://github.com/SlicerIGT/LumpNav" target="_blank" rel="noopener">GitHub - SlicerIGT/LumpNav: Slicer extension for ultrasound-guided breast...</a></h3>

    <p><span class="github-repo-description">Slicer extension for ultrasound-guided breast tumor resection (lumpectomy)</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
