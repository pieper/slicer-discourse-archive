# Slicer 5.6.1: Summary, Highlights, and Changelog

**Topic ID**: 33371
**Date**: 2023-12-12
**URL**: https://discourse.slicer.org/t/slicer-5-6-1-summary-highlights-and-changelog/33371

---

## Post #1 by @jcfr (2023-12-12 20:41 UTC)

<h1><a name="p-104599-table-of-contents-1" class="anchor" href="#p-104599-table-of-contents-1" aria-label="Heading link"></a>Table of Contents</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--changelog">Changelog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>Slicer 5.6.1 is a patch release published in December 2023, aimed at addressing various issues reported by the community and providing bug fixes, enhancements, and improvements.</p>
<p>For more details and a comprehensive list of changes, enhancements, and highlights in the Slicer 5.6 release, please also refer to the <a href="https://discourse.slicer.org/t/slicer-5-6-summary-highlights-and-changelog/33140">Slicer 5.6 release notes</a>.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<h1 id="heading--changelog">Changelog</h1>
<ul>
<li><a href="#heading--improvements">Improvements</a></li>
<li><a href="#heading--fixes">Fixes</a></li>
<li><a href="#heading--build-system">Build-system</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
</ul>
<h2 id="heading--improvements">Improvements</h2>
<ul>
<li>Disable pip version check (<a href="https://github.com/Slicer/Slicer/pull/7466">PR-7466</a>)</li>
<li>Streamline Endoscopy UX by removing the “Use this curve” button (<a href="https://github.com/Slicer/Slicer/pull/7462">PR-7462</a>)</li>
<li>Make Tables module translatable (<a href="https://github.com/Slicer/Slicer/pull/7459">PR-7459</a>)</li>
</ul>
<h2 id="heading--fixes">Fixes</h2>
<ul>
<li>Restore maximization of view on a double-click event (<a href="https://github.com/Slicer/Slicer/pull/7463">PR-7463</a>)</li>
<li>Fix loading of sequence nodes (<a href="https://github.com/Slicer/Slicer/pull/7469">PR-7469</a>)</li>
<li>Fix vtkQtTranslator leak on quick exit (<a href="https://github.com/Slicer/Slicer/pull/7465">PR-7465</a>)</li>
<li>Fix temporary folder containing special characters (<a href="https://github.com/Slicer/Slicer/pull/7460">PR-7460</a>)</li>
<li>Workaround for Slicer hang on <code>scipy.linalg</code> import on Windows 11 (<a href="https://github.com/Slicer/Slicer/pull/7468">PR-7468</a>)</li>
<li>Fix scripted loadable module importing wrapped classes (<a href="https://github.com/Slicer/Slicer/pull/7464">PR-7464</a>)</li>
</ul>
<h2 id="heading--dependencies">Dependencies</h2>
<ul>
<li>Update VTK to fix <code>vtkSMPToolsAPI</code> static initialization order issue (<a href="https://github.com/Slicer/Slicer/pull/7467">PR-7467</a>)</li>
</ul>
<h2 id="heading--build-system">Build-system</h2>
<ul>
<li>Update GitHub CI workflow to be release-specific (<a href="https://github.com/Slicer/Slicer/pull/7461">PR-7461</a>)</li>
</ul>

---
