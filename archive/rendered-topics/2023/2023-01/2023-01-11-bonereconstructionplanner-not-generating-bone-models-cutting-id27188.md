---
topic_id: 27188
title: "Bonereconstructionplanner Not Generating Bone Models Cutting"
date: 2023-01-11
url: https://discourse.slicer.org/t/27188
---

# BoneReconstructionPlanner not generating bone models/cutting guides

**Topic ID**: 27188
**Date**: 2023-01-11
**URL**: https://discourse.slicer.org/t/bonereconstructionplanner-not-generating-bone-models-cutting-guides/27188

---

## Post #1 by @R_Nara (2023-01-11 13:12 UTC)

<p>Dear Sir,</p>
<p>I’m trying to plan a case of mandibular reconstruction using BoneReconstructionPlanner, but i’m stuck at one step, “create bone models from segmentations” doesn’t do anything and returns empty bone models, hence i’m not able to perform any steps beyond this point.(like centering fibula line, automatic mandibular cutting plane positioning, fibula surgical guide generation etc.)</p>
<p>Please guide me and help me in resolving this issue</p>
<p>Regards</p>

---

## Post #2 by @mau_igna_06 (2023-01-11 14:20 UTC)

<p>Hi. I just installed BoneReconstructionPlanner and executed its automatic tests and they worked successfully on both <a href="https://download.slicer.org/" rel="noopener nofollow ugc">the stable and preview release</a> of Slicer.</p>
<p>It should look like this video:</p><div class="youtube-onebox lazy-video-container" data-video-id="HRciwWEOAKk" data-video-title="BoneReconstructionPlanner (Software tests)" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=HRciwWEOAKk" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/HRciwWEOAKk/hqdefault.jpg" title="BoneReconstructionPlanner (Software tests)" width="" height="">
  </a>
</div>

<p>Although it may take around 10 minutes for you because Slicer will be downloading the test data (around 500MB) for the first time (after that it is cached).</p>
<p>To be able to execute the tests you need to enable developer mode on Slicer:</p>
<pre><code class="lang-auto">Edit -&gt; Application Settings -&gt; Developer -&gt; Enable developer mode
</code></pre>
<p>Then restart Slicer. After that you should be able to execute the BoneReconstructionPlanner automatic tests. You should see the same GUI that appears on the video.</p>
<p>Please let me know if you have more questions</p>

---

## Post #3 by @R_Nara (2023-01-12 09:08 UTC)

<p>thanks for the prompt response<br>
i’m getting error on running the test, here are the details</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\Admin\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:\Users\Admin\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\ScriptedLoadableModule.py”, line 224, in onReloadAndTest<br>
test(msec=int(slicer.app.userSettings().value(“Developer/SelfTestDisplayMessageDelay”)), **kwargs)<br>
File “C:\Users\Admin\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\ScriptedLoadableModule.py”, line 86, in runTest<br>
testCase.runTest(**kwargs)<br>
File “C:/Users/Admin/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 3656, in runTest<br>
self.section_MakeModels()<br>
File “C:/Users/Admin/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 3803, in section_MakeModels<br>
self.assertEqual(decimatedFibulaModelNode.GetMesh().GetNumberOfPoints(), 9872)<br>
File “C:\Users\Admin\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\unittest\case.py”, line 837, in assertEqual<br>
assertion_func(first, second, msg=msg)<br>
File “C:\Users\Admin\AppData\Local\NA-MIC\Slicer 5.2.1\lib\Python\Lib\unittest\case.py”, line 830, in _baseAssertEqual<br>
raise self.failureException(msg)<br>
AssertionError: 9871 != 9872</p>
<p>how should I proceed?</p>

---

## Post #4 by @mau_igna_06 (2023-01-12 21:04 UTC)

