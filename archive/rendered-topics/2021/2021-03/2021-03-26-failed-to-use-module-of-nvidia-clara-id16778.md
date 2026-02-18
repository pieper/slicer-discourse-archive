# Failed to use module of NVidia clara

**Topic ID**: 16778
**Date**: 2021-03-26
**URL**: https://discourse.slicer.org/t/failed-to-use-module-of-nvidia-clara/16778

---

## Post #1 by @pcjaywalker (2021-03-26 15:21 UTC)

<p>Problem report for Slicer 4.13.0-2021-03-24 win-amd64: [please describe expected and actual behavior]</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/pcjaywalker/AppData/Local/NA-MIC/Slicer 4.13.0-2021-03-24/NA-MIC/Extensions-29799/NvidiaAIAssistedAnnotation/lib/Slicer-4.13/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 492, in onClickAnnotation
    result_file = self.logic.dextr3d(in_file, session_id, model, pointSet)
  File "C:/Users/pcjaywalker/AppData/Local/NA-MIC/Slicer 4.13.0-2021-03-24/NA-MIC/Extensions-29799/NvidiaAIAssistedAnnotation/lib/Slicer-4.13/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 1112, in dextr3d
    session_id=session_id,
  File "C:\Users\pcjaywalker\AppData\Local\NA-MIC\Slicer 4.13.0-2021-03-24\NA-MIC\Extensions-29799\NvidiaAIAssistedAnnotation\lib\Slicer-4.13\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py", line 287, in dextr3d
    raise AIAAException(AIAAError.SERVER_ERROR, 'Status: {}; Response: {}'.format(status, form))
NvidiaAIAAClientAPI.client_api.AIAAException: (3, 'Status: 500; Response: b\'&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;\\n&lt;title&gt;500 Internal Server Error&lt;/title&gt;\\n&lt;h1&gt;Internal Server Error&lt;/h1&gt;\\n&lt;p&gt;The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.&lt;/p&gt;\\n\'')
</code></pre>

---

## Post #2 by @jamesobutler (2021-03-26 16:07 UTC)

<aside class="quote" data-post="2" data-topic="16643">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/nvidia-aiaa-default-server-error-when-running-auto-segmentation/16643/2">NVIDIA AIAA default server error when running auto-segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Unfortunately, the liver model and the default server is not compatible with the latest NVidia AIAA client version (see error report <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/76" rel="noopener nofollow ugc">here</a>). 
You can segment from boundary points (that is faster and more robust anyway) or set up your own server as described in the link provided in <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#setup" rel="noopener nofollow ugc">setup instructions</a>.
  </blockquote>
</aside>


---
