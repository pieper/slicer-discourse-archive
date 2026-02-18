# A error of MRMLCorePython when making code

**Topic ID**: 35440
**Date**: 2024-04-11
**URL**: https://discourse.slicer.org/t/a-error-of-mrmlcorepython-when-making-code/35440

---

## Post #1 by @czgchd (2024-04-11 15:18 UTC)

<p>cmake version 3.28.4</p>
<p>ubuntu 22.04</p>
<p>3D Slicer</p>
<p>when i performed the command :  make, i met a error</p>
<p>[ 33%] Linking CXX shared module …/…/…/bin/MRMLCorePython.so<br>
[ 33%] Built target MRMLCorePython<br>
make[3]: *** [Makefile:166: all] Error 2<br>
make[2]: *** [CMakeFiles/Slicer.dir/build.make:90: Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2<br>
make[1]: *** [CMakeFiles/Makefile2:1450: CMakeFiles/Slicer.dir/all] Error 2<br>
make: *** [Makefile:101: all] Error 2</p>
<p>i do not know how to fix it, thanks</p>

---

## Post #2 by @pieper (2024-04-11 17:35 UTC)

<p>It looks like the actual error is not in this build log, so you might need to scroll up to find it.</p>
<p>I happened to be building on 22.04 earlier today and added these notes to the documentation.  You may need one of these dependecies:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7689/files">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7689/files" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7689/files" target="_blank" rel="noopener">DOC: Add ubuntu 22.04 build instructions</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Slicer:doc-ubuntu2204-build</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-04-11" data-time="17:31:38" data-timezone="UTC">05:31PM - 11 Apr 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 6 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7689/files" target="_blank" rel="noopener">
            <span class="added">+6</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">With these prerequisites I could build from scratch on a freshly booted 22.04 ma<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7689" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">chine running on Jetstream2.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @czgchd (2024-04-12 02:30 UTC)

<p>thanks for your reply .</p>
<p>lastly, i take this site <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/ANTsX/ANTs/issues/1248">
  <header class="source">

      <a href="https://github.com/ANTsX/ANTs/issues/1248" target="_blank" rel="noopener nofollow ugc">github.com/ANTsX/ANTs</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/ANTsX/ANTs/issues/1248" target="_blank" rel="noopener nofollow ugc">Error building ANTs related to MD5</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-06" data-time="14:43:21" data-timezone="UTC">02:43PM - 06 Oct 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-10-07" data-time="15:18:37" data-timezone="UTC">03:18PM - 07 Oct 21 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/ik362" target="_blank" rel="noopener nofollow ugc">
          <img alt="ik362" src="https://avatars.githubusercontent.com/u/57671726?v=4" class="onebox-avatar-inline" width="20" height="20">
          ik362
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">&lt;!--
Text in these brackets are comments, and won't be visible when you submit <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">your
issue. Please read before submitting.

Before opening an issue, please review the build documentation here

https://github.com/ANTsX/ANTs/wiki/Compiling-ANTs-on-Linux-and-Mac-OS

You can also search the wiki and previous issues using the main Github search
bar. Enter search terms and select "In this repository".

If you are using system ITK or VTK, please verify you have the correct
versions (see the Wiki link above). If you can, please also attempt a
Superbuild and let us know if that compiles successfully.
--&gt;

**When did the error occur?**

[ ] CMake configuration (cmake / ccmake)
[X] Compilation (make)
[ ] Installation (make install)

**Build environment**
 - OS: Mac OS
 - OS version: 11.6 (20G165)
 - Type of system: laptop

&lt;!--
If you are building inside a virtual machine, container, Cygwin, Windows
Subsystem for Linux, or other non-native environment, please let us know and
include details of both the virtual Linux and the host OS.
--&gt;

**ANTs version**
&lt;!--
Specify the release tag or commit hash of the code you are building
from with `git show` in your source directory. If you downloaded a snapshot as a
ZIP file, please provide the tag version (if applicable) or date of the download.
--&gt;
Ecphorella

**Build configuration and logs**
&lt;!--
Please attach the following files (relative to your build directory)

  - build.log (the terminal output from make, eg `make | tee build.log`)
  - CMakeCache.txt
  - CMakeFiles/CMakeError.log
  - CMakeFiles/CMakeOutput.log
--&gt;

  - build.log: [build.log](https://github.com/ANTsX/ANTs/files/7294846/build.log)
  - CMakeCache.txt: [CMakeCache.txt](https://github.com/ANTsX/ANTs/files/7294851/CMakeCache.txt)
  - CMakeFiles/CMakeError.log: [CMakeError.log](https://github.com/ANTsX/ANTs/files/7294862/CMakeError.log)
  - CMakeFiles/CMakeOutput.log: [CMakeOutput.log](https://github.com/ANTsX/ANTs/files/7294873/CMakeOutput.log)


**Additional context**

Hi there,

I am trying to build ANTs however I keep running into the following error:
```shell
-- Fetching "file:///~/ANTs/.ExternalData/MD5/37aaa33029410941bf4affff0479fa18"
-- Fetching "http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;checksum=37aaa33029410941bf4affff0479fa18"
-- Fetching "https://data.kitware.com:443/api/v1/file/hashsum/MD5/37aaa33029410941bf4affff0479fa18/download"
-- Fetching "http://www.itk.org/files/ExternalData/MD5/37aaa33029410941bf4affff0479fa18"
-- [download 100% complete]
* Closing connection 0
CMake Error at /usr/local/Cellar/cmake/3.21.3_1/share/cmake/Modules/ExternalData.cmake:1181 (message):
  

  Object MD5=37aaa33029410941bf4affff0479fa18 not found at:

    file:///~/ANTs/.ExternalData/MD5/37aaa33029410941bf4affff0479fa18 ("Couldn't read a file:// file")
    http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;checksum=37aaa33029410941bf4affff0479fa18 ("HTTP response code said error")
    https://data.kitware.com:443/api/v1/file/hashsum/MD5/37aaa33029410941bf4affff0479fa18/download ("HTTP response code said error")
    http://www.itk.org/files/ExternalData/MD5/37aaa33029410941bf4affff0479fa18 ("HTTP response code said error")


make[5]: *** [ExternalData/TestData/Data/r16slice.nii.gz-hash-stamp] Error 1
make[4]: *** [Examples/TestSuite/CMakeFiles/ANTSFetchData.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [ANTS-prefix/src/ANTS-stamp/ANTS-build] Error 2
make[1]: *** [CMakeFiles/ANTS.dir/all] Error 2
```
This seems to be a similar (but slightly different issue) to #1236. I have also made sure that `xcode-select` (v2384), `brew` (v3.2.15), `cmake` (v3.21.3), and `make` (v3.81) are all up to date.

Thanks!</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>command <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>cmake -DBUILD_TESTING=OFF , and then make</p>
<p>successfuly end.</p>

---
