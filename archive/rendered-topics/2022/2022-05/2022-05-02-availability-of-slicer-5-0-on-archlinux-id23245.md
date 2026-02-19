---
topic_id: 23245
title: "Availability Of Slicer 5 0 On Archlinux"
date: 2022-05-02
url: https://discourse.slicer.org/t/23245
---

# Availability of Slicer 5.0 on ArchLinux

**Topic ID**: 23245
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/availability-of-slicer-5-0-on-archlinux/23245

---

## Post #1 by @Alex_Vergara (2022-05-02 12:29 UTC)

<p>Manjaro here (from AUR, so I asume the same for all pacman based linux)</p>
<pre><code class="lang-auto">:: 1 Packages to upgrade.
1  aur/3dslicer-nightly-bin  4.13.0.r20220113-1 -&gt; 20220501.071714-1
==&gt; Packages to exclude: (eg: "1 2 3", "1-3", "^4" or repo name)
==&gt; 
:: Checking for conflicts...
:: Checking for inner conflicts...
[Aur:1]  3dslicer-nightly-bin-20220501.071714-1

  1 3dslicer-nightly-bin                     (Installed) (Build Files Exist)
==&gt; Packages to cleanBuild?
==&gt; [N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2 3, 1-3, ^4)
==&gt; 
:: PKGBUILD up to date, Skipping (1/0): 3dslicer-nightly-bin
  1 3dslicer-nightly-bin                     (Installed) (Build Files Exist)
==&gt; Diffs to show?
==&gt; [N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2 3, 1-3, ^4)
==&gt; 
:: (1/1) Parsing SRCINFO: 3dslicer-nightly-bin
==&gt; Making package: 3dslicer-nightly-bin 20220501.071714-1 (lun 02 may 2022 14:09:59)
==&gt; Retrieving sources...
  -&gt; Found 3dslicer-20220501.071714.tar.gz
  -&gt; Found 3dslicer.svg
==&gt; Validating source files with sha512sums...
    3dslicer-20220501.071714.tar.gz ... FAILED
    3dslicer.svg ... Passed
==&gt; ERROR: One or more files did not pass the validity check!
 -&gt; error downloading sources: 3dslicer-nightly-bin 
         context: exit status 1 
         

==&gt; Making package: 3dslicer-nightly-bin 20220501.071714-1 (lun 02 may 2022 14:10:04)
==&gt; Checking runtime dependencies...
==&gt; Checking buildtime dependencies...
==&gt; Retrieving sources...
  -&gt; Found 3dslicer-20220501.071714.tar.gz
  -&gt; Found 3dslicer.svg
==&gt; Validating source files with sha512sums...
    3dslicer-20220501.071714.tar.gz ... FAILED
    3dslicer.svg ... Passed
==&gt; ERROR: One or more files did not pass the validity check!
 -&gt; error making: 3dslicer-nightly-bin
</code></pre>
<p>so searching in aur</p>
<pre><code class="lang-auto">pamac search 3dslicer
3dslicer-nightly-bin                                                                                                     20220501.071714-1    AUR 
    A free, open source and multi-platform software package widely used for medical, biomedical, and related imaging
    research (nightly build)
3dslicer-nightly                                                                                                         4.11.0_2019_03_06-1  AUR 
    A free, open source software package for image analysis and scientific visualization.
3dslicer-bin                                                                                                 [Installed] 5.0.1-1              AUR 
    A free, open source and multi-platform software package widely used for medical, biomedical, and related imaging
    research
3dslicer                                                                                                                 5.0.1-1              AUR 
    A free, open source and multi-platform software package widely used for medical, biomedical, and related imaging
    research
</code></pre>
<p>But the Slicer executable installed is still 4.11</p>

---

## Post #2 by @jcfr (2022-05-02 19:33 UTC)

