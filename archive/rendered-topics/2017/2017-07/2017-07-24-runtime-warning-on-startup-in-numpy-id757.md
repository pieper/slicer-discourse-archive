# Runtime warning on startup in numpy

**Topic ID**: 757
**Date**: 2017-07-24
**URL**: https://discourse.slicer.org/t/runtime-warning-on-startup-in-numpy/757

---

## Post #1 by @fedorov (2017-07-24 15:16 UTC)

<p>I am getting this warning on startup:</p>
<pre><code class="lang-auto">/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/core/getlimits.py:82: 
RuntimeWarning: invalid value encountered in power
  self.resolution = float_to_float(float_conv(10) ** (-self.precision))
</code></pre>
<p>Probably related to <a href="https://github.com/Slicer/Slicer/pull/746">https://github.com/Slicer/Slicer/pull/746</a>?</p>

---

## Post #2 by @jcfr (2017-07-24 15:29 UTC)

<p>Most likely.</p>
<p>By any chance, do you happen to have a complete stack trace ?</p>

---

## Post #3 by @fedorov (2017-07-24 15:32 UTC)

<p>That message is all I get on the console. It is a warning, not error, so there is no stack trace.</p>
<p>Here it is in context:</p>
<pre><code class="lang-auto">Number of registered modules: 146
/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/core/getlimits.py:82: RuntimeWarning: invalid value encountered in power
  self.resolution = float_to_float(float_conv(10) ** (-self.precision))
Number of instantiated modules: 146
</code></pre>

---

## Post #4 by @lassoan (2017-07-24 16:09 UTC)

<p>Is there a file&amp;line number in the application log?</p>

---

## Post #5 by @fedorov (2017-07-24 16:20 UTC)

<p>Yes, I included it:</p>
<p><code>/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/core/getlimits.py:82</code></p>

---

## Post #6 by @lassoan (2017-07-24 16:30 UTC)

<p>Is there a call stack to see where the problem originates from? If not, then you could add <code>raise Exception()</code> before the referenced line in <code>getlimits.py</code> to raise an exception and get a call stack.</p>

---

## Post #7 by @fedorov (2017-07-24 16:45 UTC)

<p>After adding <code>raise Exception()</code>, here is the stack trace. The warning is triggered on <code>import numpy</code></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Slicer-4.7/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 1, in &lt;module&gt;
    import numpy
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/__init__.py", line 142, in &lt;module&gt;
    from . import add_newdocs
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/add_newdocs.py", line 13, in &lt;module&gt;
    from numpy.lib import add_newdoc
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/lib/__init__.py", line 8, in &lt;module&gt;
    from .type_check import *
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/lib/type_check.py", line 11, in &lt;module&gt;
    import numpy.core.numeric as _nx
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/core/__init__.py", line 51, in &lt;module&gt;
    from . import getlimits
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/core/getlimits.py", line 126, in &lt;module&gt;
    tiny=_f16(2 ** -14))
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/site-packages/numpy-1.13.1-py2.7-macosx-10.6-x86_64.egg/numpy/core/getlimits.py", line 82, in __init__
    raise Exception()
Exception
</code></pre>

---

## Post #8 by @lassoan (2017-07-24 17:25 UTC)

<p>Thank you. There is nothing particularly suspicious in this call stack. Maybe instead of throwing an exception, you could print the call stack and let the execution continue:</p>
<pre><code>import traceback
traceback.print_stack()
</code></pre>
<p>This way we could see which call stack corresponds to the warning message (there may be several calls without warnings but after one of them the warning message will be printed as well).</p>
<p>We could also print some variables, such as <code>self.eps</code> and <code>self.precision</code>.</p>
<p>Do you have this warning by simply installing the latest nightly version of Slicer, without installing any extensions? There is no such warning on Windows.</p>

---

## Post #9 by @fedorov (2017-07-24 18:13 UTC)

<p>Andras, I get this warning with the latest nightly on mac.</p>
<p><a class="mention" href="/u/msmolens">@msmolens</a> <a class="mention" href="/u/jcfr">@jcfr</a> if you can’t reproduce this issue on mac with a nightly after <a href="https://github.com/Slicer/Slicer/pull/746">https://github.com/Slicer/Slicer/pull/746</a> let me know, and I will investigate later as suggested by <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #10 by @pieper (2017-07-24 19:33 UTC)

<p>FWIW I don’t get this error on my mac local build after upgrading to numpy 1.13.1.  (Note: to test new numpy you need to delete it from site-package before rebuilding).</p>

---

## Post #11 by @fedorov (2017-07-24 20:01 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I get this warning while launching a nightly binary.</p>

---

## Post #12 by @jcfr (2017-07-25 03:38 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> What is you version of macOS ?</p>

---

## Post #13 by @Fernando (2017-07-25 08:19 UTC)

<p>I have the same on macOS Sierra 10.12.5</p>

---

## Post #14 by @fedorov (2017-07-25 13:28 UTC)

<p>I also had the warning on Sierra 10.12.5</p>

---

## Post #15 by @leochan2009 (2017-08-10 18:25 UTC)

<p>I have the same issue on El captian 10.11.4</p>

---

## Post #16 by @fedorov (2017-08-15 13:41 UTC)

<p>I just noticed that the same warning shows up in the extension builds, but it is treated as an error:</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1079946" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1079946</a></p>

---

## Post #17 by @fedorov (2017-08-22 21:15 UTC)

<p>I logged an issue about this <a href="https://issues.slicer.org/view.php?id=4419">https://issues.slicer.org/view.php?id=4419</a></p>

---

## Post #18 by @jcfr (2017-08-22 21:34 UTC)

<p>Hi,</p>
<p>We will be addressing these shortly.</p>
<p>Thanks<br>
Jc</p>

---

## Post #19 by @jcfr (2017-09-04 21:01 UTC)

<p>This should be addressed by the following PR.</p>
<p>If there are no objections, I will integrate later tonight.</p>
<p>Note: Developer may have to delete <code>NUMPY-*</code> directories before re-configuring.</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/786" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/786" target="_blank">display loaded VolumeProperty files as presets in VolumeRendering module</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:58" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:58" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #20 by @jcfr (2017-09-05 04:24 UTC)

<p>Fixes integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26337">r26337</a> and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26338">r26338</a></p>
<p>Note that the fix consist in temporarily disabling the warnings.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/numpy-03-core-getlimits-ignore-warnings.patch" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/numpy-03-core-getlimits-ignore-warnings.patch" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/SuperBuild/numpy-03-core-getlimits-ignore-warnings.patch</a></h4>
<pre><code class="lang-patch">--- numpy-1.13.1/numpy/core/getlimits.py	2017-07-01 09:18:08.000000000 -0400
+++ NUMPY/numpy/core/getlimits.py	2017-09-04 16:12:45.169686811 -0400
@@ -167,7 +167,9 @@
 # Ignore runtime error when this is not f128
 with numeric.errstate(all='ignore'):
     _huge_f128 = (_ld(1) - _epsneg_f128) / _tiny_f128 * _ld(4)
-_float128_ma = MachArLike(_ld,
+with warnings.catch_warnings():
+    warnings.simplefilter("ignore")
+    _float128_ma = MachArLike(_ld,
                          machep=-112,
                          negep=-113,
                          minexp=-16382,
</code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #21 by @fedorov (2017-09-05 14:14 UTC)

<p>Thank you JC - I confirm the extension now builds without errors on the dashboard.</p>

---
