# SSL error with the sample data module (Linux only)

**Topic ID**: 8572
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/ssl-error-with-the-sample-data-module-linux-only/8572

---

## Post #1 by @muratmaga (2019-09-25 20:35 UTC)

<p>I am getting a SSL certificate error for the sample data with distribute with SlicerMorph. This is the URL:<br>
<a href="https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true" class="onebox" target="_blank" rel="nofollow noopener">https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true</a></p>
<p>I can get to this file from a web browser using the same in Linux box, but I when I use the sample data module I get this error messages with a [SSL:: CERTIFICATE_VERIFY_FAILED] and it only happens with our Linux boxes. Windows doesn’t seem to be affected.</p>
<pre><code class="lang-auto">Download failed: Traceback (most recent call last): 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 1318, in do_open encode_chunked=req.has_header('Transfer-encoding')) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1239, in request self._send_request(method, url, body, headers, encode_chunked) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1285, in _send_request self.endheaders(body, encode_chunked=encode_chunked) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1234, in endheaders self._send_output(message_body, encode_chunked=encode_chunked) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1026, in _send_output self.send(msg) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 964, in send self.connect() 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1400, in connect server_hostname=server_hostname) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 407, in wrap_socket _context=self, _session=session) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 817, in __init__ self.do_handshake() 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 1077, in do_handshake self._sslobj.do_handshake() 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 689, in do_handshake self._sslobj.do_handshake() ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847) 

During handling of the above exception, another exception occurred: Traceback (most recent call last): File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 812, in download
File urllib.request.urlretrieve(uri, filePath, self.reportHook) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 248, in urlretrieve with contextlib.closing(urlopen(url, data)) as fp: 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 223, in urlopen return opener.open(url, data, timeout) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 526, in open response = self._open(req, data) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 544, in _open '_open', req) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 504, in _call_chain result = func(*args) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 1361, in https_open context=self._context, check_hostname=self._check_hostname) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 1320, in do_open raise URLError(err) urllib.error.URLError: 

During handling of the above exception, another exception occurred: Traceback (most recent call last): 
File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 609, in downloadFromSource filePath = self.downloadFileIntoCache(uri, fileName, checksum) F
ile "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 576, in downloadFileIntoCache return self.downloadFile(uri, destFolderPath, name, checksum) 
File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 816, in downloadFile raise ValueError(f"Failed to download {uri} to {filePath}") ValueError: Failed to download https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true to /home/maga/SlicerTemp/RemoteIO/mouse_skull_LMs.zip 

During handling of the above exception, another exception occurred: Traceback (most recent call last): 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 1318, in do_open encode_chunked=req.has_header('Transfer-encoding')) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1239, in request self._send_request(method, url, body, headers, encode_chunked) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1285, in _send_request self.endheaders(body, encode_chunked=encode_chunked) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1234, in endheaders self._send_output(message_body, encode_chunked=encode_chunked) File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1026, in _send_output self.send(msg) File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 964, in send self.connect() 
File "/home/maga/Slicer/lib/Python/lib/python3.6/http/client.py", line 1400, in connect server_hostname=server_hostname) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 407, in wrap_socket _context=self, _session=session) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 817, in __init__ self.do_handshake() 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 1077, in do_handshake self._sslobj.do_handshake() 
File "/home/maga/Slicer/lib/Python/lib/python3.6/ssl.py", line 689, in do_handshake self._sslobj.do_handshake() ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847) 

During handling of the above exception, another exception occurred: Traceback (most recent call last): 
File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 812, in downloadFile urllib.request.urlretrieve(uri, filePath, self.reportHook) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 248, in urlretrieve with contextlib.closing(urlopen(url, data)) as fp: 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 223, in urlopen return opener.open(url, data, timeout) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 526, in open response = self._open(req, data) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 544, in _open '_open', req) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 504, in _call_chain result = func(*args) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 1361, in https_open context=self._context, check_hostname=self._check_hostname) 
File "/home/maga/Slicer/lib/Python/lib/python3.6/urllib/request.py", line 1320, in do_open raise URLError(err) urllib.error.URLError: 

