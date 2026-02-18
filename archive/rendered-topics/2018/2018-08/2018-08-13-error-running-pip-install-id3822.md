# Error running pip install

**Topic ID**: 3822
**Date**: 2018-08-13
**URL**: https://discourse.slicer.org/t/error-running-pip-install/3822

---

## Post #1 by @darekdev (2018-08-13 16:12 UTC)

<p>I have built Slicer and always have working pip but now module is empty and I can’t run pip.main([‘install’, ‘module’])<br>
&gt;&gt;&gt; import pip</p>
<p>&gt;&gt;&gt; pip</p>
<p>&lt;module ‘pip’ from ‘/home/software/medical/slicer4.9/Slicer-SuperBuild-Release/python-install/lib/python2.7/site-packages/pip/<strong>init</strong>.pyc’&gt;</p>
<p>&gt;&gt;&gt; dir(pip)</p>
<p>[‘<strong>builtins</strong>’, ‘<strong>doc</strong>’, ‘<strong>file</strong>’, ‘<strong>name</strong>’, ‘<strong>package</strong>’, ‘<strong>path</strong>’, ‘<strong>version</strong>’]</p>
<p>I can run for exanple</p>
<blockquote>
<p>./Slicer --launch …/python-install/bin/pip install jedi</p>
</blockquote>
<p>but can’t <strong>import distutils</strong>, and can’t run python code from <a href="https://github.com/ihnorton/SlicerJupyter/blob/auto_comp/JupyterKernel/qSlicerJupyterKernelModule.cxx" rel="noopener nofollow ugc">https://github.com/ihnorton/SlicerJupyter/blob/auto_comp/JupyterKernel/qSlicerJupyterKernelModule.cxx</a></p>

---
