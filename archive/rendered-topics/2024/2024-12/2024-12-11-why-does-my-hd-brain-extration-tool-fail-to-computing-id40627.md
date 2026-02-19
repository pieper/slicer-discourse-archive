---
topic_id: 40627
title: "Why Does My Hd Brain Extration Tool Fail To Computing"
date: 2024-12-11
url: https://discourse.slicer.org/t/40627
---

# Why does my HD Brain Extration Tool fail to computing?

**Topic ID**: 40627
**Date**: 2024-12-11
**URL**: https://discourse.slicer.org/t/why-does-my-hd-brain-extration-tool-fail-to-computing/40627

---

## Post #1 by @researchtomliu (2024-12-11 09:02 UTC)

<p>Hello, I have updated the Slicer to the latest version 5.7. When I used the model “HD Brain Extration Tool”, It could not comptue and gave some error warnning masages. How to solve it? Thanks!</p>
<p>Traceback (most recent call last):<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\urllib\request.py”, line 1346, in do_open<br>
h.request(req.get_method(), req.selector, req.data, headers,<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\http\client.py”, line 1285, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\http\client.py”, line 1331, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\http\client.py”, line 1280, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\http\client.py”, line 1040, in _send_output<br>
self.send(msg)<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\http\client.py”, line 980, in send<br>
self.connect()<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\http\client.py”, line 1447, in connect<br>
super().connect()<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\http\client.py”, line 946, in connect<br>
self.sock = self._create_connection(<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\socket.py”, line 823, in create_connection<br>
for res in getaddrinfo(host, port, 0, SOCK_STREAM):<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\socket.py”, line 954, in getaddrinfo<br>
for res in _socket.getaddrinfo(host, port, family, type, proto, flags):<br>
socket.gaierror: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “D:\Slicer 5.7.0-2024-12-09\bin\Python\slicer\util.py”, line 3295, in tryWithErrorDisplay<br>
yield<br>
File “D:/Slicer 5.7.0-2024-12-09/slicer.org/Extensions-33147/HDBrainExtraction/lib/Slicer-5.7/qt-scripted-modules/HDBrainExtractionTool.py”, line 237, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputVolumeSelector.currentNode(),<br>
File “D:/Slicer 5.7.0-2024-12-09/slicer.org/Extensions-33147/HDBrainExtraction/lib/Slicer-5.7/qt-scripted-modules/HDBrainExtractionTool.py”, line 379, in process<br>
run_hd_bet([input_file], [output_file], mode, config_file, device, postprocess = True, do_tta = enable_augmentation, keep_mask = save_mask, overwrite = True, bet = save_masked_volume)<br>
File “D:\Slicer 5.7.0-2024-12-09\slicer.org\Extensions-33147\HDBrainExtraction\lib\Slicer-5.7\qt-scripted-modules\HD_BET\run.py”, line 51, in run_hd_bet<br>
maybe_download_parameters(i)<br>
File “D:\Slicer 5.7.0-2024-12-09\slicer.org\Extensions-33147\HDBrainExtraction\lib\Slicer-5.7\qt-scripted-modules\HD_BET\utils.py”, line 37, in maybe_download_parameters<br>
data = urlopen(url).read()<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\urllib\request.py”, line 214, in urlopen<br>
return opener.open(url, data, timeout)<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\urllib\request.py”, line 517, in open<br>
response = self._open(req, data)<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\urllib\request.py”, line 534, in _open<br>
result = self._call_chain(self.handle_open, protocol, protocol +<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\urllib\request.py”, line 494, in _call_chain<br>
result = func(*args)<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\urllib\request.py”, line 1389, in https_open<br>
return self.do_open(http.client.HTTPSConnection, req,<br>
File “D:\Slicer 5.7.0-2024-12-09\lib\Python\Lib\urllib\request.py”, line 1349, in do_open<br>
raise URLError(err)<br>
urllib.error.URLError: &lt;urlopen error [Errno 11004] getaddrinfo failed&gt;</p>

---

## Post #2 by @lassoan (2024-12-11 15:58 UTC)

<p>The extension needs to download Python packages and AI model weights. Your co m outer seems to have network connectivity issues (most likely caused by too aggressive fiirewall or proxy server). Your IT administrators should be able to help you.</p>

---

## Post #3 by @researchtomliu (2024-12-14 01:34 UTC)

<p>Thank you very much Mr. Lassoan.</p>

---
