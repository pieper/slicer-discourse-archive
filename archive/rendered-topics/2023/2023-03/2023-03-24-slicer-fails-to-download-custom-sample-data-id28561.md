# Slicer fails to download custom sample data

**Topic ID**: 28561
**Date**: 2023-03-24
**URL**: https://discourse.slicer.org/t/slicer-fails-to-download-custom-sample-data/28561

---

## Post #1 by @dzenanz (2023-03-24 17:43 UTC)

<p>I have this code:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/88f947cb239fd8e30e5be75a0380c44a100ec937/BModeFromRF/BModeFromRF.py#L46-L57">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/88f947cb239fd8e30e5be75a0380c44a100ec937/BModeFromRF/BModeFromRF.py#L46-L57" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerITKUltrasound/blob/88f947cb239fd8e30e5be75a0380c44a100ec937/BModeFromRF/BModeFromRF.py#L46-L57" target="_blank" rel="noopener nofollow ugc">KitwareMedical/SlicerITKUltrasound/blob/88f947cb239fd8e30e5be75a0380c44a100ec937/BModeFromRF/BModeFromRF.py#L46-L57</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="46" style="counter-reset: li-counter 45 ;">
          <li>import SampleData</li>
          <li>iconsPath = os.path.join(os.path.dirname(__file__), 'Resources/Icons')</li>
          <li>file_sha512 = "b648140f38d2c3189388a35fea65ef3b4311237de8c454c6b98480d84b139ec8afb8ec5881c5d9513cdc208ae781e1e442988be81564adff77edcfb30b921a28"</li>
          <li>SampleData.SampleDataLogic.registerCustomSampleDataSource(</li>
          <li>    category='ITKUltrasound',</li>
          <li>    sampleName='ITKUltrasoundPhantomRF',</li>
          <li>    thumbnailFileName=os.path.join(iconsPath, 'SampleRF.png'),</li>
          <li>    uris=f"https://data.kitware.com:443/api/v1/file/hashsum/SHA512/{file_sha512}/download",  # "https://data.kitware.com/api/v1/item/57b5d5d88d777f10f269444b/download", "https://data.kitware.com/api/v1/file/57b5d5d88d777f10f269444f/download",</li>
          <li>    fileNames='uniform_phantom_8.9_MHz.mha',</li>
          <li>    checksums=f'SHA512:{file_sha512}',</li>
          <li>    nodeNames='ITKUltrasoundPhantomRF'</li>
          <li>)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
which results in a download error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f80a7be96d105317151e4ce56e99b7134b741.png" data-download-href="/uploads/short-url/eLAlQK0lrCxGGdHljdQkM2kl8w9.png?dl=1" title="DownloadFailed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/677f80a7be96d105317151e4ce56e99b7134b741_2_690x175.png" alt="DownloadFailed" data-base62-sha1="eLAlQK0lrCxGGdHljdQkM2kl8w9" width="690" height="175" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/677f80a7be96d105317151e4ce56e99b7134b741_2_690x175.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/677f80a7be96d105317151e4ce56e99b7134b741_2_1035x262.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/677f80a7be96d105317151e4ce56e99b7134b741_2_1380x350.png 2x" data-dominant-color="D7DFEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DownloadFailed</span><span class="informations">2935×747 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The file can be downloaded using Chrome and <code>curl.exe</code>. What is wrong?</p>

---

## Post #2 by @pieper (2023-03-24 19:04 UTC)

<p>What version of Slicer are you using?</p>

---

## Post #3 by @dzenanz (2023-03-24 19:15 UTC)

<p>5.2.1 official release. But the same thing happens with 5.3.0-2022-12-14 3d62cbf.</p>

---

## Post #4 by @pieper (2023-03-24 19:33 UTC)

<p>Hmm, that preview build should have <a href="https://github.com/Slicer/Slicer/blob/fbc2ede79060e2e2c653ddb2f0b7d2bba9fab16b/Base/QTCore/Resources/Certs/Slicer.crt">this version of the cert</a>.  But maybe check the current preview version?</p>

---

## Post #5 by @dzenanz (2023-03-24 20:06 UTC)

<p>The same error happens with the latest nightly (5.3.0-2023-03-22 r31691 / fbc2ede).</p>

---

## Post #6 by @jcfr (2023-03-24 20:34 UTC)

<p>The following snippet allows to directly test without having to explicitly register a <code>SampleDataSource</code>:</p>
<pre><code class="lang-python">import os

from SampleData import SampleDataLogic

print(f"RemoteCacheDirectory: {slicer.mrmlScene.GetCacheManager().GetRemoteCacheDirectory()}")

file_sha512 = "b648140f38d2c3189388a35fea65ef3b4311237de8c454c6b98480d84b139ec8afb8ec5881c5d9513cdc208ae781e1e442988be81564adff77edcfb30b921a28"

# Download
SampleDataLogic().downloadFileIntoCache(
    f"https://data.kitware.com:443/api/v1/file/hashsum/SHA512/{file_sha512}/download",
    "uniform_phantom_8.9_MHz.mha",
    f'SHA512:{file_sha512}')

