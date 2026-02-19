---
topic_id: 44660
title: "Seglg Slicer Modules Segmentations Logic Attributeerror Modu"
date: 2025-10-03
url: https://discourse.slicer.org/t/44660
---

# segLg = slicer.modules.segmentations.logic() AttributeError: module 'modules' has no attribute 'segmentations'

**Topic ID**: 44660
**Date**: 2025-10-03
**URL**: https://discourse.slicer.org/t/seglg-slicer-modules-segmentations-logic-attributeerror-module-modules-has-no-attribute-segmentations/44660

---

## Post #1 by @jumbojing (2025-10-03 13:26 UTC)

<p>Are the modules not fully imported? What’s wrong in py?</p>
<blockquote>
<blockquote>
<blockquote>
<p>segLg = slicer.modules.segmentations.logic()<br>
AttributeError: module ‘modules’ has no attribute ‘segmentations’<br>
print(dir(slicer.modules))<br>
[‘AddManyMarkupsFiducialTestInstance’, ‘AtlasTestsInstance’, ‘BRAINSFitRigidRegistrationCrashIssue4139Instance’, ‘ColorLegendSelfTestInstance’, ‘CompareVolumesInstance’, ‘CropVolumeSelfTestInstance’, ‘CropVolumeSequenceInstance’, ‘DICOMEnhancedUSVolumePluginInstance’, ‘DICOMGeAbusPluginInstance’, ‘DICOMImageSequencePluginInstance’, ‘DICOMInstance’, ‘DICOMPatcherInstance’, ‘DICOMScalarVolumePluginInstance’, ‘DICOMSlicerDataBundlePluginInstance’, ‘DICOMVolumeSequencePluginInstance’, ‘DataProbeInstance’, ‘EndoscopyInstance’, ‘ExtensionWizardInstance’, ‘FiducialLayoutSwitchBug1914Instance’, ‘ImportItkSnapLabelInstance’, ‘JRC2013VisInstance’, ‘JupyterNotebooksInstance’, ‘LandmarkRegistrationInstance’, ‘MarkupsInCompareViewersSelfTestInstance’, ‘MarkupsInViewsSelfTestInstance’, ‘MultiVolumeImporterInstance’, ‘MultiVolumeImporterPluginInstance’, ‘NeurosurgicalPlanningTutorialMarkupsSelfTestInstance’, ‘<strong>doc</strong>’, ‘<strong>file</strong>’, ‘<strong>loader</strong>’, ‘<strong>name</strong>’, ‘<strong>package</strong>’, ‘<strong>spec</strong>’, ‘dicomPlugins’, ‘registrationPlugins’]</p>
</blockquote>
</blockquote>
</blockquote>
<p>However in <code>python console</code> this situation does not occur.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c30a048eb3989a7ef7649d5cc11a3a55afa2bfc8.png" alt="image" data-base62-sha1="rPozkeBEY4eGpgnkbFdgseffR9e" width="690" height="49" data-dominant-color="2E3032"></p>

---

## Post #2 by @cpinter (2025-10-03 13:30 UTC)

<p>Is it a build you did yourself or downloaded and installed?</p>
<p>Are there any errors on startup?</p>

---

## Post #3 by @jumbojing (2025-10-03 13:32 UTC)

<p>downloaded and installed from <a href="https://download.slicer.org/bitstream/67c52e9629825655577d0353" rel="noopener nofollow ugc">https://download.slicer.org/bitstream/67c52e9629825655577d0353</a></p>

---

## Post #4 by @pieper (2025-10-03 13:59 UTC)

<p>That is Slicer 5.8.1 for mac, and when I run it this works:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.modules.segmentations.logic()
&lt;vtkSlicerSegmentationsModuleLogicPython.vtkSlicerSegmentationsModuleLogic(0x600003b38af0) at 0x1b4b7f100&gt;
</code></pre>

---

## Post #5 by @cpinter (2025-10-03 14:01 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="44660">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Are there any errors on startup?</p>
</blockquote>
</aside>
<p>Please answer this question too, this is the more important one. Thanks</p>

---

## Post #6 by @jumbojing (2025-10-03 14:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e04a4fd85272820b55d82c1a4377a5a7837ccc.png" data-download-href="/uploads/short-url/tNNQV6aAzFLoCTG4fv7RUrYd7xW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0e04a4fd85272820b55d82c1a4377a5a7837ccc.png" alt="image" data-base62-sha1="tNNQV6aAzFLoCTG4fv7RUrYd7xW" width="690" height="385" data-dominant-color="331C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×447 79.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @pieper (2025-10-03 14:05 UTC)

<p>You’ll need to narrow down to something reproducible or we can’t help you out.</p>

