---
topic_id: 14279
title: "Slicer Radiomics Error"
date: 2020-10-27
url: https://discourse.slicer.org/t/14279
---

# Slicer Radiomics error 

**Topic ID**: 14279
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/slicer-radiomics-error/14279

---

## Post #1 by @ngillingham (2020-10-27 20:12 UTC)

<p>Hello, I’ve run into the following error with both nightly and stable releases of Slicer, on a Mac. Same error when I tried at work, on Windows, with both nightly and stable release, although I’m not able to poke around the installed software at work as much as I can at home.</p>
<pre><code class="lang-auto">RadiomicsCLI standard error:

Traceback (most recent call last):
  File "/Applications/Slicer 4.11.2 Stable .app/Contents/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/cli-modules/SlicerRadiomicsCLI.py", line 7, in 
    from radiomics.scripts import parse_args
  File "/Applications/Slicer 4.11.2 Stable .app/Contents/Extensions-29402/SlicerRadiomics/lib/python3.6/site-packages/radiomics/__init__.py", line 15, in 
    from . import imageoperations
  File "/Applications/Slicer 4.11.2 Stable .app/Contents/Extensions-29402/SlicerRadiomics/lib/python3.6/site-packages/radiomics/imageoperations.py", line 6, in 
    import pywt
ModuleNotFoundError: No module named 'pywt'
</code></pre>
<p>No improvement after I uninstalled and reinstalled python and pyradiomics (via pip, including all the prerequisites it seems)</p>
<p>I’m not the <em>most</em> tech savvy but I know to find that I have Python 3.8.6 installed.</p>
<p>Thanks for any help,<br>
Nick</p>

---

## Post #2 by @jamesobutler (2020-10-27 20:47 UTC)

<p>This appears to match the reported error that another user reported over at the SlicerRadiomics github repo <a href="https://github.com/Radiomics/SlicerRadiomics/issues/62" rel="noopener nofollow ugc">https://github.com/Radiomics/SlicerRadiomics/issues/62</a></p>
<p>cc: <a class="mention" href="/u/joostjm">@JoostJM</a> <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #3 by @fedorov (2020-10-27 20:52 UTC)

<p>Yes, we discussed this with <a class="mention" href="/u/jcfr">@jcfr</a> today, and if I understood correctly, something has changed on the factory machine about 27 days ago, which broke packaging of the pywt extension. JC was going to change something on the factory to fix this.</p>
<p>In the interim, I was able to make the module work again by manually installing the missing packages from the Slicer python console:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.pip_install('pywavelets')
&gt;&gt;&gt; slicer.util.pip_install('python-dateutil')
</code></pre>

---

## Post #4 by @jcfr (2020-10-28 03:24 UTC)

<p>The issue is that <code>pywavelets</code> is installed in the main Slicer build tree and this prevent the package from being  packaged into the extension.</p>
<p>I manually deleted the package from the <code>site-packages</code> in the build tree associated with the latest stable build.</p>
<p>We will re-assess tomorrow.</p>

---

## Post #5 by @fedorov (2020-11-10 19:47 UTC)

<p>Yesterday I added a fix to check for missing modules and install if they are not present. Please check the latest stable build and let us know if the issue is not resolved.</p>

---
