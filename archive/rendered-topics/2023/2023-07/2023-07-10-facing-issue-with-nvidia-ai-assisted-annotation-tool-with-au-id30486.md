---
topic_id: 30486
title: "Facing Issue With Nvidia Ai Assisted Annotation Tool With Au"
date: 2023-07-10
url: https://discourse.slicer.org/t/30486
---

# Facing issue with NVIDIA AI-Assisted Annotation tool with auto -segmentation

**Topic ID**: 30486
**Date**: 2023-07-10
**URL**: https://discourse.slicer.org/t/facing-issue-with-nvidia-ai-assisted-annotation-tool-with-auto-segmentation/30486

---

## Post #1 by @linda_varghese (2023-07-10 07:12 UTC)

<p>I am facing a server connection issue while running the Auto segmentation tool on Nvidia.<br>
I am getting the following error:<br>
Traceback (most recent call last):<br>
File “C:/ProgramData/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 198, in fetchAIAAModels<br>
models = self.logic.list_models()<br>
File “C:/ProgramData/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1076, in list_models<br>
return aiaaClient.model_list(label)<br>
File “C:\ProgramData\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\NvidiaAIAssistedAnnotation\lib\Slicer-5.2\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 192, in model_list<br>
raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, response))<br>
NvidiaAIAAClientAPI.client_api.AIAAException: (3, “Status: 404; Response: b’\r\n404 Not Found\r\n\r\n</p><h1>404 Not Found</h1>\r\n<hr>nginx/1.18.0 (Ubuntu)\r\n\r\n\r\n’”)<p></p>
<p>it was working properly 4 days before, but suddenly an issue with server. Can someone help me to troubleshoot this.</p>

---

## Post #2 by @mangotee (2023-07-10 14:44 UTC)

<p>Hi,<br>
this server for NVIDIA AIAA was hosted by the Slicer team, I think it is probably switched off by now. NVIDIA AIAA is no longer recommended. The successor tool is <a href="https://github.com/Project-MONAI/MONAILabel" rel="noopener nofollow ugc">MONAI Label</a>, and there is an accompanying plugin for 3D Slicer, which can be installed via the Extension Manager. For more details on the module, visit <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #3 by @akmal871026 (2023-07-10 20:38 UTC)

<p>I have face same issue.</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 198, in fetchAIAAModels<br>
models = self.logic.list_models()<br>
File “C:/Users/Akmal/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1076, in list_models<br>
return aiaaClient.model_list(label)<br>
File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\NvidiaAIAssistedAnnotation\lib\Slicer-5.2\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 190, in model_list<br>
status, response = AIAAUtils.http_method(‘GET’, self._server_url, selector)<br>
File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 5.2.2\NA-MIC\Extensions-31382\NvidiaAIAssistedAnnotation\lib\Slicer-5.2\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 620, in http_method<br>
conn = httplib.HTTPConnection(parsed.hostname, parsed.port)<br>
File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 857, in <strong>init</strong><br>
(self.host, self.port) = self._get_hostport(host, port)<br>
File “C:\Users\Akmal\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\http\client.py”, line 891, in _get_hostport<br>
i = host.rfind(‘:’)<br>
AttributeError: ‘NoneType’ object has no attribute ‘rfind’</p>

---