# Load into the scene
filePath = os.path.join(slicer.mrmlScene.GetCacheManager().GetRemoteCacheDirectory(), "uniform_phantom_8.9_MHz.mha")
SampleDataLogic().loadNode(filePath, "uniform_phantom_8")
</code></pre>
<hr>
<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> The code above works as expected using the latest nightly on Linux (<code>Slicer-5.3.0-2023-03-22</code>)</p>

---

## Post #7 by @jcfr (2023-03-24 20:42 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  Download using the installed version on Windows also seems to work (from within kitware network):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6415bf01a4ab5713e24f646b8e9a69c7c80aba60.png" data-download-href="/uploads/short-url/ehokWQypXgm3Igli3lm8mAJAQbS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415bf01a4ab5713e24f646b8e9a69c7c80aba60_2_517x350.png" alt="image" data-base62-sha1="ehokWQypXgm3Igli3lm8mAJAQbS" width="517" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415bf01a4ab5713e24f646b8e9a69c7c80aba60_2_517x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415bf01a4ab5713e24f646b8e9a69c7c80aba60_2_775x525.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/6415bf01a4ab5713e24f646b8e9a69c7c80aba60_2_1034x700.png 2x" data-dominant-color="D8DBDD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1823×1236 455 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @jcfr (2023-03-24 20:52 UTC)

<p>To summarize, I confirm the download works as expected after installing the following versions:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Version</th>
<th>Linux</th>
<th>macOS</th>
<th>Windows</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>5.2.1</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
<tr>
<td><code>5.2.2</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
<tr>
<td><code>5.3.0-2023-03-22</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> (*)</td>
</tr>
</tbody>
</table>
</div><p>(*) This one was tested inside &amp; outside the kitware network and downloads works from both</p>

---

## Post #9 by @dzenanz (2023-03-24 21:07 UTC)

