# NVIDIA AIAA server internal error

**Topic ID**: 17988
**Date**: 2021-06-07
**URL**: https://discourse.slicer.org/t/nvidia-aiaa-server-internal-error/17988

---

## Post #1 by @Chenglin_Zhu (2021-06-07 02:59 UTC)

<p>Hello Andras,</p>
<p><strong>Could you please help me with this error message when using the Nvidia Segmentation extension:</strong></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 492, in onClickAnnotation
    result_file = self.logic.dextr3d(in_file, session_id, model, pointSet)
  File "/Applications/Slicer.app/Contents/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 1112, in dextr3d
    session_id=session_id,
  File "/Applications/Slicer.app/Contents/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py", line 287, in dextr3d
    raise AIAAException(AIAAError.SERVER_ERROR, 'Status: {}; Response: {}'.format(status, form))
NvidiaAIAAClientAPI.client_api.AIAAException: (3, 'Status: 500; Response: b\'&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;\\n&lt;title&gt;500 Internal Server Error&lt;/title&gt;\\n&lt;h1&gt;Internal Server Error&lt;/h1&gt;\\n&lt;p&gt;The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.&lt;/p&gt;\\n\'')
</code></pre>
<p>thank you</p>

---

## Post #2 by @lassoan (2021-06-07 04:13 UTC)

<p>There is an issue with the free server that we have set up that we expect to resolve within a few weeks (<a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/62" class="inline-onebox">Slicer default server needs an upgrade to latest version of AIAA/Clara · Issue #62 · NVIDIA/ai-assisted-annotation-client · GitHub</a>). You can either wait for that fix or set up your own Clara server.</p>

---
