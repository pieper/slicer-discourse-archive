# ROI fiducial placement in Surface Cut

**Topic ID**: 13059
**Date**: 2020-08-17
**URL**: https://discourse.slicer.org/t/roi-fiducial-placement-in-surface-cut/13059

---

## Post #1 by @Slicer410 (2020-08-17 22:03 UTC)

<p>Hi<br>
I’m new in Slicer.  I’ve installed Slicer 4.10.2 for Windows 8.</p>
<p>While trying to use Surface Cut, I can see that Fiducial Placement doesn’t work. My button appears as it’s inactive (grey) and I can’t click on it.</p>
<p>I’ve already installed “SegmentEditorExtraEffects” extensión, including “Marks Up To Model”, then I re-started slicer, but it sill doesn´t work.</p>
<p>The extension was installed in the folder: AppData</p>
<p>Error:</p>
<p>Cannot load library C:\Users\whoareyou\AppData\Roaming\NA-MIC\Extensions-28257\MarkupsToModel\lib\Slicer-4.10\qt-loadable-modules\qSlicerMarkupsToModelModule.dll: No se puede encontrar el m?dulo especificado.</p>
<p>[DEBUG][Python] 17.08.2020 15:30:55 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations</p>
<p>[DEBUG][Python] 17.08.2020 15:30:59 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor</p>
<p>[DEBUG][Python] 17.08.2020 15:30:59 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics</p>
<p>[INFO][Python] 17.08.2020 15:31:01 [Python] (C:/Users/whoareyou/AppData/Roaming/NA-MIC/Extensions-28257/NvidiaAIAssistedAnnotation/lib/Slicer-4.10/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/whoareyou/AppData/Roaming/NA-MIC/Extensions-28257/NvidiaAIAssistedAnnotation/lib/Slicer-4.10/qt-scripted-modules</p>

---

## Post #2 by @lassoan (2020-08-17 22:09 UTC)

<p>Sorry, when we updated the extension for Slicer-4.11, something went wrong. Until we fix it, you can use Slicer-4.11.</p>

---
