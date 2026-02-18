# Sometimes slicer3d crash when excuting python coded

**Topic ID**: 22224
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/sometimes-slicer3d-crash-when-excuting-python-coded/22224

---

## Post #1 by @yllgl (2022-03-01 05:19 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ae3003667cd26823f470f413e2bd4d20b44250f.gif" alt="动画" data-base62-sha1="cY1jNGfuFY46Tqs4GzNKxYALn4P" width="690" height="364" class="animated"><br>
My main.py file is as follows:</p>
<pre><code class="lang-python">import slicer
import os
from pathlib import Path
def getres(patient):
    res = {'CT':{'轴':None,'冠':None,'矢':None},'MR':{'轴':None,'冠':None,'矢':None}}
    for study in slicer.dicomDatabase.studiesForPatient(patient):
        series = slicer.dicomDatabase.seriesForStudy(study)
        for seriesIndex, currentSeries in enumerate(series, start=1):
            files = slicer.dicomDatabase.filesForSeries(currentSeries)
            if len(files):
                seriesDescription = slicer.dicomDatabase.fileValue(files[0], '0008,103E')
                def _getPluginAndLoadableForFiles(seriesDescription, files):
                    for pluginName in ['MultiVolumeImporterPlugin', 'DICOMScalarVolumePlugin']:
                        plugin = slicer.modules.dicomPlugins[pluginName]()
                        loadables = plugin.examine([files])
                        if len(loadables) == 0:
                            continue
                        loadables.sort(key=lambda x: x.confidence, reverse=True)
                        if loadables[0].confidence &gt; 0.1:
                            return plugin, loadables[0]
                plugin, loadable = _getPluginAndLoadableForFiles(seriesDescription, files)
                node = plugin.load(loadable)
                if node:
                    path = Path(files[0])
                    location = path.parent
                    mode = location.parent
                    patient = mode.parent
                    location = location.name
                    mode = mode.name
                    patient = patient.name
                    if "CT" in location:
                        if '轴' in location:
                            res['CT']['轴'] = node
                        elif '冠' in location:
                            res['CT']['冠'] = node
                        elif '矢' in location:
                            res['CT']['矢'] = node
                    elif "MR" in location:
                        if '轴' in location:
                            res['MR']['轴'] = node
                        elif '冠' in location:
                            res['MR']['冠'] = node
                        elif '矢' in location:
                            res['MR']['矢'] = node
    res['CT']['轴'].SetName("CT-轴")
    res['CT']['冠'].SetName("CT-冠")
    res['CT']['矢'].SetName("CT-矢")
    res['MR']['轴'].SetName("MR-轴")
    res['MR']['冠'].SetName("MR-冠")
    res['MR']['矢'].SetName("MR-矢")
    return res
</code></pre>
<p>message:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Session start time .......: 2022-03-01 13:09:26
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Slicer version ...........: 4.13.0-2021-12-10 (revision 30497 / 6e85ffc) win-amd64 - installed release
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 19042, Code Page 65001) - 64-bit
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Memory ...................: 15790 MB physical, 18350 MB virtual
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 7 4800H with Radeon Graphics         , 16 cores, 16 logical processors
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Application path .........: D:/Slicer 4.13.0-2021-12-10/bin
[DEBUG][Qt] 01.03.2022 13:09:26 [] (unknown:0) - Additional module paths ..: NA-MIC/Extensions-30497/SlicerJupyter/lib/Slicer-4.13/qt-loadable-modules, NA-MIC/Extensions-30497/SlicerJupyter/lib/Slicer-4.13/qt-scripted-modules, NA-MIC/Extensions-30497/SurfaceWrapSolidify/lib/Slicer-4.13/qt-scripted-modules, NA-MIC/Extensions-30497/SegmentEditorExtraEffects/lib/Slicer-4.13/qt-loadable-modules, NA-MIC/Extensions-30497/SegmentEditorExtraEffects/lib/Slicer-4.13/qt-scripted-modules, NA-MIC/Extensions-30497/MarkupsToModel/lib/Slicer-4.13/qt-loadable-modules, NA-MIC/Extensions-30497/SlicerANTs/lib/Slicer-4.13/cli-modules, NA-MIC/Extensions-30497/SlicerANTs/lib/Slicer-4.13/qt-scripted-modules
[DEBUG][Python] 01.03.2022 13:09:28 [Python] (D:\Slicer 4.13.0-2021-12-10\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 01.03.2022 13:09:29 [Python] (D:\Slicer 4.13.0-2021-12-10\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 01.03.2022 13:09:29 [Python] (D:\Slicer 4.13.0-2021-12-10\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 01.03.2022 13:09:29 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 01.03.2022 13:10:32 [] (unknown:0) - Python console user input: import sys
[DEBUG][Qt] 01.03.2022 13:10:53 [] (unknown:0) - Python console user input: sys.path.append("D:/slicerExportData")
[DEBUG][Qt] 01.03.2022 13:11:02 [] (unknown:0) - Python console user input: from main  import getres
[INFO][Python] 01.03.2022 13:11:12 [Python] (D:/Slicer 4.13.0-2021-12-10/bin/../lib/Slicer-4.13/qt-scripted-modules/DICOMScalarVolumePlugin.py:384) - Loading with imageIOName: GDCM
</code></pre>

---

## Post #2 by @yllgl (2022-03-01 05:32 UTC)

<p>The most interesting thing is the crash disappears when I add a line <code>print('1')</code>  before _getPluginAndLoadableForFiles.</p>

---

## Post #3 by @lassoan (2022-03-01 05:50 UTC)

<p>Could you please test if you can reproduce this on the latest Slicer Preview Release?</p>

---

## Post #5 by @yllgl (2022-03-01 10:09 UTC)

<p>not useful. Although I successfully run once a time, after that, I still get into crash.</p>

---

## Post #6 by @lassoan (2022-03-08 19:04 UTC)

<p>Do you have any problems if you load the images using the DICOM module GUI?<br>
Does it help if you change the <code>DICOM reader approach</code> in menu: Application Settings / DICOM?</p>
<p>If you need help with investigating the problem, please provide a minimal example (as short as possible, remove all parts that are not necessary for reproducing the crash) and corresponding data that reproduces the issue. If the problem is not reproducible with publicly available DICOM data sets then you would need to share an example data set, too (remove all patient information; you can also blank out the image data).</p>

---
