---
topic_id: 9995
title: "Elastix Build Error"
date: 2020-01-29
url: https://discourse.slicer.org/t/9995
---

# Elastix build error

**Topic ID**: 9995
**Date**: 2020-01-29
**URL**: https://discourse.slicer.org/t/elastix-build-error/9995

---

## Post #1 by @Alex_Vergara (2020-01-29 13:22 UTC)

<p>As seen here <a href="http://slicer.cdash.org/buildSummary.php?buildid=1809996" rel="nofollow noopener">http://slicer.cdash.org/buildSummary.php?buildid=1809996</a></p>
<p>elastix is failing and it is not being built, there is any schedule to solve this issue, it seems quite complicated errors there</p>

---

## Post #2 by @lassoan (2020-01-29 17:32 UTC)

<p>Thank you, probably we just need to update to a more recent Elastix version that is compatible with the ITK version that Slicer uses. Could you give it a try?</p>

---

## Post #3 by @Alex_Vergara (2020-01-30 11:12 UTC)

<p>Since Elastix is not core part of slicer I don’t know how to test this:</p>
<ul>
<li>Shall I build slicer, then elastix?</li>
<li>Shall I build only elastix?</li>
</ul>
<p>Never tried this before</p>

---

## Post #4 by @lassoan (2020-01-30 14:47 UTC)

<p>Yes, first you need to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build Slicer</a> and then build <a href="https://github.com/lassoan/SlicerElastix">SlicerElastix extension</a>.</p>

---

## Post #5 by @lassoan (2020-01-30 21:57 UTC)

<p>I had a look at this build error. It is due to recent backward-incompatible changes in ITK related to typed enums. I <a href="https://github.com/lassoan/elastix/commit/dbb5a0e88feceee92b5c72be6c45d305a6fb0854">applied a quick patch to Elastix in my fork</a> and switched to this patched version for now. This should fix the build problem in SlicerElastix.</p>
<p><a class="mention" href="/u/dzenanz">@dzenanz</a> I don’t know if these kind of issues are expected with ITK-v5.1rc01 but it would be nice if the final ITK-v5.1 release would not have such problems.</p>

---

## Post #6 by @Alex_Vergara (2020-01-31 12:28 UTC)

<p>Well, that was not enough accordingly to <a href="http://slicer.cdash.org/buildSummary.php?buildid=1811816" rel="nofollow noopener">http://slicer.cdash.org/buildSummary.php?buildid=1811816</a></p>

---

## Post #7 by @Alex_Vergara (2020-01-31 13:06 UTC)

<p>I anm currently running a test in a container with</p>
<pre><code class="lang-auto"># only one stage, since gitlab-ci does not support passing images between stages
image: unnmdnwb3/slicer3d-nightly:0.7.0

build-and-test:
  variables:
    DISPLAY: ":99.0"
  script:
    - mkdir $CI_BUILDS_DIR/elastix-build &amp;&amp; cd $CI_BUILDS_DIR/elastix-build
    - cmake -DSlicer_DIR:PATH=/usr/src/Slicer-build/Slicer-build -DITK_DIR:PATH$
    - make -j32
</code></pre>

---

## Post #8 by @lassoan (2020-01-31 13:07 UTC)

<p>Build is successful on Windows and Linux now, but yes, the compiler on MacOS still struggles with some type conversion. I saw similar issue when we first built Slicer and BRAINSTools with ITK5 a d probably the solution will be similar, too. I’ll try to fix it today, but I don’t have a Mac to test on, so it may take a few more days until we converge to a solution.</p>

---

## Post #9 by @Alex_Vergara (2020-01-31 13:33 UTC)

<p>For reference this is the container output (truncated)</p>
<pre><code class="lang-auto">/builds/project-0/Common/Transforms/itkAdvancedRigid2DTransform.hxx:125:5: warning: ‘vnl_matrix_fixed&lt;T, num_rows, num_cols&gt;::operator const vnl_matrix_ref&lt;T&gt;() const [with T = double; unsigned int num_rows = 2u; unsigned int num_cols = 2u]’ is deprecated: Implicit cast conversion is dangerous.
USE: .as_vector() or .as_ref() member function for clarity. [-Wdeprecated-declarations]
   p = this-&gt;GetMatrix().GetVnlMatrix();
     ^
