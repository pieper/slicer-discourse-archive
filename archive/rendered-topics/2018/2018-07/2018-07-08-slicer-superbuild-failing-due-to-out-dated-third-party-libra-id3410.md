# Slicer superbuild failing due to out-dated third party libraries: VTK and curl

**Topic ID**: 3410
**Date**: 2018-07-08
**URL**: https://discourse.slicer.org/t/slicer-superbuild-failing-due-to-out-dated-third-party-libraries-vtk-and-curl/3410

---

## Post #1 by @phcerdan (2018-07-08 04:07 UTC)

<p>Using Archlinux with gcc 8.1.1, the Slicer superbuild with VTKv9 and Qt5 is failing in the following packages: VTK, python, and curl.</p>
<hr>
<ul>
<li>VTK compiling error is related with HDF5, that has been solved upstream, but Slicer branch/tag has to be updated. This is the branch created to merge in the Slicer/vtk fork pointing to VTK master: <a href="https://github.com/phcerdan/vtk/tree/slicer-v9.0.0-2018-07-06-982ec1c561" rel="nofollow noopener">https://github.com/phcerdan/vtk/tree/slicer-v9.0.0-2018-07-06-982ec1c561</a>
</li>
</ul>
<hr>
<ul>
<li>Current curl version in slicer is failing, with error:</li>
</ul>
<pre><code class="lang-auto">Software/Slicer/build-relwithdebinfo/curl/lib/ssluse.c:1957:45: error: dereferencing pointer to incomplete type ‘X509_EXTENSION’ {aka ‘struct X509_extension_st’}
       M_ASN1_OCTET_STRING_print(bio_out, ext-&gt;value);
                                             ^~
Software/Slicer/build-relwithdebinfo/curl/lib/ssluse.c: In function ‘get_cert_chain’:
Software/Slicer/build-relwithdebinfo/curl/lib/ssluse.c:2114:13: error: dereferencing pointer to incomplete type ‘X509’ {aka ‘struct x509_st’}
     cinf = x-&gt;cert_info;
             ^~
/Software/Slicer/build-relwithdebinfo/curl/lib/ssluse.c:2116:30: error: dereferencing pointer to incomplete type ‘X509_CINF’ {aka ‘struct x509_cinf_st’}
     j = asn1_object_dump(cinf-&gt;signature-&gt;algorithm, bufp, CERTBUFFERSIZE);
                              ^~
Software/Slicer/build-relwithdebinfo/curl/lib/ssluse.c:2142:20: error: dereferencing pointer to incomplete type ‘EVP_PKEY’ {aka ‘struct evp_pkey_st’}
       switch(pubkey-&gt;type) {
                    ^~
[42/76] Building C object lib/CMakeFiles/libcurl.dir/imap.c.o
In file included from /usr/include/sys/types.h:25,
                 from lib/../include/curl/curlbuild.h:130,
                 from /home/phc/Software/Slicer/build-relwithdebinfo/curl/lib/curl_setup.h:125,
                 from /home/phc/Software/Slicer/build-relwithdebinfo/curl/lib/multi.c:23:
/usr/include/features.h:184:3: warning: #warning "_BSD_SOURCE and _SVID_SOURCE are deprecated, use _DEFAULT_SOURCE" [-Wcpp]
 # warning "_BSD_SOURCE and _SVID_SOURCE are deprecated, use _DEFAULT_SOURCE"
   ^~~~~~~
[45/76] Building C object lib/CMakeFiles/libcurl.dir/imap.c.o
ninja: build stopped: subcommand failed.
[140/200] Performing build step for 'curl'
FAILED: curl-prefix/src/curl-stamp/curl-build

</code></pre>
<p>curl-master works. There are three commits in the Slicer branch on top of a quite old curl-master, not sure if they are still relevant and have to be cherry-picked after the update: <a href="https://github.com/slicer/curl/tree/curl-7_34_0-maint" rel="nofollow noopener">https://github.com/slicer/curl/tree/curl-7_34_0-maint</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<hr>
<p>Also current CTK tag: <code>f0386cba0dd62d728bca9a00a2c89bc0528ff768</code> generates this error, that is solved updating Slicer to use latest CTK with this PR merged: <a href="https://github.com/commontk/CTK/pull/817" rel="nofollow noopener">https://github.com/commontk/CTK/pull/817</a></p>
<pre><code class="lang-auto">/Software/Slicer/build-relwithdebinfo/CTK/Libs/Visualization/VTK/Widgets/ctkVTKDiscretizableColorTransferWidget.cpp:378:45: error: invalid use of incomplete type ‘class vtkRenderWindowInteractor’
   self-&gt;ScalarsToColorsView-&gt;GetInteractor()-&gt;Render();
                                             ^~
In file included from /Software/Slicer/build-relwithdebinfo/CTK/Libs/Visualization/VTK/Widgets/ctkVTKDiscretizableColorTransferWidget.cpp:50:
/home/phc/Software/Slicer/build-relwithdebinfo/VTKv9/GUISupport/Qt/QVTKOpenGLWidget.h:31:7: note: forward declaration of ‘class vtkRenderWindowInteractor’
 class vtkRenderWindowInteractor;
Software/Slicer/build-relwithdebinfo/CTK/Libs/Visualization/VTK/Widgets/ctkVTKDiscretizableColorTransferWidget.cpp: In member function ‘void ctkVTKDiscretizableColorTransferWidget::onPaletteIndexChanged(vtkScalarsToColors*)’:
/Software/Slicer/build-relwithdebinfo/CTK/Libs/Visualization/VTK/Widgets/ctkVTKDiscretizableColorTransferWidget.cpp:756:42: error: invalid use of incomplete type ‘class vtkRenderWindowInteractor’
   d-&gt;ScalarsToColorsView-&gt;GetInteractor()-&gt;Render();
                                          ^~
In file included from /Software/Slicer/build-relwithdebinfo/CTK/Libs/Visualization/VTK/Widgets/ctkVTKDiscretizableColorTransferWidget.cpp:50:
/Software/Slicer/build-relwithdebinfo/VTKv9/GUISupport/Qt/QVTKOpenGLWidget.h:31:7: note: forward declaration of ‘class vtkRenderWindowInteractor’
 class vtkRenderWindowInteractor;

</code></pre>
<hr>
<ul>
<li>And finally python is failing in the superbuild due to this reported bug:<br>
<a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/issues/224" rel="nofollow noopener">https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/issues/224</a>
</li>
</ul>
<p>A workaround is to use system python with:</p>
<pre><code class="lang-auto">mkvirtualenv -p python2.7 slicer
workon slicer
pip install chardet appdirs packaging pyparsing smmap gitdb GitPython PyGithub nose numpy dicom couchdb
</code></pre>
<hr>
<p>The cmake options for the workaround. Note that curl is latest in my system.</p>
<pre><code class="lang-bash">cmake -G Ninja ../Slicer-src \
-DSlicer_VTK_VERSION_MAJOR:STRING=9 \
-DSlicer_USE_SYSTEM_curl:BOOL=ON \
-DSlicer_USE_SYSTEM_python:BOOL=ON \
-DVTK_DIR:PATH=/path/VTKv9-master-build
</code></pre>

---
