# Python-scipy build error

**Topic ID**: 26616
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/python-scipy-build-error/26616

---

## Post #1 by @miniminic (2022-12-07 04:55 UTC)

<p>python-scipy-install-err.log</p>
<pre><code class="lang-auto">WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/scipy/
ERROR: Could not find a version that satisfies the requirement scipy==1.8.1 (from versions: none)
ERROR: No matching distribution found for scipy==1.8.1

</code></pre>
<p>python-scipy-install-out.log</p>
<pre><code class="lang-auto">Could not fetch URL https://pypi.org/simple/scipy/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/scipy/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping

[notice] A new release of pip available: 22.2 -&gt; 22.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip

</code></pre>
<p>It looks like he can’t find the 1.8.1 version of scipy. Is there something wrong with my network or my configuration</p>

---

## Post #2 by @lassoan (2022-12-08 02:28 UTC)

<p>It seems that your computer has SSL communication error. Do you connect to the internet through some firewall or proxy server?</p>

---

## Post #3 by @miniminic (2022-12-08 02:52 UTC)

<p>Yes I shut down the proxy and tried again and I got another error<br>
python-scipy-install-err.log</p>
<pre><code class="lang-auto">ERROR: Exception:
Traceback (most recent call last):
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\urllib3\response.py", line 435, in _error_catcher
    yield
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\urllib3\response.py", line 516, in read
    data = self._fp.read(amt) if not fp_closed else b""
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\cachecontrol\filewrapper.py", line 90, in read
    data = self.__fp.read(amt)
  File "E:\QY\Build\D\python-install\Lib\http\client.py", line 463, in read
    n = self.readinto(b)
  File "E:\QY\Build\D\python-install\Lib\http\client.py", line 507, in readinto
    n = self.fp.readinto(b)
  File "E:\QY\Build\D\python-install\Lib\socket.py", line 704, in readinto
    return self._sock.recv_into(b)
  File "E:\QY\Build\D\python-install\Lib\ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "E:\QY\Build\D\python-install\Lib\ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
socket.timeout: The read operation timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\cli\base_command.py", line 167, in exc_logging_wrapper
    status = run_func(*args)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\cli\req_command.py", line 247, in wrapper
    return func(self, options, args)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\commands\install.py", line 369, in run
    requirement_set = resolver.resolve(
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\resolver.py", line 92, in resolve
    result = self._result = resolver.resolve(
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\resolvelib\resolvers.py", line 481, in resolve
    state = resolution.resolve(requirements, max_rounds=max_rounds)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\resolvelib\resolvers.py", line 348, in resolve
    self._add_to_criteria(self.state.criteria, r, parent=None)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\resolvelib\resolvers.py", line 172, in _add_to_criteria
    if not criterion.candidates:
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\resolvelib\structs.py", line 151, in __bool__
    return bool(self._sequence)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\found_candidates.py", line 155, in __bool__
    return any(self)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\found_candidates.py", line 143, in &lt;genexpr&gt;
    return (c for c in iterator if id(c) not in self._incompatible_ids)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\found_candidates.py", line 47, in _iter_built
    candidate = func()
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\factory.py", line 206, in _make_candidate_from_link
    self._link_candidate_cache[link] = LinkCandidate(
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\candidates.py", line 297, in __init__
    super().__init__(
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\candidates.py", line 162, in __init__
    self.dist = self._prepare()
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\candidates.py", line 231, in _prepare
    dist = self._prepare_distribution()
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\candidates.py", line 308, in _prepare_distribution
    return preparer.prepare_linked_requirement(self._ireq, parallel_builds=True)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\operations\prepare.py", line 438, in prepare_linked_requirement
    return self._prepare_linked_requirement(req, parallel_builds)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\operations\prepare.py", line 483, in _prepare_linked_requirement
    local_file = unpack_url(
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\operations\prepare.py", line 165, in unpack_url
    file = get_http_url(
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\operations\prepare.py", line 106, in get_http_url
    from_path, content_type = download(link, temp_dir.path)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\network\download.py", line 147, in __call__
    for chunk in chunks:
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\cli\progress_bars.py", line 53, in _rich_progress_bar
    for chunk in iterable:
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_internal\network\utils.py", line 63, in response_chunks
    for chunk in response.raw.stream(
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\urllib3\response.py", line 573, in stream
    data = self.read(amt=amt, decode_content=decode_content)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\urllib3\response.py", line 538, in read
    raise IncompleteRead(self._fp_bytes_read, self.length_remaining)
  File "E:\QY\Build\D\python-install\Lib\contextlib.py", line 137, in __exit__
    self.gen.throw(typ, value, traceback)
  File "E:\QY\Build\D\python-install\lib\site-packages\pip\_vendor\urllib3\response.py", line 440, in _error_catcher
    raise ReadTimeoutError(self._pool, None, "Read timed out.")
pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.

</code></pre>
<p>python-scipy-install-out.log</p>
<pre><code class="lang-auto">Collecting scipy==1.8.1
  Downloading scipy-1.8.1-cp39-cp39-win_amd64.whl (36.9 MB)
                                              0.0/36.9 MB 21.1 kB/s eta 0:29:05

[notice] A new release of pip available: 22.2 -&gt; 22.3.1
[notice] To update, run: python.exe -m pip install --upgrade pip

</code></pre>

---

## Post #4 by @lassoan (2022-12-08 03:09 UTC)

<aside class="quote no-group" data-username="miniminic" data-post="3" data-topic="26616">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/miniminic/48/16647_2.png" class="avatar"> miniminic:</div>
<blockquote>
<p><code>pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.</code></p>
</blockquote>
</aside>
<p>You still have network/SSL configuration errors. There is something special about your network configuration or internet connection.</p>
<p>As a workaround, you can try to pip install scipy-1.8.1 for Python-3.9 in any Python environment. The packages are cached on your computer, so when you build Slicer, Python will probably find it and it won’t need to download it from the network.</p>

---

## Post #5 by @jcfr (2022-12-08 03:11 UTC)

<p>As as side note, I just reviewed and integrated <a href="https://github.com/Slicer/Slicer/pull/6719">Slicer PR-6719</a>  updating <code>Slicer.crt</code> but I doubt it will help address the issue being discussed here.</p>

---

## Post #6 by @miniminic (2022-12-08 03:20 UTC)

<p>I ran the command in a separate cmd window and it worked<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce60f0c6cb64ac88c9ea0e28f154a3f5bb940f61.png" data-download-href="/uploads/short-url/trI3hUFD0woOre4gF7UI2Qh5d9n.png?dl=1" title="批注 2022-12-08 112010" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce60f0c6cb64ac88c9ea0e28f154a3f5bb940f61.png" alt="批注 2022-12-08 112010" data-base62-sha1="trI3hUFD0woOre4gF7UI2Qh5d9n" width="690" height="357" data-dominant-color="212020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">批注 2022-12-08 112010</span><span class="informations">983×510 12.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
