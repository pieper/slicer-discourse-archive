# Model drop-down in Nvidia AIAA is empty

**Topic ID**: 9812
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/model-drop-down-in-nvidia-aiaa-is-empty/9812

---

## Post #1 by @Apex (2020-01-14 17:17 UTC)

<p>Operating system:Windows<br>
Slicer version:4.11.0<br>
Expected behavior: Model drop-down should contain organ segmentation in Nvidia AIAA<br>
Actual behavior: Model drop-down in Nvidia AIAA is empty.</p>
<p>Error:<br>
Traceback (most recent call last):<br>
File “C:/Users/John/AppData/Roaming/NA-MIC/Extensions-28723/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 164, in onClickFetchModels<br>
models = self.logic.list_models(self.ui.modelFilterLabelLineEdit.text)<br>
File “C:/Users/John/AppData/Roaming/NA-MIC/Extensions-28723/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 692, in list_models<br>
result = self.aiaaClient.model_list(label)<br>
File “C:\Users\John\AppData\Roaming\NA-MIC\Extensions-28723\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 107, in model_list<br>
response = AIAAUtils.http_get_method(self.server_url, selector)<br>
File “C:\Users\John\AppData\Roaming\NA-MIC\Extensions-28723\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 404, in http_get_method<br>
conn.request(‘GET’, selector)<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\http\client.py”, line 1239, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\http\client.py”, line 1285, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\http\client.py”, line 1234, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\http\client.py”, line 1026, in _send_output<br>
self.send(msg)<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\http\client.py”, line 964, in send<br>
self.connect()<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\http\client.py”, line 936, in connect<br>
(self.host,self.port), self.timeout, self.source_address)<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\socket.py”, line 724, in create_connection<br>
raise err<br>
File “C:\Users\John\AppData\Local\NA-MIC\Slicer 4.11.0-2020-01-08\lib\Python\Lib\socket.py”, line 713, in create_connection<br>
sock.connect(sa)<br>
TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond</p>

---

## Post #2 by @lassoan (2020-01-14 20:53 UTC)

<p>The segmentation server is up, so if the server is not responding then there is either a network issue (too aggressive firewall, etc.) or you have entered a custom address in Models / NVidia AIAA server (to use the default server, leave the field empty).</p>

---