<p>Hi</p>
<p>Ok, so the test is not so robust as it’s needed and fails:</p>
<pre><code class="lang-auto">self.assertEqual(decimatedFibulaModelNode.GetMesh().GetNumberOfPoints(), 9872)
</code></pre>
<p>returns:</p>
<pre><code class="lang-auto">AssertionError: 9871 != 9872
</code></pre>
<p>The difference is 1.</p>
<p>This maybe due to vtk implementation differences on Windows (where you executed the tests) and Ubuntu (where I coded the tests and they were successful)</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> do you have any quick fix suggestion?</p>

---

## Post #5 by @lassoan (2023-01-12 21:36 UTC)

<p>Result of floating-point operations depend on many things - compiler options, hardware, operating systems, etc. Therefore results of any image or mesh processing operations is often slightly different on each system.</p>
<p>There are special compilation options that could be used to get consistent computation results, but the generated code is very slow, therefore these are rarely used in practice.</p>
<p>A simple solution is to specify tolerances for your tests to allow some small numerical differences.</p>

---

## Post #6 by @R_Nara (2023-01-13 01:32 UTC)

<p>This is the place where I’m stuck as well… nothing works after “generate bone models step”</p>

---

## Post #7 by @mau_igna_06 (2023-01-13 13:20 UTC)

<p><a class="mention" href="/u/r_nara">@R_Nara</a> I’ll solve this during the weekend</p>
<p>Thank you for your patience</p>

---

## Post #8 by @R_Nara (2023-01-13 15:36 UTC)

<p>Thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
i found a workaround for now… i’ve installed Ubuntu VM and running slicer on it now… i’m able to run the test successfully…</p>
<p>I started from scratch on this VM. But I still can’t go past “create models from segmentations” using my data… models turn out to be empty</p>
<p>will it be possible for you to  have a look at this project file please</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1cFKuPOnmNZhxsKXPJE3DIRjbV6kW7vrZ/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1cFKuPOnmNZhxsKXPJE3DIRjbV6kW7vrZ/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1cFKuPOnmNZhxsKXPJE3DIRjbV6kW7vrZ/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1cFKuPOnmNZhxsKXPJE3DIRjbV6kW7vrZ/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">2023-01-13-Scene.mrb</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Regards</p>

---

## Post #9 by @R_Nara (2023-01-13 15:44 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5ba4cbad4f7d8dc272fc7e04ae11ca4e9a1960b6.jpeg" data-download-href="/uploads/short-url/d4IwpA2MEpzTIivnf19YcEMsQbs.jpeg?dl=1" title="Screenshot 2023-01-13 211103" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5ba4cbad4f7d8dc272fc7e04ae11ca4e9a1960b6_2_345x176.jpeg" alt="Screenshot 2023-01-13 211103" data-base62-sha1="d4IwpA2MEpzTIivnf19YcEMsQbs" width="345" height="176" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5ba4cbad4f7d8dc272fc7e04ae11ca4e9a1960b6_2_345x176.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5ba4cbad4f7d8dc272fc7e04ae11ca4e9a1960b6_2_517x264.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5ba4cbad4f7d8dc272fc7e04ae11ca4e9a1960b6_2_690x352.jpeg 2x" data-dominant-color="A4A6BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-01-13 211103</span><span class="informations">1833×936 210 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
i get decimated fibula, decimated mandible, and then it stops at fibula… all models are blank, if i hide segments, the 3D view is blank<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2619587702419bc2e12d5b4715e6130f6229a1c.jpeg" data-download-href="/uploads/short-url/wiEYQ49x1e6rJNz7GaA9xXyFnPK.jpeg?dl=1" title="Screenshot 2023-01-13 211355" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2619587702419bc2e12d5b4715e6130f6229a1c_2_345x174.jpeg" alt="Screenshot 2023-01-13 211355" data-base62-sha1="wiEYQ49x1e6rJNz7GaA9xXyFnPK" width="345" height="174" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2619587702419bc2e12d5b4715e6130f6229a1c_2_345x174.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2619587702419bc2e12d5b4715e6130f6229a1c_2_517x261.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2619587702419bc2e12d5b4715e6130f6229a1c_2_690x348.jpeg 2x" data-dominant-color="A7A8C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-01-13 211355</span><span class="informations">1826×923 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @mau_igna_06 (2023-01-13 16:03 UTC)