---

## Post #8 by @jumbojing (2025-10-03 14:22 UTC)

<pre><code class="lang-auto"># ...docs/segLg.py
import slicer
segLg = slicer.modules.segmentations.logic()
</code></pre>
<p>For example, add the above file docs/segLg.py to modules as follows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abfd34ed99a047640725ffc9a85c9de69d827293.png" data-download-href="/uploads/short-url/oxu8HJ6gtDo0LipeyhZzcbnhX6H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abfd34ed99a047640725ffc9a85c9de69d827293_2_690x168.png" alt="image" data-base62-sha1="oxu8HJ6gtDo0LipeyhZzcbnhX6H" width="690" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abfd34ed99a047640725ffc9a85c9de69d827293_2_690x168.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abfd34ed99a047640725ffc9a85c9de69d827293.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abfd34ed99a047640725ffc9a85c9de69d827293.png 2x" data-dominant-color="424548"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">824×201 45.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>**The error is as follows:**</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c776c3319fd02da233ba096d5c9c79c836b47cd.png" data-download-href="/uploads/short-url/dbZMVrWiiK6xyUuSsbpqamm53QN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c776c3319fd02da233ba096d5c9c79c836b47cd.png" alt="image" data-base62-sha1="dbZMVrWiiK6xyUuSsbpqamm53QN" width="690" height="187" data-dominant-color="361B1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">794×216 40.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @pieper (2025-10-03 14:58 UTC)

<p>Ah, okay.  Your module is being discovered before the segmentations has loaded.</p>
<p>You need something like:</p>
<pre><code class="lang-auto">self.parent.dependencies = ["Segmentations"]
</code></pre>
<p>in your module’s main class.</p>

---

## Post #10 by @jumbojing (2025-10-03 15:09 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> For example, how to modify <code>segLg.py</code> <img src="https://emoji.discourse-cdn.com/twitter/backhand_index_pointing_down.png?v=14" title=":backhand_index_pointing_down:" class="emoji" alt=":backhand_index_pointing_down:" loading="lazy" width="20" height="20">?</p>
<pre><code class="lang-auto">import slicer
# ? self.parent.dependencies = ["Segmentations"]
segLg = slicer.modules.segmentations.logic()
</code></pre>

---

## Post #11 by @pieper (2025-10-03 15:11 UTC)

<p>Since you added this <code>docs</code> path to the module path it needs to be in the scripted module format, like you get when you use the ExtensionWizard.  That’s there the dependency is expressed.</p>

---

## Post #12 by @jumbojing (2025-10-03 15:18 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Teacher, could you be more specific? Could you give an example🌰?</p>

---

## Post #13 by @pieper (2025-10-03 15:20 UTC)

