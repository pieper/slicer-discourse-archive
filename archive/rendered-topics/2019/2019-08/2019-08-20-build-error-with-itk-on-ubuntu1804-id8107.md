# Build error with itk on ubuntu1804

**Topic ID**: 8107
**Date**: 2019-08-20
**URL**: https://discourse.slicer.org/t/build-error-with-itk-on-ubuntu1804/8107

---

## Post #1 by @chenray844 (2019-08-20 18:36 UTC)

<p>when I build slicer on ubuntu1804 with latest code, some error happens.</p>
<pre><code class="lang-auto">[ 74%] Building C object Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/__/shared/H5Tinit.c.o
In file included from /home/chenrf/Projects/medical/slicer/build/ITK-build/Modules/ThirdParty/HDF5/src/itkhdf5/shared/H5Tinit.c:82:0:
/home/chenrf/Projects/medical/slicer/build/ITK/Modules/ThirdParty/HDF5/src/itkhdf5/src/H5Tpkg.h:23:2: error: #error "Do not include this file outside the H5T package!"
 #error "Do not include this file outside the H5T package!"
  ^~~~~
Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/build.make:3944: recipe for target 'Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/__/shared/H5Tinit.c.o' failed
make[5]: *** [Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/__/shared/H5Tinit.c.o] Error 1
CMakeFiles/Makefile2:6965: recipe for target 'Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/all' failed
make[4]: *** [Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/all] Error 2
make[4]: *** Waiting for unfinished jobs....

</code></pre>
<p>ITK:</p>
<pre><code class="lang-auto">$ git branch
* (HEAD detached at 35e6f54643)
  welcome
</code></pre>
<p>Slicer:</p>
<pre><code class="lang-auto">git reflog
aa245a9d5 (HEAD -&gt; master, origin/master, origin/HEAD) HEAD@{0}: pull: Fast-forward
ced36e5fa (origin/nightly-master) HEAD@{1}: pull: Fast-forward
1b7888e90 HEAD@{2}: pull: Fast-forward

</code></pre>
<p>cmake</p>
<pre><code class="lang-auto"> cmake --version
cmake version 3.15.0

CMake suite maintained and supported by Kitware (kitware.com/cmake).

</code></pre>
<p>How can I fix this bug?</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/509#issuecomment-522998801" target="_blank" rel="nofollow noopener">github.com/InsightSoftwareConsortium/ITK</a>
  </header>
  <article class="onebox-body">
    <a href="https://github.com/phcerdan" rel="nofollow noopener">
<img src="https://avatars1.githubusercontent.com/u/3021667?v=2&amp;s=96" class="thumbnail onebox-avatar" width="96" height="96">
</a>

<h4><a href="https://github.com/InsightSoftwareConsortium/ITK/issues/509#issuecomment-522998801" target="_blank" rel="nofollow noopener">Issue: HDF5 error about including private headers H5Tpkg.h</a></h4>

<div class="date" style="margin-top:10px;">
	<div class="user" style="margin-top:10px;">
	opened by <a href="https://github.com/phcerdan" target="_blank" rel="nofollow noopener">phcerdan</a>
	on <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/509#issuecomment-522998801" target="_blank" rel="nofollow noopener">2019-02-15</a>
	</div>
	<div class="user">
	</div>
</div>

<pre class="content" style="white-space: pre-wrap;">Raised by @lorensen in discourse https://discourse.itk.org/t/gcc-8-2/1601/2
and reproduced locally with gcc8.2.
build log: https://open.cdash.org/viewBuildError.php?buildid=5754102
Might be related to latest hdf5 update?
Building C object Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/__/shared/H5Tinit.c.o
FAILED:...</pre>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @chenray844 (2019-08-19 07:31 UTC)

<p>In file included from /home/chenrf/Projects/medical/slicer/build/ITK-build/Modules/ThirdParty/HDF5/src/itkhdf5/shared/H5Tinit.c:82:0:<br>
/home/chenrf/Projects/medical/slicer/build/ITK/Modules/ThirdParty/HDF5/src/itkhdf5/src/H5Tpkg.h:23:2: error: <a class="hashtag-cooked" href="/tag/error" data-type="tag" data-slug="error" data-id="446"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>error</span></a> “Do not include this file outside the H5T package!”<br>
<a class="hashtag-cooked" href="/tag/error" data-type="tag" data-slug="error" data-id="446"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>error</span></a> “Do not include this file outside the H5T package!”<br>
^~~~~<br>
Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/build.make:3944: recipe for target 'Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/<strong>/shared/H5Tinit.c.o’ failed<br>
make[5]: *** [Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/</strong>/shared/H5Tinit.c.o] Error 1<br>
CMakeFiles/Makefile2:6965: recipe for target ‘Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/all’ failed<br>
make[4]: *** [Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/all] Error 2<br>
make[4]: *** Waiting for unfinished jobs…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02c88470e7a55ba6fedea6b89022c9e8230e48f9.png" data-download-href="/uploads/short-url/oCyNVUoqTEwF9BnqqqWaC7Vvtf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02c88470e7a55ba6fedea6b89022c9e8230e48f9_2_690x109.png" alt="image" data-base62-sha1="oCyNVUoqTEwF9BnqqqWaC7Vvtf" width="690" height="109" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02c88470e7a55ba6fedea6b89022c9e8230e48f9_2_690x109.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02c88470e7a55ba6fedea6b89022c9e8230e48f9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02c88470e7a55ba6fedea6b89022c9e8230e48f9.png 2x" data-dominant-color="F3BAB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1005×159 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><span class="mention">@all</span></p>
<p>What can I do to fit this build ITK error?</p>

---

## Post #3 by @lassoan (2019-08-23 18:27 UTC)

<p>You can see on the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview" rel="nofollow noopener">dashboard</a> that Slicer builds without problems on Linux. Maybe try with the same tools as used on the dashboard computer (CMake version, compiler, etc.), and maybe also try to uninstall any system ITK, VTK, HDF5 libraries.</p>

---