<p>Based on comment associated with issue <a href="https://github.com/Slicer/Slicer/issues/5546">#5546</a>, it looks like we should update <a href="https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=3dslicer-bin">https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=3dslicer-bin</a> to include the SHA of the latest release.</p>
<p>Looking at the history (see <a href="https://aur.archlinux.org/cgit/aur.git/log/PKGBUILD?h=3dslicer-bin">here</a>), it has been updated <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>That said, the list of <code>sha512sums</code> seems to have been untouched.</p>
<p>cc: <a class="mention" href="/u/butuihu">@ButuiHu</a></p>

---

## Post #3 by @Alex_Vergara (2022-05-03 08:05 UTC)

<p>The only thing working so far is to add the archlinuxcn repository from <a href="https://aur.archlinux.org/packages/3dslicer#comment-793716" rel="noopener nofollow ugc">this comment</a></p>
<p>This way is working, however there shows these errors after installing slicerrt:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e8d7f47781e608e8763ee83e0fb21b62dd73dc3.png" data-download-href="/uploads/short-url/fLZG2uJbX98zAXby4QsQ0BKEjTB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e8d7f47781e608e8763ee83e0fb21b62dd73dc3_2_690x258.png" alt="image" data-base62-sha1="fLZG2uJbX98zAXby4QsQ0BKEjTB" width="690" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e8d7f47781e608e8763ee83e0fb21b62dd73dc3_2_690x258.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e8d7f47781e608e8763ee83e0fb21b62dd73dc3_2_1035x387.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e8d7f47781e608e8763ee83e0fb21b62dd73dc3.png 2x" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1161×435 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1885bd2c7aa4bbc2e73c4ef819941272f3ed61d.png" data-download-href="/uploads/short-url/n2Z1epn8dqkEXSenFLAJwvHWVMp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1885bd2c7aa4bbc2e73c4ef819941272f3ed61d_2_690x388.png" alt="image" data-base62-sha1="n2Z1epn8dqkEXSenFLAJwvHWVMp" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1885bd2c7aa4bbc2e73c4ef819941272f3ed61d_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1885bd2c7aa4bbc2e73c4ef819941272f3ed61d_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a1885bd2c7aa4bbc2e73c4ef819941272f3ed61d_2_1380x776.png 2x" data-dominant-color="312E36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 286 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Alex_Vergara (2022-05-03 08:23 UTC)

<p>My module is running but the test are failing since the coverage package is not working because of missing sqlite3 package</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e8c4abc013c5796f37e29b904585f406206676.png" data-download-href="/uploads/short-url/wF1z9h0tYFlNxUjS5u9eaEQLjbU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e8c4abc013c5796f37e29b904585f406206676_2_690x388.png" alt="image" data-base62-sha1="wF1z9h0tYFlNxUjS5u9eaEQLjbU" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e8c4abc013c5796f37e29b904585f406206676_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e8c4abc013c5796f37e29b904585f406206676_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4e8c4abc013c5796f37e29b904585f406206676_2_1380x776.png 2x" data-dominant-color="3F3D43"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Alex_Vergara (2022-05-03 08:33 UTC)

<p>Something is broken now in brainsresample module, it is not working anymore</p>
<p>this code used to work fine in 4.13</p>
<pre><code class="lang-python">            parameters = {'inputVolume': nodeCT.data, 'referenceVolume': nodeSPECT.data, 'outputVolume': CTRSNode,
                          'interpolationMode': 'Lanczos', 'defaultValue': minCT}

            slicer.cli.run(slicer.modules.brainsresample,
                           None, parameters, wait_for_completion=True, update_display=False)
</code></pre>
<p>Now it produces a volume without voxel data</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bd2552fb47b918552d6db47be44466cac439d96.png" data-download-href="/uploads/short-url/aOKrEY6uTL9bseRpimPd8JqV6w6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bd2552fb47b918552d6db47be44466cac439d96_2_690x388.png" alt="image" data-base62-sha1="aOKrEY6uTL9bseRpimPd8JqV6w6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bd2552fb47b918552d6db47be44466cac439d96_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bd2552fb47b918552d6db47be44466cac439d96_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4bd2552fb47b918552d6db47be44466cac439d96_2_1380x776.png 2x" data-dominant-color="32303B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 498 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Alex_Vergara (2022-05-03 11:16 UTC)

