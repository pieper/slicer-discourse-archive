---
topic_id: 32017
title: "Installing Slicer Extensions From Cmd With Python"
date: 2023-10-03
url: https://discourse.slicer.org/t/32017
---

# Installing Slicer Extensions from cmd with python

**Topic ID**: 32017
**Date**: 2023-10-03
**URL**: https://discourse.slicer.org/t/installing-slicer-extensions-from-cmd-with-python/32017

---

## Post #1 by @wesselk (2023-10-03 20:18 UTC)

<p>Hello, I am working on moving a Slicer routine from my work computer to the machine it will be deployed on.  Unfortunately the machine is headless and my employer has a very sensitive firewall preventing extensions from being simply added with slicer.app.installExtensionFromServer().</p>
<p>In the slicer docs <a href="https://gist.github.com/pieper/a9c0ba57de3833c9f5aea68247bda597" rel="noopener nofollow ugc">this link</a> is provided for installing from git.  I have made the following changes to install from a zipped file instead:</p>
<pre><code class="lang-auto">downloadedArchiveFilePath = "/extensions/SlicerExtension-VMTK-master.zip"

outputDir = os.path.join(slicer.app.temporaryPath, "SlicerVMTK")

try:
    shutil.rmtree(outputDir)
    os.mkdir(outputDir)
except FileNotFoundError:
    pass

slicer.util.extractArchive(
    archiveFilePath=downloadedArchiveFilePath,
    outputDir=outputDir
)

factoryManager = slicer.app.moduleManager().factoryManager()
mod_list = ["ExtractCenterline", "CrossSectionAnalysis"]
for mod in mod_list:
    import os # I know this is odd but somehow it says "os not defined" by the second time through the loop if I omit this
    modulePath = os.path.join(outputDir, "SlicerExtension-VMTK-master", mod, mod+".py")
    factoryManager.registerModule(qt.QFileInfo(modulePath))

factoryManager.loadModules(mod_list)

slicer.util.selectModule("ExtractCenterline")
</code></pre>
<p>This all runs fine and as a result I am able to run the lines “import ExtractCenterline” and “import CrossSectionAnalysis”.  However, when I run the extract centerline logic I am met with the following error:</p>
<blockquote>
<p>line 445, in preprocess<br>
import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry<br>
ModuleNotFoundError: No module named ‘vtkvmtkComputationalGeometryPython’</p>
</blockquote>
<p>The only other threads I see on this topic encourage downloading the newest stable release, I am using Slicer 5.4.0 and still encountering this issue.  I suspect I am not correctly importing the SlicerVMTK extension because I specifically go after the 2 modules I need, but I don’t know how I would get the whole thing as there is no SlicerVMTK.py and I am naively repurposing the example code.</p>
<p>Thanks in advance for any input!</p>

---

## Post #2 by @wesselk (2023-10-25 21:20 UTC)

<h1><a name="p-102296-update-1" class="anchor" href="#p-102296-update-1" aria-label="Heading link"></a>Update</h1>
<p>I’m now able to run Slicer from command and access <em>some</em> extensions without triggering my employer’s firewall, but it only works for simple extensions like AirwaySegmentation or Sandbox.  This method still fails for adding SlicerVMTK: <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#additional-module-paths" rel="noopener nofollow ugc">Documentation here</a>.  It would be nice if someone could point me to the location of the “additional module paths” file so I could just permanently alter it.</p>
<p>What I’d really like to do is to access the “install from file” utility from python/cmd line (which is what I thought em.installExtension() would be but it yells at my file path). But at this point if I knew how I would manually copy the correct directories into the extensions section of Slicer and append the necessary info onto slicer’s extension settings files, etc.</p>
<p>Any advice is appreciated! Thanks</p>

---

## Post #3 by @muratmaga (2023-10-25 23:05 UTC)