<p>Using your test script (pasting into Slicer’s Python console), I get an error:</p>
<pre data-code-wrap="log"><code class="lang-plaintext">Python 3.9.10 (main, Mar 23 2023, 23:31:17) [MSC v.1930 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
import os

from SampleData import SampleDataLogic

print(f"RemoteCacheDirectory: {slicer.mrmlScene.GetCacheManager().GetRemoteCacheDirectory()}")

file_sha512 = "b648140f38d2c3189388a35fea65ef3b4311237de8c454c6b98480d84b139ec8afb8ec5881c5d9513cdc208ae781e1e442988be81564adff77edcfb30b921a28"

# Download
SampleDataLogic().downloadFileIntoCache(
    f"https://data.kitware.com:443/api/v1/file/hashsum/SHA512/{file_sha512}/download",
    "uniform_phantom_8.9_MHz.mha",
    f'SHA512:{file_sha512}')

# Load into the scene
filePath = os.path.join(slicer.mrmlScene.GetCacheManager().GetRemoteCacheDirectory(), "uniform_phantom_8.9_MHz.mha")
SampleDataLogic().loadNode(filePath, "uniform_phantom_8")
RemoteCacheDirectory: C:/Users/Dzenan/AppData/Local/slicer.org/Slicer/cache/SlicerIO
Traceback (most recent call last):
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\http\client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\http\client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\http\client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\http\client.py", line 1040, in _send_output
    self.send(msg)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\http\client.py", line 980, in send
    self.connect()
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\http\client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\ssl.py", line 1040, in _create
    self.do_handshake()
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/Dzenan/AppData/Local/slicer.org/Slicer 5.3.0-2023-03-22/bin/../lib/Slicer-5.3/qt-scripted-modules/SampleData.py", line 862, in downloadFile
    urllib.request.urlretrieve(uri, filePath, self.reportHook)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 239, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 214, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 517, in open
    response = self._open(req, data)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 494, in _call_chain
    result = func(*args)
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 1389, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "C:\Users\Dzenan\AppData\Local\slicer.org\Slicer 5.3.0-2023-03-22\lib\Python\Lib\urllib\request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 10, in &lt;module&gt;
  File "C:/Users/Dzenan/AppData/Local/slicer.org/Slicer 5.3.0-2023-03-22/bin/../lib/Slicer-5.3/qt-scripted-modules/SampleData.py", line 631, in downloadFileIntoCache
    return self.downloadFile(uri, destFolderPath, name, checksum)
  File "C:/Users/Dzenan/AppData/Local/slicer.org/Slicer 5.3.0-2023-03-22/bin/../lib/Slicer-5.3/qt-scripted-modules/SampleData.py", line 866, in downloadFile
    raise ValueError(f"Failed to download {uri} to {filePath}")
ValueError: Failed to download https://data.kitware.com:443/api/v1/file/hashsum/SHA512/b648140f38d2c3189388a35fea65ef3b4311237de8c454c6b98480d84b139ec8afb8ec5881c5d9513cdc208ae781e1e442988be81564adff77edcfb30b921a28/download to C:/Users/Dzenan/AppData/Local/slicer.org/Slicer/cache/SlicerIO/uniform_phantom_8.9_MHz.mha
[Python] &lt;b&gt;	Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;&lt;/b&gt;
&gt;&gt;&gt; 
</code></pre>
<p>Once the current Slicer incremental build finishes, I will try restarting the computer.</p>

---

## Post #10 by @jcfr (2023-03-24 21:45 UTC)

<p>Could you try the following ?</p>
<p>The snippet is expected to work in both <code>PythonSlicer</code> and a regular <code>python</code> interpreter.</p>
<pre><code class="lang-python">import sys
import traceback
import urllib.request


def processEvents():
    try:
        import slicer
        slicer.app.processEvents()
    except (AttributeError, ImportError):
        pass

    
def display(text, file=sys.stdout):
    processEvents()
    print(text, flush=True, file=file)

    
def error(text):
    display(text, file=sys.stderr)


for url, expected_success in [
    ("https://data.kitware.com", True),
    ("https://www.httpvshttps.com/", True),
    ("https://slicer.org/", True),
    ("https://expired.badssl.com/", False),
    ("https://github.com/", True),
]:
    display("-" * 8)
    display(f"Checking {url}")
    try:
        with urllib.request.urlopen(url) as response:
           data = response.read()
           html = data.decode('utf8')
           assert "&lt;head&gt;" in html[:600]
        if expected_success:
            display(f"Checking {url} - OK")
        else:
            error(f"Checking {url} - FAILED - should have raised an exception")
    except Exception as exc:
        if expected_success:
            error(f"Checking {url} - FAILED - unexpected exception")
            traceback.print_exc()
        else:
            display(f"Checking {url} - OK  [Expected {exc}]")
</code></pre>
<p>Expected output:</p>
<pre><code class="lang-plaintext">--------
Checking https://data.kitware.com
Checking https://data.kitware.com - ok
--------
Checking https://www.httpvshttps.com/
Checking https://www.httpvshttps.com/ - ok
--------
Checking https://slicer.org/
Checking https://slicer.org/ - ok
--------
Checking https://expired.badssl.com/
Checking https://expired.badssl.com/ - ok  [Expected &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;]
--------
Checking https://github.com/
Checking https://github.com/ - OK
</code></pre>

---

## Post #11 by @pieper (2023-03-25 18:51 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="8" data-topic="28561">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<div class="md-table">
<table>
<thead>
<tr>
<th>Version</th>
<th>Linux</th>
<th>macOS</th>
<th>Windows</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>5.2.1</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
<tr>
<td><code>5.2.2</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
<tr>
<td><code>5.3.0-2023-03-22</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji only-emoji" alt=":question:" loading="lazy" width="20" height="20"></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> (*)</td>
</tr>
</tbody>
</table>
</div></blockquote>
</aside>
<p>I can confirm that all three of the macOS versions listed generate the expected results when running that script on my machine.</p>

---

## Post #12 by @rbumm (2023-03-25 19:38 UTC)

<p>From Slicer 5.2.2</p>
<pre><code class="lang-auto">-------------
Checking https://data.kitware.com
Checking https://data.kitware.com - OK

--------
Checking https://www.httpvshttps.com/
Checking https://www.httpvshttps.com/ - OK
--------
Checking https://slicer.org/
Checking https://slicer.org/ - OK
--------

Checking https://expired.badssl.com/
Checking https://expired.badssl.com/ - OK [Expected &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;]

--------

Checking https://github.com/
Checking https://github.com/ - OK

&gt;&gt;&gt;
</code></pre>

---

## Post #13 by @rbumm (2023-03-25 19:42 UTC)

<p>Same from Powershell Windows 11:</p>
<pre><code class="lang-auto">--------
Checking https://data.kitware.com
Checking https://data.kitware.com - OK
--------
Checking https://www.httpvshttps.com/
Checking https://www.httpvshttps.com/ - OK
--------
Checking https://slicer.org/
Checking https://slicer.org/ - OK
--------
Checking https://expired.badssl.com/
Checking https://expired.badssl.com/ - OK  [Expected &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;]
--------
Checking https://github.com/
Checking https://github.com/ - OK

</code></pre>

---

## Post #14 by @lassoan (2023-03-26 13:56 UTC)

<p>Most often this kind of errors are due to overly aggressive firewalls/proxy servers/special network (mis)configuration to use custom SSL certificates, etc. But in this case the network seems to be OK because <a class="mention" href="/u/jcfr">@jcfr</a> on the same network and same operating system does not have any issue. <a class="mention" href="/u/dzenanz">@dzenanz</a> can you confirm that you have this issue when your computer is on the same network?</p>
<p>If they are on the same network then it must be something special on your computer. Maybe you could <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">try Dependency Walker to see if a wrong SSL DLL is loaded</a>. It would be also interesting to know if others on the same network and same operating system have the same issue as you.</p>

---

## Post #15 by @dzenanz (2023-03-27 13:03 UTC)

<p>Computer still not restarted. Outputs from JC’s script:</p>
<pre data-code-wrap="log"><code class="lang-plaintext">Microsoft Windows [Version 10.0.22621.1413]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Dzenan&gt;python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import sys
&gt;&gt;&gt; import traceback
&gt;&gt;&gt; import urllib.request
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; def processEvents():
...     try:
...         import slicer
...         slicer.app.processEvents()
...     except (AttributeError, ImportError):
...         pass
...
&gt;&gt;&gt;
&gt;&gt;&gt; def display(text, file=sys.stdout):
...     processEvents()
...     print(text, flush=True, file=file)
...
&gt;&gt;&gt;
&gt;&gt;&gt; def error(text):
...     display(text, file=sys.stderr)
...
&gt;&gt;&gt;
&gt;&gt;&gt; for url, expected_success in [
...     ("https://data.kitware.com", True),
...     ("https://www.httpvshttps.com/", True),
...     ("https://slicer.org/", True),
...     ("https://expired.badssl.com/", False),
...     ("https://github.com/", True),
... ]:
...     display("-" * 8)
...     display(f"Checking {url}")
...     try:
...         with urllib.request.urlopen(url) as response:
...            data = response.read()
...            html = data.decode('utf8')
...            assert "&lt;head&gt;" in html[:600]
...         if expected_success:
...             display(f"Checking {url} - OK")
...         else:
...             error(f"Checking {url} - FAILED - should have raised an exception")
...     except Exception as exc:
...         if expected_success:
...             error(f"Checking {url} - FAILED - unexpected exception")
...             traceback.print_exc()
...         else:
...             display(f"Checking {url} - OK  [Expected {exc}]")
...
--------
Checking https://data.kitware.com
Checking https://data.kitware.com - FAILED - unexpected exception
Traceback (most recent call last):
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Program Files\Python39\lib\http\client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1040, in _send_output
    self.send(msg)
  File "C:\Program Files\Python39\lib\http\client.py", line 980, in send
    self.connect()
  File "C:\Program Files\Python39\lib\http\client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
  File "C:\Program Files\Python39\lib\ssl.py", line 501, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Program Files\Python39\lib\ssl.py", line 1041, in _create
    self.do_handshake()
  File "C:\Program Files\Python39\lib\ssl.py", line 1310, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 11, in &lt;module&gt;
  File "C:\Program Files\Python39\lib\urllib\request.py", line 214, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 517, in open
    response = self._open(req, data)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "C:\Program Files\Python39\lib\urllib\request.py", line 494, in _call_chain
    result = func(*args)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1389, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;
--------
Checking https://www.httpvshttps.com/
Checking https://www.httpvshttps.com/ - FAILED - unexpected exception
Traceback (most recent call last):
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Program Files\Python39\lib\http\client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1040, in _send_output
    self.send(msg)
  File "C:\Program Files\Python39\lib\http\client.py", line 980, in send
    self.connect()
  File "C:\Program Files\Python39\lib\http\client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
  File "C:\Program Files\Python39\lib\ssl.py", line 501, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Program Files\Python39\lib\ssl.py", line 1041, in _create
    self.do_handshake()
  File "C:\Program Files\Python39\lib\ssl.py", line 1310, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 11, in &lt;module&gt;
  File "C:\Program Files\Python39\lib\urllib\request.py", line 214, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 517, in open
    response = self._open(req, data)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "C:\Program Files\Python39\lib\urllib\request.py", line 494, in _call_chain
    result = func(*args)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1389, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;
--------
Checking https://slicer.org/
Checking https://slicer.org/ - FAILED - unexpected exception
Traceback (most recent call last):
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Program Files\Python39\lib\http\client.py", line 1285, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1331, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1280, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python39\lib\http\client.py", line 1040, in _send_output
    self.send(msg)
  File "C:\Program Files\Python39\lib\http\client.py", line 980, in send
    self.connect()
  File "C:\Program Files\Python39\lib\http\client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
  File "C:\Program Files\Python39\lib\ssl.py", line 501, in wrap_socket
    return self.sslsocket_class._create(
  File "C:\Program Files\Python39\lib\ssl.py", line 1041, in _create
    self.do_handshake()
  File "C:\Program Files\Python39\lib\ssl.py", line 1310, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 11, in &lt;module&gt;
  File "C:\Program Files\Python39\lib\urllib\request.py", line 214, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 517, in open
    response = self._open(req, data)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "C:\Program Files\Python39\lib\urllib\request.py", line 494, in _call_chain
    result = func(*args)
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1389, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
  File "C:\Program Files\Python39\lib\urllib\request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;
--------
Checking https://expired.badssl.com/
Checking https://expired.badssl.com/ - OK  [Expected &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)&gt;]
--------
Checking https://github.com/
Checking https://github.com/ - OK
&gt;&gt;&gt; ^Z


C:\Users\Dzenan&gt;where python
C:\Program Files\Python39\python.exe
C:\Program Files\Python311\python.exe
C:\Users\Dzenan\AppData\Local\Microsoft\WindowsApps\python.exe

C:\Users\Dzenan&gt;"C:\Program Files\Python311\python.exe"
Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import sys
&gt;&gt;&gt; import traceback
&gt;&gt;&gt; import urllib.request
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; def processEvents():
...     try:
...         import slicer
...         slicer.app.processEvents()
...     except (AttributeError, ImportError):
...         pass
...
&gt;&gt;&gt;
&gt;&gt;&gt; def display(text, file=sys.stdout):
...     processEvents()
...     print(text, flush=True, file=file)
...
&gt;&gt;&gt;
&gt;&gt;&gt; def error(text):
...     display(text, file=sys.stderr)
...
&gt;&gt;&gt;
&gt;&gt;&gt; for url, expected_success in [
...     ("https://data.kitware.com", True),
...     ("https://www.httpvshttps.com/", True),
...     ("https://slicer.org/", True),
...     ("https://expired.badssl.com/", False),
...     ("https://github.com/", True),
... ]:
...     display("-" * 8)
...     display(f"Checking {url}")
...     try:
...         with urllib.request.urlopen(url) as response:
...            data = response.read()
...            html = data.decode('utf8')
...            assert "&lt;head&gt;" in html[:600]
...         if expected_success:
...             display(f"Checking {url} - OK")
...         else:
...             error(f"Checking {url} - FAILED - should have raised an exception")
...     except Exception as exc:
...         if expected_success:
...             error(f"Checking {url} - FAILED - unexpected exception")
...             traceback.print_exc()
...         else:
...             display(f"Checking {url} - OK  [Expected {exc}]")
...
--------
Checking https://data.kitware.com
Checking https://data.kitware.com - FAILED - unexpected exception
Traceback (most recent call last):
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1348, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Program Files\Python311\Lib\http\client.py", line 1282, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1328, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1277, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1037, in _send_output
    self.send(msg)
  File "C:\Program Files\Python311\Lib\http\client.py", line 975, in send
    self.connect()
  File "C:\Program Files\Python311\Lib\http\client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\ssl.py", line 517, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\ssl.py", line 1075, in _create
    self.do_handshake()
  File "C:\Program Files\Python311\Lib\ssl.py", line 1346, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 11, in &lt;module&gt;
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 216, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 519, in open
    response = self._open(req, data)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 536, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 496, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1391, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1351, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)&gt;
--------
Checking https://www.httpvshttps.com/
Checking https://www.httpvshttps.com/ - FAILED - unexpected exception
Traceback (most recent call last):
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1348, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Program Files\Python311\Lib\http\client.py", line 1282, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1328, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1277, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1037, in _send_output
    self.send(msg)
  File "C:\Program Files\Python311\Lib\http\client.py", line 975, in send
    self.connect()
  File "C:\Program Files\Python311\Lib\http\client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\ssl.py", line 517, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\ssl.py", line 1075, in _create
    self.do_handshake()
  File "C:\Program Files\Python311\Lib\ssl.py", line 1346, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 11, in &lt;module&gt;
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 216, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 519, in open
    response = self._open(req, data)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 536, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 496, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1391, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1351, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)&gt;
