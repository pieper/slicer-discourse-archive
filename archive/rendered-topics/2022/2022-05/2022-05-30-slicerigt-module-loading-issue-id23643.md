# SlicerIGT module loading issue

**Topic ID**: 23643
**Date**: 2022-05-30
**URL**: https://discourse.slicer.org/t/slicerigt-module-loading-issue/23643

---

## Post #1 by @cpinter (2022-05-30 14:52 UTC)

<p>I’m trying to use the latest SlicerIGT, which now requires SlicerIGSIO. I use the latest of this as well.</p>
<p>I have Slicer built in release mode, from May 5 (<a href="https://github.com/Slicer/Slicer/commit/9f108c3ffe3a7f3f466204ae6a4eee715f67f0b0">this hash</a>).</p>
<p>I built SlicerIGSIO and SlicerIGT with the default CMake options, except adding the SlicerIGSIO inner folder to SlicerIGT for the dependency. When I start Slicer with the proper folders added (qt-loadable-module/Release and the SlicerIGSIO bin folder, plus the one that has the x64 vp9 dll), I get the following errors:</p>
<pre><code class="lang-auto">DLL load failed while importing vtkSlicerLandmarkDetectionModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPivotCalibrationModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerVolumeReconstructionModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerVolumeReconstructionModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerSequenceIOModuleLogicPython: The specified module could not be found.
Failed to load vtkSlicerVideoUtilModuleLogicPython: No module named vtkSlicerSequenceIOModuleMRMLPython
DLL load failed while importing vtkSlicerSequenceIOModuleMRMLPython: The specified module could not be found.
</code></pre>
<p>I tried:</p>
<ul>
<li>Copying the stray dlls all into qt-loadable-module/Release, same thing</li>
<li>Load one of the dlls that fail to load into depends (started with the launcher, with the SlicerIGT additional launcher settings ini), no DLL in the list that is actually not there (it listed things like vtkImaging-9.1.dll and a few similar ones, but they are present, especially that Slicer needs them too and it started alright)</li>
<li>Package both SlicerIGSIO and SlicerIGT and add the folders in the unzipped packages</li>
<li>Installed today’s nightly (05.30)
<ul>
<li>Compared the content of my packages with the factory packages, they are identical</li>
<li>Starting the nightly with the two extensions installed, I get the following: <code>Failed to load vtkSlicerVolumeReconstructionModuleLogicPython: No module named vtkSlicerIGSIOCommonPython</code> which probably indicates that not everything is alright even in the factory</li>
</ul>
</li>
<li>Double and triple checked that I built the matching configurations (all Release mode).</li>
</ul>
<p>I don’t have any more ideas other than using a more recent Slicer, which build I’ll start now.</p>
<p>Does anyone have any tips that may help?</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2022-05-31 12:16 UTC)

<p>Update: the same thing happens with the latest Slicer as well.</p>
<p>Has anyone successfully used locally built Slicer with locally build SlicerIGT recently? If so, how?</p>

---

## Post #3 by @chir.set (2022-05-31 15:15 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="23643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Has anyone successfully used locally built Slicer with locally build SlicerIGT recently? If so, how?</p>
</blockquote>
</aside>
<p>I’m running Slicer locally built with IGT/IGSIO on Arch. IGT is configured with</p>
<p><code>cmake -DSlicer_DIR:PATH=/home/arc/src/Slicer-SuperBuild9/Slicer-build -DCMAKE_BUILD_TYPE:STRING=Release -DSlicerIGSIO_DIR:PATH=/home/arc/src/SlicerIGSIO-SuperBuild9/inner-build -DSlicer_USE_GIT_PROTOCOL:BOOL=OFF /home/arc/src/SlicerIGT</code></p>
<p>Slicer itself works, when it loads. Sometimes it must be launched 2 - 3 times before it loads. And there’s always a crash message when it is closed normally. I didn’t have time to cross check if it may be related to IGSIO. Never had this before.</p>

---

## Post #4 by @cpinter (2022-05-31 15:39 UTC)

<p>Thanks <a class="mention" href="/u/chir.set">@chir.set</a> ! When you launch Slicer successfully, do you see the Pivot Calibration or Volume Reconstruction module? Do you have the errors in the Python window that I reported above? If you have those modules and you don’t have those specific errors then it is a different issue and I suggest opening a new topic for your problem so that the two unrelated things don’t mix.</p>
<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="23643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>it must be launched 2 - 3 times before it loads</p>
</blockquote>
</aside>
<p>What does this mean? What happens the rest of the times?</p>

---

## Post #5 by @chir.set (2022-05-31 16:42 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="23643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>do you see the Pivot Calibration or Volume Reconstruction module?</p>
</blockquote>
</aside>
<p>These modules are available in the module list, they can be searched and selected.</p>
<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="23643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Do you have the errors in the Python window that I reported above?</p>
</blockquote>
</aside>
<p>The errors you have reported above are not in the Python console, nor in applictaion log, and neither in bash stdout.</p>
<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="23643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I suggest opening a new topic for your problem so that the two unrelated things don’t mix.</p>
</blockquote>
</aside>
<p>Yes, you are right. I’ll build again this weekend and if the problem persists, I’ll dig deeper into that and start a discussion on its own.</p>
<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="23643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>What does this mean? What happens the rest of the times?</p>
</blockquote>
</aside>
<p>It means that Slicer may occasionally fail to start with this in console :</p>
<pre><code class="lang-auto">$ programs/Slicer/Slicer 
  Error(s):
    CLI executable: /home/user/programs/Slicer/bin/../lib/Slicer-5.1/qt-loadable-modules/vtkvmtk.py
    The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.
