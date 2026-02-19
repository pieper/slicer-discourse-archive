---
topic_id: 16910
title: "Extensions Manager Errors In 4 1 Macos Nightly"
date: 2021-04-01
url: https://discourse.slicer.org/t/16910
---

# Extensions manager errors in 4/1 MacOS nightly

**Topic ID**: 16910
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/extensions-manager-errors-in-4-1-macos-nightly/16910

---

## Post #1 by @hherhold (2021-04-01 18:17 UTC)

<p>MacOS latest nightly 4/1, downloaded moments ago after extremely cool images with ambient shadows.</p>
<p>Extensions manager very slow to come up, and I get the following in the console:</p>
<pre><code>DevTools listening on ws://127.0.0.1:1337/devtools/browser/9ae9e464-66ac-45f1-905a-c47398a57373
Remote debugging server started successfully. Try pointing a Chromium-based browser to http://127.0.0.1:1337
[47425:115715:0401/141148.634762:ERROR:gl_context_cgl.cc(118)] Error creating context.
"Error retrieving extension metadata: amd64, macosx, SurfaceWrapSolidify, 29807 ({87fefc7b-8af2-48f9-a19c-26d6eb03cf04}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, SegmentEditorExtraEffects, 29807 ({f5bb0a26-a3c1-4a1a-a7e7-650f8f8a6b20}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, MarkupsToModel, 29807 ({b2a63237-8345-48e8-af0a-239a17e45f51}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, RawImageGuess, 29807 ({123a18fb-bae8-4a1d-9e94-e4edda2760f3}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, SlicerIGT, 29807 ({f2dc8f93-3a0e-46de-80c1-014c537e07a3}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, SlicerJupyter, 29807 ({fd67a6aa-d5d4-4d15-8e8d-35defefebb18}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, SlicerOpenIGTLink, 29807 ({03520161-35ae-4a3d-9e13-cb101418ab67}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, Sandbox, 29807 ({76cd8d54-e5e0-422e-a279-bc438160ba76}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, SlicerMorph, 29807 ({e1cf78fc-d1d2-49c9-a7c0-db5e531ddcfa}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, SlicerDcm2nii, 29807 ({c23ee6f9-9c05-4d9b-ae86-0f7b266c2c29}: 5: Operation canceled)"
"Error retrieving extension metadata: amd64, macosx, Auto3dgm, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SegmentEditorExtraEffects, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, MarkupsToModel, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SurfaceWrapSolidify, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, RawImageGuess, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerDcm2nii, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerMorph, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Sandbox, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerIGT, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Auto3dgm, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerRadiomics, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerVMTK, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SegmentEditorExtraEffects, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, MarkupsToModel, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Sandbox, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerDcm2nii, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SurfaceWrapSolidify, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, RawImageGuess, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerMorph, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerIGT, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Auto3dgm, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerVMTK, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerOpenIGTLink, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Auto3dgm, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SurfaceWrapSolidify, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerVMTK, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, DebuggingTools, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerJupyter, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SegmentEditorExtraEffects, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, MarkupsToModel, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, RawImageGuess, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerMorph, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Sandbox, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerDcm2nii, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerIGT, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerOpenIGTLink, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, RawImageGuess, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SurfaceWrapSolidify, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Sandbox, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, Auto3dgm, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SegmentEditorExtraEffects, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerMorph, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, MarkupsToModel, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerDcm2nii, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerIGT, 29807 (No data)"
"Error retrieving extension metadata: amd64, macosx, SlicerPRISMRendering, 29807 (No data)"</code></pre>

---

## Post #2 by @hherhold (2021-04-02 17:13 UTC)

<p>Never mind, this works now. Apologies for any confusion.</p>

---

## Post #3 by @lassoan (2021-04-03 01:03 UTC)

<p>The extension server sometimes becomes temporarily overloaded, as described here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-manager-does-not-show-any-extensions" class="inline-onebox">Extensions Manager — 3D Slicer documentation</a></p>
<p>We’ll replace the server backend soon (<a class="mention" href="/u/jcfr">@jcfr</a> may have more specific date) and then the server will be both much faster and more reliable.</p>

---
