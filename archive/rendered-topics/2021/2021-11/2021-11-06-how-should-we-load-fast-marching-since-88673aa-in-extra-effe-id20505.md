---
topic_id: 20505
title: "How Should We Load Fast Marching Since 88673Aa In Extra Effe"
date: 2021-11-06
url: https://discourse.slicer.org/t/20505
---

# How should we load 'Fast marching' since 88673aa in extra effects?

**Topic ID**: 20505
**Date**: 2021-11-06
**URL**: https://discourse.slicer.org/t/how-should-we-load-fast-marching-since-88673aa-in-extra-effects/20505

---

## Post #1 by @chir.set (2021-11-06 11:14 UTC)

<p>Hi,</p>
<p>I usually load extra effects with --additional-module-paths. Since <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/commit/88673aa16b5c818f8319c7860eef73c361be985b" rel="noopener nofollow ugc">88673aa</a>, Fast Marching no longer works, yielding :</p>
<pre><code class="lang-auto">  File "/home/user/Documents/Slicer4/Custom_Ext/SlicerSegmentEditorExtraEffects/SegmentEditorFastMarching/SegmentEditorFastMarchingLib/SegmentEditorEffect.py", line 110, in onMarch
    self.fastMarching(self.percentMax.value)
  File "/home/user/Documents/Slicer4/Custom_Ext/SlicerSegmentEditorExtraEffects/SegmentEditorFastMarching/SegmentEditorFastMarchingLib/SegmentEditorEffect.py", line 175, in fastMarching
    import vtkSlicerSegmentEditorFastMarchingModuleLogicPython
ModuleNotFoundError: No module named 'vtkSlicerSegmentEditorFastMarchingModuleLogicPython'
</code></pre>
<p>There are now *.cxx files in SegmentEditorFastMarching/Logic/ folder, so I guess SlicerSegmentEditorExtraEffects needs to be built on the dev machine. If so, how should we proceed if we don’t use factory built Slicer  (Linux) ?</p>
<p>Thank you.</p>

---

## Post #2 by @chir.set (2021-11-06 12:19 UTC)

<p>OK, I got a successful build and packaging on the dev machine with :</p>
<p><code>ccmake -DSlicer_DIR:PATH=/home/arc/src/Slicer-SuperBuild9/Slicer-build -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo -DSlicer_USE_GIT_PROTOCOL:BOOL=OFF $HOME/src/SlicerSegmentEditorExtraEffects</code></p>
<p>Will next test it, should just work.</p>

---
