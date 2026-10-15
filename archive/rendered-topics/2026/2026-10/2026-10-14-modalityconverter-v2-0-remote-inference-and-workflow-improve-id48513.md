---
topic_id: 48513
title: "ModalityConverter v2.0 - Remote Inference and Workflow Improvements"
date: 2026-10-14
url: https://discourse.slicer.org/t/48513
last_bumped: 2026-10-14T15:21:54.981Z
---

# ModalityConverter v2.0 - Remote Inference and Workflow Improvements

**Topic ID**: 48513
**Date**: 2026-10-14
**URL**: https://discourse.slicer.org/t/modalityconverter-v2-0-remote-inference-and-workflow-improvements/48513

---

## Post #1 by @ciro.raggio (2026-10-14 15:21 UTC)

<p>I’ve been working on a major update to <a href="https://github.com/ciroraggio/SlicerModalityConverter" rel="noopener nofollow ugc">SlicerModalityConverter</a>.</p>
<p>Here’s a video introducing the new features, with two use cases: generating synthetic CT from a T1-weighted brain MRI and synthetic PET from a chest CT scan.</p>
<p>This release focuses on improving the inference workflow in 3D Slicer, with several practical additions:</p>
<p>• An improved inference process that speeds up local inference while keeping 3D Slicer responsive.<br>
• Support for remote inference, including HTTP/HTTPS connections and authentication.<br>
• Real-time monitoring of local and remote resources, with the ability to select resources on the remote machine.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/beef3f2ab98cec27727a3df43e766eb93515653b.mp4">
  </div><p></p>
<p>If you would like to integrate your own model for personal use on your local machine, or make it available to the 3D Slicer community through the extension, the <a href="https://github.com/ciroraggio/SlicerModalityConverter" rel="noopener nofollow ugc">GitHub repository</a> includes a <a href="https://github.com/ciroraggio/SlicerModalityConverter/blob/main/README.md#how-to-integrate-a-custom-model" rel="noopener nofollow ugc">guide to help you get started</a>.</p>
<p>The goal is to make medical image synthesis more accessible to researchers and developers working with AI and medical imaging in 3D Slicer.</p>
<p>I hope you’ll find it useful. Feedback and contributions are always welcome! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=15" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>

---
