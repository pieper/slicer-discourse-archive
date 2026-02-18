# General registration(BRAINS) error"LBFGSB optimizer does not support scaling. All scales are set to one. "

**Topic ID**: 7780
**Date**: 2019-07-27
**URL**: https://discourse.slicer.org/t/general-registration-brains-error-lbfgsb-optimizer-does-not-support-scaling-all-scales-are-set-to-one/7780

---

## Post #1 by @11126 (2019-07-27 13:22 UTC)

<p>I am trying to do general registration according to the tutorial. I have completed the linear transform but when I tried to apply BSpline transform it completed with error:</p>
<p>General Registration (BRAINS) standard error:</p>
<p>WARNING: In D:\D\P\Slicer-0-build\ITK\Modules\Numerics\Optimizersv4\src\itkLBFGSBOptimizerv4.cxx, line 113LBFGSBOptimizerv4 (0000027566CF45A0): LBFGSB optimizer does not support scaling. All scales are set to one.</p>
<p>Exception during registration:</p>
<p>itk::ExceptionObject (000000E4F3BC3BC0)<br>
Location: “unknown”<br>
File: d:\d\p\slicer-0-build\brainstools\brainscommonlib\BRAINSFitHelperTemplate.hxx<br>
Line: 1552<br>
Description: itk::ERROR: Exception caught:<br>
itk::ExceptionObject (000000E4F3BC2C40)<br>
Location: “unknown”<br>
File: D:\D\P\Slicer-0-build\ITK\Modules\Core\Common\src\itkPoolMultiThreader.cxx<br>
Line: 154<br>
Description: itk::ERROR: PoolMultiThreader(0000027566CA90D0): Exception occurred during SingleMethodExecutebad allocation</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6034ae679ff91b72ab0022bef2837a7d54374b11.png" data-download-href="/uploads/short-url/dJ4HMRHSa28agGlTSoN6ooynXUJ.png?dl=1" title="V5%7DC(YC_3154LF%60ALV%40_XCR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6034ae679ff91b72ab0022bef2837a7d54374b11.png" alt="V5%7DC(YC_3154LF%60ALV%40_XCR" data-base62-sha1="dJ4HMRHSa28agGlTSoN6ooynXUJ" width="690" height="212" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">V5%7DC(YC_3154LF%60ALV%40_XCR</span><span class="informations">925×285 8.68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I really don’t know why because I’m doing exactly according to the tutorial. Can anyone help me solve this issue? Thank you in advance!</p>

---

## Post #2 by @pieper (2019-07-28 18:51 UTC)

<p>Hi - I think the scaling issue is just a warning and not the real issue.</p>
<aside class="quote no-group" data-username="11126" data-post="1" data-topic="7780">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/11126/48/4272_2.png" class="avatar"> 11126:</div>
<blockquote>
<p>bad allocation</p>
</blockquote>
</aside>
<p>This almost always means you’ve run out of memory, so maybe try on a bigger machine or allocate more virtual memory.</p>
<p>On the other hand it’s not clear why memory is an issue if there are just two MR volumes.  Maybe best to try with just the <code>Rigid</code>option and see if that works.  If you are still having trouble let us know which tutorial and where - maybe something has changed and it’s broken.</p>

---