<p>The same version of my module runs fine in MacOS, there is no problem with sqlite, no problem with coverage, and the resample is working as expected:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85368a621a150f5ed94a22cae3d7b9ba1f8bc60a.jpeg" data-download-href="/uploads/short-url/j0sm59vOvUcWsCxK5YGfIO1ojWy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85368a621a150f5ed94a22cae3d7b9ba1f8bc60a_2_690x388.jpeg" alt="image" data-base62-sha1="j0sm59vOvUcWsCxK5YGfIO1ojWy" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85368a621a150f5ed94a22cae3d7b9ba1f8bc60a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85368a621a150f5ed94a22cae3d7b9ba1f8bc60a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/85368a621a150f5ed94a22cae3d7b9ba1f8bc60a_2_1380x776.jpeg 2x" data-dominant-color="39373F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1081 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @fragosoj (2022-05-03 12:33 UTC)

<p>OpenDose3D works fine on 3D Slicer 5.1.0-2022-05-01 on CentOS<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87724429f6953b8e854d3eee6e3f3e6a21da4014.jpeg" data-download-href="/uploads/short-url/jkdgUQYKIMDLeWlZqZm6jlTWF6Y.jpeg?dl=1" title="OD3D" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87724429f6953b8e854d3eee6e3f3e6a21da4014_2_690x431.jpeg" alt="OD3D" data-base62-sha1="jkdgUQYKIMDLeWlZqZm6jlTWF6Y" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87724429f6953b8e854d3eee6e3f3e6a21da4014_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87724429f6953b8e854d3eee6e3f3e6a21da4014_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87724429f6953b8e854d3eee6e3f3e6a21da4014_2_1380x862.jpeg 2x" data-dominant-color="828185"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OD3D</span><span class="informations">1920×1200 245 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
7</p>

---

## Post #8 by @PaoloZaffino (2022-05-03 12:35 UTC)

<p>I’m on Arch too, let me know if I can run some tests.</p>
<p>Paolo</p>

---

## Post #9 by @Alex_Vergara (2022-05-03 13:03 UTC)

<p>Please, just enable developper mode and run the tests. they are automatic, so you just need to report if something goes wrong. Just be sure to report the specific Slicer version and how did you installed it.</p>

---

## Post #10 by @Alex_Vergara (2022-05-04 10:09 UTC)

<p>Current status (04/05/2022):</p>
<p>from AUR:</p>
<p>3dslicer fails to build<br>
3dslicer-bin installs 4.11<br>
3dslicer-nightly installs 4.11</p>
<p>from archlinuxcn:</p>
<p>3dslicer installs 5.0.1 but basic stuffs are not working<br>
3dslicer-bin installs 5.0.1 but basic stuffs are not working<br>
3dslicer-nightly-bin installs 5.0.0 and it is working fine</p>

---

## Post #11 by @chir.set (2022-05-04 14:12 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="9" data-topic="23245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>just enable developper mode and run the tests</p>
</blockquote>
</aside>
<p>What and where are these tests? I just built <em>5.1.0-2022-05-04 r30818 / 68a506f</em> on Arch,which is working seamlessly in my workflow. If there are some standardized tests available, I’ll be happy to contribute.</p>

---

## Post #12 by @Alex_Vergara (2022-05-04 15:03 UTC)