<p>Additional paths are specified in Slicer.ini file under the section:</p>
<pre><code class="lang-auto">[LibraryPaths]
1\path=Extensions-31938/SlicerMorph/lib/Slicer-5.4
10\path=Extensions-31938/MarkupsToModel/lib/Slicer-5.4
11\path=Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules
12\path=Extensions-31938/SlicerJupyter/lib/Slicer-5.4
13\path=Extensions-31938/SlicerJupyter/lib/Slicer-5.4/qt-loadable-modules
14\path=Extensions-31938/Sandbox/lib/Slicer-5.4
15\path=Extensions-31938/Sandbox/lib/Slicer-5.4/qt-loadable-modules
16\path=Extensions-31938/SlicerOpenAnatomy/lib/Slicer-5.4
17\path=Extensions-31938/ModelToModelDistance/lib/Slicer-5.4
18\path=Extensions-31938/ModelToModelDistance/lib/Slicer-5.4/cli-modules
19\path=Extensions-31938/LanguagePacks/lib/Slicer-5.4
2\path=Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4
20\path=Extensions-31938/DeveloperToolsForExtensions/lib/Slicer-5.4
21\path=Extensions-31938/MEMOS/lib/Slicer-5.4
22\path=Extensions-31938/PyTorch/lib/Slicer-5.4
3\path=Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-loadable-modules
4\path=Extensions-31938/SlicerIGT/lib/Slicer-5.4
5\path=Extensions-31938/SlicerIGT/lib/Slicer-5.4/qt-loadable-modules
6\path=Extensions-31938/SlicerIGSIO/lib/Slicer-5.4
7\path=Extensions-31938/SlicerIGSIO/lib/Slicer-5.4/qt-loadable-modules
8\path=Extensions-31938/Pipelines/lib/Slicer-5.4
9\path=Extensions-31938/Pipelines/lib/Slicer-5.4/qt-loadable-modules
size=22

[Modules]
AdditionalPaths=Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-loadable-modules, Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/SlicerIGT/lib/Slicer-5.4/qt-loadable-modules, Extensions-31938/SlicerIGT/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/SlicerIGSIO/lib/Slicer-5.4/qt-loadable-modules, Extensions-31938/Pipelines/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/MarkupsToModel/lib/Slicer-5.4/qt-loadable-modules, Extensions-31938/SlicerJupyter/lib/Slicer-5.4/qt-loadable-modules, Extensions-31938/SlicerJupyter/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/SlicerMorph/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/Sandbox/lib/Slicer-5.4/qt-loadable-modules, Extensions-31938/Sandbox/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/SlicerOpenAnatomy/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/ModelToModelDistance/lib/Slicer-5.4/cli-modules, Extensions-31938/LanguagePacks/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/DeveloperToolsForExtensions/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/MEMOS/lib/Slicer-5.4/qt-scripted-modules, Extensions-31938/PyTorch/lib/Slicer-5.4/qt-scripted-modules
IgnoreModules=@Invalid()

[PYTHONPATH]
1\path=Extensions-31938/SlicerMorph/lib/Slicer-5.4/qt-scripted-modules
10\path=Extensions-31938/DeveloperToolsForExtensions/lib/Slicer-5.4/qt-scripted-modules
11\path=Extensions-31938/MEMOS/lib/Slicer-5.4/qt-scripted-modules
12\path=Extensions-31938/PyTorch/lib/Slicer-5.4/qt-scripted-modules
2\path=Extensions-31938/SegmentEditorExtraEffects/lib/Slicer-5.4/qt-scripted-modules
3\path=Extensions-31938/SlicerIGT/lib/Slicer-5.4/qt-scripted-modules
4\path=Extensions-31938/Pipelines/lib/Slicer-5.4/qt-scripted-modules
5\path=Extensions-31938/SlicerJupyter/lib/Slicer-5.4/qt-scripted-modules
6\path=Extensions-31938/SlicerJupyter/lib/python3.9/site-packages
7\path=Extensions-31938/Sandbox/lib/Slicer-5.4/qt-scripted-modules
8\path=Extensions-31938/SlicerOpenAnatomy/lib/Slicer-5.4/qt-scripted-modules
9\path=Extensions-31938/LanguagePacks/lib/Slicer-5.4/qt-scripted-modules
size=12

[Paths]
1\path=Extensions-31938/ModelToModelDistance/lib/Slicer-5.4/cli-modules
size=1


</code></pre>

---

## Post #4 by @lassoan (2023-10-25 23:59 UTC)

