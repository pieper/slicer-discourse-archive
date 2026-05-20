---
topic_id: 47088
title: "Improved Python Package Installation Slicer Packaging"
date: 2026-05-19
url: https://discourse.slicer.org/t/47088
---

# Improved python package installation: slicer.packaging

**Topic ID**: 47088
**Date**: 2026-05-19
**URL**: https://discourse.slicer.org/t/improved-python-package-installation-slicer-packaging/47088

---

## Post #1 by @ebrahim (2026-05-19 15:58 UTC)

<p>An improved python package installation experience is now available out of the box for extension developers: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.packaging"><code>slicer.packaging</code></a>.</p>
<p>This feature was <a href="https://github.com/Slicer/Slicer/pull/9010">merged</a> about a month ago and is available in the preview version of Slicer.</p>
<p>The existing <code>slicer.util.pip_install</code> has been expanded in functionality to support a more interactive experience: a GUI like the one shown below when blocking, or the possibility to run without blocking the application.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9e372df086c99c3a720589043d5420ab994f3b8.png" data-download-href="/uploads/short-url/oeTZWF6cIwOFLMx3gMUSZ3YStOU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9e372df086c99c3a720589043d5420ab994f3b8.png" alt="image" data-base62-sha1="oeTZWF6cIwOFLMx3gMUSZ3YStOU" width="520" height="285"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">520×285 38.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Additionally, new functions have been added:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><strong>Function</strong></th>
<th><strong>Purpose</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>slicer.packaging.load_requirements(path)</code></td>
<td>Parse a <code>requirements.txt</code> into <code>Requirement</code> objects.</td>
</tr>
<tr>
<td><code>slicer.packaging.load_pyproject_dependencies(path)</code></td>
<td>Parse <code>[project.dependencies]</code> from a <code>pyproject.toml</code></td>
</tr>
<tr>
<td><code>slicer.packaging.pip_check(reqs)</code></td>
<td>Are the requirements already satisfied?</td>
</tr>
<tr>
<td><code>slicer.packaging.pip_install(...)</code></td>
<td>Install, with various modes and hooks.</td>
</tr>
<tr>
<td><code>slicer.packaging.pip_ensure(reqs, requester="...")</code></td>
<td>High-level workflow: check, prompt, install with progress, and offer restart if needed.</td>
</tr>
</tbody>
</table>
</div><p>The bottom line for extension developers is: Use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.packaging.pip_ensure"><code>slicer.packaging.pip_ensure</code></a>! If you need lower level control, you can instead use <code>slicer.packaging.pip_check</code> and <code>slicer.packaging.pip_install</code> directly.</p>
<p>See the following for more details:</p>
<ul>
<li>the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#python-package-management">python package management</a> section of the script repository</li>
<li>the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.packaging"><code>slicer.packaging</code> API docs</a></li>
<li>the <a href="https://www.kitware.com/improving-python-dependency-handling-for-3d-slicer-extension-development/">Kitware blog post</a></li>
</ul>

---
