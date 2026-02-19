---
topic_id: 35593
title: "Cannot Load Rtstruct File"
date: 2024-04-18
url: https://discourse.slicer.org/t/35593
---

# Cannot load RTSTRUCT file

**Topic ID**: 35593
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/cannot-load-rtstruct-file/35593

---

## Post #1 by @Freja (2024-04-18 11:35 UTC)

<p>Operating system: MacOS<br>
Slicer version: 5.6.2</p>
<p>Hello<br>
I have a problem with loading RTSTRUCT files (RS.dcm) in 3Dslicer. The data is imported without any error massages, and I can see the files in the “DICOM database” window. But when I press load nothing happens. I do not get any error massage but I do not see the files in the “Loaded data” window (se attached screenshot). CT images and RD.dcm fils loads correctly.</p>
<p>I have tried to re-instal RTSlicer. I have also tried different structure-sets, including DICOM-files downloaded from <a href="https://github.com/SlicerRt/SlicerRtData" rel="noopener nofollow ugc">https://github.com/SlicerRt/SlicerRtData</a></p>
<p>I would be very happy for some help!<br>
Thanks in advance</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccdd94b8074dfb0a1442ff5b83c00e472a2b0459.png" data-download-href="/uploads/short-url/tek8C3cm0vCFviWdA0a64dyInfX.png?dl=1" title="Screenshot 2024-04-18 at 11.13.14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccdd94b8074dfb0a1442ff5b83c00e472a2b0459_2_690x392.png" alt="Screenshot 2024-04-18 at 11.13.14" data-base62-sha1="tek8C3cm0vCFviWdA0a64dyInfX" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccdd94b8074dfb0a1442ff5b83c00e472a2b0459_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccdd94b8074dfb0a1442ff5b83c00e472a2b0459_2_1035x588.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccdd94b8074dfb0a1442ff5b83c00e472a2b0459_2_1380x784.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-04-18 at 11.13.14</span><span class="informations">2910×1656 352 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-04-18 19:03 UTC)

<p>Please open the Python console using this button<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63442665ce03715700c4ba5064f0a1856d53cc2b.png" alt="image" data-base62-sha1="ea9hniZIsvQfTlQh8pf3ZL3HMIb" width="616" height="337"><br>
and copy-paste here the red text you find.</p>

---

## Post #3 by @Freja (2024-04-19 07:35 UTC)

<p>Thank you for your help! Opening the Python console made me realize I had problems with installation and that my problem was the same as in this thread: <a href="https://discourse.slicer.org/t/failure-to-load-rtstruct-dicom-file/33504" class="inline-onebox">Failure to load RTSTRUCT dicom file</a></p>
<p>I have now also <strong>solved it by installing Slicer 5.2.2</strong> instead of Slicer 5.6.2.</p>
<p>There was alot of red massages when I opend the console so I will not paste all of them here, but for documentation, some of the error massages I got was:<br>
<strong>When opening slicer after installation:</strong><br>
[Qt] Populating font family aliases took 190 ms. Replace uses of missing font family “.AppleSystemUIFont” with one that exists to avoid this cost.</p>
<p><strong>After restarting slicer after slicerRT installation:</strong><br>
Cannot load library /Applications/Slicer.app/Contents/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerBeamsModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-32448/SlicerRT/lib/Slicer-5.6/qt-loadable-modules/libqSlicerBeamsModule.dylib, 0x0085): Library not loaded: <span class="mention">@rpath</span>/libomp.dylib</p>

---

## Post #4 by @cpinter (2024-04-19 09:45 UTC)

<p>Ah yes I just see you’re on Mac. That’s right, new Slicer versions do not have SlicerRT on Mac.</p><aside class="onebox githubissue" data-onebox-src="https://github.com/SlicerRt/SlicerRT/issues/242">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRT/issues/242" target="_blank" rel="noopener">github.com/SlicerRt/SlicerRT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerRt/SlicerRT/issues/242" target="_blank" rel="noopener">SlicerRT Slicer extension is not working on mac</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-03-25" data-time="19:56:51" data-timezone="UTC">07:56PM - 25 Mar 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/fedorov" target="_blank" rel="noopener">
          <img alt="fedorov" src="https://avatars.githubusercontent.com/u/313942?v=4" class="onebox-avatar-inline" width="20" height="20">
          fedorov
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As discussed in this thread https://discourse.slicer.org/t/failure-to-load-rtstr<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">uct-dicom-file/33504/5, it has been failing at least since Slicer 5.6.1.

```
Qt]   Error(s):
[Qt]     Cannot load library /Applications/Slicer-5.7.0-20240306.app/Contents/Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libqSlicerBeamsModule.dylib: (dlopen(/Applications/Slicer-5.7.0-20240306.app/Contents/Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libqSlicerBeamsModule.dylib, 0x0085): Library not loaded: @rpath/libomp.dylib
[Qt]   Referenced from: &lt;8CC410E5-7FE3-33F6-BC6E-A68391968FE8&gt; /Applications/Slicer-5.7.0-20240306.app/Contents/Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libvtkSlicerBeamsModuleMRML.dylib
[Qt]   Reason: tried: '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/QuantitativeReporting/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerDevelopmentToolbox/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/IDCBrowser/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/DCMQI/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/DCMQI/lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/PETDICOMExtension/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/PETDICOMExtension/lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerRT/lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerRT/lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../Extensions-32750/SlicerRT/lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Slicer-5.7/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Slicer-5.7/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../../lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/../lib/Slicer-5.7/qt-loadable-modules/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/Frameworks/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/Frameworks/QtCore.framework/Versions/5/Frameworks/libomp.dylib' (no such file), '/Applications/Slicer-5.7.0-20240306.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache))
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
