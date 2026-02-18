# DeCA module does not operate under the 5-4-2026.01.02 release

**Topic ID**: 45782
**Date**: 2026-01-15
**URL**: https://discourse.slicer.org/t/deca-module-does-not-operate-under-the-5-4-2026-01-02-release/45782

---

## Post #1 by @philippepellerin (2026-01-15 09:20 UTC)

<p>I tried running DeCA with the 3D Slicer 5-11-2026.01.02 release, but the module window opens like in the attachment, and the extension can’t be operated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f4b0c0e7d4446dfe09a349e92da446e82d415ac.png" data-download-href="/uploads/short-url/fSxMMLVYyED33jaMegRdQiJRZ1i.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4b0c0e7d4446dfe09a349e92da446e82d415ac_2_185x500.png" alt="image" data-base62-sha1="fSxMMLVYyED33jaMegRdQiJRZ1i" width="185" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4b0c0e7d4446dfe09a349e92da446e82d415ac_2_185x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4b0c0e7d4446dfe09a349e92da446e82d415ac_2_277x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f4b0c0e7d4446dfe09a349e92da446e82d415ac_2_370x1000.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">736×1984 62.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ebrahim (2026-01-15 14:04 UTC)

<p>In the screenshot it looks like you are in the Data module. What happens when you try switching to one of the DeCA  modules?</p>

---

## Post #3 by @philippepellerin (2026-01-15 15:45 UTC)

<p>Sorry, I did not capture the right screen; here is a better one. When I switch to the DeCA module, I do not see the options to select the models and landmarks folders, thus can’t operate a DeCA atlas creation….<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d50a2a112753fdfd91f2a926671f4bfc2ff9f6a.png" data-download-href="/uploads/short-url/hSArx1ITPowO8WTO1j9z0e78rW2.png?dl=1" title="PastedGraphic-1.png" rel="noopener nofollow ugc"><img width="118" alt="PastedGraphic-1.png" src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d50a2a112753fdfd91f2a926671f4bfc2ff9f6a_2_118x318.png" data-base62-sha1="hSArx1ITPowO8WTO1j9z0e78rW2" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d50a2a112753fdfd91f2a926671f4bfc2ff9f6a_2_118x318.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d50a2a112753fdfd91f2a926671f4bfc2ff9f6a_2_177x477.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d50a2a112753fdfd91f2a926671f4bfc2ff9f6a_2_236x636.png 2x" data-dominant-color="FBFBFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PastedGraphic-1.png</span><span class="informations">237×640 22.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2026-01-15 16:53 UTC)

<p>I can’t replicate this on my Mac with todays preview. Module shows and works fine:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8875f70c56333bf706ef41dfbda149f5a56c136.png" data-download-href="/uploads/short-url/o2SfuOLJq20lqQLKmKT69GpCOcC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8875f70c56333bf706ef41dfbda149f5a56c136.png" alt="image" data-base62-sha1="o2SfuOLJq20lqQLKmKT69GpCOcC" width="383" height="479"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">383×479 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There might be an issue with that specific build from that day. If you need to use it try with today’s preview, better yet use the stable (5.10).</p>
<p>If you encounter the issue with today’s preview as well, please share the full log file from that session.</p>

---

## Post #5 by @philippepellerin (2026-01-16 15:27 UTC)

