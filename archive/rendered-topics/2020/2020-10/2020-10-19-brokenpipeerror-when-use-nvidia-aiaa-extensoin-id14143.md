# BrokenPipeError when use Nvidia AIAA extensoin

**Topic ID**: 14143
**Date**: 2020-10-19
**URL**: https://discourse.slicer.org/t/brokenpipeerror-when-use-nvidia-aiaa-extensoin/14143

---

## Post #1 by @ragwing_mmh (2020-10-19 18:13 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.11.0<br>
The version of Python: 2.7.17<br>
Expected behavior: Start auto-segmentation with Nvidia AIAA server<br>
Actual behavior: fail</p>
<p>I installed the slicer &amp; Nvidia AIAA in the same ubuntu server, and  connect to localhost:5000/v1/models to retrieved the installed pre-trained model from NGC</p>
<p>But when I hit the Start button with Nvidia logo, the slicer just showed unexpected error &amp; the detal shows BrokenPipeError: [Errno 32] Broken pipe</p>
<p>Here is the full log:<br>
Traceback (most recent call last):</p>
<p>File “/home/usm500/.config/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 390, in onClickSegmentation</p>
<p>extreme_points, result_file = self.logic.segmentation(in_file, session_id, model)</p>
<p>File “/home/usm500/.config/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1038, in segmentation</p>
<p>params = aiaaClient.inference(model, {}, image_in, result_file, session_id=session_id)</p>
<p>File “/home/usm500/.config/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py”, line 374, in inference</p>
<p>status, form, files = AIAAUtils.http_multipart(‘POST’, self._server_url, selector, in_fields, in_files)</p>
<p>File “/home/usm500/.config/NA-MIC/Extensions-29402/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/NvidiaAIAAClientAPI/client_api.py”, line 634, in http_multipart</p>
<p>conn.request(method, selector, body, headers)</p>
<p>File “/home/usm500/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/http/client.py”, line 1239, in request</p>
<p>self._send_request(method, url, body, headers, encode_chunked)</p>
<p>File “/home/usm500/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/http/client.py”, line 1285, in _send_request</p>
<p>self.endheaders(body, encode_chunked=encode_chunked)</p>
<p>File “/home/usm500/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/http/client.py”, line 1234, in endheaders</p>
<p>self._send_output(message_body, encode_chunked=encode_chunked)</p>
<p>File “/home/usm500/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/http/client.py”, line 1065, in _send_output</p>
<p>self.send(chunk)</p>
<p>File “/home/usm500/Downloads/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/http/client.py”, line 986, in send</p>
<p>self.sock.sendall(data)</p>
<p>BrokenPipeError: [Errno 32] Broken pipe</p>
<p>Does someone know how to fix it ? Thank you !</p>

---

## Post #2 by @lassoan (2020-10-20 02:07 UTC)

<p>This means that the server abruptly disconnects. Does the server crash when you get this error message? Does the server log any error?</p>
<p>Do things work well with the default server (when you leave the server address field empty)?</p>

---

## Post #3 by @ragwing_mmh (2020-10-25 06:35 UTC)

<p>Dear Prof. Lasso:</p>
<p>Greatly appreciated for your help<br>
I checked the docker image of our Clara SDK &amp; found the version is still in 2.0<br>
Than pull the docker image in SDK 3.0 &amp; start AIAA properly</p>
<p>Now it works flawless. Thank you for everything</p>

---
