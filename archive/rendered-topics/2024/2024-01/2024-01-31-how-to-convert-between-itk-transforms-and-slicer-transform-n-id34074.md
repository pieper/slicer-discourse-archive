# How to convert between ITK transforms and Slicer transform nodes?

**Topic ID**: 34074
**Date**: 2024-01-31
**URL**: https://discourse.slicer.org/t/how-to-convert-between-itk-transforms-and-slicer-transform-nodes/34074

---

## Post #1 by @dzenanz (2024-01-31 20:07 UTC)

<p>I am creating a scripted module for ANTs registration (<a href="https://github.com/SlicerMorph/SlicerANTs/tree/wip" rel="noopener nofollow ugc">wip</a>). It is invoking a wrapped <a href="https://github.com/thewtex/ANTsWasm/blob/main/include/itkANTSRegistration.h" rel="noopener nofollow ugc">itk::ANTSRegistration</a>. For Slicer node ↔ ITKImage conversion, I am using <a href="https://github.com/Slicer/Slicer/pull/7094" rel="noopener nofollow ugc">previously added</a> utility functions. But I am not aware of a convenient way to convert between ITK transforms and Slicer transform nodes.</p>
<p>These <a href="https://github.com/Slicer/Slicer/blob/v5.6.1/Libs/MRML/Core/vtkITKTransformConverter.h#L65-L88" rel="noopener nofollow ugc">static methods</a> from <code>vtkITKTransformConverter</code> look interesting. I don’t know how to access them from Python, and whether that is even possible. I assume <code>vtkTransform</code>s would be usable for invoking <a href="https://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#a90e8e50aee3cb6ac67521e5f1ea252dc" rel="noopener nofollow ugc">GetTransformFromNode</a> and <a href="https://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#a5e20fac995080403020e3a06db8b7854" rel="noopener nofollow ugc">SetAndObserveTransformToParent</a> methods of <code>vtkMRMLTransformNode</code>.</p>
<p>My fallback is using <a href="https://github.com/Slicer/Slicer/blob/v5.6.1/Base/Python/slicer/util.py#L1907-L2054" rel="noopener nofollow ugc">existing utility functions</a>, which will almost certainly necessitate more coding.</p>
<p>Are there any suggestions?</p>

---

## Post #2 by @muratmaga (2024-02-06 17:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/simonoxen">@simonoxen</a></p>
<p>Any suggestions?</p>

---

## Post #3 by @lassoan (2024-02-06 18:49 UTC)

<p>You can use <code>transformNode = slicer.util.loadTransform(path)</code> utility function. Internally, it uses transform storage MRML nodes, which use vtkITKTransformConverter functions. Similarly, for loading images, I would recommend to use <code>volumeNode = slicer.util.loadVolume(path)</code>.</p>
<p>Important: There is a quite nice extension for <a href="https://github.com/netstim/SlicerANTs/">ANTs registration in Slicer</a>. It provides command-line interface and Python scripted module interface. It can execute registration in a background process (does not block the application), has comprehensive GUI for adjusting parameters, manages registration parameter sets, etc.</p>
<p>Having two extensions for the exact same purpose would confuse users, divide developers, and double maintenance and support costs. Therefore, in the long term, having two extensions for the same thing is actually worse than just having one. To avoid these issues, please do not create a new extension but consolidate your efforts with development and maintenance of the existing one. There are many ways to achieve this, you could add an option to choose between Elastix backends, improve the existing GUI, add a new frontend if the feature sets are impossible to merge, etc.</p>

---

## Post #4 by @muratmaga (2024-02-06 19:08 UTC)

<p>Thanks Andras. the purpose of this project is to make the whole ANTsX ecosystem available in the Slicer, not just the registration. This includes things like atlas building, jacobian analysis, etc…</p>

---

## Post #5 by @lassoan (2024-02-06 19:27 UTC)

<p>Great, then there should be no overlap (you just save some time by not having to write an entirely new module for registration). Please add the new modules to the existing extension.</p>

