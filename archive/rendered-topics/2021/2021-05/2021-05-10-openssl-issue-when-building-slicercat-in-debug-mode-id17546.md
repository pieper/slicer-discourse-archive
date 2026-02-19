---
topic_id: 17546
title: "Openssl Issue When Building Slicercat In Debug Mode"
date: 2021-05-10
url: https://discourse.slicer.org/t/17546
---

# OpenSSL issue when building SlicerCAT in Debug mode

**Topic ID**: 17546
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/openssl-issue-when-building-slicercat-in-debug-mode/17546

---

## Post #1 by @keri (2021-05-10 14:08 UTC)

<p>Hi,</p>
<p><strong>On Linux (Ubuntu 20.04)</strong> when SlicerCAT is built in <strong>Debug</strong> mode and I try to use wget in a way:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; import wget
&gt;&gt;&gt; url = "https://julialang-s3.julialang.org/bin/linux/x64/1.6/julia-1.6.1-linux-x86_64.tar.gz"
&gt;&gt;&gt; wget.download(url)
</code></pre>
<p>I get an error:</p>
<pre data-code-wrap="python"><code class="lang-python">Traceback (most recent call last):
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 1318, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/http/client.py", line 1239, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/http/client.py", line 1285, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/http/client.py", line 1234, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/http/client.py", line 1026, in _send_output
    self.send(msg)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/http/client.py", line 964, in send
    self.connect()
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/http/client.py", line 1400, in connect
    server_hostname=server_hostname)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/ssl.py", line 407, in wrap_socket
    _context=self, _session=session)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/ssl.py", line 817, in __init__
    self.do_handshake()
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/ssl.py", line 1077, in do_handshake
    self._sslobj.do_handshake()
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/ssl.py", line 689, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/site-packages/wget.py", line 526, in download
    (tmpfile, headers) = ulib.urlretrieve(binurl, tmpfile, callback)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 248, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 223, in urlopen
    return opener.open(url, data, timeout)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 526, in open
    response = self._open(req, data)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 544, in _open
    '_open', req)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 504, in _call_chain
    result = func(*args)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 1361, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/home/kerim/Documents/Colada/d/python-install/lib/python3.6/urllib/request.py", line 1320, in do_open
    raise URLError(err)
urllib.error.URLError: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)&gt;
</code></pre>
<p>There is no problems when doing the same on SlicerCAT <strong>Release</strong> mode.</p>
<p>I’ve tried to google the problem but as I understood usually <a href="https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error?page=1&amp;tab=votes#tab-top" rel="noopener nofollow ugc">this problem happens on macOS</a></p>
<p>Also python notes tells that some problems may arise when building <a href="https://www.python.org/downloads/release/python-360/" rel="noopener nofollow ugc">python 3.6 from source against OpenSSL 1.1.0c</a>:</p>
<blockquote>
<ul>
<li>If you are building Python from source, beware that the OpenSSL 1.1.0c release, the most recent as of this update, is known to cause Python 3.6 test suite failures and its use should be avoided without additional patches. It is expected that the next release of the OpenSSL 1.1.0 series will fix these problems. See <a href="http://bugs.python.org/issue28689" class="inline-onebox" rel="noopener nofollow ugc">Issue 28689: OpenSSL 1.1.0c test failures - Python tracker</a> for more information.</li>
</ul>
</blockquote>
<p>By the way on Windows 10 there were no such problems. At least it worked for SlicerCAT Debug (haven’t tried Release).</p>
<p>Could someone approve this problem or refute it?<br>
May this happen because of OpenSSL config (release/debug) mismatch with python config?</p>
<p>P.S. <a href="https://github.com/johnnychen94/jill.py/issues/68" rel="noopener nofollow ugc">additional information</a></p>

---

## Post #2 by @keri (2021-06-22 20:05 UTC)

<p>I’m recompiling my slicercat and I noticed that there is actually no difference whether I use debug or release config: any of them gives the same mentionned error.</p>
<p><strong>I guess the error is caused by OpenSSL missing certificate.</strong></p>
<p>On almost <strong>fresh Ubuntu 20.04</strong> the PythonSlicer command:</p>
<pre><code class="lang-python">import ssl
ssl.get_default_verify_paths()
</code></pre>
<p><strong>gives:</strong></p>
<p><em>DefaultVerifyPaths(cafile=None, capath=’/home/kerim/.vs/T/out/build/Linux-GCC-Debug/OpenSSL/certs’, openssl_cafile_env=‘SSL_CERT_FILE’, openssl_cafile=’/home/kerim/.vs/T/out/build/Linux-GCC-Debug/OpenSSL/cert.pem’, openssl_capath_env=‘SSL_CERT_DIR’, openssl_capath=’/home/kerim/.vs/T/out/build/Linux-GCC-Debug/OpenSSL/certs’)</em></p>
<p>(by the way there is no <em>/home/kerim/.vs/T/out/build/Linux-GCC-Debug/OpenSSL/certs</em> folder)</p>
<p><strong>and on Windows 10 the output is:</strong><br>
<em>DefaultVerifyPaths(cafile=‘C:/C/d/python-install/bin/…/…/Slicer-build/share/Colada-4.13/Slicer.crt’, capath=‘C:\Program Files\Common Files\SSL/certs’, openssl_cafile_env=‘SSL_CERT_FILE’, openssl_cafile=‘C:\Program Files\Common Files\SSL/cert.pem’, openssl_capath_env=‘SSL_CERT_DIR’, openssl_capath=‘C:\Program Files\Common Files\SSL/certs’)</em></p>
<p>Output on Ubuntu is gotten while slicercat was not completely installed as it has external package (External_julia.cmake) that depends on python and uses <code>wget</code> inside python and thus produces the mentionned error while build step.</p>
<p>Output on Windows 10 is gotten after complete slicercat installation.</p>
<p>So what may be the reason why SSL path are so different on Ubuntu and Windows 10?<br>
Also will Ubuntu add this file after complete Slicer build <code>C:/C/d/python-install/bin/../../Slicer-build/share/Colada-4.13/Slicer.crt</code>?</p>