<p>With the last issue I can’t even load the module.</p>
<p>Here after a screen grab of the research display.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/581f18ef4c168c24bb818a20b13414510ff03fbd.jpeg" data-download-href="/uploads/short-url/czyDSKngfEfac5g4BssDJcmE3OR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/581f18ef4c168c24bb818a20b13414510ff03fbd_2_690x111.jpeg" alt="image" data-base62-sha1="czyDSKngfEfac5g4BssDJcmE3OR" width="690" height="111" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/581f18ef4c168c24bb818a20b13414510ff03fbd_2_690x111.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/581f18ef4c168c24bb818a20b13414510ff03fbd_2_1035x166.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/581f18ef4c168c24bb818a20b13414510ff03fbd_2_1380x222.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3612×586 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I copy here after the session.</p>
<p>Python 3.12.10 (main, Jan 14 2026, 23:49:19) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin</p>
<p>&gt;&gt;&gt;</p>
<p>[Python] get_frame_offsets is deprecated and will be removed in v4.0</p>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>Collecting git+https://github.com/SlicerMorph/dataset-matcher.git</p>
<p>Cloning <a href="https://github.com/SlicerMorph/dataset-matcher.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/dataset-matcher: A lightweight Python library for matching datasets (file lists) by basename across directories</a> to /private/var/folders/xw/49j5chs13nl_nzll7509jd5h0000gn/T/pip-req-build-aeuthwvj</p>
<p>Running command git clone --filter=blob:none --quiet <a href="https://github.com/SlicerMorph/dataset-matcher.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/dataset-matcher: A lightweight Python library for matching datasets (file lists) by basename across directories</a> /private/var/folders/xw/49j5chs13nl_nzll7509jd5h0000gn/T/pip-req-build-aeuthwvj</p>
<p>Resolved <a href="https://github.com/SlicerMorph/dataset-matcher.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/dataset-matcher: A lightweight Python library for matching datasets (file lists) by basename across directories</a> to commit 8b14a56d598952fd4da3f2bfbf827c697a8d9f81</p>
<p>Installing build dependencies: started</p>
<p>Installing build dependencies: finished with status ‘done’</p>
<p>Getting requirements to build wheel: started</p>
<p>Getting requirements to build wheel: finished with status ‘done’</p>
<p>Preparing metadata (pyproject.toml): started</p>
<p>Preparing metadata (pyproject.toml): finished with status ‘done’</p>
<p>Building wheels for collected packages: dataset-matcher</p>
<p>Building wheel for dataset-matcher (pyproject.toml): started</p>
<p>Building wheel for dataset-matcher (pyproject.toml): finished with status ‘done’</p>
<p>Created wheel for dataset-matcher: filename=dataset_matcher-0.1.0-py3-none-any.whl size=8513 sha256=3950b04006d36514218b86debb6fc00d97444e16b5c7e42271c5eb709293ac3c</p>
<p>Stored in directory: /private/var/folders/xw/49j5chs13nl_nzll7509jd5h0000gn/T/pip-ephem-wheel-cache-6pvs1xkv/wheels/b4/0a/87/bf155e2f13d7fed2f6ecc8572258f8e2091e9bdcbf12363c9e</p>
<p>Successfully built dataset-matcher</p>
<p>Installing collected packages: dataset-matcher</p>
<p>Successfully installed dataset-matcher-0.1.0</p>
<p>[Qt] libpng warning: iCCP: known incorrect sRGB profile</p>
<p>Collecting mistune</p>
<p>Using cached mistune-3.2.0-py3-none-any.whl.metadata (1.9 kB)</p>
<p>Using cached mistune-3.2.0-py3-none-any.whl (53 kB)</p>
<p>Installing collected packages: mistune</p>
<p>Successfully installed mistune-3.2.0</p>
<p>[VTK] Warning: In vtkSlicerTerminologiesModuleLogic.cxx, line 3370</p>
<p>[VTK] vtkSlicerTerminologiesModuleLogic (0x6000003f4680): LoadAnatomicContextFromFile is deprecated. Use LoadRegionContextFromFile instead.</p>
<p>[FD] [47392:137219:0116/161113.945652:ERROR:gl_context_cgl.cc(118)] Error creating context.</p>
<p>[Qt] Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!</p>
<p>[Qt] Property ‘verbose’’ of object ‘qSlicerWebPythonProxy’ has no notify signal and is not constant, value updates in HTML will be broken!</p>
<p>[FD] [47392:157443:0116/161122.043137:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161125.101992:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161141.446527:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161144.503438:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161150.729947:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161153.785437:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161320.891331:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161323.946523:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161403.693959:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161406.749718:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161707.086846:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[FD] [47392:157443:0116/161710.144168:ERROR:ssl_client_socket_impl.cc(960)] handshake failed; returned -1, SSL error code 1, net_error -100</p>
<p>[Qt] Populating font family aliases took 175 ms. Replace uses of missing font family “Courier” with one that exists to avoid this cost.</p>

---

## Post #6 by @muratmaga (2026-01-16 17:12 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="5" data-topic="45782">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>Here after a screen grab of the research display.</p>
</blockquote>
</aside>
<p>Extension is called DenseCorrespondenceAnalysis (not DeCA). Search for Dense and it should come up</p>

---

## Post #7 by @philippepellerin (2026-01-17 09:53 UTC)

<p>Thank you, everything is going well.<br>
Best.</p>

---
