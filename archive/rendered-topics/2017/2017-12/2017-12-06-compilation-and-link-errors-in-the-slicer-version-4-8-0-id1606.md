# Compilation and link errors in the Slicer version 4.8.0

**Topic ID**: 1606
**Date**: 2017-12-06
**URL**: https://discourse.slicer.org/t/compilation-and-link-errors-in-the-slicer-version-4-8-0/1606

---

## Post #1 by @carlos-luque (2017-12-06 21:30 UTC)

<p>Operating system: Windows 8.1 64 bits<br>
Slicer version: 4.8.0 (revision 944c364) with Qt 5.9.2<br>
Compiler: visual studio 2015</p>
<p>Hello,</p>
<p>I tried to build Slicer (4.8.0) in debug mode and I faced several issues:</p>
<ul>
<li>
<p>Compilation errors:<br>
** Error	C1083	Cannot open include file: ‘vtkSlicerVersionConfigure.h’: No such file or directory [D:\SLicer480D\Slicer-build\Modules\Loadable\Markups\MRML\vtkSlicerMarkupsModuleMRML.vcxproj]	Slicer	D:\MacBioIDi\Slicer\Slicer\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialStorageNode.cxx	23	<br>
Error	C1083	Cannot open include file: ‘vtkSlicerVersionConfigure.h’: No such file or directory [D:\SLicer480D\Slicer-build\Modules\Loadable\Markups\MRML\vtkSlicerMarkupsModuleMRML.vcxproj]	Slicer	D:\MacBioIDi\Slicer\Slicer\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialStorageNode.cxx	23</p>
</li>
<li>
<p>Link errors:<br>
** There are 138 errors if the ITKWrap is enabled.<br>
Error	LNK1104	cannot open file ‘python27_d.lib’<br>
[D:\SLicer480D\ITKv4-build\Wrapping\Modules\BridgeNumPy\BridgeNumPyPython.vcxproj]	ITKv4	D:\SLicer480D\LINK	1	<br>
[D:\SLicer480D\ITKv4-build\Wrapping\Modules\ITKAnisotropicSmoothingITKAnisotropicSmoothingPython.vcxproj]	<br>
[D:\SLicer480D\ITKv4-build\Wrapping\Modules\ITKAntiAlias\ITKAntiAliasPython.vcxproj]	<br>
…</p>
</li>
<li>
<p>I can run Slicer correctly, but I can install new extensions. The manager warns the following message: “No extensions found for win:64-bit, revision: ‘944c364’. Please try a different combination”</p>
</li>
</ul>
<p>Has anybody faced those issues before?</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2017-12-06 21:54 UTC)

<aside class="quote no-group" data-username="carlos-luque" data-post="1" data-topic="1606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carlos-luque/48/976_2.png" class="avatar"> carlos-luque:</div>
<blockquote>
<p>Error	C1083	Cannot open include file: ‘vtkSlicerVersionConfigure.h’:</p>
</blockquote>
</aside>
<p>Most likely this is not the first error. To find the root cause of the problem, we would need to see the complete build log. Please upload it to somewhere and post here the link. The file should be at a location like this: <code>c:\D\S4D\Testing\Temporary\LastBuild_20171031-1243.log</code></p>
<aside class="quote no-group" data-username="carlos-luque" data-post="1" data-topic="1606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carlos-luque/48/976_2.png" class="avatar"> carlos-luque:</div>
<blockquote>
<p>I can run Slicer correctly, but I can install new extensions. The manager warns the following message: “No extensions found for win:64-bit, revision: ‘944c364’. Please try a different combination”</p>
</blockquote>
</aside>
<p>This is normal. If you build Slicer then you also have to build all the extensions that you need.</p>

---

## Post #3 by @carlos-luque (2017-12-07 00:29 UTC)

<p>Thank Andras for your reply.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="1606" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="carlos-luque" data-post="1" data-topic="1606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carlos-luque/48/976_2.png" class="avatar"> carlos-luque:</div>
<blockquote>
<p>Error	C1083	Cannot open include file: ‘vtkSlicerVersionConfigure.h’:</p>
</blockquote>
</aside>
<p>Most likely this is not the first error. To find the root cause of the problem, we would need to see the complete build log. Please upload it to somewhere and post here the link. The file should be at a location like this: <code>c:\D\S4D\Testing\Temporary\LastBuild_20171031-1243.log</code></p>
</blockquote>
</aside>
<p>I will look for that file.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="1606" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="carlos-luque" data-post="1" data-topic="1606">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carlos-luque/48/976_2.png" class="avatar"> carlos-luque:</div>
<blockquote>
<p>I can run Slicer correctly, but I can install new extensions. The manager warns the following message: “No extensions found for win:64-bit, revision: ‘944c364’. Please try a different combination”</p>
</blockquote>
</aside>
<p>This is normal. If you build Slicer then you also have to build all the extensions that you need.</p>
</blockquote>
</aside>
<p>Ok, I found the link about extension index to search all available extensions</p>

---

## Post #4 by @carlos-luque (2017-12-07 14:50 UTC)

<p>Hello,</p>
<p>I couldn’t find any file with name LastBuild*.log in my system. I found the file Slicer.log where the error is written.</p>
<pre><code class="lang-auto">D:\SLicer480D\Slicer-build\ALL_BUILD.vcxproj" (default target) (1) -&gt;
         "D:\SLicer480D\Slicer-build\Modules\CLI\ExecutionModelTour\ExecutionModelTour.vcxproj" (default target) (65) -&gt;
         "D:\SLicer480D\Slicer-build\Modules\CLI\ExecutionModelTour\ExecutionModelTourLib.vcxproj" (default target) (66) -&gt;
         "D:\SLicer480D\Slicer-build\Modules\Loadable\Markups\MRML\vtkSlicerMarkupsModuleMRML.vcxproj" (default target) (71) -&gt;
         (ClCompile target) -&gt; 
     1&gt;D:\Slicer\Slicer\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsFiducialStorageNode.cxx(23): fatal error C1083: Cannot open include file: 'vtkSlicerVersionConfigure.h': No such file or directory [D:\SLicer480D\Slicer-build\Modules\Loadable\Markups\MRML\vtkSlicerMarkupsModuleMRML.vcxproj]
</code></pre>
<p>The filename <code>vtkSlicerVersionConfigure.h</code> is located in the folder <code>D:\SLicer480D\Slicer-build\vtkSlicerVersionConfigure.h</code></p>
<p>I built the slicer solution in release mode in new location and the error is shown as well.</p>
<p>Thanks in advance</p>

---

## Post #5 by @lassoan (2017-12-07 15:38 UTC)

<p>It must be some very simple, trivial error, but it is difficult to decode from this very little amount of information. Please skype me from the computer where you have this problem (so that you can share your screen) anytime when you have 10 minutes.</p>

---

## Post #6 by @carlos-luque (2017-12-08 12:41 UTC)

<p>Thanks a lot Andras for your time.</p>

---

## Post #7 by @darekdev (2018-03-26 14:21 UTC)

<p>Hi,<br>
I have exactly same error in similar environment. I can run Slicer, but I can’t use vtkMRMLMarkupFiducialNodes etc., because compilation ended with error at this point. What should I do?<br>
Thanks in advance.</p>
<p>Edit 1.<br>
Work!!!<br>
I don’t know if enabled Slicer_USE_SimpleITK(I checked only this) was it but everything was compiled correctly.</p>

---
