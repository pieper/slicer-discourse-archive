---
topic_id: 24709
title: "Slicer In A Python Pipeline But Not In The Slicer Python Int"
date: 2022-08-10
url: https://discourse.slicer.org/t/24709
---

# Slicer in a python pipeline (but not in the slicer python interpretor)

**Topic ID**: 24709
**Date**: 2022-08-10
**URL**: https://discourse.slicer.org/t/slicer-in-a-python-pipeline-but-not-in-the-slicer-python-interpretor/24709

---

## Post #1 by @Jean_Jacquemier (2022-08-10 12:46 UTC)

<p>I would like to use slicer in a python pipeline that will be executed on a large cluster in a batch mode.</p>
<p>I succeed to execute the python code on my laptop:</p>
<ul>
<li>thanks to the Slicer3D JupyterKernel kernel extention.</li>
<li>thanks to a external python env, throw jupyter (after  having executing this command <code>jupyter-kernelspec install "/home/jacquemi/usr/local/Slicer-5.0.2-linux-amd64/NA-MIC/Extensions-30822/SlicerJupyter/share/Slicer-5.0/qt-loadable-modules/JupyterKernel/Slicer-5.0" --replace --user</code>)</li>
</ul>
<p>But I did not succeed to install slicer (using pip or whatever) in an external Python virtualenv without using jupyter. As I need to execute my pipeline into a cluster in batch mode, I cannot use neither Jupyter nor the 3D slicer python interpreter</p>
<p>So is there a way to install slicer Python library in a virtual<br>
venv and to load (and use) it in a simple python session (not a jupyter one) ?</p>
<p>This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html" rel="noopener nofollow ugc">documentation</a> indicates that :   “Python scripting and development of new Slicer modules in Python does not require building the application either”<br>
.</p>

---

## Post #2 by @pieper (2022-08-10 14:01 UTC)

<aside class="quote no-group" data-username="Jean_Jacquemier" data-post="1" data-topic="24709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jean_jacquemier/48/15947_2.png" class="avatar"> Jean_Jacquemier:</div>
<blockquote>
<p>So is there a way to install slicer Python library in a virtual<br>
venv and to load (and use) it in a simple python session (not a jupyter one) ?</p>
</blockquote>
</aside>
<p>No, Slicer needs to use Slicer’s python build for all the dependencies to work.  You should be able to run Slicer from a directory available to your cluster node.  You can use xvfb to get an X session if it’s not available on your node.  This requires some memory (real or virtual) on the node, but this is usually manageable and small compared to a large computing task requirement.</p>
<aside class="quote no-group" data-username="Jean_Jacquemier" data-post="1" data-topic="24709">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jean_jacquemier/48/15947_2.png" class="avatar"> Jean_Jacquemier:</div>
<blockquote>
<p>This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html">documentation</a> indicates that : “Python scripting and development of new Slicer modules in Python does not require building the application either”</p>
</blockquote>
</aside>
<p>That means you can use Slicer’s python to develop Slicer modules, but you still need Slicer itself.</p>
<p>As a future goal we’d like to support installing parts of Slicer as packages for standard python systems but this isn’t possible currently.</p>

---
