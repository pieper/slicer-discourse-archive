---
topic_id: 10500
title: "Nvdia Aiaa Server Error"
date: 2020-03-02
url: https://discourse.slicer.org/t/10500
---

# NVDIA AIAA server error

**Topic ID**: 10500
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/nvdia-aiaa-server-error/10500

---

## Post #1 by @Flash (2020-03-02 16:45 UTC)

<p>Hello,</p>
<p>I have set up AIAA server and downloaded model from NGC which is visible in Slicer.<br>
When I try to run the Auto-segmentation-clara_mri_seg_brain_tumors_br16_full or any  other pre-loaded model.<br>
It throws an error :<br>
Traceback (most recent call last):<br>
File “C:/Users/Biocliq/AppData/Roaming/NA-MIC/Extensions-28793/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 358, in createAiaaSessionIfNotExists<br>
in_file, session_id = self.logic.createSession(inputVolume)<br>
File “C:/Users/Biocliq/AppData/Roaming/NA-MIC/Extensions-28793/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 965, in createSession<br>
response = aiaaClient.create_session(in_file)<br>
File “C:\Users\Biocliq\AppData\Roaming\NA-MIC\Extensions-28793\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 108, in create_session<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, response))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 500; Response: b’{“error”:{“message”:[],“type”:“NotFound”},“success”:false}\n’’)</p>
<p>Kindly Respond!!</p>

---

## Post #2 by @lassoan (2020-03-03 02:32 UTC)

<p>A post was merged into an existing topic: <a href="/t/nviaa-aiaa-segmentation-error/10503">NVIAA AIAA segmentation error</a></p>

---

## Post #3 by @lassoan (2020-03-03 02:32 UTC)



---
