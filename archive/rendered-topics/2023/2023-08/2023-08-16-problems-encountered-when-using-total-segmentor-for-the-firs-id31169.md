# Problems encountered when using Total Segmentor for the first time - zenodo.org ... Failed to establish a new connection

**Topic ID**: 31169
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/problems-encountered-when-using-total-segmentor-for-the-first-time-zenodo-org-failed-to-establish-a-new-connection/31169

---

## Post #1 by @shziyang (2023-08-16 10:09 UTC)

<p>Processing started<br>
Writing input file to C:/Users/23398/AppData/Local/Temp/Slicer/__SlicerTemp__2023-08-16_15+49+58.272/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/23398/AppData/Local/Temp/Slicer/__SlicerTemp__2023-08-16_15+49+58.272/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/23398/AppData/Local/Temp/Slicer/__SlicerTemp__2023-08-16_15+49+58.272/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" class="inline-onebox" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a></p>
<p>Using ‘fast’ option: resampling to lower resolution (3mm)<br>
Downloading pretrained weights for Task 256 (~230MB) …<br>
Traceback (most recent call last):<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\connection.py”, line 174, in _new_conn<br>
conn = connection.create_connection(<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\util\connection.py”, line 72, in create_connection<br>
for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\socket.py”, line 954, in getaddrinfo<br>
for res in _socket.getaddrinfo(host, port, family, type, proto, flags):<br>
socket.gaierror: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 703, in urlopen<br>
httplib_response = self._make_request(<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 386, in _make_request<br>
self._validate_conn(conn)<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 1042, in _validate_conn<br>
conn.connect()<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\connection.py”, line 358, in connect<br>
self.sock = conn = self._new_conn()<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\connection.py”, line 186, in _new_conn<br>
raise NewConnectionError(<br>
urllib3.exceptions.NewConnectionError: &lt;urllib3.connection.HTTPSConnection object at 0x0000024D31FC65E0&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\requests\adapters.py”, line 489, in send<br>
resp = conn.urlopen(<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 787, in urlopen<br>
retries = retries.increment(<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\urllib3\util\retry.py”, line 592, in increment<br>
raise MaxRetryError(_pool, url, error or ResponseError(cause))<br>
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host=‘<a href="http://zenodo.org" rel="noopener nofollow ugc">zenodo.org</a>’, port=443): Max retries exceeded with url: /record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1 (Caused by NewConnectionError(‘&lt;urllib3.connection.HTTPSConnection object at 0x0000024D31FC65E0&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed’))</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator”, line 93, in <br>
main()<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator”, line 86, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 157, in totalsegmentator<br>
download_pretrained_weights(task_id)<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 183, in download_pretrained_weights<br>
download_url_and_unpack(WEIGHTS_URL, config_dir)<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 69, in download_url_and_unpack<br>
raise e<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 55, in download_url_and_unpack<br>
with requests.get(url, stream=True) as r:<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\requests\api.py”, line 73, in get<br>
return request(“get”, url, params=params, **kwargs)<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\requests\api.py”, line 59, in request<br>
return session.request(method=method, url=url, **kwargs)<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\requests\sessions.py”, line 587, in request<br>
resp = self.send(prep, **send_kwargs)<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\requests\sessions.py”, line 701, in send<br>
r = adapter.send(request, **kwargs)<br>
File “E:\3D slicer\Slicer 5.2.2\lib\Python\Lib\site-packages\requests\adapters.py”, line 565, in send<br>
raise ConnectionError(e, request=request)<br>
requests.exceptions.ConnectionError: HTTPSConnectionPool(host=‘<a href="http://zenodo.org" rel="noopener nofollow ugc">zenodo.org</a>’, port=443): Max retries exceeded with url: /record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1 (Caused by NewConnectionError(‘&lt;urllib3.connection.HTTPSConnection object at 0x0000024D31FC65E0&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed’))</p>

---

## Post #2 by @lassoan (2023-08-16 10:13 UTC)

<aside class="quote no-group" data-username="shziyang" data-post="1" data-topic="31169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shziyang/48/67185_2.png" class="avatar"> shziyang:</div>
<blockquote>
<p>urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host=‘<a href="http://zenodo.org">zenodo.org</a>’, port=443): Max retries exceeded with url: /record/6802052/files/Task256_TotalSegmentator_3mm_1139subj.zip?download=1 (Caused by NewConnectionError(‘&lt;urllib3.connection.HTTPSConnection object at 0x0000024D31FC65E0&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed’))</p>
</blockquote>
</aside>
<p>It means that the server the model weights are downloaded from was overloaded. Most probably the download will succeed if you retry later (the downloaded data is cached, so once it is downloaded, you don’t need to worry about the server again) or you can try to manually download the model weights as described <a href="https://github.com/lassoan/SlicerTotalSegmentator/issues/13">here</a>.</p>

---

## Post #3 by @lassoan (2023-08-16 10:20 UTC)

<p>On a second look, the <code>Failed to establish a new connection</code> indicates that the server was not accessible at all. This is more likely to be caused by a too aggressive firewall or proxy server.</p>
<p>If you cannot access <a href="http://zenodo.org">zenodo.org</a> in your web browser then you may need to connect via a VPN.</p>
<p>If you can access <a href="http://zenodo.org">zenodo.org</a> in your web browser then you may need to adjust your proxy settings. Slicer uses these system proxy settings by default, but you can set proxy server information in environment variables <code>http_proxy</code> and <code>https_proxy</code>.</p>

---