<p>Probably there was an error. Please open the python interactor and copy the error message and paste it here. I’ll help then.</p>
<p>Here is a <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#mouse-keyboard-shortcuts" rel="noopener nofollow ugc">keyboard-shortcut</a> on how to open the python console</p>

---

## Post #11 by @R_Nara (2023-01-13 16:30 UTC)

<p>here it is</p>
<p>Python 3.9.10 (main, Nov 24 2022, 08:11:57)<br>
[GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux2</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>[Qt] QLayout::addChildLayout: layout “” already has a parent<br>
[Qt] ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1<br>
[Qt] QString qSlicerSegmentEditorAbstractEffect::parameter(QString) : Parameter named “regionSegmentID” cannot be found for effect “Wrap Solidify”<br>
[Qt] ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 1<br>
Traceback (most recent call last):<br>
File “/home/opd4/Downloads/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 261, in setup<br>
self.initializeParameterNode()<br>
File “/home/opd4/Downloads/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 379, in initializeParameterNode<br>
self.setParameterNode(self.logic.getParameterNode())<br>
File “/home/opd4/Downloads/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 400, in setParameterNode<br>
self.updateGUIFromParameterNode()<br>
File “/home/opd4/Downloads/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 426, in updateGUIFromParameterNode<br>
scalarVolumeID = self._parameterNode.GetNodeReference(“currentScalarVolume”).GetID()<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetID’<br>
[VTK] Warning: In /work/Stable/Slicer-0/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.cxx, line 2839<br>
[VTK] vtkMRMLSubjectHierarchyNode (0x433cb20): GetItemChildren: Invalid item ID given<br>
[VTK] Warning: In /work/Stable/Slicer-0/Libs/MRML/Core/vtkMRMLSubjectHierarchyNode.cxx, line 2839<br>
[VTK] vtkMRMLSubjectHierarchyNode (0x433cb20): GetItemChildren: Invalid item ID given<br>
Traceback (most recent call last):<br>
File “/home/opd4/Downloads/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 620, in onMakeModelsButton<br>
self.logic.makeModels()<br>
File “/home/opd4/Downloads/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 2299, in makeModels<br>
seg.GetSegmentation().CreateRepresentation(slicer.vtkSegmentationConverter.GetSegmentationClosedSurfaceRepresentationName())<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetSegmentation’</p>

---

## Post #12 by @mau_igna_06 (2023-01-13 17:41 UTC)

<aside class="quote no-group" data-username="R_Nara" data-post="11" data-topic="27188">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/r_nara/48/17980_2.png" class="avatar"> R_Nara:</div>
<blockquote>
<p>here it is</p>
</blockquote>
</aside>
<p>Thank you. There was a bug and <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commit/b4c167c723360dcd0dc32ed8cabae836053474da" rel="noopener nofollow ugc">I fixed it</a></p>
<p>I loaded to Slicer only the CT volumes and the two segmentations from your scene and I could do Virtual Surgical Planning in both Slicer Preview and Stable release with the updated code. Also the automatic tests executed successfully.</p>
<p>The new BRP code will be available tomorrow as an extension update on Stable release or as an extension install on the Preview version of tomorrow. You can also download the code by yourself and add the module path to Slicer settings to start using it today but you first need to uninstall BRP from the extensions manager to avoid conflicts</p>

---

## Post #13 by @R_Nara (2023-01-13 18:10 UTC)

<p>Perfect. I’m totally new to 3D slicer and Linux, i don’t know how to download and use the code manually… I’ll wait for the update tomorrow and get back to you with a feedback.<br>
Regards</p>

---

## Post #14 by @R_Nara (2023-01-14 16:55 UTC)

<p>Looks like it’s working, I’m able to get past the error… thanks a lot for the prompt response and solution. Will update once i complete the process or if I come across any error.</p>
<p>It’s still not working on windows, but working on ubuntu</p>
<p>Regards</p>

---

## Post #15 by @mau_igna_06 (2023-01-14 23:23 UTC)

<p>Hi</p>
<p>Some tests were failing and got fixed… Please use Slicer Preview release of tomorrow (or update BRP extension on Stable release tomorrow). Both Ubuntu and Windows should work.</p>
<p>Please try executing the automatic tests as I pointed in the video above, they should be a very graphic learning tool for new users</p>

---

## Post #16 by @R_Nara (2023-01-15 13:57 UTC)

<p>Hi</p>
<p>I’m getting a new error in windows app now. here are the details</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\abc\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:\Users\abc\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\ScriptedLoadableModule.py”, line 224, in onReloadAndTest<br>
test(msec=int(slicer.app.userSettings().value(“Developer/SelfTestDisplayMessageDelay”)), **kwargs)<br>
File “C:\Users\abc\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\ScriptedLoadableModule.py”, line 86, in runTest<br>
testCase.runTest(**kwargs)<br>
File “C:/Users/abc/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 3654, in runTest<br>
self.section_SimulateAndImproveMandibleReconstruction()<br>
File “C:/Users/abc/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/BoneReconstructionPlanner/lib/Slicer-5.2/qt-scripted-modules/BoneReconstructionPlanner.py”, line 4123, in section_SimulateAndImproveMandibleReconstruction<br>
layoutManager.addMaximizedViewNode(mandibleViewNode)<br>
AttributeError: qSlicerLayoutManager has no attribute named ‘addMaximizedViewNode’</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5efc87b6dd049000bd19ca24f8e4a74d04e2002f.jpeg" data-download-href="/uploads/short-url/dyhVnLSAsxMseaujzYUO0OgmyaH.jpeg?dl=1" title="Screenshot 2023-01-15 192638" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5efc87b6dd049000bd19ca24f8e4a74d04e2002f_2_345x179.jpeg" alt="Screenshot 2023-01-15 192638" data-base62-sha1="dyhVnLSAsxMseaujzYUO0OgmyaH" width="345" height="179" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5efc87b6dd049000bd19ca24f8e4a74d04e2002f_2_345x179.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5efc87b6dd049000bd19ca24f8e4a74d04e2002f_2_517x268.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5efc87b6dd049000bd19ca24f8e4a74d04e2002f_2_690x358.jpeg 2x" data-dominant-color="6B6983"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-01-15 192638</span><span class="informations">1920×1000 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #17 by @jamesobutler (2023-01-15 14:20 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> Your latest code changes are compatible with the latest Slicer Preview but not the latest Slicer stable (5.2.1). You’ll need to add some compatibility statements like below</p>
<pre><code class="lang-python">if (slicer.app.majorVersion, slicer.app.minorVersion) &lt; (5, 3):
  layoutManager.setMaximizedViewNode(fibulaViewNode)
else:
  layoutManager.addMaximizedViewNode(fibulaViewNode)
</code></pre>

---

## Post #18 by @mau_igna_06 (2023-01-15 19:12 UTC)

<p>Thank you <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. You are right.</p>
<p>Dear <a class="mention" href="/u/r_nara">@R_Nara</a><br>
Thank you for bearing with me. Your testing is very important since we are still developing auto-tests that would send us an email to developers when things are not working.<br>
Stable release should work after updating the BoneReconstructionPlanner extension tomorrow</p>

---

## Post #19 by @R_Nara (2023-01-22 10:53 UTC)

<p>thanks for resolving the  issues, i was able to generate the cutting guides and complete the surgical plan without further issues…</p>

---
