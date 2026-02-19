---
topic_id: 27507
title: "Extension Name Vs Repo Name"
date: 2023-01-27
url: https://discourse.slicer.org/t/27507
---

# Extension name vs repo name

**Topic ID**: 27507
**Date**: 2023-01-27
**URL**: https://discourse.slicer.org/t/extension-name-vs-repo-name/27507

---

## Post #1 by @smrolfe (2023-01-27 21:19 UTC)

<p>I am submitting a new extension: <a href="https://github.com/Slicer/ExtensionsIndex/pull/1908" class="inline-onebox" rel="noopener nofollow ugc">Add MEMOS extension by smrolfe · Pull Request #1908 · Slicer/ExtensionsIndex · GitHub</a><br>
and would like to understand how the extension names are set in the catalog.</p>
<p>I would like the display name of the extension to be “MEMOS”, and have named to repo to “SlicerMEMOS” according to the guidelines. If the extension description file I submitted is “MEMOS.s4ext”, will the extension catalog show “MEMOS”?</p>

---

## Post #2 by @jcfr (2023-01-27 22:30 UTC)

<p>The extension name is indeed <code>MEMOS</code></p>
<p>The extension name is derived from the project name set in the <code>CMakeLists.txt</code>.</p>
<h3><a name="p-89624-details-1" class="anchor" href="#p-89624-details-1" aria-label="Heading link"></a>Details</h3>
<p>This is confirmed by reviewing the project name defined in the top-level <code>CMakeLists.txt</code> <sup class="footnote-ref"><a href="#footnote-89624-1" id="footnote-ref-89624-1">[1]</a></sup> using <code>project(MEMOS)</code>.</p>
<p>Indeed, the project name is then used by CMake code associated with <code>include(${Slicer_USE_FILE})</code> <sup class="footnote-ref"><a href="#footnote-89624-2" id="footnote-ref-89624-2">[2]</a></sup> to set the variable <code>EXTENSION_NAME</code>.</p>
<p>Itself used to define the extension name used <sup class="footnote-ref"><a href="#footnote-89624-3" id="footnote-ref-89624-3">[3]</a></sup> to upload the package on the server.</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-89624-1" class="footnote-item"><p><a href="https://github.com/SlicerMorph/SlicerMEMOS/blob/24a02f686adfd7542df3fa14a97097723302bc8c/CMakeLists.txt#L3">https://github.com/SlicerMorph/SlicerMEMOS/blob/24a02f686adfd7542df3fa14a97097723302bc8c/CMakeLists.txt#L3</a> <a href="#footnote-ref-89624-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-89624-2" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/38056565bb247c7affb80fdd0d861197eaa50a31/CMake/UseSlicer.cmake.in#L56-L78">https://github.com/Slicer/Slicer/blob/38056565bb247c7affb80fdd0d861197eaa50a31/CMake/UseSlicer.cmake.in#L56-L78</a> <a href="#footnote-ref-89624-2" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-89624-3" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/38056565bb247c7affb80fdd0d861197eaa50a31/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake#L278-L295">https://github.com/Slicer/Slicer/blob/38056565bb247c7affb80fdd0d861197eaa50a31/Extensions/CMake/SlicerExtensionPackageAndUploadTarget.cmake#L278-L295</a> <a href="#footnote-ref-89624-3" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---