<p>First of all, thank you very much for your interest.</p>
<p>Please, enable developper mode<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38182fb5bced23ec1d38c64c35b14488f2487fd.png" data-download-href="/uploads/short-url/wsBRwcZRG6ETJXiNcOjQdyh6qbb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e38182fb5bced23ec1d38c64c35b14488f2487fd_2_690x319.png" alt="image" data-base62-sha1="wsBRwcZRG6ETJXiNcOjQdyh6qbb" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e38182fb5bced23ec1d38c64c35b14488f2487fd_2_690x319.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38182fb5bced23ec1d38c64c35b14488f2487fd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e38182fb5bced23ec1d38c64c35b14488f2487fd.png 2x" data-dominant-color="474849"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">786×364 32.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then install my module OpenDose3D, remember to restart Slicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f5650b0a8a73753b5b4d5339f723d11fbbf4589.jpeg" data-download-href="/uploads/short-url/iatzea8H0ZnToRotpE4towZd3aF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f5650b0a8a73753b5b4d5339f723d11fbbf4589_2_689x322.jpeg" alt="image" data-base62-sha1="iatzea8H0ZnToRotpE4towZd3aF" width="689" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f5650b0a8a73753b5b4d5339f723d11fbbf4589_2_689x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f5650b0a8a73753b5b4d5339f723d11fbbf4589_2_1033x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f5650b0a8a73753b5b4d5339f723d11fbbf4589.jpeg 2x" data-dominant-color="4B494B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1344×629 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Finally do the tests and report any error. The module uses extensively the Slicer API, so anything wrong shall be reported in the specific section in the test output.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a86d0dbe30f0330d24a295acecb320295f7c7ca7.png" alt="image" data-base62-sha1="o1XRpvty2ABOznxJ4JETyuRt9R5" width="479" height="464"></p>
<p>If everything is ok you will have in the python interpreter the following<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935ce55ba1ae1afc4e26c92e88bbfab7d5d16d1e.png" data-download-href="/uploads/short-url/l1DdrfCPbfdoXJ4xjzkcw7X3etE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935ce55ba1ae1afc4e26c92e88bbfab7d5d16d1e.png" alt="image" data-base62-sha1="l1DdrfCPbfdoXJ4xjzkcw7X3etE" width="292" height="500" data-dominant-color="2E2E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">535×913 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @chir.set (2022-05-04 15:24 UTC)

<p>Unfortunately the tests did not succeed :</p>
<pre><code class="lang-auto">
***** vtkmrmlutils Module Testing *****

DICOM test data dir: /home/user/Documents/Slicer_Ext/opendose3d/OpenDose3D/Resources/DICOM/A_Cycle3-6848MBq-9h57
Successfully loaded patient 599 with StudyInstanceUID: 1.2.752.37.5.626934496.20171125.26473.4.1934 and SeriesInstanceUID: 1.3.6.1.4.1.33868.20191002120418.51247
Test isDICOM_false_positive started!
Test isDICOM_false_positive passed!
Test isDICOM_true_positive started!
Could not load dicom files from database
Reload and Test failed.


Traceback (most recent call last):
  File "/home/user/bin/Slicer_Ext/opendose3d/OpenDose3D/Logic/testbuilder.py", line 84, in setupDICOM
    _ = DICOMUtils.loadPatientByName(dicomValues.patientName)
  File "/home/user/programs/Slicer/lib/Slicer-5.1/qt-scripted-modules/DICOMLib/DICOMUtils.py", line 104, in loadPatientByName
    raise OSError('Patient not found by name %s' % patientName)
OSError: Patient not found by name Patient1^Cycle3

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/user/programs/Slicer/bin/Python/slicer/ScriptedLoadableModule.py", line 216, in onReloadAndTest
    test(msec=int(slicer.app.userSettings().value("Developer/SelfTestDisplayMessageDelay")), **kwargs)
  File "/home/user/bin/Slicer_Ext/opendose3d/OpenDose3D/OpenDose3D.py", line 107, in runTest
    testCase.runTest(**kwargs)
  File "/home/user/bin/Slicer_Ext/opendose3d/OpenDose3D/Logic/vtkmrmlutilsTest.py", line 49, in runTest
    self.isDICOM_true_positive()
  File "/home/user/bin/Slicer_Ext/opendose3d/OpenDose3D/Logic/vtkmrmlutilsTest.py", line 106, in isDICOM_true_positive
    itemIDs = setupDICOM()
  File "/home/user/bin/Slicer_Ext/opendose3d/OpenDose3D/Logic/testbuilder.py", line 87, in setupDICOM
    raise Error('Unable to load series from database')
Logic.errors.Error

</code></pre>
<p>Please note it’s self-built Slicer without any customization.</p>

---

## Post #14 by @Alex_Vergara (2022-05-04 15:28 UTC)

<p>do you have a valid dicom database? if not, please create one first</p>

