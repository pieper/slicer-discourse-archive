# Slicer build failed

**Topic ID**: 42319
**Date**: 2025-03-26
**URL**: https://discourse.slicer.org/t/slicer-build-failed/42319

---

## Post #1 by @TinaNant28 (2025-03-26 19:06 UTC)

<p>Hi,<br>
I followed the Build Instructions to build Slicer on Windows 11.<br>
CMake: 3.31.6<br>
Git: 2.48.1<br>
Qt: 5.15.2 64-bit (MSVC 2019)<br>
Visual Studio 2022 C++ x64<br>
After build Slicer in Visual Studio, 10 errors occurred.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2989aa3e1b50bd62a5da68d0e475e8fad93f670b.png" data-download-href="/uploads/short-url/5VswnnQleRcu0crMHI8CBKdsBJx.png?dl=1" title="Capture d'écran 2025-03-26 135231" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2989aa3e1b50bd62a5da68d0e475e8fad93f670b_2_690x131.png" alt="Capture d'écran 2025-03-26 135231" data-base62-sha1="5VswnnQleRcu0crMHI8CBKdsBJx" width="690" height="131" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2989aa3e1b50bd62a5da68d0e475e8fad93f670b_2_690x131.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2989aa3e1b50bd62a5da68d0e475e8fad93f670b_2_1035x196.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2989aa3e1b50bd62a5da68d0e475e8fad93f670b_2_1380x262.png 2x" data-dominant-color="2F2F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d'écran 2025-03-26 135231</span><span class="informations">3760×716 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How to solve these errors please? Thanks!</p>

---

## Post #2 by @lassoan (2025-03-27 01:39 UTC)

<p>This seems to be an ITK error:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/InsightSoftwareConsortium/ITK/issues/4820">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/4820" target="_blank" rel="noopener">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/4820" target="_blank" rel="noopener">5.4 ITK Failed to build(CMake) with error LNK2005: __ucrt_int_to_float already defined</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-08-26" data-time="08:59:04" data-timezone="UTC">08:59AM - 26 Aug 24 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2024-11-17" data-time="21:31:55" data-timezone="UTC">09:31PM - 17 Nov 24 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/wbkangtc" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/177302876?v=4" class="onebox-avatar-inline" width="20" height="20">
          wbkangtc
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:Bug
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:Compiler
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">### Description

Fails to build on CMake 3.30.1
Windows SDK version 10.0.2610<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">0.0 to target Windows 10.0.22631.
[build]   -- Using MSVC's dynamic CRT (/MD and /MDd)
With error message
```
[build]     itktiff.vcxproj -&gt; C:\TSS\build\Extern\ITK\src\ITK-build\lib\Debug\itktiff-5.4.lib
[build] itktiff-5.4.lib(tif_luv.obj) : error LNK2005: __ucrt_int_to_float already defined in itktiff-5.4.lib(tif_aux.obj) [C:\TSS\build\Extern\ITK\src\ITK-build\Modules\IO\TIFF\src\ITKIOTIFF.vcxproj] [C:\TSS\build\ITK.vcxproj]
[build] itktiff-5.4.lib(tif_color.obj) : error LNK2005: __ucrt_int_to_float already defined in itktiff-5.4.lib(tif_aux.obj) [C:\TSS\build\Extern\ITK\src\ITK-build\Modules\IO\TIFF\src\ITKIOTIFF.vcxproj] [C:\TSS\build\ITK.vcxproj]
```

### Steps to Reproduce
1. Attempt build.

