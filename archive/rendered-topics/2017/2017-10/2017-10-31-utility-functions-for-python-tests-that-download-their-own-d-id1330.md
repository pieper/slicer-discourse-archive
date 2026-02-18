# Utility functions for python tests that download their own (DICOM or other) data from the web

**Topic ID**: 1330
**Date**: 2017-10-31
**URL**: https://discourse.slicer.org/t/utility-functions-for-python-tests-that-download-their-own-dicom-or-other-data-from-the-web/1330

---

## Post #1 by @cpinter (2017-10-31 14:29 UTC)

<p>I’m writing a few new automated python tests for extensions, and realized that I keep adding the same functions in my tests unchanged. These functions</p>
<ul>
<li>Download data, unzip to temp folder, verify total number of unzipped files</li>
<li>Import data to temporary DICOM database from the above folder</li>
<li>Select loadables, verify plugin selection, and load loadables</li>
</ul>
<p>Do you think it would make sense to add these in the ScriptedLoadableModuleTest class?</p>

---

## Post #2 by @jcfr (2017-10-31 14:34 UTC)

<p>It could be added to the <code>slicer.testing</code>  module.</p>
<p>Ideally, it could be used as a function or a context manager.</p>
<p>something like:</p>
<pre><code class="lang-auto">with TemporaryDICOMData(url="http://path/to/file.zip") as loader:
  assert loader.selected_plugins == ["plugin1", ...]
  [...]
</code></pre>

---

## Post #3 by @cpinter (2017-10-31 18:46 UTC)

<p>Thanks! I’ll try to do it like this then. I’ll be back with a PR.</p>

---

## Post #4 by @cpinter (2017-11-06 20:53 UTC)

<p>I think I’ll add this to <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py</a> instead. There is a feature very similar to the proposed one here already, and it would be confusing to separate them.</p>

---

## Post #5 by @cpinter (2017-11-08 21:36 UTC)

<p>I issued the pull request: <a href="https://github.com/Slicer/Slicer/pull/835">https://github.com/Slicer/Slicer/pull/835</a></p>
<p>I tested it with SubjectHierarchyGenericSelfTest and GelDosimetryAnalysis, both work well.</p>

---
