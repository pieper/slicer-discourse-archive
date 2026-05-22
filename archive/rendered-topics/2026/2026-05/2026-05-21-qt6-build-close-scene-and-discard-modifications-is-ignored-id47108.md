---
topic_id: 47108
title: "Qt6 Build Close Scene And Discard Modifications Is Ignored"
date: 2026-05-21
url: https://discourse.slicer.org/t/47108
---

# Qt6 build: close scene and discard modifications is ignored

**Topic ID**: 47108
**Date**: 2026-05-21
**URL**: https://discourse.slicer.org/t/qt6-build-close-scene-and-discard-modifications-is-ignored/47108

---

## Post #1 by @chir.set (2026-05-21 17:10 UTC)

<p>I am experimenting with using Slicer built with <code>Qt6</code> on <code>Arch Linux</code> on a daily basis.</p>
<p>When a scene is closed, the <code>SaveBeforeClosingScene</code> appears. When the <code>Close scene (discard modifications)</code> button is clicked, the scene is not closed as it happens with <code>Qt5</code> builds. Instead, the <code>SaveSceneAndUnsavedData</code> dialog appears. The only way to close the scene and discard modifications is to uncheck all items and click the <code>Save</code> button.</p>
<p>That’s a manageable annoyance, I just wish to bring it to your attention.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a52a259e9a05fe9e8a2d71c69f36b403a0accc.png" data-download-href="/uploads/short-url/wLxcFsECs8h5FMND9eH9noPtGLW.png?dl=1" title="SaveBeforeClosingScene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5a52a259e9a05fe9e8a2d71c69f36b403a0accc_2_690x95.png" alt="SaveBeforeClosingScene" data-base62-sha1="wLxcFsECs8h5FMND9eH9noPtGLW" width="690" height="95" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5a52a259e9a05fe9e8a2d71c69f36b403a0accc_2_690x95.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a52a259e9a05fe9e8a2d71c69f36b403a0accc.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a52a259e9a05fe9e8a2d71c69f36b403a0accc.png 2x" data-dominant-color="484A4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SaveBeforeClosingScene</span><span class="informations">902×125 32.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b733000acfa51f9b4a8865d5fcba803d8da07092.png" data-download-href="/uploads/short-url/q8EDXeuL4huQgysx1NSpXWwA9Ds.png?dl=1" title="SaveSceneAndUnsavedData" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b733000acfa51f9b4a8865d5fcba803d8da07092_2_690x220.png" alt="SaveSceneAndUnsavedData" data-base62-sha1="q8EDXeuL4huQgysx1NSpXWwA9Ds" width="690" height="220" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b733000acfa51f9b4a8865d5fcba803d8da07092_2_690x220.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b733000acfa51f9b4a8865d5fcba803d8da07092.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b733000acfa51f9b4a8865d5fcba803d8da07092.png 2x" data-dominant-color="373737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SaveSceneAndUnsavedData</span><span class="informations">868×278 43.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For precision, Slicer is built with <code>Qt 6.10.2</code> (to build CTK successfully) and runs equally with <code>6.10.2</code> and with system <code>6.11.1</code>.</p>

---