--------
Checking https://slicer.org/
Checking https://slicer.org/ - FAILED - unexpected exception
Traceback (most recent call last):
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1348, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "C:\Program Files\Python311\Lib\http\client.py", line 1282, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1328, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1277, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Program Files\Python311\Lib\http\client.py", line 1037, in _send_output
    self.send(msg)
  File "C:\Program Files\Python311\Lib\http\client.py", line 975, in send
    self.connect()
  File "C:\Program Files\Python311\Lib\http\client.py", line 1454, in connect
    self.sock = self._context.wrap_socket(self.sock,
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\ssl.py", line 517, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\ssl.py", line 1075, in _create
    self.do_handshake()
  File "C:\Program Files\Python311\Lib\ssl.py", line 1346, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 11, in &lt;module&gt;
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 216, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 519, in open
    response = self._open(req, data)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 536, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 496, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1391, in https_open
    return self.do_open(http.client.HTTPSConnection, req,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python311\Lib\urllib\request.py", line 1351, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)&gt;
--------
Checking https://expired.badssl.com/
Checking https://expired.badssl.com/ - OK  [Expected &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:992)&gt;]
--------
Checking https://github.com/
Checking https://github.com/ - OK
&gt;&gt;&gt; ^Z
</code></pre>
<p>On my Ubuntu box, the script works as expected. Restarting the computer now.</p>

---

## Post #16 by @dzenanz (2023-03-27 13:12 UTC)

<p>After restart, the error is still the same in system Python. I will now examine DLLs being loaded.</p>

---

## Post #17 by @dzenanz (2023-03-27 13:34 UTC)

<p>Exploring dependencies of both System Python, and SlicerApp-real.exe does not reveal anything interesting. JC’s script produces expected output on my laptop with Windows 11 and freshly installed Python 3.11.2.</p>
<p>I will ask Kitware’s sysadmin team for help. Thanks to everyone who has pitched in here.</p>

---

## Post #18 by @dzenanz (2023-04-06 13:20 UTC)

<p><code>conda update</code> stopped working, with a different error message. Can some actionable advice be gotten from this?</p>
<p>(M:\Something\env) M:\Something\deep_learning&gt;conda env update --prefix …/env --file environment.yml<br>
Retrieving notices: …working… ERROR conda.notices.fetch:get_channel_notice_response(63): Request error &lt;HTTPSConnectionPool(host=‘<a href="http://repo.anaconda.com" rel="noopener nofollow ugc">repo.anaconda.com</a>’, port=443): Max retries exceeded with url: /pkgs/r/notices.json (Caused by SSLError(“Can’t connect to HTTPS URL because the SSL module is not available.”))&gt; for channel: defaults url: <a href="https://repo.anaconda.com/pkgs/r/notices.json" rel="noopener nofollow ugc">https://repo.anaconda.com/pkgs/r/notices.json</a><br>
ERROR conda.notices.fetch:get_channel_notice_response(63): Request error &lt;HTTPSConnectionPool(host=‘<a href="http://repo.anaconda.com" rel="noopener nofollow ugc">repo.anaconda.com</a>’, port=443): Max retries exceeded with url: /pkgs/msys2/notices.json (Caused by SSLError(“Can’t connect to HTTPS URL because the SSL module is not available.”))&gt; for channel: defaults url: <a href="https://repo.anaconda.com/pkgs/msys2/notices.json" rel="noopener nofollow ugc">https://repo.anaconda.com/pkgs/msys2/notices.json</a><br>
ERROR conda.notices.fetch:get_channel_notice_response(63): Request error &lt;HTTPSConnectionPool(host=‘<a href="http://repo.anaconda.com" rel="noopener nofollow ugc">repo.anaconda.com</a>’, port=443): Max retries exceeded with url: /pkgs/main/notices.json (Caused by SSLError(“Can’t connect to HTTPS URL because the SSL module is not available.”))&gt; for channel: defaults url: <a href="https://repo.anaconda.com/pkgs/main/notices.json" rel="noopener nofollow ugc">https://repo.anaconda.com/pkgs/main/notices.json</a><br>
done<br>
Collecting package metadata (repodata.json): failed</p>
<p>CondaSSLError: OpenSSL appears to be unavailable on this machine. OpenSSL is required to<br>
download and install packages.</p>
<p>Exception: HTTPSConnectionPool(host=‘<a href="http://conda.anaconda.org" rel="noopener nofollow ugc">conda.anaconda.org</a>’, port=443): Max retries exceeded with url: /pytorch/win-64/repodata.json (Caused by SSLError(“Can’t connect to HTTPS URL because the SSL module is not available.”))</p>

---

## Post #19 by @dzenanz (2023-04-06 13:30 UTC)

<p>This conda issue is solved by <a href="https://stackoverflow.com/a/56934348/276168" rel="noopener nofollow ugc">copying some DLLs</a>, so I assume it is unrelated to my Python SSL issue.</p>

---

## Post #20 by @lassoan (2023-04-06 18:30 UTC)

<p>It is very hard to tell what’s causing your network problems. Most likely some software is messing with your SSL certifications or OpenSSL libraries. You can try searching for all OpenSSL dll instances on your computer and temporarily rename/remove them to see if it makes any difference (just leaving those in place that you are testing). You can also try logging in as a different user (maybe the troublesome software is only installed for your current user). You can also track down what exactly is happening (what executable files are loaded, what data files (SSL certificates, etc.) are accessed using <a href="https://learn.microsoft.com/en-us/sysinternals/downloads/procmon">Process Monitor</a>.</p>

---

## Post #21 by @dzenanz (2023-04-07 13:44 UTC)

<p>I have narrowed the problem down. This script works:</p>
<pre><code class="lang-py">import sys
import traceback
import urllib.request
import requests

def processEvents():
    try:
        import slicer
        slicer.app.processEvents()
    except (AttributeError, ImportError):
        pass

    
def display(text, file=sys.stdout):
    processEvents()
    print(text, flush=True, file=file)

    
def error(text):
    display(text, file=sys.stderr)


for url, expected_success in [
    ("https://data.kitware.com", True),
    ("https://www.httpvshttps.com/", True),
    ("https://slicer.org/", True),
    ("https://expired.badssl.com/", False),
    ("https://github.com/", True),
]:
    display("-" * 8)
    display(f"Checking {url}")
    goodCert = r"C:\Program Files\Python39\Lib\site-packages\certifi\cacert.pem"
    badCert = requests.utils.DEFAULT_CA_BUNDLE_PATH  # C:\Users\Dzenan\AppData\Local\.certifi
    try:
        with urllib.request.urlopen(url, cafile=goodCert) as response:
           data = response.read()
           html = data.decode('utf8')
           assert "&lt;head&gt;" in html[:600]
        if expected_success:
            display(f"Checking {url} - OK")
        else:
            error(f"Checking {url} - FAILED - should have raised an exception")
    except Exception as exc:
        if expected_success:
            error(f"Checking {url} - FAILED - unexpected exception")
            traceback.print_exc()
        else:
            display(f"Checking {url} - OK  [Expected {exc}]")
</code></pre>
<p>I tried copying <code>goodCert</code> into <code>badCert</code>’s place. But when this script is run, the <code>goodCert</code> gets turned into <code>badCert</code> by extending it by a bunch more entries. The file’s size is increased from 253KB to 425KB.</p>
<p>Does anyone have an idea what to try next?</p>

---

## Post #22 by @dzenanz (2023-04-07 17:00 UTC)

<p>I have now narrowed it down to a single certificate.</p>
<pre data-code-wrap="log"><code class="lang-plaintext">-----BEGIN CERTIFICATE-----
MIIEZTCCA02gAwIBAgIQQAF1BIMUpMghjISpDBbN3zANBgkqhkiG9w0BAQsFADA/
MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
DkRTVCBSb290IENBIFgzMB4XDTIwMTAwNzE5MjE0MFoXDTIxMDkyOTE5MjE0MFow
MjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxCzAJBgNVBAMT
AlIzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuwIVKMz2oJTTDxLs
jVWSw/iC8ZmmekKIp10mqrUrucVMsa+Oa/l1yKPXD0eUFFU1V4yeqKI5GfWCPEKp
Tm71O8Mu243AsFzzWTjn7c9p8FoLG77AlCQlh/o3cbMT5xys4Zvv2+Q7RVJFlqnB
U840yFLuta7tj95gcOKlVKu2bQ6XpUA0ayvTvGbrZjR8+muLj1cpmfgwF126cm/7
gcWt0oZYPRfH5wm78Sv3htzB2nFd1EbjzK0lwYi8YGd1ZrPxGPeiXOZT/zqItkel
/xMY6pgJdz+dU/nPAeX1pnAXFK9jpP+Zs5Od3FOnBv5IhR2haa4ldbsTzFID9e1R
oYvbFQIDAQABo4IBaDCCAWQwEgYDVR0TAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8E
BAMCAYYwSwYIKwYBBQUHAQEEPzA9MDsGCCsGAQUFBzAChi9odHRwOi8vYXBwcy5p
ZGVudHJ1c3QuY29tL3Jvb3RzL2RzdHJvb3RjYXgzLnA3YzAfBgNVHSMEGDAWgBTE
p7Gkeyxx+tvhS5B1/8QVYIWJEDBUBgNVHSAETTBLMAgGBmeBDAECATA/BgsrBgEE
AYLfEwEBATAwMC4GCCsGAQUFBwIBFiJodHRwOi8vY3BzLnJvb3QteDEubGV0c2Vu
Y3J5cHQub3JnMDwGA1UdHwQ1MDMwMaAvoC2GK2h0dHA6Ly9jcmwuaWRlbnRydXN0
LmNvbS9EU1RST09UQ0FYM0NSTC5jcmwwHQYDVR0OBBYEFBQusxe3WFbLrlAJQOYf
r52LFMLGMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjANBgkqhkiG9w0B
AQsFAAOCAQEA2UzgyfWEiDcx27sT4rP8i2tiEmxYt0l+PAK3qB8oYevO4C5z70kH
ejWEHx2taPDY/laBL21/WKZuNTYQHHPD5b1tXgHXbnL7KqC401dk5VvCadTQsvd8
S8MXjohyc9z9/G2948kLjmE6Flh9dDYrVYA9x2O+hEPGOaEOa1eePynBgPayvUfL
qjBstzLhWVQLGAkXXmNs+5ZnPBxzDJOLxhF2JIbeQAcH5H0tZrUlo5ZYyOqA7s9p
O5b85o3AM/OJ+CktFBQtfvBhcJVd9wvlwPsk+uyOy2HI7mNxKKgsBTt375teA2Tw
UdHkhVNcsAKX1H7GNNLOEADksd86wuoXvg==
-----END CERTIFICATE-----
</code></pre>
<p>human readable variant:</p>
<pre data-code-wrap="log"><code class="lang-plaintext">Certificate[129]:
Owner: CN=R3, O=Let's Encrypt, C=US
Issuer: CN=DST Root CA X3, O=Digital Signature Trust Co.
Serial number: 400175048314a4c8218c84a90c16cddf
Valid from: Wed Oct 07 15:21:40 EDT 2020 until: Wed Sep 29 15:21:40 EDT 2021
Certificate fingerprints:
SHA1: 48:50:4E:97:4C:0D:AC:5B:5C:D4:76:C8:20:22:74:B2:4C:8C:71:72
SHA256: 73:0C:1B:DC:D8:5F:57:CE:5D:C0:BB:A7:33:E5:F1:BA:5A:92:5B:2A:77:1D:64:0A:26:F7:A4:54:22:4D:AD:3B
Signature algorithm name: SHA256withRSA
Subject Public Key Algorithm: 2048-bit RSA key
Version: 3

Extensions:

#1: ObjectId: 1.3.6.1.5.5.7.1.1 Criticality=false
AuthorityInfoAccess [
  [
   accessMethod: caIssuers
   accessLocation: URIName: http://apps.identrust.com/roots/dstrootcax3.p7c
]
]

#2: ObjectId: 2.5.29.35 Criticality=false
AuthorityKeyIdentifier [
KeyIdentifier [
0000: C4 A7 B1 A4 7B 2C 71 FA   DB E1 4B 90 75 FF C4 15  .....,q...K.u...
0010: 60 85 89 10                                        `...
]
]

#3: ObjectId: 2.5.29.19 Criticality=true
BasicConstraints:[
  CA:true
  PathLen:0
]

#4: ObjectId: 2.5.29.31 Criticality=false
CRLDistributionPoints [
  [DistributionPoint:
     [URIName: http://crl.identrust.com/DSTROOTCAX3CRL.crl]
]]

#5: ObjectId: 2.5.29.32 Criticality=false
CertificatePolicies [
  [CertificatePolicyId: [2.23.140.1.2.1]
[]  ]
  [CertificatePolicyId: [1.3.6.1.4.1.44947.1.1.1]
[PolicyQualifierInfo: [
  qualifierID: 1.3.6.1.5.5.7.2.1
  qualifier: 0000: 16 22 68 74 74 70 3A 2F   2F 63 70 73 2E 72 6F 6F  ."http://cps.roo
0010: 74 2D 78 31 2E 6C 65 74   73 65 6E 63 72 79 70 74  t-x1.letsencrypt
0020: 2E 6F 72 67                                        .org

]]  ]
]

#6: ObjectId: 2.5.29.37 Criticality=false
ExtendedKeyUsages [
  serverAuth
  clientAuth
]

#7: ObjectId: 2.5.29.15 Criticality=true
KeyUsage [
  DigitalSignature
  Key_CertSign
  Crl_Sign
]

#8: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: 14 2E B3 17 B7 58 56 CB   AE 50 09 40 E6 1F AF 9D  .....XV..P.@....
0010: 8B 14 C2 C6                                        ....
]
]
</code></pre>
<p>If this certificate is not present in cacert.pem, the script works as it should. If this certificate is present, all websites have “certificate has expired” problem within Python.</p>
<p>I tried deleting it from the local computer, but it reappeared.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7319386a92a10d3569b1dc1a38b28f0208aec38.jpeg" data-download-href="/uploads/short-url/zgM9pOygUL5Vjjxb0feCZVTnZuE.jpeg?dl=1" title="Screenshot 2023-04-07 12.49.16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7319386a92a10d3569b1dc1a38b28f0208aec38_2_508x500.jpeg" alt="Screenshot 2023-04-07 12.49.16" data-base62-sha1="zgM9pOygUL5Vjjxb0feCZVTnZuE" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7319386a92a10d3569b1dc1a38b28f0208aec38_2_508x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7319386a92a10d3569b1dc1a38b28f0208aec38_2_762x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7319386a92a10d3569b1dc1a38b28f0208aec38_2_1016x1000.jpeg 2x" data-dominant-color="E2E4E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-07 12.49.16</span><span class="informations">1379×1355 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @jcfr (2023-04-07 17:14 UTC)

<p>The <code>DST Root CA X3</code> certificate expired <sup class="footnote-ref"><a href="#footnote-93209-1" id="footnote-ref-93209-1">[1]</a></sup> in September 2021.</p>
<p>Consider updating the version of <code>certifi</code> associated with your Python install. See <a href="https://pypi.org/project/certifi/">https://pypi.org/project/certifi/</a></p>
<blockquote>
<p>But when this script is run, the <code>goodCert</code> gets turned into <code>badCert</code> by extending it by a bunch more entries.</p>
</blockquote>
<p>Involved functions are the following:</p>
<ul>
<li><a href="https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen">https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen</a></li>
<li><a href="https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations">https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations</a></li>
</ul>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-93209-1" class="footnote-item"><p><a href="https://letsencrypt.org/docs/dst-root-ca-x3-expiration-september-2021/" class="inline-onebox">DST Root CA X3 Expiration (September 2021) - Let's Encrypt</a> <a href="#footnote-ref-93209-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #24 by @dzenanz (2023-04-07 20:13 UTC)

<p>JC and I had a debugging session on my computer. We didn’t resolve the problem. But JC found this:</p>
<blockquote>
<p>Starting with Python 2.7.9 and 3.2, the function “ssl.create_default_context()” automatically loads system certificates. This explains why the “Slicer.crt” we provide (through the SSL_CERT_FILE env. variable expected by openssl) is being ignored</p>
</blockquote>

---

## Post #25 by @dzenanz (2023-04-07 20:22 UTC)

<p>I also figured out why the certificate comes back after I delete it:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6330fab6af558ce741eb1b8f21a6ec54b992df9.png" alt="Screenshot 2023-04-07 15.49.39" data-base62-sha1="nIgEOeTQH7ojpC8SBOYzkor7xep" width="614" height="369"><br>
And in text form for easier searching:</p>
<blockquote>
<p>Deleting system root certificates might prevent some Windows components from working properly. The list of system critical root certificates can be reviewed at <a href="https://support.microsoft.com/?id=293781" class="inline-onebox" rel="noopener nofollow ugc">Microsoft Support</a>. If Update Root Certificates is installed, any deleted third-party root certificates will be restored automatically, but the system root certificates will not. Do you want to delete the selected certificate(s)?</p>
</blockquote>

---

## Post #26 by @dzenanz (2023-04-07 20:50 UTC)

<p>Downloading and installing certificates from <a href="https://www.stephenwagner.com/2021/09/30/sophos-dst-root-ca-x3-expiration-problems-fix/" rel="noopener nofollow ugc">this website</a> solved the problem for me. Here are the links:</p>
<blockquote>
<p>Root CA Certificates (PEM format):</p>
<ul>
<li><a href="https://letsencrypt.org/certs/isrgrootx1.pem" rel="noopener nofollow ugc">ISRG Root X1</a> (Or <a href="https://letsencrypt.org/certs/isrgrootx1.der" rel="noopener nofollow ugc">ISRG Root X1 DER Format</a>)</li>
<li><a href="https://letsencrypt.org/certs/isrg-root-x2.pem" rel="noopener nofollow ugc">ISRG Root X2</a> (Or <a href="https://letsencrypt.org/certs/isrg-root-x2.der" rel="noopener nofollow ugc">ISRG Root X2 DER Format</a>)</li>
</ul>
<p>Intermediate Certificate (PEM format):</p>
<ul>
<li><a href="https://letsencrypt.org/certs/lets-encrypt-r3.pem" rel="noopener nofollow ugc">Let’s Encrypt R3</a> (Or <a href="https://letsencrypt.org/certs/lets-encrypt-r3.der" rel="noopener nofollow ugc">Let’s Encrypt R3 DER Format</a>)</li>
</ul>
</blockquote>
<p>Thank you JC, Andras and <a class="mention" href="/u/jake.stookey">@jake.stookey</a> for the help.</p>

---
