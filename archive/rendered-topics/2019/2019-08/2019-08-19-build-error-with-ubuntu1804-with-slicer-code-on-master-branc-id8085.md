# Build error with ubuntu1804 with slicer code on master branch

**Topic ID**: 8085
**Date**: 2019-08-19
**URL**: https://discourse.slicer.org/t/build-error-with-ubuntu1804-with-slicer-code-on-master-branch/8085

---

## Post #1 by @chenray844 (2019-08-19 07:31 UTC)

<p>In file included from /home/chenrf/Projects/medical/slicer/build/ITK-build/Modules/ThirdParty/HDF5/src/itkhdf5/shared/H5Tinit.c:82:0:<br>
/home/chenrf/Projects/medical/slicer/build/ITK/Modules/ThirdParty/HDF5/src/itkhdf5/src/H5Tpkg.h:23:2: error: <a class="hashtag-cooked" href="/tag/error" data-type="tag" data-slug="error" data-id="446"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>error</span></a> “Do not include this file outside the H5T package!”<br>
<a class="hashtag-cooked" href="/tag/error" data-type="tag" data-slug="error" data-id="446"><span class="hashtag-icon-placeholder"><svg class="fa d-icon d-icon-square-full svg-icon svg-node"><use href="#square-full"></use></svg></span><span>error</span></a> “Do not include this file outside the H5T package!”<br>
^~~~~<br>
Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/build.make:3944: recipe for target 'Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/<strong>/shared/H5Tinit.c.o’ failed<br>
make[5]: *** [Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/</strong>/shared/H5Tinit.c.o] Error 1<br>
CMakeFiles/Makefile2:6965: recipe for target ‘Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/all’ failed<br>
make[4]: *** [Modules/ThirdParty/HDF5/src/itkhdf5/src/CMakeFiles/hdf5-shared.dir/all] Error 2<br>
make[4]: *** Waiting for unfinished jobs…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02c88470e7a55ba6fedea6b89022c9e8230e48f9.png" data-download-href="/uploads/short-url/oCyNVUoqTEwF9BnqqqWaC7Vvtf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02c88470e7a55ba6fedea6b89022c9e8230e48f9.png" alt="image" data-base62-sha1="oCyNVUoqTEwF9BnqqqWaC7Vvtf" width="690" height="109" data-dominant-color="F3BAB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1005×159 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><span class="mention">@all</span></p>
<p>What can I do to fit this build ITK error?</p>

---

## Post #2 by @lassoan (2019-08-23 18:24 UTC)

<p>A post was merged into an existing topic: <a href="/t/build-error-with-itk-on-ubuntu1804/8107">Build error with itk on ubuntu1804</a></p>

---

## Post #3 by @lassoan (2019-08-23 18:24 UTC)



---
