# ALPACA in SlicerMorph

**Topic ID**: 17770
**Date**: 2021-05-24
**URL**: https://discourse.slicer.org/t/alpaca-in-slicermorph/17770

---

## Post #1 by @Morpho_T (2021-05-24 18:40 UTC)

<p>Hello,<br>
I am new to Slicer, tying to learn ALPACA in SlicerMorph.<br>
I am following the steps described <a href="https://github.com/SlicerMorph/Spr_2021/blob/main/Day_4/ALPACA/README.md" rel="noopener nofollow ugc">here</a>.<br>
When I click on “Run subsampling”, an error occurs : Import Error: cannot import name ‘registration’<br>
I wonder how to solve the problem. Any advice would be appreciated.</p>
<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: getting a target mesh<br>
Actual behavior: an error occurs</p>

---

## Post #2 by @muratmaga (2021-05-24 18:45 UTC)

<p>Can you open Python console and type:<br>
import open3d<br>
and report what it says?</p>
<p>M</p>

---

## Post #3 by @Morpho_T (2021-05-24 18:52 UTC)

<p>It does not seem to say anything.<br>
I installed open3d with “pip_install(“open3d”)”</p>

---

## Post #4 by @muratmaga (2021-05-24 18:55 UTC)

<p>It should automatically install both open3d and pycpd. Did you install that as well with<br>
pip_install(‘pycpd’)</p>

---

## Post #5 by @Morpho_T (2021-05-24 19:00 UTC)

<p>Yes. I also tried different versions of open3d. All caused an error (sometimes not the same error though).<br>
Is there anything else I could try?</p>

---

## Post #6 by @muratmaga (2021-05-24 19:25 UTC)

<p>This is a bit strange because I can’t replicate this error on any of my windows 10 computer with the latest stable (which is what you are runngin). Can you provide a screen capture of the settings (and copy and paste the entire log file)<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/agporto">@agporto</a> ?</p>

---

## Post #7 by @Morpho_T (2021-05-24 19:39 UTC)

<p>What settings are you referring to?<br>
Here is the log file:</p>
<p>[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Session start time …: 2021-05-24 15:30:52<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Memory …: 98022 MB physical, 112358 MB virtual<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - CPU …: GenuineIntel , 16 cores, 16 logical processors<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Application path …: C:/Slicer 4.11.20210226/bin<br>
[DEBUG][Qt] 24.05.2021 15:30:52 [] (unknown:0) - Additional module paths …: NA-MIC/Extensions-29738/SurfaceWrapSolidify/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/RawImageGuess/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerDcm2nii/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/Auto3dgm/lib/Slicer-4.11/cli-modules, NA-MIC/Extensions-29738/Auto3dgm/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/Sandbox/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/Sandbox/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules<br>
[DEBUG][Python] 24.05.2021 15:30:53 [Python] (C:\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[WARNING][Qt] 24.05.2021 15:30:53 [] (unknown:0) - libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[WARNING][Qt] 24.05.2021 15:30:54 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[DEBUG][Python] 24.05.2021 15:30:54 [Python] (C:\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 24.05.2021 15:30:55 [Python] (C:\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 24.05.2021 15:30:55 [Python] (C:\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Python] 24.05.2021 15:30:56 [Python] (C:\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: ExportAs<br>
[DEBUG][Qt] 24.05.2021 15:30:56 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 24.05.2021 15:31:08 [] (unknown:0) - Switch to module:  “ALPACA”<br>
[INFO][Stream] 24.05.2021 15:31:09 [] (unknown:0) - o3d installed<br>
[INFO][Stream] 24.05.2021 15:31:09 [] (unknown:0) - pycpd installed<br>
[CRITICAL][Stream] 24.05.2021 15:31:09 [] (unknown:0) - PythonQt: QObject::connect() signal ‘validInputChanged(bool)’ does not exist on QCheckBox<br>
[INFO][Stream] 24.05.2021 15:31:37 [] (unknown:0) - :: Loading point clouds and downsampling<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) -   File “C:/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 353, in onSubsampleButton<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) -     self.targetModelSelector.currentPath, self.skipScalingCheckBox.checked, self.parameterDictionary)<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) -   File “C:/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 903, in runSubsample<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) -     source_down, source_fpfh = self.preprocess_point_cloud(source, voxel_size, parameters[“normalSearchRadius”], parameters[“FPFHSearchRadius”])<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) -   File “C:/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 942, in preprocess_point_cloud<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) -     from open3d import registration<br>
[CRITICAL][Stream] 24.05.2021 15:31:37 [] (unknown:0) - ImportError: cannot import name ‘registration’</p>

---

## Post #8 by @agporto (2021-05-24 19:41 UTC)