```
	ExternalProject_add(ITK
	  PREFIX ${CMAKE_BINARY_DIR}/Extern/ITK
	  GIT_REPOSITORY https://github.com/InsightSoftwareConsortium/ITK.git
	  GIT_TAG v5.4.0
	  UPDATE_COMMAND ""
	  CMAKE_ARGS
		-DBUILD_EXAMPLES:BOOL=OFF
		-DBUILD_SHARED_LIBS:BOOL=ON
		-DBUILD_TESTING:BOOL=OFF
		-DCMAKE_BUILD_TYPE:STRING=${CUSTOM_BUILD_TYPE}
		-DITK_BUILD_DEFAULT_MODULES:BOOL=ON
		-DModule_ITKReview:BOOL=ON
		-DITK_LEGACY_REMOVE:BOOL=ON
		-DCMAKE_INSTALL_PREFIX:PATH=${INSTALL_DEPENDENCIES_DIR}/ITK
		-DITK_USE_SYSTEM_HDF5:BOOL=OFF
		-DModule_ITKVtkGlue:BOOL=OFF
		-DHDF5_ROOT:STRING=${HDF5_ROOT}
	  INSTALL_DIR ${INSTALL_DEPENDENCIES_DIR}
	  DEPENDS HDF5
	)
```

### Expected behavior

Build
### Actual behavior

```
[build]     itktiff.vcxproj -&gt; C:\TSS\build\Extern\ITK\src\ITK-build\lib\Debug\itktiff-5.4.lib
[build] itktiff-5.4.lib(tif_luv.obj) : error LNK2005: __ucrt_int_to_float already defined in itktiff-5.4.lib(tif_aux.obj) [C:\TSS\build\Extern\ITK\src\ITK-build\Modules\IO\TIFF\src\ITKIOTIFF.vcxproj] [C:\TSS\build\ITK.vcxproj]
[build] itktiff-5.4.lib(tif_color.obj) : error LNK2005: __ucrt_int_to_float already defined in itktiff-5.4.lib(tif_aux.obj) [C:\TSS\build\Extern\ITK\src\ITK-build\Modules\IO\TIFF\src\ITKIOTIFF.vcxproj] [C:\TSS\build\ITK.vcxproj]
```
### Reproducibility
100
### Versions
v5.4.0
### Environment
Fails to build on CMake 3.30.1
Windows SDK version 10.0.26100.0 to target Windows 10.0.22631.
[build]   -- Using MSVC's dynamic CRT (/MD and /MDd)
MSVC 17.10 (VS2022)

### Additional Information</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Probably you can fix it by upgrading or downgrading your Windows SDK or compiler today; or applying one of the workarounds described in the referenced issue.</p>

---

## Post #3 by @jamesobutler (2025-03-27 12:58 UTC)

<p>This PR aims to update the Slicer ITK version to one that includes a fix for that reported ITK issue:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8339">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8339" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8339" target="_blank" rel="noopener nofollow ugc">COMP: Update ITK to 5.4.3</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jamesobutler:bump-itk-5.4.3</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-03-26" data-time="19:56:35" data-timezone="UTC">07:56PM - 26 Mar 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8339/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This updates ITK from a version based on 5.4.0 to now being based on the 5.4.3 r<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8339" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">elease. 

This should address build issues such as the one mentioned at https://discourse.slicer.org/t/slicer-build-failed/42319 as this now includes the https://github.com/InsightSoftwareConsortium/ITK/commit/6025654de3d815b131cebe969655c7173a27756c fix along with other various fixes included with the recent ITK patch releases on the 5.4.x release branch.

