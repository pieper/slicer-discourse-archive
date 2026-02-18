# NAC Brain Atlas 2015 from Data Store is giving scene hierarchy errors after loading

**Topic ID**: 7160
**Date**: 2019-06-13
**URL**: https://discourse.slicer.org/t/nac-brain-atlas-2015-from-data-store-is-giving-scene-hierarchy-errors-after-loading/7160

---

## Post #1 by @mikebind (2019-06-13 14:56 UTC)

<p>Hello, the NAC Brain Atlas 2015 from the Data Store loads without errors, but after trying to load one of the saved scene views from that mrb, Slicer 4.10.1 reports the following errors and the Subject Hierarchy in the Data view becomes unresponsive:</p>
<p>bool __cdecl qSlicerSubjectHierarchyFolderPlugin::resolveHierarchies(void) : Unable to find subject hierarchy item for hierarchy node  AnnotationHierarchy_2<br>
bool __cdecl qSlicerSubjectHierarchyFolderPlugin::resolveHierarchies(void) : Unable to find subject hierarchy item for hierarchy node  SceneViewHierarchy</p>

---

## Post #2 by @lassoan (2019-06-13 15:16 UTC)

<p>Can you reproduce the problem with the latest stable version (Slicer-4.10.2)?</p>

---