---

## Post #15 by @PaoloZaffino (2022-05-04 15:59 UTC)

<p>Hi all,<br>
here is my output (too long for pasting it here):</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pastebin.com/4fFXprus">
  <header class="source">
      <img src="https://pastebin.com/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://pastebin.com/4fFXprus" target="_blank" rel="noopener nofollow ugc">Pastebin</a>
  </header>

  <article class="onebox-body">
    <img src="https://pastebin.com/i/facebook.png" class="thumbnail" width="" height="">

<h3><a href="https://pastebin.com/4fFXprus" target="_blank" rel="noopener nofollow ugc">&gt;&gt;&gt; Reloading OpenDose3D------------------------------Reloading modu...</a></h3>

  <p>Pastebin.com is the number one paste tool since 2002. Pastebin is a website where you can store text online for a set period of time.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Let me know if I can help with other tests.</p>
<p>Paolo</p>

---

## Post #16 by @chir.set (2022-05-04 16:33 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="14" data-topic="23245" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>do you have a valid dicom database? if not, please create one first</p>
</blockquote>
</aside>
<p>Yes, there is a valid database :</p>
<pre><code class="lang-auto">sqlite3 /home/user/Documents/SlicerDICOMDatabase_1/ctkDICOM.sql
SQLite version 3.38.2 2022-03-26 13:51:10
Enter ".help" for usage hints.
sqlite&gt; .tables
ColumnDisplayProperties       Patients                    
Directories                   SchemaInfo                  
DisplayedFieldGeneratorRules  Series                      
Images                        Studies                     
sqlite&gt;
</code></pre>

---

## Post #17 by @Alex_Vergara (2022-05-04 16:43 UTC)

<p>Thanks for testing, OpenDose3D is working correctly in your system. May you tell something about your 3DSlicer installation method.</p>

---

## Post #18 by @Alex_Vergara (2022-05-04 16:45 UTC)

