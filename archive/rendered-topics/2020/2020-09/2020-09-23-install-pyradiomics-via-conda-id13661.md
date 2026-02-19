---
topic_id: 13661
title: "Install Pyradiomics Via Conda"
date: 2020-09-23
url: https://discourse.slicer.org/t/13661
---

# install pyradiomics via conda

**Topic ID**: 13661
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/install-pyradiomics-via-conda/13661

---

## Post #1 by @YinYunchao (2020-09-23 13:36 UTC)

<p>Hi there,</p>
<p>I was trying to install pyradiomics by the command line ‘conda install -c radiomics pyradiomics’. However, it reported:</p>
<ul>
<li>pyradiomics -&gt; python[version=’&gt;=2.7,&lt;2.8.0a0|&gt;=3.7,&lt;3.8.0a0|&gt;=3.6,&lt;3.7.0a0|&gt;=3.5,&lt;3.6.0a0|&gt;=3.4,&lt;3.5.0a0’]</li>
</ul>
<p>Your python: python=3.8</p>
<p>Then I create another env with python =3.7, it reported <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:">Specifications:</p>
<ul>
<li>pyradiomics -&gt; python[version=’&gt;=3.8,&lt;3.9.0a0’]</li>
</ul>
<p>Your python: python=3.7</p>
<p>Besides, it also reported that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:">The following specifications were found to be incompatible with your CUDA driver:</p>
<ul>
<li>feature:/win-64::__cuda==10.2=0</li>
<li>feature:|@/win-64::__cuda==10.2=0</li>
</ul>
<p>Your installed CUDA driver is: 10.2</p>
<p>I also tried python3.5 but it reported same error as 3.7. Does anyone know which python version do I need?</p>
<p>For the error about cuda version, I didn’t read on the intro of pyradiomics required specific cuda version, is that related to the failure of instllment as well? Thanks for helping!!</p>

---

## Post #2 by @JoostJM (2020-09-30 11:34 UTC)

<p>Currently, conda installation of PyRadiomics is providing errors. See also <a href="https://github.com/Radiomics/pyradiomics/issues/608">this issue</a> and <a href="https://github.com/Radiomics/pyradiomics/issues/627">this issue</a> on the PyRadiomics github. For Python 3.7, there are also distributed wheels available (i.e. <code>pip install pyradiomics</code>). Finally, PyRadiomics is installed as part of the SlicerRadiomics installation, therefore there would be no need to install it in the slicer environment.</p>
<p>Questions/issues regarding the standalone version of PyRadiomics are also handled on the github issue tracker of the PyRadiomics repository.</p>

---
