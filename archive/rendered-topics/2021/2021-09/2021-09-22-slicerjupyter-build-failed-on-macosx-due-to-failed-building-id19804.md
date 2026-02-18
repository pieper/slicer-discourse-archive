# SlicerJupyter build failed on MacOSX due to failed building wheel for argon2-cffi

**Topic ID**: 19804
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/slicerjupyter-build-failed-on-macosx-due-to-failed-building-wheel-for-argon2-cffi/19804

---

## Post #1 by @RuoyanMeng (2021-09-22 11:20 UTC)

<p>MacOS: 11.6<br>
3D Slicer build version: 4.13.0</p>
<p>I can install jupyterlab from Slicer python kernel and argon2-cffi is successfully installed. But when making a build for SlicerJupyter, argon2-cffi build is failed.</p>
<p>Here is the build log:</p>
<pre><code class="lang-auto">[  1%] Creating directories for 'python-packages'
[  2%] No download step for 'python-packages'
[  3%] Generate version-python-packages.txt and license-python-packages.txt
[  4%] No update step for 'python-packages'
[  6%] No patch step for 'python-packages'
[  7%] No configure step for 'python-packages'
[  8%] No build step for 'python-packages'
[  9%] Performing install step for 'python-packages'
Collecting jedi==0.18.0
  Using cached jedi-0.18.0-py2.py3-none-any.whl (1.4 MB)