<p>Inside Slicer please check this is not shown. If it is shown, then create a new database or upgrade the existing one.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbdac69ec4bb1d4973c2dd5e763a89c184168778.png" data-download-href="/uploads/short-url/vmVi3asrhL4iW7anZA3AZl9Wl7i.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbdac69ec4bb1d4973c2dd5e763a89c184168778_2_690x88.png" alt="image" data-base62-sha1="vmVi3asrhL4iW7anZA3AZl9Wl7i" width="690" height="88" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbdac69ec4bb1d4973c2dd5e763a89c184168778_2_690x88.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbdac69ec4bb1d4973c2dd5e763a89c184168778_2_1035x132.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/dbdac69ec4bb1d4973c2dd5e763a89c184168778_2_1380x176.png 2x" data-dominant-color="515147"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1430×184 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @chir.set (2022-05-04 17:31 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="18" data-topic="23245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Inside Slicer please check this is not shown.</p>
</blockquote>
</aside>
<p>This is definitely not shown, no database warning is issued at any time. I’ll still try with a new one tomorrow when I get back to work.</p>

---

## Post #20 by @chir.set (2022-05-04 17:37 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="17" data-topic="23245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>May you tell something about your 3DSlicer installation method.</p>
</blockquote>
</aside>
<p>Slicer is built from source (not from PKGBUILD), packaged, then unpacked in a usual location. OpenDose3D is cloned from gitlab, and loaded in Slicer with <em>–additional-module-paths</em> pointing to the <em>OpenDose3D/</em> directory. Nothing exotic in here.</p>

---

## Post #21 by @Alex_Vergara (2022-05-04 18:15 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="20" data-topic="23245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>OpenDose3D is cloned from gitlab</p>
</blockquote>
</aside>
<p>This is the problem, in this case you need to download the patient and import it manually, since the clone does not place the patient images in the correct folder.<br>
The other option is to install the module using the extension manager (recommended). In this case everything shall work out of the box.</p>

---

## Post #22 by @chir.set (2022-05-04 18:47 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="21" data-topic="23245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>you need to download the patient and import it manually</p>
</blockquote>
</aside>
<p>You mean the files in Resources/DICOM/ ? If so, I’ll test that tomorrow.</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="21" data-topic="23245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>install the module using the extension manager</p>
</blockquote>
</aside>
<p>Yes, except that I’m using self-built Slicer, whose revision is rarely the same as preview builds. But I’ll try with the current nightly build using the extension manager and report.</p>

---

## Post #23 by @chir.set (2022-05-04 19:40 UTC)

<p>OpenDose3D test passed !</p>
<pre><code class="lang-auto">******** ADR workflow Tests passed ***************

Test FullTest_positive passed on Arch with preview build 5.1.0-2022-05-04 r30918 / 68a506f!

******** OpenDose3D Tests passed ***************
</code></pre>
<p>To be complete, the test on my machine was bound to fail with any Slicer build and OpenDose3D installed by any means. Because my slicerrc.py just empties the Dicom database whenever a scene is closed, and the test process does close the scene at least once ! So with an empty slicerrc.py, it just works on Arch with 5.1.</p>

---

## Post #24 by @Alex_Vergara (2022-05-05 07:18 UTC)

<p>So the problem is really the arch packaging that is not yet working in AUR.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a href="https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=3dslicer-bin" class="inline-onebox" rel="noopener nofollow ugc">PKGBUILD - aur.git - AUR Package Repositories</a> is still installing the version 4.11 even when the package says it is 5.0.1</p>

---

## Post #25 by @PaoloZaffino (2022-05-06 14:58 UTC)

<p>Maybe I didn’t understand correctly, but I used the binary files downloaded from Slicer website.<br>
Let me know if I have to use AUR</p>

---

## Post #26 by @Alex_Vergara (2022-05-06 21:44 UTC)

<p>The point is to have arch users to get slicer using the normal pacman packages. But the common ones doesn’t work. The binaries from the slicer webpage are working as you could see.</p>

---

## Post #27 by @jamesobutler (2022-05-06 22:56 UTC)

<aside class="quote no-group quote-modified" data-username="jcfr" data-post="2" data-topic="23245" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Based on comment associated with issue <a href="https://github.com/Slicer/Slicer/issues/5546" rel="noopener nofollow ugc">#5546</a>, it looks like we should update <a href="https://aur.archlinux.org/cgit/aur.git/tree/PKGBUILD?h=3dslicer-bin" class="inline-onebox" rel="noopener nofollow ugc">PKGBUILD - aur.git - AUR Package Repositories</a> to include the SHA of the latest release.</p>
<p>Looking at the history (see <a href="https://aur.archlinux.org/cgit/aur.git/log/PKGBUILD?h=3dslicer-bin" rel="noopener nofollow ugc">here </a>), it has been updated <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>That said, the list of <code>sha512sums</code> seems to have been untouched.</p>
<p>cc: <a class="mention" href="/u/butuihu">@ButuiHu</a></p>
</blockquote>
</aside>
<p>Yes, the regular AUR needs sha512sums updates to have any chance of working. The lilac bot is just bumping the version number, but not the sha512sums.</p>
<aside class="quote no-group" data-username="Alex_Vergara" data-post="10" data-topic="23245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>from archlinuxcn:</p>
<p>3dslicer installs 5.0.1 but basic stuffs are not working</p>
</blockquote>
</aside>
<p>^Appears that the Chinese based version skips over the sha512sums check for <code>3dslicer</code> package as seen <a href="https://github.com/archlinuxcn/repo/blob/084d20db2edcbcdec2b96fd8bd036169bcf0ea33/archlinuxcn/3dslicer/PKGBUILD#L41-L43" rel="noopener nofollow ugc">here</a>.</p>
<p>It will likely be up to the users in the various communities to maintain the latest versions of Slicer in their package manager of choice. I know I have seen previous posts about having Slicer available through <code>brew</code>. Install through these package managers is likely used by a few active users.</p>
<p>I’m not sure of all the considerations, but going directly to <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> for the download would seem to be the easiest option especially with users frequently getting help from <a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a> at different subdomain <a href="https://discourse.slicer.org/">https://discourse.slicer.org/</a>.</p>

---