In file included from /usr/src/Slicer-build/ITK/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_matrix_fixed.hxx:9:0,
                 from /usr/src/Slicer-build/ITK/Modules/Core/Common/include/itkMatrix.h:25,
                 from /usr/src/Slicer-build/ITK/Modules/Core/Common/include/itkSymmetricSecondRankTensor.h:28,
                 from /usr/src/Slicer-build/ITK/Modules/IO/ImageBase/include/itkImageIOBase.h:30,
                 from /usr/src/Slicer-build/ITK/Modules/IO/ImageBase/include/itkImageFileReader.h:24,
                 from /builds/project-0/Core/Kernel/elxElastixBase.h:39,
                 from /builds/project-0/Core/Kernel/elxElastixTemplate.h:21,
                 from /builds/project-0/Core/Install/elxIncludes.h:39,
                 from /builds/project-0/Components/Transforms/EulerStackTransform/elxEulerStackTransform.h:21,
                 from /builds/project-0/Components/Transforms/EulerStackTransform/elxEulerStackTransform.cxx:19:
/usr/src/Slicer-build/ITK/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_matrix_fixed.h:687:3: note: declared here
   operator const vnl_matrix_ref&lt;T&gt;() const { return  this-&gt;as_ref(); }
   ^

[ 99%] Linking CXX executable ../bin/elastix
[100%] Linking CXX executable ../bin/transformix
[100%] Built target elastix
[100%] Built target transformix
e[0KAuthenticating with credentials from /home/alex/.docker/config.json
e[0;me[0KAuthenticating with credentials from /home/alex/.docker/config.json
e[0;me[32;1mJob succeeded
e[0;m
</code></pre>

---

## Post #10 by @lassoan (2020-02-01 23:42 UTC)

<p>I’ve committed a <a href="https://github.com/lassoan/elastix/commit/e82e1fde91ad90cd0a5dc398a503237a6c5f0856">change</a> in Elastix that fixed a similar issue in Slicer core. We’ll see tomorrow on the dashboard if this fixes the Mac build error.</p>

---

## Post #11 by @lassoan (2020-02-02 19:09 UTC)

<p>Elastix build error is now fixed on Mac. It would be great if you could check if it works well.</p>

---

## Post #12 by @Alex_Vergara (2020-02-04 15:01 UTC)

<p>Well It is being built</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4bc1fa21e2ec770b1a1e96bc77dce169e8123d.png" data-download-href="/uploads/short-url/p0JRMFTgLeYKJTzDI1DErInRmsl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af4bc1fa21e2ec770b1a1e96bc77dce169e8123d_2_690x432.png" alt="image" data-base62-sha1="p0JRMFTgLeYKJTzDI1DErInRmsl" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af4bc1fa21e2ec770b1a1e96bc77dce169e8123d_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4bc1fa21e2ec770b1a1e96bc77dce169e8123d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4bc1fa21e2ec770b1a1e96bc77dce169e8123d.png 2x" data-dominant-color="535251"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">818×513 57.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And it is running very well</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9db66331216a4477ef8dd1035e9bae2bb82aac8.jpeg" data-download-href="/uploads/short-url/zEkWWRh6U3HsvTdPnAWu76mFrGo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9db66331216a4477ef8dd1035e9bae2bb82aac8_2_690x489.jpeg" alt="image" data-base62-sha1="zEkWWRh6U3HsvTdPnAWu76mFrGo" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9db66331216a4477ef8dd1035e9bae2bb82aac8_2_690x489.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9db66331216a4477ef8dd1035e9bae2bb82aac8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9db66331216a4477ef8dd1035e9bae2bb82aac8.jpeg 2x" data-dominant-color="292C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">963×683 94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2020-02-04 15:02 UTC)

<p>Great, thanks for testing!</p>

---