Collecting argon2-cffi==20.1.0
  Using cached argon2-cffi-20.1.0.tar.gz (1.8 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Collecting parso&lt;0.9.0,&gt;=0.8.0
  Using cached parso-0.8.2-py2.py3-none-any.whl (94 kB)
Collecting six
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting cffi&gt;=1.0.0
  Using cached cffi-1.14.6-cp36-cp36m-macosx_10_9_x86_64.whl (176 kB)
Collecting pycparser
  Using cached pycparser-2.20-py2.py3-none-any.whl (112 kB)
Building wheels for collected packages: argon2-cffi
  Building wheel for argon2-cffi (PEP 517) ... error
  ERROR: Command errored out with exit status 1:
   command: /Users/documents/Slicer/build/python-install/bin/./python /Users/documents/Slicer/build/python-install/lib/python3.6/site-packages/pip/_vendor/pep517/in_process/_in_process.py build_wheel /var/folders/_k/fjl1stps49q7q8lxvnx447hm0000gn/T/tmpikzho0io
       cwd: /private/var/folders/_k/fjl1stps49q7q8lxvnx447hm0000gn/T/pip-install-4o978ieo/argon2-cffi_515aaeab54504515917372aa03f299b2
  Complete output (27 lines):
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.13-x86_64-3.6
  creating build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/__init__.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/low_level.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_ffi_build.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_password_hasher.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/exceptions.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_legacy.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/__main__.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  copying src/argon2/_utils.py -&gt; build/lib.macosx-10.13-x86_64-3.6/argon2
  running build_clib
  building 'argon2' library
  creating build/temp.macosx-10.13-x86_64-3.6
  creating build/temp.macosx-10.13-x86_64-3.6/extras
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src
  creating build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/blake2
  /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/argon2.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/argon2.o
  extras/libargon2/src/argon2.c:18:10: fatal error: 'string.h' file not found
  #include &lt;string.h&gt;
           ^~~~~~~~~~
  1 error generated.
  error: command '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for argon2-cffi
Failed to build argon2-cffi
ERROR: Could not build wheels for argon2-cffi which use PEP 517 and cannot be installed directly
WARNING: You are using pip version 21.1.2; however, version 21.2.4 is available.
You should consider upgrading via the '/Users/ruooo/documents/Slicer/build/python-install/bin/./python -m pip install --upgrade pip' command.
make[2]: *** [python-packages-prefix/src/python-packages-stamp/python-packages-install] Error 1
make[1]: *** [CMakeFiles/python-packages.dir/all] Error 2
make: *** [all] Error 2
</code></pre>

---

## Post #2 by @pll_llq (2021-09-22 21:39 UTC)

<p>AFAIK this is a mac-only issue that will resolve itself once Slicer upgrades to a higher version of python which is hopefully soon.</p>
<p>In the mean time if you install Jupyter Lab outside of 3D Slicer and install the Slicer Jupyter kernel into it - it’s going to work nicely. To install the Slicer Jupyter Kernel into a lab environment use the snippet in the JupyterKernel extension<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bec4e77384ac79c164c7753b3f5348e959a5c1ea.png" data-download-href="/uploads/short-url/rdCAeLMEW2EDNYamhzcumBFLdA6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec4e77384ac79c164c7753b3f5348e959a5c1ea_2_690x157.png" alt="image" data-base62-sha1="rdCAeLMEW2EDNYamhzcumBFLdA6" width="690" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec4e77384ac79c164c7753b3f5348e959a5c1ea_2_690x157.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec4e77384ac79c164c7753b3f5348e959a5c1ea_2_1035x235.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bec4e77384ac79c164c7753b3f5348e959a5c1ea.png 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1146×262 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @RuoyanMeng (2021-09-23 09:17 UTC)

<p>Can you explain more on how to install the JupyterKernel extension? Is this installed in Slicer or JupyterLab outside the Slicer env?</p>

---

## Post #4 by @pll_llq (2021-09-23 11:10 UTC)

<p>This is the procedure that worked for me. It is required to be performed only once.</p>
<ol>
<li>
<p>Install the latest Slicer nightly</p>
</li>
<li>
<p>Install the SlicerJupyter extension from the extension manager in Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3065b10f4dba34642334bb59d4a2ae1669d07a2b.png" data-download-href="/uploads/short-url/6U8N67v52Us7qDziURaoBVkqQjN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3065b10f4dba34642334bb59d4a2ae1669d07a2b_2_690x469.png" alt="image" data-base62-sha1="6U8N67v52Us7qDziURaoBVkqQjN" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3065b10f4dba34642334bb59d4a2ae1669d07a2b_2_690x469.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3065b10f4dba34642334bb59d4a2ae1669d07a2b_2_1035x703.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3065b10f4dba34642334bb59d4a2ae1669d07a2b_2_1380x938.png 2x" data-dominant-color="ECEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1662×1132 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Create and activate a python3 virtual environment outside of Slicer. Let’s call it <code>myJupyterEnvironment</code>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/811cd2cd791fb064af9328380b457f793a3d8f6f.jpeg" data-download-href="/uploads/short-url/iqblykl1KovV9sOsjLMxZkhTbf9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811cd2cd791fb064af9328380b457f793a3d8f6f_2_690x210.jpeg" alt="image" data-base62-sha1="iqblykl1KovV9sOsjLMxZkhTbf9" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811cd2cd791fb064af9328380b457f793a3d8f6f_2_690x210.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811cd2cd791fb064af9328380b457f793a3d8f6f_2_1035x315.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/811cd2cd791fb064af9328380b457f793a3d8f6f_2_1380x420.jpeg 2x" data-dominant-color="333E30"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1654×504 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Install Jupyter Lab into <code>myJupyterEnvironment</code> with<br>
<code>pip install jupyterlab</code></p>
</li>
<li>
<p>Open the JupyterKernel module in Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/506ad1a92f18b1605282e08b2407f286a79981ed.png" data-download-href="/uploads/short-url/btp3ugL2sYzom9ibs4CuUQQrYJL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506ad1a92f18b1605282e08b2407f286a79981ed_2_690x440.png" alt="image" data-base62-sha1="btp3ugL2sYzom9ibs4CuUQQrYJL" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506ad1a92f18b1605282e08b2407f286a79981ed_2_690x440.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506ad1a92f18b1605282e08b2407f286a79981ed_2_1035x660.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/506ad1a92f18b1605282e08b2407f286a79981ed_2_1380x880.png 2x" data-dominant-color="B6B6B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1772×1130 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Copy the command that’s displayed in the “Jupyter server in external Python environment” section and execute it in <code>myJupyterEnvironment</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3de2b06cd622050711eccc906fbd37ed24d59a72.png" data-download-href="/uploads/short-url/8PsNUmilj7L1tHVOjn4EruibBgS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3de2b06cd622050711eccc906fbd37ed24d59a72_2_690x158.png" alt="image" data-base62-sha1="8PsNUmilj7L1tHVOjn4EruibBgS" width="690" height="158" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3de2b06cd622050711eccc906fbd37ed24d59a72_2_690x158.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3de2b06cd622050711eccc906fbd37ed24d59a72_2_1035x237.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3de2b06cd622050711eccc906fbd37ed24d59a72.png 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1150×264 22.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c36900c69e63a066e1bed1c36508609501ae341.jpeg" data-download-href="/uploads/short-url/k0nKfbtj5h2nQMSICGCj8QfpbZD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c36900c69e63a066e1bed1c36508609501ae341_2_690x82.jpeg" alt="image" data-base62-sha1="k0nKfbtj5h2nQMSICGCj8QfpbZD" width="690" height="82" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c36900c69e63a066e1bed1c36508609501ae341_2_690x82.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c36900c69e63a066e1bed1c36508609501ae341_2_1035x123.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8c36900c69e63a066e1bed1c36508609501ae341_2_1380x164.jpeg 2x" data-dominant-color="242F21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1614×194 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This command will install a Slicer kernel into your Jupyter lab. You can check that the extension has been installed by running <code>jupyter-kernelspec list</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a15d0f9b6ec1f96c8471ffbd9879834265ec248c.jpeg" data-download-href="/uploads/short-url/n1ufNZDLuMdE6EWCzm2DFou0hUo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a15d0f9b6ec1f96c8471ffbd9879834265ec248c_2_690x135.jpeg" alt="image" data-base62-sha1="n1ufNZDLuMdE6EWCzm2DFou0hUo" width="690" height="135" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a15d0f9b6ec1f96c8471ffbd9879834265ec248c_2_690x135.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a15d0f9b6ec1f96c8471ffbd9879834265ec248c_2_1035x202.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a15d0f9b6ec1f96c8471ffbd9879834265ec248c_2_1380x270.jpeg 2x" data-dominant-color="30382F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1618×318 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="7">
<li>
<p>Launch Jupyter Lab by running <code>jupyter lab</code> in <code>myJupyterEnvironment</code>. You’ll see “S” 2 icons. The orange one creates a notebook in the Slicer kernel and the blue one creates a kernel console<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82335ac28edd92be90bdd4969ba018eaf1877c4c.png" data-download-href="/uploads/short-url/izO63GLBfbsDdjt0TN3IsCnVrcg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82335ac28edd92be90bdd4969ba018eaf1877c4c_2_690x310.png" alt="image" data-base62-sha1="izO63GLBfbsDdjt0TN3IsCnVrcg" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82335ac28edd92be90bdd4969ba018eaf1877c4c_2_690x310.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82335ac28edd92be90bdd4969ba018eaf1877c4c_2_1035x465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82335ac28edd92be90bdd4969ba018eaf1877c4c_2_1380x620.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2482×1118 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Click on the notebook icon to connect to a kernel. A Slicer window will be created hidden in the dock. Pop it out if you need to access the UI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ac3c6a0d3c11c26e1d06b43b354343b8b8d7c31.jpeg" data-download-href="/uploads/short-url/aFoMp6WWNtU15b1Gnv8mZuvhYOZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ac3c6a0d3c11c26e1d06b43b354343b8b8d7c31_2_690x374.jpeg" alt="image" data-base62-sha1="aFoMp6WWNtU15b1Gnv8mZuvhYOZ" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ac3c6a0d3c11c26e1d06b43b354343b8b8d7c31_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ac3c6a0d3c11c26e1d06b43b354343b8b8d7c31_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ac3c6a0d3c11c26e1d06b43b354343b8b8d7c31_2_1380x748.jpeg 2x" data-dominant-color="C3C3C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1043 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>

---

## Post #5 by @RuoyanMeng (2021-09-24 17:55 UTC)

<p>Thanks, this works for me too when I install the dmg file! However, I need to build the slicer from the source code, somehow the extension manager is not working after being built, there are no extensions showing. And I cannot install the SlicerJupyter extension from there. Then this leads to my original question.</p>

---

## Post #6 by @jamesobutler (2021-09-24 18:37 UTC)

<aside class="quote no-group" data-username="RuoyanMeng" data-post="5" data-topic="19804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ruoyanmeng/48/12403_2.png" class="avatar"> RuoyanMeng:</div>
<blockquote>
<p>somehow the extension manager is not working after being built, there are no extensions showing.</p>
</blockquote>
</aside>
<p>When you build Slicer from source you are also expected to build extensions from source as well. You can at times use extensions built from the Slicer factory build machines if you have built the same revision as one of the Slicer factory builds. However you can potentially run into incompatibilities</p>

---

## Post #7 by @pll_llq (2021-09-24 19:10 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="19804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>When you build Slicer from source you are also expected to build extensions from source as well.</p>
</blockquote>
</aside>
<p>Is it enough to set the<br>
<code>option(Slicer_BUILD_EXTENSIONMANAGER_SUPPORT "Build Slicer extensions manager" ON)</code><br>
parameter in the <code>CMakeLists.txt</code> to have the extension manager working?</p>

---

## Post #8 by @jamesobutler (2021-09-24 20:36 UTC)

<p>That will build the extension manager, but the question of will there be any extensions from the server to choose from depends on the revision of Slicer that is built (one that matches latest stable or a preview build).</p>
<p>For example, if you have checked out the commit that is <code>ENH: Improve resolution of splashscreen and welcome icon</code> which was the first commit of several commits on Sept 22nd, then you won’t see any Slicer factory built extensions in the Extensions Manager since it won’t correspond to the revision of a Slicer Preview build (latest commit prior to 11pm EST). You would have to manually build extensions and could package those extensions and manually install using the Extensions Manager.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb3ea89794f2d18f417b26bde22de0c6a7887c58.png" data-download-href="/uploads/short-url/qIrx0gbpKaYooGqnmQbRrbKjCQ0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb3ea89794f2d18f417b26bde22de0c6a7887c58.png" alt="image" data-base62-sha1="qIrx0gbpKaYooGqnmQbRrbKjCQ0" width="607" height="500" data-dominant-color="1A1F25"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">609×501 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @pll_llq (2021-09-24 20:47 UTC)

<p>Thanks for the clarification</p>

---
