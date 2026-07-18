---
topic_id: 47654
title: "Slicer AURs throw CMAKE errors"
date: 2026-07-17
url: https://discourse.slicer.org/t/47654
last_bumped: 2026-07-17T13:14:02.099Z
---

# Slicer AURs throw CMAKE errors

**Topic ID**: 47654
**Date**: 2026-07-17
**URL**: https://discourse.slicer.org/t/slicer-aurs-throw-cmake-errors/47654

---

## Post #1 by @kikubamutwe (2026-07-17 13:14 UTC)

<p>The AURs listed for Arch in the docs do not work on CachyOS: <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#linux" class="inline-onebox" rel="noopener nofollow ugc">Getting Started — 3D Slicer documentation</a></p>
<p>They throw CMAKE errors as follows:</p>
<pre><code class="lang-auto">patching file CMakeLists.txt
CMake Error at CMakeLists.txt:25 (CMAKE_MINIMUM_REQUIRED):
Compatibility with CMake &lt; 3.5 has been removed from CMake.

Update the VERSION argument  value.  Or, use the ... syntax
to tell CMake that the project requires at least  but has been updated
to work with policies introduced by  or earlier.

Or, add -DCMAKE_POLICY_VERSION_MINIMUM=3.5 to try configuring anyway.

-- Configuring incomplete, errors occurred!
</code></pre>

---
