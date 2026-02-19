---
topic_id: 16765
title: "Use Julia With Slicer"
date: 2021-03-25
url: https://discourse.slicer.org/t/16765
---

# Use Julia with Slicer

**Topic ID**: 16765
**Date**: 2021-03-25
**URL**: https://discourse.slicer.org/t/use-julia-with-slicer/16765

---

## Post #1 by @keri (2021-03-25 19:27 UTC)

<p>Hi,</p>
<p>When building SlicerCAT I’m thinking about installing Julia (+miniconda) instead of Slicer’s Python while keeping Slicer+Python tight interaction.<br>
If someone has any thoughts please give an advice.</p>

---

## Post #2 by @lassoan (2021-04-14 06:05 UTC)

<p>I don’t think anybody has tried to interface Slicer with Julia. We are pretty happy with the vast amount of packages available for Python and we can implement all performance-critical code in C++.</p>
<p>A couple of years ago we tried to <a href="https://www.slicer.org/wiki/Documentation/Labs/SlicerCondaIntegration">build Slicer against miniconda Python libraries and it seemed to work</a>, but since we can use <code>pip</code> in Slicer now, there is not much motivation in trying to use conda.</p>

---

## Post #3 by @keri (2021-04-28 00:17 UTC)

<p>I decided not to use miniconda so far but I’m going to use Julia.</p>
<p>To install Julia I’m going to use <a href="https://julialang.org/downloads/platform/#cross-platform_installer" rel="noopener nofollow ugc">crossplatform</a> python module <a href="https://github.com/johnnychen94/jill.py" rel="noopener nofollow ugc">Jill.py</a>. It will install Julia in some dir inside build tree like <code>C:/C/d/julia-1.6</code>. Then I need to add Julia to CPack to make installation available for usual user. I can see that Slicer handles CPack modules via <code>SlicerBlockInstallMyLib.cmake</code> and <code>SlicerExtensionCPack.cmake</code> but there is quite a lot of code and for now I can’t understand how can I apply the same Slicer CPackaging style to Julia (maybe because it is time to go to sleep).</p>
<p>But anyway, if somebody has instruction please give me an advice.</p>

---

## Post #4 by @lassoan (2021-05-01 14:20 UTC)

<p>You actually already have several options to run Julia scripts directly from Slicer as CLI modules.</p>
<p>You can implement CLI modules in any language. For now, you need to create an executable (sh, bat, py, exe,…) launcher the starts your script with Julia. But with a small change in Slicer core, you could implement direct Julia launching capability the same way as Python CLIs. See example here:</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/lassoan/SlicerPythonCLIExample" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/f3f03579607f871fabb51fff4ad1f4d3c6e8d8c8d64d031ae2011bfb22cffccc/lassoan/SlicerPythonCLIExample" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/lassoan/SlicerPythonCLIExample" target="_blank" rel="noopener">lassoan/SlicerPythonCLIExample</a></h3>


  <p><span class="label1">Example extension for 3D Slicer that demonstrates how to make a Python script available as a CLI module</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If Julia.exe startup time is too slow then you can do the same that we did for Matlab. We implemented a  very simple TCP server in Matlab that receives commands from Slicer executes them, and sends back to result to Slicer. See details here:</p>
<aside class="onebox githubfolder">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/PerkLab/SlicerMatlabBridge" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <img src="https://opengraph.githubassets.com/dde5311bd8c3d7aecaf60e83d811cd2112d17e5f87dc93d80b81fcd779e0e33e/PerkLab/SlicerMatlabBridge" class="thumbnail onebox-full-image" width="60" height="60">

<h3><a href="https://github.com/PerkLab/SlicerMatlabBridge" target="_blank" rel="noopener">PerkLab/SlicerMatlabBridge</a></h3>


  <p><span class="label1">MatlabBridge extension for 3D Slicer. Contribute to PerkLab/SlicerMatlabBridge development by creating an account on GitHub.</span></p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Slicer also supports the Jupyter kernel protocol, so you can access Slicer features via this interface.</p>
