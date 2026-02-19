---
topic_id: 43103
title: "Configuring The Running Environment For An Extension Build T"
date: 2025-05-26
url: https://discourse.slicer.org/t/43103
---

# Configuring the running environment for an extension build-tree

**Topic ID**: 43103
**Date**: 2025-05-26
**URL**: https://discourse.slicer.org/t/configuring-the-running-environment-for-an-extension-build-tree/43103

---

## Post #1 by @RafaelPalomar (2025-05-26 14:01 UTC)

<p>Hello. Is there any reason for the following code not taking effect when added to a <code>External_something.cmake</code> file in a superbuild extension?</p>
<pre><code class="lang-auto">  set(${proj}_ENVVARS_LAUNCHER_BUILD
    "VAR1=${VAR1}"
    "VAR2=anything"
    )
  mark_as_superbuild(
    VARS ${proj}_ENVVARS_LAUNCHER_BUILD
    LABELS "ENVVARS_LAUNCHER_BUILD"
    )
</code></pre>
<p>This, in turn, works fine:</p>
<pre><code class="lang-auto">  # python paths
  set(${proj}_PYTHONPATH_LAUNCHER_BUILD
    ${EP_BINARY_DIR}/lib/python3/site-packages
    )
  mark_as_superbuild(
    VARS ${proj}_PYTHONPATH_LAUNCHER_BUILD
    LABELS "PYTHONPATH_LAUNCHER_BUILD"
    )
</code></pre>
<p>And I can see that the <code>AdditionalLauncherSettings.ini</code> file includes the expected path in the <code>PYTHONPATH</code> variable.</p>
<p>Any pointers? Thank you in advance.</p>

---

## Post #2 by @RafaelPalomar (2025-05-26 20:02 UTC)

<p>I’ve done some investigation and it seems to be a bug in the Slicer CMake infrastructure for generating the <code>AdditionalLauncherSettings.ini</code> file. I’ll come up with PR to solve this</p>

---
