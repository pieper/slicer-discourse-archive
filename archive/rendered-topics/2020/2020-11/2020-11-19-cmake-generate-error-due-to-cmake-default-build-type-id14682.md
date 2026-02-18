# CMake generate error due to CMAKE_DEFAULT_BUILD_TYPE

**Topic ID**: 14682
**Date**: 2020-11-19
**URL**: https://discourse.slicer.org/t/cmake-generate-error-due-to-cmake-default-build-type/14682

---

## Post #1 by @JaceYang (2020-11-19 03:54 UTC)

<p>Hello everyone<br>
When I use cmake-gui to build 3dSlicer,I run into this problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ea9c6a50a2ed9a674ec580daae29ae6c0acfd9.png" data-download-href="/uploads/short-url/w5HBw5Z1VJLm8Nmhh0cLCOmuiKZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ea9c6a50a2ed9a674ec580daae29ae6c0acfd9.png" alt="image" data-base62-sha1="w5HBw5Z1VJLm8Nmhh0cLCOmuiKZ" width="689" height="475" data-dominant-color="F3DADB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1268×874 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-11-19 04:11 UTC)

<p>CMAKE_DEFAULT_BUILD_TYPE must not be used with CMake &gt;=3.17 (see <a href="https://github.com/Slicer/Slicer/pull/4799">https://github.com/Slicer/Slicer/pull/4799</a> for details).</p>
<p>Please use latest stable or master version of Slicer source code and follow the current build instructions: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html</a></p>

---
