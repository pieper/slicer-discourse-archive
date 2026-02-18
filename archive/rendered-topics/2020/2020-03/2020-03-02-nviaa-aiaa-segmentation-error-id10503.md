# NVIAA AIAA segmentation error

**Topic ID**: 10503
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/nviaa-aiaa-segmentation-error/10503

---

## Post #1 by @Flash (2020-03-02 17:12 UTC)

<p>Hello,</p>
<p>I have installed 3D slicer version 4.11.0<br>
I have uploaded some unlocked models in my AIAA server and set it up.<br>
It is loading the models.but when I try to run it(clara_mri_fed_learning_seg_brain_tumors_br16_t1c2tc_amp),is giving slicer error:<br>
Traceback (most recent call last):<br>
File “C:/Users/Biocliq/AppData/Roaming/NA-MIC/Extensions-28793/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 358, in createAiaaSessionIfNotExists<br>
in_file, session_id = self.logic.createSession(inputVolume)<br>
File “C:/Users/Biocliq/AppData/Roaming/NA-MIC/Extensions-28793/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 965, in createSession<br>
response = aiaaClient.create_session(in_file)<br>
File “C:\Users\Biocliq\AppData\Roaming\NA-MIC\Extensions-28793\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 108, in create_session<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, response))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 500; Response: b’{“error”:{“message”:[],“type”:“NotFound”},“success”:false}\n’’)</p>

---

## Post #2 by @lassoan (2020-03-02 17:51 UTC)

<p>Sorry, a few of the Slicer Preview Releases last week had a temporary regression (compatibility with Nvidia AIAA v1 server API got turned off). Please install the latest Slicer Preview Release.</p>

---
