---
topic_id: 10908
title: "Which To Choose Crash Or Build Failure"
date: 2020-03-30
url: https://discourse.slicer.org/t/10908
---

# Which to choose: Crash or Build failure?

**Topic ID**: 10908
**Date**: 2020-03-30
**URL**: https://discourse.slicer.org/t/which-to-choose-crash-or-build-failure/10908

---

## Post #1 by @gcsharp (2020-03-30 17:33 UTC)

<p>Hi all,<br>
This is on Debian buster (stable).</p>
<p>If I set Slicer_USE_PYTHONQT_WITH_OPENSSL=ON, Slicer builds, but it crashes due to the popular OpenSSL version mismatch issue.</p>
<p>If I set Slicer_USE_PYTHONQT_WITH_OPENSSL=OFF, Slicer build fails with the following:</p>
<pre><code>[ 19%] Performing install step for 'python-setuptools'
CMake Error at /PHShome/gcs6/build/slicer-4/Slicer-build/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-Debug.cmake:16 (message):
  Command failed: 1

   '/PHShome/gcs6/build/slicer-4/Slicer-build/python-install/bin/PythonSlicer' '-m' 'pip' 'install' '--require-hashes' '-r' '/PHShome/gcs6/build/slicer-4/Slicer-build/python-setuptools-requirements.txt'
</code></pre>
<p>More information here:</p>
<pre><code>$ cat /PHShome/gcs6/build/slicer-4/Slicer-build/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-*.log
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
  Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Could not find a version that satisfies the requirement setuptools==46.0.0 (from -r /PHShome/gcs6/build/slicer-4/Slicer-build/python-setuptools-requirements.txt (line 1)) (from versions: )
No matching distribution found for setuptools==46.0.0 (from -r /PHShome/gcs6/build/slicer-4/Slicer-build/python-setuptools-requirements.txt (line 1))
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
Collecting setuptools==46.0.0 (from -r /PHShome/gcs6/build/slicer-4/Slicer-build/python-setuptools-requirements.txt (line 1))
  Could not fetch URL https://pypi.org/simple/setuptools/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/setuptools/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)) - skipping
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)) - skipping
</code></pre>
<p>Any thoughts on solving either problem?</p>

---

## Post #2 by @jamesobutler (2020-03-30 18:48 UTC)

<p>This looks quite similar to what another user described in <a href="https://discourse.slicer.org/t/failed-in-building-3d-slicer-on-win10-with-vs2015x64/10773" class="inline-onebox">Failed in building 3D Slicer on win10 with vs2015x64</a>. Is there anything on that thread you might be able try? In that case I think the OpenSSL version from an Anaconda install was a problem.</p>

---

## Post #3 by @gcsharp (2020-03-30 20:25 UTC)

<p>Thank you James, it is an interesting thread.  I’m not sure, however, what to make from it.  It seems that I would have to uninstall OpenSSL, which hundreds of programs depend on.</p>
<p>If I could just tell Slicer to use my OpenSSL instead of its own, I guess the problem would go away.</p>
<p>The other choice could be to build the necessary Qt dependencies against the Slicer-provided OpenSSL.  Is there an easy way to do this?</p>

---

## Post #4 by @jamesobutler (2020-03-31 00:59 UTC)

<p>I haven’t yet looked into using a system OpenSSL instead of the one Slicer uses by default (<a href="https://github.com/Slicer/Slicer-OpenSSL" rel="nofollow noopener">https://github.com/Slicer/Slicer-OpenSSL</a>).</p>
<p>I do think Slicer is long over due to using the latest OpenSSL 1.1.1 version since older releases are not supported anymore. This would probably at least avoid incompatibilities. Qt 5.12.4 I know was the first release on that line to support OpenSSL 1.1.1</p>

---

## Post #5 by @gcsharp (2020-03-31 15:19 UTC)

<p>Indeed.  Debian stable is on 1.1.1.</p>

---

## Post #6 by @jamesobutler (2020-04-01 03:22 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="3" data-topic="10908">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>If I could just tell Slicer to use my OpenSSL instead of its own, I guess the problem would go away.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> You can try and follow these instructions</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/9403adc7ebe768be78a5a5033c39f7424f72adaf/SuperBuild/External_OpenSSL.cmake#L183-L186">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/9403adc7ebe768be78a5a5033c39f7424f72adaf/SuperBuild/External_OpenSSL.cmake#L183-L186" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/9403adc7ebe768be78a5a5033c39f7424f72adaf/SuperBuild/External_OpenSSL.cmake#L183-L186" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/9403adc7ebe768be78a5a5033c39f7424f72adaf/SuperBuild/External_OpenSSL.cmake#L183-L186</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="183" style="counter-reset: li-counter 182 ;">
          <li>(2) configure Slicer providing your own version of OpenSSL that matches the version</li>
          <li>    of OpenSSL also used to compile Qt library.</li>
          <li>    The options to specify are OPENSSL_INCLUDE_DIR, LIB_EAY_DEBUG, LIB_EAY_RELEASE,</li>
          <li>    SSL_EAY_DEBUG and SSL_EAY_RELEASE.")</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
