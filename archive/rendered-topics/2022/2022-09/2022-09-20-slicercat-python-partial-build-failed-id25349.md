# SLicerCAT Python partial build failed

**Topic ID**: 25349
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/slicercat-python-partial-build-failed/25349

---

## Post #1 by @miniminic (2022-09-20 07:09 UTC)

<p>I’m building SlicerCAT, and all the other projects are succeeding, except the Python project<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3bf2d937aa1cc6088e333c094b952abec4d70c.jpeg" data-download-href="/uploads/short-url/vQOUKdXrc0ESWGDYatwZ86xIbPm.jpeg?dl=1" title="屏幕截图 2022-09-20 150830" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3bf2d937aa1cc6088e333c094b952abec4d70c_2_690x162.jpeg" alt="屏幕截图 2022-09-20 150830" data-base62-sha1="vQOUKdXrc0ESWGDYatwZ86xIbPm" width="690" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3bf2d937aa1cc6088e333c094b952abec4d70c_2_690x162.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df3bf2d937aa1cc6088e333c094b952abec4d70c_2_1035x243.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3bf2d937aa1cc6088e333c094b952abec4d70c.jpeg 2x" data-dominant-color="302F31"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2022-09-20 150830</span><span class="informations">1245×294 80.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @miniminic (2022-09-20 07:19 UTC)

<p>python-requests-requirements-install-err.log</p>
<pre><code class="lang-auto">ERROR: Exception:
Traceback (most recent call last):
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\cli\base_command.py", line 173, in _main
    status = self.run(options, args)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\cli\req_command.py", line 203, in wrapper
    return func(self, options, args)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\commands\install.py", line 315, in run
    requirement_set = resolver.resolve(
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\resolver.py", line 94, in resolve
    result = self._result = resolver.resolve(
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\resolvelib\resolvers.py", line 472, in resolve
    state = resolution.resolve(requirements, max_rounds=max_rounds)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\resolvelib\resolvers.py", line 341, in resolve
    self._add_to_criteria(self.state.criteria, r, parent=None)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\resolvelib\resolvers.py", line 172, in _add_to_criteria
    if not criterion.candidates:
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\resolvelib\structs.py", line 151, in __bool__
    return bool(self._sequence)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\found_candidates.py", line 140, in __bool__
    return any(self)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\found_candidates.py", line 128, in &lt;genexpr&gt;
    return (c for c in iterator if id(c) not in self._incompatible_ids)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\found_candidates.py", line 29, in _iter_built
    for version, func in infos:
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\resolution\resolvelib\factory.py", line 272, in iter_index_candidate_infos
    result = self._finder.find_best_candidate(
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\index\package_finder.py", line 851, in find_best_candidate
    candidates = self.find_all_candidates(project_name)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\index\package_finder.py", line 798, in find_all_candidates
    page_candidates = list(page_candidates_it)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\index\sources.py", line 134, in page_candidates
    yield from self._candidates_from_page(self._link)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\index\package_finder.py", line 758, in process_project_url
    html_page = self._link_collector.fetch_page(project_url)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\index\collector.py", line 490, in fetch_page
    return _get_html_page(location, session=self.session)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\index\collector.py", line 400, in _get_html_page
    resp = _get_html_response(url, session=session)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\index\collector.py", line 115, in _get_html_response
    resp = session.get(
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\requests\sessions.py", line 555, in get
    return self.request('GET', url, **kwargs)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_internal\network\session.py", line 454, in request
    return super().request(method, url, *args, **kwargs)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\requests\sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\requests\sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\cachecontrol\adapter.py", line 53, in send
    resp = super(CacheControlAdapter, self).send(request, **kw)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\requests\adapters.py", line 439, in send
    resp = conn.urlopen(
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\urllib3\connectionpool.py", line 696, in urlopen
    self._prepare_proxy(conn)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\urllib3\connectionpool.py", line 964, in _prepare_proxy
    conn.connect()
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\urllib3\connection.py", line 359, in connect
    conn = self._connect_tls_proxy(hostname, conn)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\urllib3\connection.py", line 500, in _connect_tls_proxy
    return ssl_wrap_socket(
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\urllib3\util\ssl_.py", line 453, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls)
  File "E:\QY3DB\QY3DR\python-install\lib\site-packages\pip\_vendor\urllib3\util\ssl_.py", line 495, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock)
  File "E:\QY3DB\QY3DR\python-install\Lib\ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "E:\QY3DB\QY3DR\python-install\Lib\ssl.py", line 997, in _create
    raise ValueError("check_hostname requires server_hostname")
ValueError: check_hostname requires server_hostname

</code></pre>

---

## Post #3 by @miniminic (2022-09-21 02:31 UTC)

<p>I turned off the VPN to solve this problem</p>

---