---

## Post #6 by @muratmaga (2024-02-06 20:06 UTC)

<p>That will be something JC and Matt McCormick to decide. I believe plan is to actually leverage the antspy package as opposed to re-implement all the functionality.</p>

---

## Post #7 by @lassoan (2024-02-06 20:37 UTC)

<p>It should not matter much for the extension if the ANTs binaries are from wheels or downloaded from PyPI or built locally - changes in the existing extension should be minimal.</p>
<p>By switching to getting ANTs from PyPI, we give up our freedom to choose how ANTs is built (you cannot easily have a debug build to do C++ troubleshooting, you cannot decide if you want VTK support, etc.) and binary compatibility is no longer guaranteed. However, using antspy would make it easier to use ANTs from Python and extension build system would be a bit simpler. Overall, switching to antspy may make sense.</p>
<p>Let’s hear from <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/thewtex">@thewtex</a>, and <a class="mention" href="/u/simonoxen">@simonoxen</a> and make a decision here.</p>

---

## Post #8 by @simonoxen (2024-02-07 09:08 UTC)

<p>Hi, great to hear that there’s interest in integrating more of ANTs into Slicer!</p>
<p>Back then I chose to go with a superbuild because I found it easier to integrate with Slicer build for all OSs; using CLIs in the background; and the capability to modify ANTs more freely.</p>
<p>Currently, the antspy <a href="https://github.com/ANTsX/ANTsPy/blob/master/setup.py" rel="noopener nofollow ugc">setup.py</a> configures ITK and ANTs projects and builds them. I found it easier to handle this directly building ANTs from superbuild.</p>
<p>I currently also <a href="https://github.com/netstim/SlicerANTs/blob/master/SuperBuild/ants_patch.cmake#L61" rel="noopener nofollow ugc">patch ANTs</a> to show progress of the registration from CLI module. I found this very handy for processes that take some considerable time for the user.</p>
<p>Adding more ANTs functionality to this current implementation should be quite easy: <a href="https://github.com/netstim/SlicerANTs/blob/master/SuperBuild/ants_patch.cmake#L3C5-L3C20" rel="noopener nofollow ugc">select which ANTs apps to build</a>, and add them into a CLI. Then calling the CLIs from python is also easy.</p>
<p>However, if there’s interest in having the python wrappers directly from antspy, I could also consider migrating my <a href="https://github.com/netstim/SlicerANTs/tree/master/antsRegistration" rel="noopener nofollow ugc">antsRegistration</a> module, which is mostly UI work allowing the user to test lots of parameters for the registration. With not so development, this would work as well with other ANTs backends.</p>
<p>I wonder, what are the motivations in using antspy?</p>
<p>Considering there probably is more development bandwidth and expertise from this new effort, I’m happy to retire my extension once this one takes over. We could probably still keep the current antsRegistration as some sort of advanced antsRegistration or so.</p>
<p>Thanks!</p>

---

## Post #9 by @thewtex (2024-02-07 16:06 UTC)

<p>Hi,</p>
<p>Yes, we completely agree and have the same goals – we do not want to duplicate efforts and keep ants adoption easy for Slicer users.</p>
<p>We aim to merge the current draft Slicer extension development with <a class="mention" href="/u/simonoxen">@simonoxen</a> 's excellent work. Simon made nice UI development and refinements, we certainly want to keep them when it makes sense. Also extend the functionality, as <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned.</p>
<p>Under the hood, we are working to improve performance, portability, ease of use, maintainability, scalability, interoperability, and debuggability (both from C++ and Python). We are using much of the same code in antspy, contributing improvements to ants along the way, but these improvements mean it is neither exactly ants CLI or antspy. We are keeping the programmatic antspy interface when it makes sense. This interface is something that Nick and Brian worked hard to refine – they did an excellent job – and it is what antspy or antsr users are familiar with. We can modify or refine the graphical interface in Slicer when it makes sense.</p>

---