<p>Can you check your open3d version?<br>
The easiest way is to go to the python interpreter within Slicer and type:<br>
import open3d<br>
<code>open3d.__version__</code></p>
<p>The reason for that is that open3d reorganized some modules from one version to another. So, you would have to pip_uninstall(‘open3d’ and then pip_install(‘open3d==0.10.0’)<br>
That should solve it</p>

---

## Post #9 by @Morpho_T (2021-05-24 19:52 UTC)

<p>It worked out! My open3d version was 12.<br>
Thank you!</p>

---

## Post #10 by @agporto (2021-05-24 19:54 UTC)

<p>Glad to hear ! Don’t hesitate to reach out if you have other issues with it</p>

---

## Post #11 by @lassoan (2021-05-25 20:44 UTC)

<p><a class="mention" href="/u/agporto">@agporto</a> you can enforce a particular open3d version similarly to how it is done <a href="https://github.com/lassoan/SlicerDICOMwebBrowser/blob/413755a16cbf0fb50408dd8e805d2e711ddb323d/DICOMwebBrowser/DICOMwebBrowser.py#L79-L103">here</a>.</p>
<p>I maintain that this open3d package is a hodge-podge of random stuff and there are lots of red flags in the code and how it is managed. Even though it contains some useful algorithms and the package may improve in the future, I would recommend to look for alternatives if you want to avoid unnecessary trouble.</p>

---

## Post #12 by @muratmaga (2021-05-25 20:46 UTC)

<p>It is actually enforced, it is version 0.10</p><aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/5bd5ee21b9f9b7d8e92d4828701ec8a29a120972/ALPACA/ALPACA.py#L57" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/5bd5ee21b9f9b7d8e92d4828701ec8a29a120972/ALPACA/ALPACA.py#L57" target="_blank" rel="noopener">SlicerMorph/SlicerMorph/blob/5bd5ee21b9f9b7d8e92d4828701ec8a29a120972/ALPACA/ALPACA.py#L57</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="47" style="counter-reset: li-counter 46 ;">
          <li>  """</li>
          <li>
          </li>
<li>def __init__(self, parent=None):</li>
          <li>  ScriptedLoadableModuleWidget.__init__(self, parent)</li>
          <li>  try:</li>
          <li>    import open3d as o3d</li>
          <li>    print('o3d installed')</li>
          <li>  except ModuleNotFoundError as e:</li>
          <li>    if slicer.util.confirmOkCancelDisplay("ALPACA requires the open3d library. Installation may take a few minutes"):</li>
          <li>      slicer.util.pip_install('notebook==6.0.3')</li>
          <li class="selected">      slicer.util.pip_install('open3d==0.10.0')</li>
          <li>      import open3d as o3d</li>
          <li>  try:</li>
          <li>    from pycpd import DeformableRegistration</li>
          <li>    print('pycpd installed')</li>
          <li>  except ModuleNotFoundError as e:</li>
          <li>    slicer.util.pip_install('git+https://github.com/agporto/pycpd.git@development')</li>
          <li>    print('trying to install pycpd')</li>
          <li>    from pycpd import DeformableRegistration</li>
          <li>  </li>
          <li>def onSelect(self):</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But we need to update hte tutorial, which uses a generic pip_install(“open3d”)</p>

---

## Post #13 by @agporto (2021-05-25 20:54 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> . It is good to know there is a way to check the installed version. Normally, users would have version 0.10.0 installed by default, as Murat mentioned. But it seems this user manually installed open3d from the python interpreter.<br>
I also agree with regard to the issue of having external dependencies (such as open3d). However, outside of Sara (who is the main developer on SlicerMorph and has a lot of stuff on her plate), we don’t really have a dedicated developer that could tackle this issue in the short term. So, at least for now, we have to rely on these dependencies to some extent.</p>

---

## Post #14 by @Morpho_T (2021-05-25 21:19 UTC)

<p>Just to be clear with what happened to me as far as I can remember:</p>
<ol>
<li>I opened ALPACA for the first time and the installation of open3d automatically started.</li>
<li>But after that I still could not open ALPACA correctly (the two tabs did not appear).</li>
<li>So I thought there was something wrong with the installation of open3d. So I ran  pip_install(“open3d”) (which probably overwrote the version 0.10 with 0.12). After this, I also found out that pycpd was not automatically installed (I don’t know if this is default). So I ran pip_install(“pycpd”) and finally ALPACA opened. But naturally, the version of open3d is different, which caused an error.</li>
</ol>
<p>So my problem was that pycpd was not automatically installed, so ALPACA did not open. But I misinterpreted it as a problem of open3d and replaced it with a newer version. I wonder if pycpd is supposed to get automatically installed when opening ALPACA for the first time. This happened again today using another computer.</p>

---

## Post #15 by @agporto (2021-05-25 21:23 UTC)

<p>Interesting. Thanks for the follow up. One quick question, do you have git installed on those machines? I am wondering if the pycpd installation is not happening because of git</p>

---

## Post #16 by @muratmaga (2021-05-25 21:24 UTC)

<p>Thanks for details. Pycpd also should automatically installed. <a href="https://github.com/SlicerMorph/SlicerMorph/blob/5bd5ee21b9f9b7d8e92d4828701ec8a29a120972/ALPACA/ALPACA.py#L63" class="inline-onebox">SlicerMorph/ALPACA.py at 5bd5ee21b9f9b7d8e92d4828701ec8a29a120972 · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>Open3d installation can take a minute, since it has a lot of dependencies. But i haven’t seen this before. We will try with a new installation.</p>

---

## Post #17 by @Morpho_T (2021-05-25 21:28 UTC)

<p>No, I don’t have git on both computers.</p>

---

## Post #18 by @lassoan (2021-05-26 00:37 UTC)

<p>If there are known problems with any Python package versions then you can use the code snippet in the DICOMweb module that I referenced above. It does a few important things:</p>
<ul>
<li>forces installation of the correct version of the package (if the installed version is unacceptable, even if import succeeds)</li>
<li>automatically restarts the application if needed (typically you need to restart the application if the package is already imported and you want to replace it with a different version)</li>
<li>it keeps the user informed about what’s happening and why (the user can just click OK, but has the option to interrupt the process, for example if that’s needed by some other modules).</li>
</ul>

---
