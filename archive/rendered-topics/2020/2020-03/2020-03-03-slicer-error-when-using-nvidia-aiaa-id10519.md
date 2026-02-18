# Slicer error when using  Nvidia AIAA

**Topic ID**: 10519
**Date**: 2020-03-03
**URL**: https://discourse.slicer.org/t/slicer-error-when-using-nvidia-aiaa/10519

---

## Post #1 by @Memo_son (2020-03-03 14:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior: fetch models from remote server<br>
Actual behavior: fail</p>
<p>i got error when trying to use Nvidia AIAA,i am using MRBrainTumor1 from Sample Data Module.neiter can i enter the server address, nor can i leave it empty<br>
Failed to fetch models from remote server. Make sure server address is correct and &lt;server_uri&gt;/v1/models is accessible in browser</p>
<p>details<br>
Traceback (most recent call last):<br>
File “C:/Users/mehmetcane/AppData/Roaming/NA-MIC/Extensions-28798/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 196, in fetchAIAAModels<br>
models = self.logic.list_models()<br>
File “C:/Users/mehmetcane/AppData/Roaming/NA-MIC/Extensions-28798/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1021, in list_models<br>
return aiaaClient.model_list(label)<br>
File “C:\Users\mehmetcane\AppData\Roaming\NA-MIC\Extensions-28798\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 191, in model_list<br>
status, response = AIAAUtils.http_method(‘GET’, self._server_url, selector)<br>
File “C:\Users\mehmetcane\AppData\Roaming\NA-MIC\Extensions-28798\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 572, in http_method<br>
conn.request(method, selector)<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\http\client.py”, line 1239, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\http\client.py”, line 1285, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\http\client.py”, line 1234, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\http\client.py”, line 1026, in _send_output<br>
self.send(msg)<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\http\client.py”, line 964, in send<br>
self.connect()<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\http\client.py”, line 936, in connect<br>
(self.host,self.port), self.timeout, self.source_address)<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\socket.py”, line 724, in create_connection<br>
raise err<br>
File “C:\Users\mehmetcane\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Python\Lib\socket.py”, line 713, in create_connection<br>
sock.connect(sa)<br>
TimeoutError: [WinError 10060] The connected is not responding within a certain period of time accordingly or associated<br>
connection failed</p>
<p>how can i fix this, thank you.</p>

---

## Post #2 by @lassoan (2020-03-03 14:07 UTC)

<p>Are you behind a corporate firewall? Do you need to use network proxy to access the internet? Can you open the <a href="http://skull.cs.queensu.ca:8123/">http://skull.cs.queensu.ca:8123/</a> link without specifying proxy settings in your web browser?</p>

---

## Post #3 by @Memo_son (2020-03-03 21:16 UTC)

<p>I got the error while connected to the university network.I had no problems when I came home. I will try open the <a href="http://skull.cs.queensu.ca:8123/" rel="nofollow noopener">http://skull.cs.queensu.ca:8123/</a> link when i back to school tomorrow.<br>
Thank you for your interest.</p>

---

## Post #5 by @Shahin (2022-06-21 10:52 UTC)

<p>Hi,</p>
<p>What would be the solution if we have to use the university network that does not open this link? Any other way to connect to the server?</p>

---

## Post #6 by @lassoan (2022-06-21 15:43 UTC)

<p>The server address is subject to change. Follow these steps to connect to the current server:</p>
<ul>
<li>If you use the Slicer Stable Release (Slicer-5.0.x): uninstall and then install the NvidiaAIAssistedAnnotation extension</li>
<li>If you use the Slicer Preview Release (Slicer-5.1.x): install the latest Slicer Preview Release and then install the NvidiaAIAssistedAnnotation extension</li>
<li>In Segment Editor module / Nvidia AIAA effect, clear the “Nvidia AIAA server” field to use the new default server address.</li>
</ul>

---

## Post #7 by @Ning_Li (2022-06-21 19:41 UTC)

<p>I met the same problem. Have you solved it, please?</p>

---

## Post #8 by @lassoan (2022-06-22 01:25 UTC)

<p>The instructions that I provided <a href="https://discourse.slicer.org/t/slicer-error-when-using-nvidia-aiaa/10519/6">above</a> should fix the issue for you. The server works using the same protocols as all websites, so it should work even behind proxy servers and firewalls (unless your network administrators explicitly prohibited connecting to servers at Queen’s University in Canada).</p>

---

## Post #9 by @Ning_Li (2022-06-23 15:16 UTC)

<p>Thank you very much for your reply. Yes, it works at home. But maybe my institute, CRCHUM( Centre de recherche du Centre hospitalier de l’Université de Montréal) blocked the server website. I cant use it there. I also tried using the Proxy and closing virus protection and firewall. It still did not work.</p>

---

## Post #10 by @lassoan (2022-06-23 15:25 UTC)

<p>If your institution uses a proxy server then setting <code>http_proxy</code> and <code>https_proxy</code> environment variables may help. But if the proxy is very tricky then it may be necessary to set up your own server within your institution.</p>

---

## Post #11 by @Shahin (2022-06-28 16:06 UTC)

<p>When I remove “Nvidia AIAA server” and put “<a href="http://127.0.0.1:8000/" rel="noopener nofollow ugc">http://127.0.0.1:8000/</a>”, I still get the error!</p>

---

## Post #12 by @lassoan (2022-06-29 02:23 UTC)

<p><code>http://127.0.0.1:8000</code> works if you set up an NVIDIA Clara server on your computer at port 8000.</p>

---

## Post #13 by @Shahin (2022-06-29 07:34 UTC)

<p>Nvidia Clara server?! I am not sure if I have that installed on my computer!</p>

---

## Post #14 by @lassoan (2022-06-29 12:52 UTC)

<p>Setting it up is a lengthy process. If you are not sure then it means you haven’t set it up. You either need to connect to the default server or set up your own server. You may also consider using MONAILabel instead, which is easier to set up.</p>

---

## Post #15 by @Shahin (2022-06-30 07:31 UTC)

<p>This actually happens when I use MONAI Label. It does not connect to the server.</p>

---

## Post #16 by @lassoan (2022-07-13 12:26 UTC)

<p>You need to set up a MONAI Label server on your computer before you can connect to it from Slicer. See the instructions <a href="https://github.com/Project-MONAI/MONAILabel#installation">here</a>.</p>

---

## Post #17 by @musetee (2022-09-14 08:37 UTC)

<p>I have solved it. I’m using Conda environment and I think it may due to the virtual environment and host are separate. Using the true IP adress and it will be fine.<br>
It may help if you’re also using virtual environment</p>

---
