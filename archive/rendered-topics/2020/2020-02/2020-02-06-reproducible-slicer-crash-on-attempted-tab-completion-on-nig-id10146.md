# Reproducible Slicer crash on attempted tab completion, on Nightly 2020-01-08

**Topic ID**: 10146
**Date**: 2020-02-06
**URL**: https://discourse.slicer.org/t/reproducible-slicer-crash-on-attempted-tab-completion-on-nightly-2020-01-08/10146

---

## Post #1 by @mikebind (2020-02-06 23:32 UTC)

<p>Running the following code snippet in the python interactor (or a linked Jupyter notebook) and then typing “interp_f” and hitting the Tab key reproducibly crashes Slicer.</p>
<pre><code>from scipy.interpolate import RegularGridInterpolator
import numpy as np
data_kji = np.ones((10,20,30)) #arrayFromVolume(volNode)
data_ijk = np.transpose(data_kji, axes=(2,1,0)) # reverse dimension order from kji to ijk
iLen,jLen,kLen = data_ijk.shape
iVals = list(range(iLen))
jVals = list(range(jLen))
kVals = list(range(kLen))
interp_from_ijk = RegularGridInterpolator((iVals, jVals, kVals), data_ijk)
</code></pre>
<p>If I don’t use Tab completion, I can use the interpolator just fine, e.g.</p>
<pre><code>interp_from_ijk([[5,5,5]])
</code></pre>
<p>works as expected with no crash.</p>
<p>This crash occurs even after a clean Slicer start.  It also occurs without being linked to a Jupyter kernel.</p>

---

## Post #2 by @lassoan (2020-02-07 15:07 UTC)

<p>Interesting. I cannot reproduce this with latest Slicer Preview Release on Windows - auto-complete for <code>interp_f</code> works without any problem. Maybe you could start with a new Slicer installation, installing Python packages one by one and see which one introduces the crash.</p>

---

## Post #3 by @mikebind (2020-02-12 17:34 UTC)

<p>I’ll try to remember to do this at some point in the future.  At the moment, since there is an easy work-around, I am just going with that.</p>

---

## Post #4 by @mikebind (2020-05-22 23:55 UTC)

<p>I have encountered a problem like this again.  I have a very simple module I am developing (called “AirwayLandmarks”) which has a qt.QTableWidget() as a GUI element.   I had defined a convenience lambda at the Python interactor prompt:</p>
<p><code>w = lambda : slicer.modules.AirwayLandmarksWidget</code></p>
<p>I did this just to save a little typing after reloading the module as I was developing it.  That way instead of typing <code>slicer.modules.AirwayLandmarksWidget</code> I could just type <code>w()</code>.</p>
<p>The QtableWidget is stored in <code>slicer.modules.AirwayLandmarksWidget.fhTable</code>, which I can also access via <code>w().fhTable</code>.  If I try to tab-complete something after this, i.e. something like<br>
<code>&gt;&gt;&gt; w().fhTable.clearS</code><br>
and hit the tab key, the normal autocomplete list appears with appropriate options</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57498c9c0160d93d7d4318d4fdd8461733153f5e.png" data-download-href="/uploads/short-url/csb7lrBMQKiN14lDaign3bUHVyS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57498c9c0160d93d7d4318d4fdd8461733153f5e_2_690x123.png" alt="image" data-base62-sha1="csb7lrBMQKiN14lDaign3bUHVyS" width="690" height="123" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57498c9c0160d93d7d4318d4fdd8461733153f5e_2_690x123.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57498c9c0160d93d7d4318d4fdd8461733153f5e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57498c9c0160d93d7d4318d4fdd8461733153f5e.png 2x" data-dominant-color="F4F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">758×136 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>but if I select any of the options, Slicer crashes.</p>
<p>If I reopen Slicer, reopen the AirwayLandmarks module, and do the same thing without using the lambda, i.e.</p>
<p><code>&gt;&gt;&gt; slicer.modules.AirwayLandmarksWidget.fhTable.clearS</code><br>
and hit the tab key, I get the same options, but selecting one of them does not crash Slicer.</p>
<p>I’m currently running the Nightly 2020-04-07 release, but will probably update to a more recent nightly early next week.</p>

