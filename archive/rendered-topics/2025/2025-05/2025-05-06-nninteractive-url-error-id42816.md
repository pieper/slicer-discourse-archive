---
topic_id: 42816
title: "Nninteractive Url Error"
date: 2025-05-06
url: https://discourse.slicer.org/t/42816
---

# NNinteractive URL error

**Topic ID**: 42816
**Date**: 2025-05-06
**URL**: https://discourse.slicer.org/t/nninteractive-url-error/42816

---

## Post #1 by @muratmaga (2025-05-06 19:11 UTC)

<p>NNinteractive used to work, but with a recent nightly, I am getting this error.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/maga/Downloads/Slicer-5.9.0-2025-04-28-linux-amd64/bin/Python/slicer/util.py", line 3391, in tryWithErrorDisplay
    yield
  File "/home/maga/Downloads/Slicer-5.9.0-2025-04-28-linux-amd64/slicer.org/Extensions-33625/NNInteractive/lib/Slicer-5.9/qt-scripted-modules/SlicerNNInteractive.py", line 1109, in request_to_server
    response = requests.post(*args, **kwargs)
  File "/home/maga/Downloads/Slicer-5.9.0-2025-04-28-linux-amd64/lib/Python/lib/python3.9/site-packages/requests/api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "/home/maga/Downloads/Slicer-5.9.0-2025-04-28-linux-amd64/lib/Python/lib/python3.9/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "/home/maga/Downloads/Slicer-5.9.0-2025-04-28-linux-amd64/lib/Python/lib/python3.9/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/maga/Downloads/Slicer-5.9.0-2025-04-28-linux-amd64/lib/Python/lib/python3.9/site-packages/requests/sessions.py", line 697, in send
    adapter = self.get_adapter(url=request.url)
  File "/home/maga/Downloads/Slicer-5.9.0-2025-04-28-linux-amd64/lib/Python/lib/python3.9/site-packages/requests/sessions.py", line 792, in get_adapter
    raise InvalidSchema(f"No connection adapters were found for {url!r}")
requests.exceptions.InvalidSchema: No connection adapters were found for 'localhost:1527/upload_segment'
</code></pre>
<p>the docker image is running on the same computer. I have tried replacing the address with 0.0.0.0, localhost, 127.0.0.1 as well as the actual IP address. Still getting the same error. There is no output on the docker console (indicating that request reached the server).<br>
This is on ubuntu 22.04, slicer release 33625.</p>
<p>Same error on using the today’s preview on my Mac, with the same server</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a3f5b6cf5fa5ee78e035a95978f03a556a62721.jpeg" data-download-href="/uploads/short-url/f9UlWncSzozePPL2ajrChmPZ3q1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a3f5b6cf5fa5ee78e035a95978f03a556a62721_2_690x446.jpeg" alt="image" data-base62-sha1="f9UlWncSzozePPL2ajrChmPZ3q1" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a3f5b6cf5fa5ee78e035a95978f03a556a62721_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a3f5b6cf5fa5ee78e035a95978f03a556a62721_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a3f5b6cf5fa5ee78e035a95978f03a556a62721_2_1380x892.jpeg 2x" data-dominant-color="CFCBCA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1393×901 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-05-06 19:13 UTC)

<p>Maybe add http:// to localhost in the url</p>

---

## Post #3 by @muratmaga (2025-05-06 19:14 UTC)

<p>additionally there is a separate bug.</p>
<p>If you do not create a segmentation object before switching to NNInteractive, and try to set create the segmentation using the Segment Editor widget in NNInteractive, Slicer application closes with this error:</p>
<pre><code class="lang-auto">[CRITICAL][Qt] 06.05.2025 04:51:27 [] (unknown:0) - void qMRMLSegmentEditorWidget::setSourceVolumeNode(vtkMRMLNode*)  failed: need to set segment editor and segmentation nodes first
</code></pre>

---

## Post #4 by @muratmaga (2025-05-06 19:15 UTC)

<p>Himm, that fixed it, but do we really need to specify that?</p>

---