<p>Like here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L34">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L34" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L34" target="_blank" rel="noopener">Modules/Scripted/Endoscopy/Endoscopy.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L34" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="24" style="counter-reset: li-counter 23 ;">
          <li></li>
          <li>class Endoscopy(ScriptedLoadableModule):</li>
          <li>    """Uses ScriptedLoadableModule base class, available at:</li>
          <li>    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py</li>
          <li>    """</li>
          <li></li>
          <li>    def __init__(self, parent):</li>
          <li>        ScriptedLoadableModule.__init__(self, parent)</li>
          <li>        self.parent.title = _("Endoscopy")</li>
          <li>        self.parent.categories = [translate("qSlicerAbstractCoreModule", "Endoscopy")]</li>
          <li class="selected">        self.parent.dependencies = ["Markups"]</li>
          <li>        self.parent.contributors = [</li>
          <li>            "Steve Pieper (Isomics)",</li>
          <li>            "Harald Scheirich (Kitware)",</li>
          <li>            "Lee Newberg (Kitware)",</li>
          <li>            "Jean-Christophe Fillion-Robin (Kitware)",</li>
          <li>        ]</li>
          <li>        self.parent.helpText = _("""</li>
          <li>Create or import a markups curve.</li>
          <li>Pick the Camera to use for either playing the flythrough or editing associated keyframes.</li>
          <li>Select the Camera to use for playing the flythrough.</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #14 by @jumbojing (2025-10-03 15:45 UTC)

<pre><code class="lang-auto">import slicer
# self.parent.dependencies = ["Segmentations"]
print(f'{dir(slicer.modules)=}')
segLg = slicer.modules.segmentations.logic()
</code></pre>
<pre><code class="lang-auto">dir(slicer.modules)=['AddManyMarkupsFiducialTestInstance', 'AtlasTestsInstance', 'BRAINSFitRigidRegistrationCrashIssue4139Instance', 'ColorLegendSelfTestInstance', 'CompareVolumesInstance', 'CropVolumeSelfTestInstance', 'CropVolumeSequenceInstance', 'DICOMEnhancedUSVolumePluginInstance', 'DICOMGeAbusPluginInstance', 'DICOMImageSequencePluginInstance', 'DICOMInstance', 'DICOMPatcherInstance', 'DICOMScalarVolumePluginInstance', 'DICOMSlicerDataBundlePluginInstance', 'DICOMVolumeSequencePluginInstance', 'DataProbeInstance', 'EndoscopyInstance', 'ExtensionWizardInstance', 'FiducialLayoutSwitchBug1914Instance', 'ImportItkSnapLabelInstance', 'JRC2013VisInstance', 'JupyterNotebooksInstance', 'LandmarkRegistrationInstance', 'MarkupsInCompareViewersSelfTestInstance', 'MarkupsInViewsSelfTestInstance', 'MultiVolumeImporterInstance', 'MultiVolumeImporterPluginInstance', 'NeurosurgicalPlanningTutorialMarkupsSelfTestInstance', 'PedicleScrewPlannerInstance', 'PedicleScrewSimulatorInstance', 'PedicleTrianglePlannerInstance', 'PerformanceTestsInstance', 'PlotsSelfTestInstance', 'PluggableMarkupsSelfTestInstance', 'PyTorchUtilsInstance', 'RSNA2012ProstateDemoInstance', 'RSNAQuantTutorialInstance', 'RSNAVisTutorialInstance', 'SampleDataInstance', 'ScenePerformanceInstance', 'ScreenCaptureInstance', 'SegmentEditorInstance', 'SegmentStatisticsInstance', 'SelfTestsInstance', 'SequencesSelfTestInstance', 'ShaderPropertiesInstance', 'SimpleFiltersInstance', 'SliceLinkLogicInstance', 'Slicer4MinuteInstance', 'SlicerBoundsTestInstance', 'SlicerDisplayNodeSequenceTestInstance', 'SlicerMRBMultipleSaveRestoreLoopTestInstance', 'SlicerMRBMultipleSaveRestoreTestInstance', 'SlicerMRBSaveRestoreCheckPathsTestInstance', 'SlicerNNUNetInstance', 'SlicerOrientationSelectorTestInstance', 'SlicerPythonTestRunnerInstance', 'SlicerScriptedFileReaderWriterTestInstance', 'SubjectHierarchyCorePluginsSelfTestInstance', 'SubjectHierarchyGenericSelfTestInstance', 'SurfaceToolboxInstance', 'TablesSelfTestInstance', 'TotalSegmentatorInstance', 'UtilTestInstance', 'VectorToScalarVolumeInstance', 'ViewControllersSliceInterpolationBug1926Instance', 'VolumeRenderingSceneCloseInstance', 'WebEngineInstance', 'WebServerInstance', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'dicomPlugins', 'registrationPlugins', 'sampleDataSources', 'sceneImport2428Instance']
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/imp.py", line 169, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 613, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "/Users/liguimei/Documents/ppPrj/Resources/docs/segLg.py", line 4, in &lt;module&gt;
    segLg = slicer.modules.segmentations.logic()
AttributeError: module 'modules' has no attribute 'segmentations'
[Qt] loadSourceAsModule - Failed to load file "/Users/liguimei/Documents/ppPrj/Resources/docs/segLg.py"  as module "segLg" !
[Qt] Fail to instantiate module  "segLg"
</code></pre>
<p>Still don’t understand…</p>

---

## Post #15 by @jumbojing (2025-10-03 16:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> ?…………………………………………….</p>

---

## Post #16 by @shai-ikko (2025-10-16 07:49 UTC)

<p>Slicer has some expectations from files you try to use as modules. If you just drop some python code into a file, it can break, and that is what you see.</p>
<p>The particular expectation here is: It should be possible to import your file without it depending on other modules. Your code explicitly depends on other modules.</p>
<p>Re-writing the file so that it looks like the module shown by <a class="mention" href="/u/pieper">@pieper</a> would help:</p>
<ul>
<li>The code that uses <code>slicer.modules.segmentations</code> should be in one of the method of the class, so it doesn’t get executed at import time</li>
<li>Then you also have a place to declare dependencies, which will be respected</li>
</ul>
<p>Trying to add one line to your existing code would not work.</p>

---

## Post #17 by @lassoan (2025-10-16 12:15 UTC)

<p>I would recommend to use the Extensions Wizard module to generate a module skeleton and add your code to it piece by piece. The <a href="https://training.slicer.org/#STC-DEV-101">STC-DEV-101 Tutorial</a> should help.</p>

---
