# SlicerTMS extension does not work in Slicer-5.4 on macOS

**Topic ID**: 31763
**Date**: 2023-09-17
**URL**: https://discourse.slicer.org/t/slicertms-extension-does-not-work-in-slicer-5-4-on-macos/31763

---

## Post #1 by @lopezchau (2023-09-17 23:22 UTC)

<p>Dear community and developers</p>
<p>Does this solution applies to this neuronavigation and electric field simulator third party extension?</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lorifranke/SlicerTMS">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lorifranke/SlicerTMS" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/316839d57a704015531381c8863f5c95e4be0b99d8b9b867d6ec72c4e0623ef7/lorifranke/SlicerTMS" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lorifranke/SlicerTMS" target="_blank" rel="noopener nofollow ugc">GitHub - lorifranke/SlicerTMS: Extension in 3DSlicer for visualization of TMS</a></h3>

  <p>Extension in 3DSlicer for visualization of TMS. Contribute to lorifranke/SlicerTMS development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I managed to make it work with version 5.2.2 but with 5.4 the module is recognized but not actually loaded. And I get this is the error log when I run the test with version 5.4</p>
<p>(Sorry if this is a very basic question. Totally new here. I am not a developer but a physician interested in navigated guided transcranial magnetic stimulation.)</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer 5.4.app/Contents/bin/Python/slicer/ScriptedLoadableModule.py”, line 79, in runTest<br>
TestCaseClass = getattr(module, className)<br>
AttributeError: module ‘SlicerTMS’ has no attribute ‘SlicerTMSTest’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer 5.4.app/Contents/bin/Python/slicer/util.py”, line 3146, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer 5.4.app/Contents/bin/Python/slicer/ScriptedLoadableModule.py”, line 259, in onTest<br>
test(msec=int(slicer.app.userSettings().value(“Developer/SelfTestDisplayMessageDelay”)), **kwargs)<br>
File “/Applications/Slicer 5.4.app/Contents/bin/Python/slicer/ScriptedLoadableModule.py”, line 82, in runTest<br>
raise AssertionError(f’Test case class not found: {self.<strong>module</strong>}.{className} ')<br>
AssertionError: Test case class not found: SlicerTMS.SlicerTMSTest</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aab8002ca49107c52d210851cc4b47710832a00b.jpeg" data-download-href="/uploads/short-url/omfo9GNJPyRorUdnMt1YReNCXEf.jpeg?dl=1" title="Captura de Pantalla 2023-09-17 a la(s) 18.14.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aab8002ca49107c52d210851cc4b47710832a00b_2_690x424.jpeg" alt="Captura de Pantalla 2023-09-17 a la(s) 18.14.55" data-base62-sha1="omfo9GNJPyRorUdnMt1YReNCXEf" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aab8002ca49107c52d210851cc4b47710832a00b_2_690x424.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aab8002ca49107c52d210851cc4b47710832a00b_2_1035x636.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aab8002ca49107c52d210851cc4b47710832a00b_2_1380x848.jpeg 2x" data-dominant-color="383D6A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2023-09-17 a la(s) 18.14.55</span><span class="informations">1920×1182 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