<p>You can download the extension package from the extension catalog and <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#install-extensions-without-network-connection">install it from file using the Slicer GUI</a> or in Python by calling the <a href="https://apidocs.slicer.org/master/classqSlicerExtensionsManagerModel.html#a8e723a2a43f1c0e3e8aa74e0ae6bbbef">installExtension</a> method of the extensions manager:</p>
<pre><code class="lang-python">slicer.app.extensionsManagerModel().installExtension('/path/to/myextension.zip')
</code></pre>

---

## Post #5 by @wesselk (2023-10-26 17:07 UTC)

<p>Thanks for that example, I was mistakenly using the GitHub repo .zip <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=12" title=":expressionless:" class="emoji" alt=":expressionless:" loading="lazy" width="20" height="20"></p>
<p>Unfortunately I am still having the same problem as before, simple extensions like Sandbox or AirwaySegmentation are successfully installed like this, but I get the following error when rebooting slicer after installing SlicerVMTK:</p>
<blockquote>
<p>Error(s):<br>
Cannot load library /home/qiluser/Slicer/slicer.org/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-loadable-modules/libqSlicerStenosisMeasurement3DModule.so: (libvtkSlicerShapeModuleMRML.so: cannot open shared object file: No such file or directory)<br>
libvtkSlicerShapeModuleMRML.so: cannot open shared object file: No such file or directory<br>
libvtkSlicerShapeModuleMRML.so: cannot open shared object file: No such file or directory<br>
libvtkSlicerShapeModuleMRML.so: cannot open shared object file: No such file or directory<br>
Error(s):<br>
CLI executable: /home/qiluser/Slicer/slicer.org/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
Fail to instantiate module  “vtkvmtk”<br>
The following modules failed to be instantiated:<br>
vtkvmtk<br>
When loading module  “GuidedArterySegmentation” , the dependency “SegmentEditorFloodFilling” failed to be loaded.<br>
When loading module  “QuickArterySegmentation” , the dependency “SegmentEditorFloodFilling” failed to be loaded.</p>
</blockquote>
<p>I am running it like:</p>
<blockquote>
<p>em = slicer.app.extensionsManagerModel()<br>
em.interactive = False<br>
em.installExtension(extensionFilePath, True) <span class="hashtag-raw">#installing</span> dependencies</p>
</blockquote>
<p>My only guess is my work’s firewall is getting back in the way for retrieving the dependencies. Any way those can be manually installed as well?</p>
<p>Thanks so much</p>

---

## Post #6 by @lassoan (2023-10-26 17:15 UTC)

<p>Yes, you need to call <code>installExtension(..., False)</code> and manually install all extensions you need (including dependencies).</p>

---

## Post #7 by @wesselk (2023-10-26 18:04 UTC)

<p>Thank you. I am not sure which other dependencies to add at this point.  It looks like I have an identical error to <a href="https://discourse.slicer.org/t/vmtk-extension-problem/13699">this user</a>, which you have already identified as a harmless warning.</p>
<p>However, when I run my script which uses ExtractCenterline and CrossSectionAnalysis,  centerline extraction works fine but the line “cross_section_logic.run()” triggers the following:</p>
<blockquote>
<p>File “/home/qiluser/Slicer/slicer.org/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-scripted-modules/CrossSectionAnalysis.py”, line 871, in run<br>
self.updateOutputTable(self.inputCenterlineNode, self.outputTableNode)<br>
File “/home/qiluser/Slicer/slicer.org/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-scripted-modules/CrossSectionAnalysis.py”, line 995, in updateOutputTable<br>
import vtkSlicerCrossSectionAnalysisModuleLogicPython as vtkSlicerCrossSectionAnalysisModuleLogic<br>
ImportError: libvtkSlicerShapeModuleMRML.so: cannot open shared object file: No such file or directory</p>
</blockquote>
<p>and I am unable to find anything like ‘SlicerShapeModule’ or related to ‘CrossSectionAnalysis’ as a dependency I could install.</p>

---

## Post #8 by @lassoan (2023-10-26 18:58 UTC)

<p>The easiest way to find out all the dependencies (including dependencies of dependencies) is to install the extension on a computer that has network access. If that is not feasible then you get dependencies for an extension from the <code>depends</code> field of its extension description file (.s4ext) in the <a href="https://github.com/Slicer/ExtensionsIndex/">Extensions Index</a>.</p>

---
