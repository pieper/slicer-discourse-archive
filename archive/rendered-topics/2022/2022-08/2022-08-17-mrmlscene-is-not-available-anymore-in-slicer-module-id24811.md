# mrmlScene is not available anymore in slicer module

**Topic ID**: 24811
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/mrmlscene-is-not-available-anymore-in-slicer-module/24811

---

## Post #1 by @spichardo (2022-08-17 16:59 UTC)

<p>Hi,</p>
<p>I updated my Slicer installation to 5.0.3 and my scripts stopped working because the attribute mrmlScene is not available in the slice module. I tried to reinstall slicer 5.3.0, install the pre-release 5.10 version, with no luck. This is a minimal code as an example that I tried in a Jupyter session (jupyter server initiated in slicer)</p>
<pre><code class="lang-python">import slicer, vtk
#clear scene
slicer.mrmlScene.Clear(False)
</code></pre>
<p><em>AttributeError: module ‘slicer’ has no attribute ‘mrmlScene’</em></p>
<p>So what am I missing? Was there a change in the organization of the slicer module? I couldn’t find updated examples that could suggest a change in the module</p>
<p>EDIT: btw, trying to <code>import JupyterNotebooksLib as slicernb</code> crashes the jupyter kernel. So not sure truly how things got broken. Even reinstalling slicer is not fixing the issue.</p>

---

## Post #2 by @spichardo (2022-08-17 17:50 UTC)

<p>Answering to myself…  it seemed I had some weird settings in my $HOME/.jupyter directory , after deleting all there and being sure the right kernel was selected all started to work again .New versions of jupyter lab show the choice of kernels from several python installations, even if initiated from isolated python environments. This choice of python kernels can cause more problems like these.</p>

---
