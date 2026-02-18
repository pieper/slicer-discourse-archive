# NVidia AIAA segment editor effect returns "URL not found" error

**Topic ID**: 16811
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/nvidia-aiaa-segment-editor-effect-returns-url-not-found-error/16811

---

## Post #1 by @akmal871026 (2021-03-28 22:12 UTC)

<p>Hi all, I got this error when trying to use Nvidia Extension for liver and tumor segmentation. anyone can help me?</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 410, in onClickSegmentation<br>
extreme_points, result_file = self.logic.segmentation(in_file, session_id, model)<br>
File “C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1092, in segmentation<br>
session_id=session_id,<br>
File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 389, in inference<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, form))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 404; Response: b’\n404 Not Found\n</p><h1>Not Found</h1>\n<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>\n’’)<p></p>

---

## Post #2 by @jamesobutler (2021-03-28 23:28 UTC)

<p>Hi <a class="mention" href="/u/akmal871026">@akmal871026</a>, please see this thread linked below</p>
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