<p>If you want to run Julia inside the Slicer process then it should be possible, too, but much more complicated. Python can be either extended (you load your libraries into Python and let Python execute it) or Python can be embedded (your application instantiates and manages a Python interpreter). We embed Python into Slicer so that we have better control over the application and to keep Python an optional component. Probably the simplest way to integrate Julia in the Slicer application is to embed Julia - if it has this option. You may be able to extend Julia with Slicer, this is how TCL integration worked years ago. For a few years, Slicer extended TCL and embedded Python. You can go back in the version history of Slicer and see how it was implemented.</p>

---

## Post #5 by @keri (2021-05-02 11:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you very much for consulting me.<br>
Even I’m not an experienced Julia user I can see that Julia has tight integration with python. Julia can call python via <a href="https://github.com/JuliaPy/PyCall.jl" rel="noopener nofollow ugc">PyCall</a> and python is able to call Julia via <a href="https://github.com/JuliaPy/pyjulia" rel="noopener nofollow ugc">PyJulia</a>. So for now I mostly rely on this python-julia communication. I think the problem will arise when I start integrating Julia scripts and I will comeback to this thread.</p>

---

## Post #6 by @keri (2022-07-11 20:22 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="24260">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"><a href="https://discourse.slicer.org/t/sys-executable-is-different-when-running-from-slicer-and-from-pythonslicer/24260/5">`sys.executable` is different when running from Slicer and from PythonSlicer</a></div>
<blockquote>
<p>In the case of the Slicer application, you should instead considering using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file" rel="noopener nofollow ugc">Application Startup File</a></p>
</blockquote>
</aside>
<p>Didn’t know about this file, thank you.</p>
<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="24260">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"><a href="https://discourse.slicer.org/t/sys-executable-is-different-when-running-from-slicer-and-from-pythonslicer/24260/5">`sys.executable` is different when running from Slicer and from PythonSlicer</a></div>
<blockquote>
<p>To provide a more targeted answer, could you provide more details ? What are you trying to achieve ?</p>
</blockquote>
</aside>
<p>It seems this is not an issue anymore but here is why started this topic:</p>
<p>I bundle julia programming language along with SlicerCAT and I wasn’t able to build a package (<a href="https://github.com/JuliaPy/pyjulia" rel="noopener nofollow ugc">pyjulia</a>) because its dependency (<a href="https://github.com/JuliaPy/PyCall.jl" rel="noopener nofollow ugc">PyCall</a>) used to be built against <code>python.exe</code> while pyjulia determined that it is invoked from <code>PythonSlicer.exe</code> (pyjulia used to raise an exception about this).</p>
<p>But as I figured out later the problem was within Slicer build tree python library is copied to <code>Slicer-build</code> and the inconsistency was invoked by that: PyCall links to <code>python-install/bin/python39.dll</code> and pyjulia links to <code>Slicer-build/bin/python39.dll</code>.</p>
<p>This is not an issue when SlicerCAT is installed (tested).</p>

---

## Post #7 by @jcfr (2022-07-11 20:29 UTC)

<blockquote>
<p>PyCall links to <code>python-install/bin/python39.dll</code> and pyjulia links to <code>Slicer-build/bin/python39.dll</code>.</p>
</blockquote>
<p>Technically, the linking is done at build-time against <code>python-install/libs/python39.lib</code>.</p>
<p>If you share a link to your custom application, we should be able to provide hints on how to set the launcher settings to ensure the proper dynamic libraries are resolved (by for example setting relevant launcher settings).</p>

---

## Post #8 by @keri (2022-07-11 20:45 UTC)

<p>I created CTK launcher around julia programming lang and I have set there env variables to resolve mentionned issue.</p>
<p>P.S. yesterday I made the repo private as I’m not sure about the future of the project. It is an enthusiastic project but I spend too much time on this without any interest in the sense of sponsorship so far.</p>

---