During handling of the above exception, another exception occurred: Traceback (most recent call last): 
File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 355, in b.connect('clicked()', lambda s=source: logic.downloadFromSource(s)) 
File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 614, in downloadFromSource filePath = self.downloadFileIntoCache(uri, fileName, checksum) 
File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 576, in downloadFileIntoCache return self.downloadFile(uri, destFolderPath, name, checksum) 
File "/home/maga/Slicer/bin/../lib/Slicer-4.11/qt-scripted-modules/SampleData.py", line 816, in downloadFile raise ValueError(f"Failed to download {uri} to {filePath}") ValueError: Failed to download https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true to /home/maga/SlicerTemp/RemoteIO/mouse_skull_LMs.zip
</code></pre>

---

## Post #2 by @pieper (2019-09-25 21:32 UTC)

<p>Hmm, perhaps we need to update our version of <code>certifi</code> or other certificates.  Was this with 4.10.2 or the nightly or both?</p>

---

## Post #3 by @muratmaga (2019-10-15 19:49 UTC)

<p>It was with nightly, we really have no use for 4.10.2 anymore (with the all the changes to markups). But I can download and try if it is going to help.</p>

---

## Post #4 by @jcfr (2019-10-15 21:29 UTC)

<p>Could you also try the execute the following statements and report back ?</p>
<ul>
<li>
<p>(1) from Slicer python interactor</p>
</li>
<li>
<p>(2) from python interpreter shipped with Slicer (found in <code>/path/to/install/bin/PythonSlicer</code></p>
</li>
</ul>
<p>python code to execute:</p>
<pre><code class="lang-python">import urllib.request
urllib.request.urlretrieve("https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true", "/tmp//mouse_skull_LMs.zip")
</code></pre>

---

## Post #5 by @muratmaga (2019-10-16 03:28 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="8572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<pre><code class="lang-auto">import urllib.request
urllib.request.urlretrieve("https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true", "/tmp//mouse_skull_LMs.zip")
</code></pre>
</blockquote>
</aside>
<p>from <strong><span class="hashtag-raw">#1</span></strong></p>
<pre data-code-wrap="python"><code class="lang-python">    &gt;&gt;&gt; import urllib.request
    &gt;&gt;&gt; urllib.request.urlretrieve("https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true", "/tmp//mouse_skull_LMs.zip")
    Traceback (most recent call last):
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1026, in _send_output
    self.send(msg)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 964, in send
    self.connect()
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1400, in connect
    server_hostname=server_hostname)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 407, in wrap_socket
    _context=self, _session=session)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 817, in __init__
    self.do_handshake()
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 1077, in do_handshake
    self._sslobj.do_handshake()
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 689, in do_handshake
    self._sslobj.do_handshake()
    ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "&lt;console&gt;", line 1, in &lt;module&gt;
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 248, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 526, in open
    response = self._open(req, data)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 544, in _open
    '_open', req)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
      File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 1320, in do_open
    raise URLError(err)
    urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)&gt;
</code></pre>
<p>from <strong><span class="hashtag-raw">#2</span></strong></p>
<pre data-code-wrap="python"><code class="lang-python">[maga@magalab-head bin]$ PythonSlicer 
Python 3.6.7 (default, Sep 25 2019, 03:07:17) 
[GCC 5.3.1 20160406 (Red Hat 5.3.1-6)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; import urllib.request
urllib.request.urlretrieve("https://github.com/SlicerMorph/SampleData/blob/master/mouse_skull_LMs.zip?raw=true", "/tmp//mouse_skull_LMs.zip")

&gt;&gt;&gt; Traceback (most recent call last):
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1026, in _send_output
    self.send(msg)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 964, in send
    self.connect()
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/http/client.py", line 1400, in connect
    server_hostname=server_hostname)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 407, in wrap_socket
    _context=self, _session=session)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 817, in __init__
    self.do_handshake()
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 1077, in do_handshake
    self._sslobj.do_handshake()
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/ssl.py", line 689, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 248, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 526, in open
    response = self._open(req, data)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 544, in _open
    '_open', req)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/usr/local/Slicer-4.11.0-2019-09-24-linux-amd64/lib/Python/lib/python3.6/urllib/request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)&gt;
</code></pre>

---
