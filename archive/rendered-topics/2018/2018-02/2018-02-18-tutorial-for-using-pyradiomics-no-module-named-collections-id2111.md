---
topic_id: 2111
title: "Tutorial For Using Pyradiomics No Module Named Collections"
date: 2018-02-18
url: https://discourse.slicer.org/t/2111
---

# Tutorial for using pyradiomics, no module named _collections

**Topic ID**: 2111
**Date**: 2018-02-18
**URL**: https://discourse.slicer.org/t/tutorial-for-using-pyradiomics-no-module-named-collections/2111

---

## Post #1 by @gmadevs (2018-02-18 17:49 UTC)

<p>Hi to all, is there any tutorial available for using the extension pyradiomics which covers all the steps since segmentation to the analysis? I’m having trouble obtaining the results. Thank you</p>
<p>I’m using the latest stable version on mac</p>
<p>This is the error I get</p>
<pre><code class="lang-auto">RadiomicsCLI standard error:

Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-26813/SlicerRadiomics/lib/Slicer-4.8/cli-modules/SlicerRadiomicsCLIScript", line 6, in &lt;module&gt;
    from radiomics.scripts import commandline
  File "/Applications/Slicer.app/Contents/Extensions-26813/SlicerRadiomics/lib/python2.7/site-packages/radiomics/__init__.py", line 4, in &lt;module&gt;
    import collections  # noqa: F401
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/collections.py", line 20, in &lt;module&gt;
    from _collections import deque, defaultdict
ImportError: No module named _collections



RadiomicsCLI completed with errors
</code></pre>

---

## Post #2 by @JoostJM (2018-02-19 09:27 UTC)

<p>This appears to be an issue with the installation of PyRadiomics in Slicer, it is missing the package “collections”, which is normally a built-in package. Therefore, it is not checked for its presence during installation.<br>
Which version of Slicer do you use?<br>
If you’re using the nightly build, it may be a good idea to also try the stable build.</p>
<p>As to tutorials, documentation, etc on PyRadiomics, here are some useful resources:</p>
<p>PyRadiomics documentation: <a href="http://pyradiomics.readthedocs.io" rel="nofollow noopener">pyradiomics.readthedocs.io</a><br>
PyRadiomics source code &amp; examples: <a href="http://github.com/Radiomics/PyRadiomics" rel="nofollow noopener">github.com/Radiomics/PyRadiomics</a><br>
SlicerRadiomics source code: <a href="http://github.com/Radiomics/SlicerRadiomics" rel="nofollow noopener">github.com/Radiomics/SlicerRadiomics</a><br>
Radiomics start page featuring these packages: <a href="http://radiomics.io" rel="nofollow noopener">radiomics.io</a></p>
<p>Kind regards,</p>
<p>Joost</p>

---

## Post #3 by @gmadevs (2018-02-19 09:43 UTC)

<p>Thanks for the reply. I’m using the latest stable for Mac since in the nightly build pyradiomics is not available. Do I have to reinstall pyradiomics via python or in the extension manager?</p>

---

## Post #4 by @JoostJM (2018-02-19 11:55 UTC)

<p>Reinstalling the extension won’t help in this case, as it does not check for the presence of the built-in modules.<br>
I’m not sure if it works, but you could try to pip install the package.</p>
<pre><code class="lang-auto">import pip
pip.main(['install', 'collections'])
</code></pre>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, do you have additional suggestions?</p>
<p>Regards,</p>
<p>Joost</p>

---

## Post #5 by @lassoan (2018-02-19 12:56 UTC)

<p>Collections can be imported without problem in both Slicer 4.8.1 and nightly versions on Windows.</p>
<p>Could you try what happens if you start Slicer and enter <code>import collections</code> in the Python console?</p>

---

## Post #6 by @ihnorton (2018-02-19 15:59 UTC)

<p>I can reproduce this in Slicer 4.8.1. <code>import collections</code> works fine at the Slicer python prompt, but fails from RadiomicsCLI. From <code>vmmap</code>, it looks like the script wrapper ends up pulling in system libpython, and confirmed by changing the wrapper call to <code>DYLD_PRINT_LIBRARIES=1 $python_interpreter "$0Script" $*</code> in SlicerRadiomicsCLI:</p>
<pre><code class="lang-auto">RadiomicsCLI standard error:

dyld: loaded: /opt/worksw/Slicer-4.8.1.app/Contents/bin/python-real
dyld: loaded: /usr/lib/libpython2.7.dylib
...
</code></pre>
<p>Presumably there is an ABI conflict. Somebody will need to dig through the (PYTHON)PATH and figure out why (I didn’t check nightly).</p>

---

## Post #7 by @ihnorton (2018-02-19 16:16 UTC)

<p>Actually, I think I see the problem. Slicer python has DYLD_LIBRARY_PATH set by the launcher:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; os.environ["DYLD_LIBRARY_PATH"]
'/opt/worksw/Slicer-4.8.1.app/Contents/Extensions-26813/SlicerRadiomics/bin:/opt/worksw/Slicer-4.8.1.app/Contents/Extensions-26813/SlicerRadiomics/lib/Slicer-4.8:/opt/worksw/Slicer-4.8.1.app/Contents/Extensions-26813/SlicerRadiomics/lib/Slicer-4.8/cli-modules:/opt/worksw/Slicer-4.8.1.app/Contents/Extensions-26813/SlicerRadiomics/lib/Slicer-4.8:/opt/worksw/Slicer-4.8.1.app/Contents/bin:/opt/worksw/Slicer-4.8.1.app/Contents/lib/Slicer-4.8:/opt/worksw/Slicer-4.8.1.app/Contents/lib/Slicer-4.8/cli-modules:/opt/worksw/Slicer-4.8.1.app/Contents/lib/Slicer-4.8/qt-loadable-modules:../lib/Slicer-4.8/qt-loadable-modules:/opt/worksw/Slicer-4.8.1.app/Contents/lib/TclTk/lib:/opt/worksw/Slicer-4.8.1.app/Contents/lib/Python/lib:/opt/worksw/Slicer-4.8.1.app/Contents/lib/Python/lib/python2.7/site-packages/numpy/core:/opt/worksw/Slicer-4.8.1.app/Contents/lib/Python/lib/python2.7/site-packages/numpy/lib:/opt/worksw/Slicer-4.8.1.app/Contents/lib/TclTk/lib/itcl4.0.1'
</code></pre>
<p>But the wrapper script subshell does not inherit this setting because of <a href="https://forums.developer.apple.com/message/31148">Apple SIP policy</a>.  Adding <code>echo "DYLD: $DYLD_LIBRARY_PATH"</code> in <code>cli-modules/SlicerRadiomicsCLI</code> gives an empty result (<code>DYLD:</code>).</p>

---

## Post #8 by @JoostJM (2018-02-19 17:02 UTC)

<p>This topic is related to issue <a href="https://github.com/Radiomics/SlicerRadiomics/issues/43" rel="nofollow noopener">#43</a> on the SlicerRadiomics’ github.</p>

---
