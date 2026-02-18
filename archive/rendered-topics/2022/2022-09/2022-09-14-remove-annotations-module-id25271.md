# Remove Annotations module

**Topic ID**: 25271
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/remove-annotations-module/25271

---

## Post #1 by @lassoan (2022-09-14 16:52 UTC)

<p>Annotations module, which provides <code>vtkMRMLAnnotationROI</code> and <code>vtkMRMLAnnotationRuler</code> nodes have been deprecated since April 2021 and <a href="https://github.com/Slicer/Slicer/pull/6524">will be removed in Slicer-5.4 stable release</a> (around early 2023).<br>
all annotation nodes will be automatically converted to markup nodes when a scene is loaded</p>
<p>Starting in Slicer-5.3 preview releases (expected in a couple of weeks) Slicer will automatically convert annotation nodes to markup nodes to corresponding markup nodes when a scene is loaded.</p>
<p>Extensions that still use annotation nodes will have to be updated to use markup nodes before end of this year so that they continue to work with Slicer-5.4.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.3%3A_Removed_Annotation_module">This section</a> of the migration guide should help with implementing these changes, but we are happy to answer here any questions or help with any specific problems.</p>

---