---

## Post #3 by @keri (2021-06-25 15:16 UTC)

<p>I understood the error that I used to get.</p>
<p>During build step Slicer somehow changes <code>ssl.get_default_verify_paths()</code> as after full Slicer installation I can see that these paths are fine even on my Ubuntu. I have not found where Slicer do that but it does.</p>
<p>The question then: if I have an external dependency <code>External_julia.cmake</code> which calls <code>wget</code> inside python script (and thus gives me the error above) how can I tell to that external julia project that it needs to be compiled after Slicer is built in my SlicerCAT app? Because usually <code>External_julia.cmake</code> project is called before Slicer is built and this gives me error above (I need somehow specify Slicer as julia dependency).</p>

---

## Post #4 by @lassoan (2021-06-25 17:30 UTC)

<p>You can set dependencies between projects in CMake. See for example here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_ParameterSerializer.cmake#L8">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_ParameterSerializer.cmake#L8" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/SuperBuild/External_ParameterSerializer.cmake#L8" target="_blank" rel="noopener">Slicer/Slicer/blob/master/SuperBuild/External_ParameterSerializer.cmake#L8</a></h4>



  <pre class="onebox">    <code class="lang-cmake">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>
          </li>
<li>set( proj ParameterSerializer )</li>
          <li>
          </li>
<li># Set dependency list</li>
          <li>set(${proj}_DEPENDENCIES JsonCpp ITK)</li>
          <li>
          </li>
<li># Include dependent projects if any</li>
          <li class="selected">ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDENCIES)</li>
          <li>
          </li>
<li># Sanity checks</li>
          <li>if(Slicer_USE_SYSTEM_${proj})</li>
          <li>  message(FATAL_ERROR "Enabling Slicer_USE_SYSTEM_${proj} is not supported !")</li>
          <li>endif()</li>
          <li>if(DEFINED ${proj}_DIR AND NOT EXISTS ${${proj}_DIR})</li>
          <li>  message(FATAL_ERROR "${proj}_DIR variable is defined but corresponds to nonexistent directory")</li>
          <li>endif()</li>
          <li>
          </li>
<li>if(NOT DEFINED ${proj}_DIR AND NOT Slicer_USE_SYSTEM_${proj})</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @keri (2021-06-25 23:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you for answer<br>
The problem is that it seems I can’t write it:</p>
<pre><code class="lang-auto">set(${proj}_DEPENDENCIES
  Slicer    # Slicer is not an external project so I can't add it as a dependency
  )

ExternalProject_Include_Dependencies(${proj} PROJECT_VAR proj DEPENDS_VAR ${proj}_DEPENDENCIES)
</code></pre>
<p>and I need to build <code>julia</code> after all OpenSSL staff are done. And I guess it is done on the <code>Slicer</code> build step</p>

---

## Post #6 by @lassoan (2021-06-26 00:13 UTC)

<p>If you depend on openssl then you can add that as dependency. If Slicer does not depend on Julia (it should not) then you can create a superbuild type extension and build Julia in that. Extensions are built after Slicer build is completed and superbuild type extensions can build additional libraries. An additional advantage of building everything in an extension is that users can install it by a single click in the Extensions manager in Slicer.</p>
<p>By the way, there seems to beany options for running Python code from Julia. Have you looked into those? The simplest is probably to implement a CLI module in Julia, the same way as the Slicer MatlabBridge works.</p>

---

## Post #7 by @keri (2021-06-26 10:56 UTC)

<p>Probably making an extension is the right decision. Thank you</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="17546">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>By the way, there seems to beany options for running Python code from Julia. Have you looked into those? The simplest is probably to implement a CLI module in Julia, the same way as the Slicer MatlabBridge works.</p>
</blockquote>
</aside>
<p>For now I rely on <a href="https://github.com/JuliaPy/pyjulia" rel="noopener nofollow ugc">pyjulia</a> abilities. I remember we had an <a href="https://discourse.slicer.org/t/use-julia-with-slicer/16765/5">conversation on that</a>. I will refer to that later when I work with julia staff more closely</p>

---