Fail to instantiate module  "vtkvmtk"
The following modules failed to be instantiated:
   vtkvmtk
Switch to module:  "Volumes"
error: [/home/user/programs/Slicer/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>When it successfully starts, it is normally usable. Please note it is a clean build. When it launches and then it is closed via the menu, this is in stdout :</p>
<pre><code class="lang-auto">......
Loading Slicer RC file [/home/user/.slicerrc.py]
Switch to module:  "PivotCalibration"
Switch to module:  "VolumeReconstruction"
Switch to module:  ""
Switch to module:  ""
double free or corruption (out)
error: [/home/user/programs/Slicer/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>Not a blocker right now. I’ll investigate this weekend.</p>

---

## Post #6 by @cpinter (2022-06-01 15:05 UTC)

<p>I tried the same thing on another computer (locally built Slicer5 with locally built SlicerIGSIO and SlicerIGT) and the same errors appear.</p>
<p>Can someone please try it in their environment?</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> any comment?</p>
<p>Thanks!</p>

---

## Post #7 by @cpinter (2022-06-02 14:18 UTC)

<p>It seems that now we cannot copy DLLs from the <code>bin</code> folder to the <code>lib/Slicer-5.1/qt-loadable-modules/Release</code>. In the past these superbuild and 3rd party DLLs could be just copied there and they were loaded OK. Instead of copying them there, copying them to <code>S5R\Slicer-build\bin\Release</code> solved the DLL loading issue and the three modules now appear.</p>
<p>I still get these errors on startup</p>
<pre><code class="lang-auto">Failed to load vtkSlicerVolumeReconstructionModuleLogicPython: No module named vtkSlicerIGSIOCommonPython
Failed to load vtkSlicerVolumeReconstructionModuleLogicPython: No module named vtkSlicerIGSIOCommonPython
Failed to load vtkSlicerVolumeReconstructionModuleLogicPython: No module named vtkSlicerIGSIOCommonPython
</code></pre>
<p>but as I mentioned before the same errors appear with the factory build too.</p>

---

## Post #8 by @ChristophG123 (2022-06-02 19:08 UTC)

<p>Hi Csaba, I’m getting the same issue, I’ll try this solution. I’m not sure if this is related or not, but I also have these errors when I try to use the Guidelet example extension you created:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "//imagingsrv.robarts.ca/Peters_Users$/cgibson/Documents/ExampleGuideletExtension-master/ExampleGuidelet/ExampleGuidelet.py", line 22, in __init__
    self.probeModel = slicer.util.loadModel('//imagingsrv.robarts.ca/Peters_Users$/cgibson/Documents/ExampleGuideletExtension-master/ExampleGuidelet/c7hd3.stl')
  File "C:\Users\cgibson\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-24\bin\Python\slicer\util.py", line 813, in loadModel
    return loadNodeFromFile(filename, 'ModelFile', {}, returnNode)
  File "C:\Users\cgibson\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-24\bin\Python\slicer\util.py", line 668, in loadNodeFromFile
    success = app.coreIOManager().loadNodes(filetype, properties, loadedNodesCollection)
ValueError: Could not find matching overload for given arguments:
('ModelFile', {'fileName': '//imagingsrv.robarts.ca/Peters_Users$/cgibson/Documents/ExampleGuideletExtension-master/ExampleGuidelet/c7hd3.stl'}, &lt;vtkmodules.vtkCommonCore.vtkCollection(0x00000234B256E880) at 0x00000234B71808E0&gt;)
 The following slots are available:
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes, vtkMRMLMessageCollection userMessages) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes, vtkMRMLMessageCollection userMessages) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:\Users\cgibson\AppData\Local\NA-MIC\Slicer 5.1.0-2022-05-24\lib\Python\Lib\imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "C:/Users/cgibson/AppData/Local/NA-MIC/Slicer 5.1.0-2022-05-24/NA-MIC/Extensions-30970/SlicerDMRI/lib/Slicer-5.1/qt-scripted-modules/NIfTIFile.py", line 7, in &lt;module&gt;
    import nifti
ModuleNotFoundError: No module named 'nifti'
Failed to load vtkSlicerVolumeReconstructionModuleLogicPython: No module named vtkSlicerIGSIOCommonPython
</code></pre>

---

## Post #9 by @Sunderlandkyl (2022-06-03 00:42 UTC)

<p>Not sure if this helps, but normally when I’m loading/debugging multiple extensions that contain third party libraries, I create a AdditionalLauncherSettings.ini file that combines the settings for all of the extensions that I am using. Using that file to start VisualStudio, etc. seems to work.</p>
<p>I’ll take a look at the vtkSlicerIGSIOCommonPython error messages.</p>

---

## Post #10 by @cpinter (2022-06-03 11:07 UTC)

<p>Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> !</p>
<p><a class="mention" href="/u/christophg123">@ChristophG123</a> Not sure why that file cannot be loaded. The slicer.util function has not changed. It may be due to the path you’re trying to use? If you copy it locally and load it from there does it work?<br>
In any case please create a new topic for this issue because what you reported is unrelated to this topic and it’s best to keep different discussions separate. Thanks!</p>
<aside class="quote no-group" data-username="ChristophG123" data-post="8" data-topic="23643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/christophg123/48/15483_2.png" class="avatar"> ChristophG123:</div>
<blockquote>
<p>Guidelet example extension you created</p>
</blockquote>
</aside>
<p>Not sure what guidelet example extension it is, I don’t remember seeing it, let alone creating…</p>

---
