# Automatic test with --disable-cli-modules doesn't load dependencies

**Topic ID**: 20478
**Date**: 2021-11-03
**URL**: https://discourse.slicer.org/t/automatic-test-with-disable-cli-modules-doesnt-load-dependencies/20478

---

## Post #1 by @simonoxen (2021-11-03 17:13 UTC)

<p>Automatic tests use the <code>--disable-cli-modules</code> flag and the <code>--additional-module-paths</code> specifying cli modules. This reuslts however in the cli modules not being loaded (and thus the test failing for modules which depend on those cli).</p>
<p>When running the same test command without the  <code>--disable-cli-modules</code> this error doesn’t occur.</p>
<p>See <a href="https://slicer.cdash.org/test/19994249" rel="noopener nofollow ugc">this test</a> as reference.</p>

---

## Post #2 by @lassoan (2021-11-04 03:37 UTC)

<p><code>--disable-cli-modules</code> slightly decreases Slicer startup time, so it is useful for tests that don’t need CLI modules. If your test requires CLI modules then separate tests could be added, but maybe it would be nicer to add an option (<code>TESTING_WITH_CLI</code> or something similar) to <code>slicerMacroBuildScriptedModule</code> in <a href="https://github.com/Slicer/Slicer/blob/722a18ffa6b3b3bf515cdef293de418c7844a8cc/CMake/SlicerMacroBuildScriptedModule.cmake#L23-L25">SlicerMacroBuildScriptedModule.cmake</a> to not disable CLI modules for tests.</p>

---
