# Certificate issue for sample data download

**Topic ID**: 17454
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/certificate-issue-for-sample-data-download/17454

---

## Post #1 by @muratmaga (2021-05-04 18:28 UTC)

<p>We have this on going issue with sample data not being available when we run Slicer on our Linux servers at work:</p>
<p><code>Switch to module: "SampleData" &lt;b&gt;Requesting download&lt;/b&gt; &lt;i&gt;MR-head.nrrd&lt;/i&gt; from https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/cc211f0dfd9a05ca3841ce1141b292898b2dd2d3f08286affadf823a7e58df93 ... &lt;font color="red"&gt;&lt;b&gt; Download failed: &lt;urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)&gt;&lt;/b&gt;&lt;/font&gt; </code></p>
<p>On the same server (and in the same command line session), I can start firefox and paste the exact url and download the data. There is no http_proxy or any other variable set. The admin asked this:</p>
<p>“Does slicer have its own certificate store? Or does it have a flag to say which certificate store to use?”</p>
<p>I do not know the answer to this question. Any ideas?</p>

---

## Post #2 by @jcfr (2021-05-04 18:52 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="17454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>“Does slicer have its own certificate store? Or does it have a flag to say which certificate store to use?”</p>
<p>I do not know the answer to this question. Any ideas?</p>
</blockquote>
</aside>
<p>We indeed generate own certificate bundle.<br>
See <a href="https://github.com/Slicer/Slicer/tree/master/Base/QTCore/Resources/Certs" class="inline-onebox">Slicer/Base/QTCore/Resources/Certs at main · Slicer/Slicer · GitHub</a></p>
<p>Which version of Slicer is problematic ?</p>

---

## Post #3 by @muratmaga (2021-05-04 19:04 UTC)

<p>This was with the latest stable, but as far as I know every version had the issue.</p>

---

## Post #4 by @jcfr (2021-05-04 19:15 UTC)

<p>Which operating system ?  Is the issue specific to macOS ?</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Slicer version</th>
<th>Operating System</th>
<th>Type of build</th>
<th>SampleData download working</th>
</tr>
</thead>
<tbody>
<tr>
<td>4.13.0 / r29885</td>
<td>Windows</td>
<td>Preview installer</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:"> yes</td>
</tr>
<tr>
<td>4.13.0 / r29874</td>
<td>Linux</td>
<td>Local Developer build</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=9" title=":white_check_mark:" class="emoji" alt=":white_check_mark:"> yes</td>
</tr>
</tbody>
</table>
</div>

---

## Post #5 by @muratmaga (2021-05-04 19:42 UTC)

<p>This is on Linux. However, the issue is specific to our Linux environment, I think.</p>

---

## Post #6 by @jcfr (2021-05-04 19:49 UTC)

<blockquote>
<p>the issue is specific to our Linux environment</p>
</blockquote>
<p>It would be great to sort this out.</p>
<p>Few hints:</p>
<ul>
<li>Does Slicer pick up a different version of OpenSSL ?</li>
<li>Is the env. variable <code>SSL_CERT_FILE</code> set to a valid bundle ?</li>
</ul>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L68-L71">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L68-L71" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L68-L71" target="_blank" rel="noopener">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L68-L71</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="68" style="counter-reset: li-counter 67 ;">
          <li>  list(APPEND PYTHONLAUNCHER_ENVVARS_BUILD</li>
          <li>    "SSL_CERT_FILE=&lt;APPLAUNCHER_DIR&gt;/../../Slicer-build/${Slicer_SHARE_DIR}/Slicer.crt"</li>
          <li>    )</li>
          <li>endif()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L114-L118">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L114-L118" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L114-L118" target="_blank" rel="noopener">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/SuperBuild/python_configure_python_launcher.cmake#L114-L118</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="114" style="counter-reset: li-counter 113 ;">
          <li>if(PYTHON_ENABLE_SSL)</li>
          <li>  list(APPEND PYTHONLAUNCHER_ENVVARS_INSTALLED</li>
          <li>    "SSL_CERT_FILE=&lt;APPLAUNCHER_DIR&gt;/../${Slicer_SHARE_DIR}/Slicer.crt"</li>
          <li>    )</li>
          <li>endif()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @muratmaga (2021-05-04 21:38 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="17454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Does Slicer pick up a different version of OpenSSL ?</p>
</blockquote>
</aside>
<p>This is what I get from the command prompt prior to launching Slicer:</p>
<pre><code>    amaga@pplhpc1ood01:/gpfs/home/amaga/Desktop$ ldconfig -p |grep -i ssl
    	libssl3.so (libc6,x86-64) =&gt; /lib64/libssl3.so
    	libssl.so.10 (libc6,x86-64) =&gt; /lib64/libssl.so.10
    	libssl.so (libc6,x86-64) =&gt; /lib64/libssl.so
    	libevent_openssl-2.0.so.5 (libc6,x86-64) =&gt; /lib64/libevent_openssl-2.0.so.5
</code></pre>
<p>setting</p>
<p><code>export SSL_CERT_FILE=/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem</code></p>
<p>has no effect.</p>

---

## Post #8 by @muratmaga (2021-05-05 18:37 UTC)

<p>Nor setting the SSL_CERT_FILE variable to the Slicer.crt in Slicer install directory.</p>

---