---

## Post #5 by @lassoan (2020-05-23 05:13 UTC)

<p>Thanks for the follow-up. Can you share a minimal example module that reproduces the issue?</p>

---

## Post #6 by @mikebind (2020-05-25 15:28 UTC)

<p>Using the extension wizard, I created a module with the default auto-created code, called AutoCompleteCrash.  To the AutoCompleteCrash.py file I inserted the following 5 lines at line 81:</p>
<blockquote>
<pre><code>table = qt.QTableWidget()
table.setRowCount(5)
table.setColumnCount(3)
self.table = table
parametersFormLayout.addRow(self.table)
</code></pre>
</blockquote>
<p>Then, after reloading the module, at the python interactor <code>slicer.modules.AutoCompleteCrash.table.clearSelection()</code> does not cause a crash, even when tab autocomplete is used partway through typing clearSelection(), but after<br>
<code>w = lambda : slicer.modules.AutoCompleteCrashWidget</code>, then <code>w().table.clearSel</code> followed by pressing the tab key crashes Slicer and the window closes.</p>
<p>Here are the last few lines of the log file of a crashed session:</p>
<blockquote>
<p>[INFO][Stream] 25.05.2020 08:11:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ------------------------------<br>
[INFO][Stream] 25.05.2020 08:11:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Reloading module: AutoCompleteCrash<br>
[INFO][Stream] 25.05.2020 08:11:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ------------------------------<br>
[INFO][Stream] 25.05.2020 08:11:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 25.05.2020 08:11:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 25.05.2020 08:11:25 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[DEBUG][Qt] 25.05.2020 08:11:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Python console user input: slicer.modules.AutoCompleteCrashWidget.table.clearSelection()<br>
[DEBUG][Qt] 25.05.2020 08:12:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Python console user input: w = lambda : slicer.modules.AutoCompleteCrashWidget</p>
</blockquote>
<p>I am running Slicer nightly 2020-04-07 on Windows 10.</p>

---

## Post #7 by @lassoan (2020-05-25 15:58 UTC)

<p>Thank you for the more detailed information, it is very useful. Would you mind sharing your AutoCompleteCrash.py file(upload to <a href="https://gist.github.com/">https://gist.github.com/</a> and copy the link here)?</p>

---

## Post #8 by @mikebind (2020-05-26 15:48 UTC)

<p>Here you go:<br>
</p><aside class="onebox githubgist">
  <header class="source">
      <a href="https://gist.github.com/mikebind/7e9cb1ac13c3cb694cf5d3932008edf9" target="_blank" rel="nofollow noopener">gist.github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/7e9cb1ac13c3cb694cf5d3932008edf9" target="_blank" rel="nofollow noopener">https://gist.github.com/mikebind/7e9cb1ac13c3cb694cf5d3932008edf9</a></h4>
<h5>AutoCompleteCrash.py</h5>
<pre><code class="Python">import os
import unittest
import logging
import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

#
# AutoCompleteCrash
#</code></pre>
This file has been truncated. <a href="https://gist.github.com/mikebind/7e9cb1ac13c3cb694cf5d3932008edf9" target="_blank" rel="nofollow noopener">show original</a>

<p>
</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @mikebind (2020-05-28 23:10 UTC)

<p>I just downloaded and installed the 2020-05-27 preview release, and I cannot reproduce this crash on the new release.  I also can’t use the new release because it appears to not be compatible with extensions I rely on (SlicerJupyter, SegmentEditorExtraEffects, SlicerOpenCV), but at least this issue seems to have been resolved somehow, and I’ll look forward to when I can upgrade.</p>
<p>EDIT:  It turns out the Extension Manager was incorrectly informing me that these extensions were not compatible, after a series of frustrating interactions with the Extension Manager (<a href="https://discourse.slicer.org/t/problematic-behavior-of-the-extension-manager/10986">https://discourse.slicer.org/t/problematic-behavior-of-the-extension-manager/10986</a>), it told me that actually these extensions ARE compatible with the version I just installed, and I was able to install them. I did not restart immediately, and when I reopened the Extension Manager, it again told me that none of the extensions were compatible.  However, when I restarted Slicer, they were all installed, so I think things are good.</p>

---
