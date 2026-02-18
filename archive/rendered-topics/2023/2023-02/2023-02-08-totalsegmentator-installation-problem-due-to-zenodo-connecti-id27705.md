# TotalSegmentator installation problem due to Zenodo connection error

**Topic ID**: 27705
**Date**: 2023-02-08
**URL**: https://discourse.slicer.org/t/totalsegmentator-installation-problem-due-to-zenodo-connection-error/27705

---

## Post #1 by @zhangliang (2023-02-08 13:55 UTC)

<p>I have some problems installing TotalSegmentator. Let me try to describe it clearly. I hope to get your help.<br>
My device：DELL windows 10 NVIDIA GeForceRTX3060 ,Display Memory: 28386 MB</p>
<p>pyTorch :version 1.13+cu117<br>
NVidia driver: version 512.77</p>
<p>=========<br>
Processing started</p>
<p>Writing input file to C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2023-02-08_16+16+43.146/total-segmentator-input.nii</p>
<p>Creating segmentations with TotalSegmentator AI…</p>
<p>Total Segmentator arguments: [‘-i’, ‘C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2023-02-08_16+16+43.146/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2023-02-08_16+16+43.146/segmentation’, ‘–ml’, ‘–task’, ‘total’]</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a></p>
<p>Downloading pretrained weights for Task 251 (~230MB) …</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\connection.py”, line 174, in _new_conn</p>
<p>conn = connection.create_connection(</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\util\connection.py”, line 72, in create_connection</p>
<p>for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\socket.py”, line 954, in getaddrinfo</p>
<p>for res in _socket.getaddrinfo(host, port, family, type, proto, flags):</p>
<p>socket.gaierror: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 703, in urlopen</p>
<p>httplib_response = self._make_request(</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 386, in _make_request</p>
<p>self._validate_conn(conn)</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 1042, in _validate_conn</p>
<p>conn.connect()</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\connection.py”, line 358, in connect</p>
<p>self.sock = conn = self._new_conn()</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\connection.py”, line 186, in _new_conn</p>
<p>raise NewConnectionError(</p>
<p>urllib3.exceptions.NewConnectionError: &lt;urllib3.connection.HTTPSConnection object at 0x0000023943A0D700&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\requests\adapters.py”, line 489, in send</p>
<p>resp = conn.urlopen(</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\connectionpool.py”, line 787, in urlopen</p>
<p>retries = retries.increment(</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\urllib3\util\retry.py”, line 592, in increment</p>
<p>raise MaxRetryError(_pool, url, error or ResponseError(cause))</p>
<p>urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host=‘<a href="http://zenodo.org/" rel="noopener nofollow ugc">zenodo.org</a>’, port=443): Max retries exceeded with url: /record/6802342/files/Task251_TotalSegmentator_part1_organs_1139subj.zip?download=1 (Caused by NewConnectionError(‘&lt;urllib3.connection.HTTPSConnection object at 0x0000023943A0D700&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed’))</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 241, in</p>
<p>main()</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Scripts\TotalSegmentator”, line 200, in main</p>
<p>download_pretrained_weights(tid)</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 175, in download_pretrained_weights</p>
<p>download_url_and_unpack(WEIGHTS_URL, config_dir)</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 69, in download_url_and_unpack</p>
<p>raise e</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\totalsegmentator\libs.py”, line 55, in download_url_and_unpack</p>
<p>with requests.get(url, stream=True) as r:</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\requests\api.py”, line 73, in get</p>
<p>return request(“get”, url, params=params, **kwargs)</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\requests\api.py”, line 59, in request</p>
<p>return session.request(method=method, url=url, **kwargs)</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\requests\sessions.py”, line 587, in request</p>
<p>resp = self.send(prep, **send_kwargs)</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\requests\sessions.py”, line 701, in send</p>
<p>r = adapter.send(request, **kwargs)</p>
<p>File “C:\ProgramData\NA-MIC\Slicer 5.2.1\lib\Python\Lib\site-packages\requests\adapters.py”, line 565, in send</p>
<p>raise ConnectionError(e, request=request)</p>
<p>requests.exceptions.ConnectionError: HTTPSConnectionPool(host=‘<a href="http://zenodo.org/" rel="noopener nofollow ugc">zenodo.org</a>’, port=443): Max retries exceeded with url: /record/6802342/files/Task251_TotalSegmentator_part1_organs_1139subj.zip?download=1 (Caused by NewConnectionError(‘&lt;urllib3.connection.HTTPSConnection object at 0x0000023943A0D700&gt;: Failed to establish a new connection: [Errno 11004] getaddrinfo failed’))</p>

---

## Post #2 by @pieper (2023-02-08 13:57 UTC)

<p>It looks like the file download failed.  I have gotten timeouts from <a href="http://zenodo.org">zenodo.org</a> before using a web browser so I’m sure the same thing would happen from time to time using the programatic interface too.  Probably try again in a few hours or days when it’s less busy.</p>

---

## Post #3 by @zhangliang (2023-02-08 14:07 UTC)

<p>Thank you. It’s really unstable. I have tested many times and always failed, using VPN or not ，using different WiFi at different times. 3d_ The fullres folder is always empty.Is there any other way? For example, download some files manually.</p>

---

## Post #4 by @pieper (2023-02-08 14:33 UTC)

<p>I was able to install TotalSegmentator yesterday on a new windows machine.  It took a while but it succeeded.  I don’t know if it matters where the connection comes from; in my experience it is the server just being overwhelmed from time to time.  If this keeps up we might want to find a way to mirror the files somewhere else (google drive, github release, etc).</p>

---

## Post #5 by @lassoan (2023-02-08 15:19 UTC)

<p>Yesterday our collaborators from Hungary reported Zenodo servers timing out, too.</p>
<p><a class="mention" href="/u/zhangliang">@zhangliang</a> could you please <a href="https://github.com/wasserth/TotalSegmentator/issues">report this problem in the TotalSegmentator Python package repository</a>? It is important for the developers to know about this issue and start thinking about alternative hosting options.</p>

---

## Post #6 by @zhangliang (2023-02-09 11:10 UTC)

<p>OK, I have submitted the problem as required, and I look forward to solving it.</p>

---

## Post #7 by @zhang_ming (2023-02-20 12:09 UTC)

<p>I have met up with this problem too. may local weights added to slicer plugin, and upload the weights to google drive ?</p>

---

## Post #8 by @zhangliang (2023-02-22 08:17 UTC)

<p>Hello, I think I have solved this problem. You can manually download the zip file and put it in the specified location. You can sign in <a href="http://zenodo.org/" rel="noopener nofollow ugc">http://zenodo.org/</a> And search for missing files</p>

---

## Post #9 by @zhang_ming (2023-02-22 11:22 UTC)

<p>yes!!! I have download all this zip files manually, it worked</p>

---

## Post #10 by @lassoan (2023-02-27 12:35 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-segment-the-tibia-using-totalsegmentator/28065">How to segment the tibia using TotalSegmentator?</a></p>

---

## Post #11 by @xiaoli26 (2023-04-14 14:57 UTC)

<p>C:\Users\XXX.totalsegmentator\nnunet\results\nnUNet\3d_fullres</p>
<p>and it works, thx!</p>

---