```
$ git shortlog 29b78d7..55c47b7 --no-merges
Andras Lasso (1):
      ENH: Backport libtiff fix of not displaying warning for unknown tags

Brad King (1):
      COMP: itktiff: Suppress C99 inline only on MSVC from VS 2013 and below

Bradley Lowekamp (13):
      BUG: Check output of StatisticsUniqueLabelMapFilterTest1
      BUG: Address bugs in unique label map filters
      BUG: Remove dilation output in test
      ENH: A GTest for LabelUniqueLabelMapFilter
      BUG: Address race condition in SLIC filter
      DOC: Correct Documentation for PadImageFilter::SizeGreatestPrimeFactor
      BUG: Enable system TIFF with modern TIFF and cmake
      BUG: Remove SpatialObjectProperty's writable string methods from SWIG
      ENH: Download x86 clangformat on Darwin arm64
      ENH: remove repetitive monochorme1 warning
      BUG: Fix 32-bit truncation on VectorImage Accessors
      BUG: Update LabelErodeDilate remote module
      ENH: Use get_schedaffin to determine number of threads

Dženan Zukić (2):
      COMP: Get ITK_USE_FLOAT_SPACE_PRECISION=ON to compile again
      DOC: Remove duplicate new author name (Matthieu LAURENDEAU)

Hans Johnson (1):
      COMP: macOS-11 Azure CI environment EOL

James Butler (1):
      [Backport MR-4910] COMP: Update DCMTK targets based on new DCMTK namespace

Jean-Christophe Fillion-Robin (1):
      COMP: Add support for customizing ITK namespace (draft)

Matt McCormick (8):
      DOC: Update .zenodo
      BUG: Update HDF5 name mangled symbols
      DOC: Improve itk_hdf5_mangle.h.in instructions
      BUG: Move InputSpaceName, OutputSpaceName from Transform to TransformBase
      COMP: Set CastXML flag based on CMAKE_CXX_STANDARD
      STYLE: clang-format fixes to itkSLICImageFilter.hxx
      COMP: Remove unused setuptools upgrade in Linux builds
      COMP: Bump ITKTotalVariation remote module

Matthew McCormick (27):
      ENH: Initial pixi configuration
      DOC: Document development with Pixi
      ENH: Add Pixi dev environment
      ENH: Add Pixi GitHub Actions Configuration
      BUG: Fix pixi caching of Python Debug builds
      ENH: Add Pixi python-exe and python-exe-debug tasks
      ENH: Python dispatch on the first RequiredInputName
      ENH: Add Pixi osx-64 configuration
      ENH: Add Intel Mac to Pixi GitHub Action tests
      ENH: Add Pixi mac ARM configuration
      ENH: Add ARM Mac to Pixi GitHub Action tests
      ENH: Bump ITK version to 5.3.1
      DOC: Updates for release testing data uploads
      BUG: GenerateImageSource sets Size from ReferenceImage
      COMP: Use .clang-format from release-5.4 branch
      STYLE: clang-format updates to itkGridImageSourceTest2.cxx
      ENH: Bump ITK version to 5.4.2
      DOC: Update maintenance branch for 5.4 series
      DOC: Point to RTD Doxygen documentation, ITKDoxygen Docker build
      DOC: Update Doxygen class links to use ReadTheDocs
      DOC: Update versioned Doxygen links to point to ReadTheDocs
      DOC: ITK 5.4.0 release notes
      DOC: Add ITK 5.4.2 release notes
      BUG: Remove VNL Netlib rpoly files
      COMP: Bump MeshToPolyData Remote Module to 2024-03-14 main
      BUG: Clamp GlobalDefault threads with GlobalMaximum with initialization
      ENH: Bump ITK version to 5.4.3

Mihail Isakov (1):
      BUG: Fix ExposeMetaData&lt;std::vector&lt;double&gt;&gt; im MetaImageIO

Niels Dekker (3):
      ENH: Add nested CoordinateType aliases as alternative to CoordRepType
      ENH: Add ...CoordinateType aliases as alternative to ...CoordRepType
      BUG: `QuadEdgeMeshPoint` should be properly initialized by `{}`

Simon Rit (1):
      BUG: Remove check on WrapITK.pth existence in itk_python_add_test

Ziv Yaniv (1):
      BUG: Missing writing of the nifti descrip field.

ntustison (1):
      BUG: Incorrect size for closed parametric dimension.
```

Testing on Windows:
Build: ✔️ 
Package: ✔️ 
Testing: ✔️ (no new tests failing)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @TinaNant28 (2025-03-28 15:05 UTC)

<p>Thank you very much. It works!</p>

---
