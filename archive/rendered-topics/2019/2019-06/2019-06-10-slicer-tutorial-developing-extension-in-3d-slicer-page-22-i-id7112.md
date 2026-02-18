# Slicer Tutorial/Developing extension in 3D slicer/page 22,I can't understand a sentence.

**Topic ID**: 7112
**Date**: 2019-06-10
**URL**: https://discourse.slicer.org/t/slicer-tutorial-developing-extension-in-3d-slicer-page-22-i-cant-understand-a-sentence/7112

---

## Post #1 by @zhaobingshuai (2019-06-10 14:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e454bb40725fedaaf6fa0d01bfa9dd014ae922dd.png" data-download-href="/uploads/short-url/wzUoLUExZ0jOdi3fpm79JiZXZ1P.png?dl=1" title="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190610223424" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e454bb40725fedaaf6fa0d01bfa9dd014ae922dd_2_670x500.png" alt="%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190610223424" data-base62-sha1="wzUoLUExZ0jOdi3fpm79JiZXZ1P" width="670" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e454bb40725fedaaf6fa0d01bfa9dd014ae922dd_2_670x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e454bb40725fedaaf6fa0d01bfa9dd014ae922dd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e454bb40725fedaaf6fa0d01bfa9dd014ae922dd.png 2x" data-dominant-color="DBD7D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20190610223424</span><span class="informations">701×523 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As indicated in the figure：plots are supported by the Quantitative layout charts，What should I do to get this chart? Is there any extension?<br>
thanks you !</p>

---

## Post #2 by @lassoan (2019-06-10 15:04 UTC)

<p>There are many Slicer tutorials - which one is this exactly (can you provide a link)? What would you like to achieve?</p>
<p>Time/intensity plots can be displayed using Multi-volume explorer module (bundled with Slicer). Since it seems that you are following a tutorial on quantitative reporting, you may need to install Quantitative Reporting extension to access some demonstrated features.</p>
<p>“Charts” are replaced by “Plots” in Slicer. See more information on plots here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a></p>

---

## Post #3 by @zhaobingshuai (2019-06-10 15:31 UTC)

<p>This is a link to the tutorial，page22<br>
<aside class="onebox googledocs">
  <header class="source">
      <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide%3Did.g420896289_0270" target="_blank" rel="nofollow noopener">docs.google.com</a>
  </header>
  <article class="onebox-body">
    <a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide%3Did.g420896289_0270" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-slides-logo"></span></a>

<h3><a href="https://docs.google.com/presentation/d/1JXIfs0rAM7DwZAho57Jqz14MRn2BIMrjB17Uj_7Yztc/edit#slide%3Did.g420896289_0270" target="_blank" rel="nofollow noopener">Developing extension in 3D Slicer</a></h3>

<p>Developing and contributing extensions for 3D Slicer Andrey Fedorov, PhD, Brigham and Women’s Hospital/Harvard Medical School Jean-Christophe Fillion-Robin, Kitware Inc. Steve Pieper, PhD, Isomics Inc. fedorov@bwh.harvard.edu First presented: Nov 18,...</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
I follow the ppt guide step by step, but I don’t know how to get this plot when I use the Slicer ruler to spend a line in the brain image.Can you give me some detailed steps?<br>
thanks Prof.Lasso!</p>

---

## Post #5 by @zhaobingshuai (2019-06-10 16:36 UTC)

<p>Sorry to bother you, I have solved this problem，<a href="https://github.com/fedorov/MyFirst3DSlicerExtensionTutorial" rel="nofollow noopener">https://github.com/fedorov/MyFirst3DSlicerExtensionTutorial</a><br>
When I clicked on the Apply button of the LineIntensityProfile extension, I didn’t get the above plots because I used the first Part1snapshot. When I switched to Part1snapshot4, I got the results I wanted.<br>
Thank you very much for your help.</p>

---
