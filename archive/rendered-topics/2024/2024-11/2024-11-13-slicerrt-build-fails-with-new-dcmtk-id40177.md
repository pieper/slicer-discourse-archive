---
topic_id: 40177
title: "Slicerrt Build Fails With New Dcmtk"
date: 2024-11-13
url: https://discourse.slicer.org/t/40177
---

# SlicerRT build fails with new DCMTK

**Topic ID**: 40177
**Date**: 2024-11-13
**URL**: https://discourse.slicer.org/t/slicerrt-build-fails-with-new-dcmtk/40177

---

## Post #1 by @cpinter (2024-11-13 17:16 UTC)

<p>Just posting this quickly in case someone knows this off the top off their head.</p>
<p>I noticed lately that DCMTK probably changed under Slicer. Unfortunately besides some inconveniences (like having to do a clean build of Slicer), there are regressions such as this build error in SlicerRT.</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=3588396" class="onebox" target="_blank" rel="noopener">https://slicer.cdash.org/viewBuildError.php?buildid=3588396</a></p>
<p>Does anyone know what was the main change in DCMTK that causes this and how to fix it? SlicerRT is one of the most used extensions so it would be imperative to solve this before releasing 5.8 if this requires some change in Slicer itself. Thank you!</p>

---

## Post #2 by @jamesobutler (2024-11-13 18:46 UTC)

<p>As it looks to be a Plastimatch build error I would suggest that SlicerRT developers contact Plastimatch (cc <a class="mention" href="/u/gregsharp.geo">@gregsharp.geo</a> ?<a href="https://gitlab.com/gregsharp" class="inline-onebox" rel="noopener nofollow ugc">Gregory C. Sharp · GitLab</a>) about support for recent DCMTK versions. It appears the upstream specifies in its superbuild project to use DCMTK 3.6.2 so it appears there is currently not explicit support for the DCMTK 3.6.8 version that Slicer is using.</p>
<aside class="onebox gitlabblob" data-onebox-src="https://gitlab.com/plastimatch/plastimatch/-/blob/master/SuperBuild/External_DCMTK.cmake?ref_type=heads#L6">
  <header class="source">

      <a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/SuperBuild/External_DCMTK.cmake?ref_type=heads#L6" target="_blank" rel="noopener nofollow ugc">gitlab.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gitlab.com/plastimatch/plastimatch/-/blob/master/SuperBuild/External_DCMTK.cmake?ref_type=heads#L6" target="_blank" rel="noopener nofollow ugc">plastimatch/plastimatch/-/blob/master/SuperBuild/External_DCMTK.cmake?ref_type=heads#L6</a></h4>

  <pre><code class="lang-"></code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However switching SlicerRT to use Plastimatch 1.10.0 (it currently use 1.9.2)  <a href="https://gitlab.com/plastimatch/plastimatch/-/commit/db24480dc1086df3278992d62a86e70d8654cb5d" class="inline-onebox" rel="noopener nofollow ugc">Version 1.10.0 (db24480d) · Commits · plastimatch / plastimatch · GitLab</a> is probably a good starting point as it includes some likely important DCMTK linking fixes. So SlicerRT developers should try that update to keep their extension working well with latest Slicer.</p>

---

## Post #3 by @cpinter (2024-11-13 20:02 UTC)

<p>Yes I agree it is a Plastimatch issue. What I’m wondering about is if this apparent API change is something well-known. Otherwise it needs to be investigated. Good to know the Plastimatch used in SlicerRT is not the latest. I’ll start there. Thanks!</p>

---

## Post #4 by @Mik (2024-11-14 09:35 UTC)

<p>I had such a problem a week ago, but after plastimatch update to the latest release the compilation process was successful. I had to turn-off Qt support in plastimatch.</p>
<p>Slicer commit: 98a05fbee8b7eb553ec2ae439e797415e727a984<br>
Plastimatch commit: 5036f97b213d37a0a07dd232c827fb5f35049ae4</p>

---

## Post #5 by @cpinter (2024-11-14 12:45 UTC)

<p>Thanks <a class="mention" href="/u/mik">@Mik</a>. Did you also have this error before turning off Qt support?<br>
<code>LINK : fatal error LNK1181: cannot open input file 'ofstd.lib'</code></p>
<p>The reason I posted this in the first place is that I had to rebuild all Slicers that I had compiled from scratch because of the same error that I now get when trying to build SlicerRT with the latest Plastimatch. So I assumed that this is a common issue that people are aware of.</p>
<p>What I built exactly with the latest SlicerRT (and got the error above) is <a href="https://github.com/SlicerRt/plastimatch/tree/slicerrt-1.10.0-2024.10.30-5036f97b">this branch</a>, which I just pushed after rebasing the previous branch <code>slicerrt-1.9.3-2022.06.15-77b40bd3</code> on the latest Plastimatch on gitlab (the same hash as what <a class="mention" href="/u/mik">@Mik</a> mentions).</p>
<p>Update: what is strange is that the said file (ofstd.lib) is there (S5R\DCMTK-build\lib\Release\ofstd.lib).</p>

---

## Post #6 by @Mik (2024-11-14 14:56 UTC)

<p>There were link problems between plastimatch and DCMTK, i don’t remember vividly the exact error message, but it was similar.</p>
<p>Everything was done on Linux.</p>
<p>I had to disable Qt support because of plastimatch compilation error of a standalone program called <code>gamma_gui</code> or something like that, i think that issue doesn’t have a connection with linking problem.</p>

---

## Post #7 by @cpinter (2024-11-14 15:18 UTC)

<p>Thanks! Yes it seems unrelated. I’m trying to resolve the link errors one by one by adding <code>${DCMTK_LIBRARIES}</code> to the target libraries of the failing projects, there seems to be some progress (but it’s ugly). I’ll give an update when this is done, there are many projects and I find out what fails one by one.</p>

---

## Post #8 by @Mik (2024-11-14 15:24 UTC)

<p>I’m sorry for the misinformation, i’ve checked everything once again and for some reason i used an old DCMTK version 3.6.6. Now i recompiling both DCMTK and ITK to check plastimatch compilation once again, but i think the linking problem is still there.</p>
<p>Mia Culpa.</p>

---

## Post #9 by @cpinter (2024-11-14 16:03 UTC)

<p>Regarding this attempt (adding <code>${DCMTK_LIBRARIES}</code> into the CMakeLists.txt files of projects that showed the error <code>fatal error LNK1181: cannot open input file 'ofstd.lib'</code>):<br>
I added it to a dozen projects, because it seemed that it fixed the linking of the individual projects where I added them. In the end I reached <code>SlicerRtCommon</code>, and it seems that adding this does not fix that project. I get this when I add it to SlicerRtCommon:</p>
<pre><code class="lang-auto">  Performing build step for 'inner'
  MSBuild version 17.10.4+10fbfbf2e for .NET Framework

    Configuring: AdditionalLauncherSettings.ini
LINK : fatal error LNK1181: cannot open input file 'ofstd.lib' [C:\d\_Extensions\SlicerRT_R\inner-build\SlicerRtCommon\
vtkSlicerRtCommon.vcxproj] [C:\d\_Extensions\SlicerRT_R\inner.vcxproj]
LINK : fatal error LNK1181: cannot open input file 'ofstd.lib' [C:\d\_Extensions\SlicerRT_R\inner-build\DoseVolumeHisto
gram\MRML\vtkSlicerDoseVolumeHistogramModuleMRML.vcxproj] [C:\d\_Extensions\SlicerRT_R\inner.vcxproj]
LINK : fatal error LNK1181: cannot open input file 'ofstd.lib' [C:\d\_Extensions\SlicerRT_R\inner-build\Isodose\MRML\vt
kSlicerIsodoseModuleMRML.vcxproj] [C:\d\_Extensions\SlicerRT_R\inner.vcxproj]
</code></pre>
<p>I have absolutely no idea how to proceed, because the file is there, and don’t know what could be the reason that it is not found. Maybe this specific target is somehow not exposed? I’m not an expert of CMake unfortunately…</p>
<p>Happy to try stuff if someone has an idea!</p>

---

## Post #10 by @PaoloZaffino (2024-11-14 16:11 UTC)

<p>Hi all,<br>
I confirm plastimatch did not compile with the new version of DCMTK, but this was fixed in September (<a href="https://gitlab.com/plastimatch/plastimatch/-/commit/fb3d4cbc8e4f4062cdc30fc001714b60c06dcd00" rel="noopener nofollow ugc">commit 1</a>, <a href="https://gitlab.com/plastimatch/plastimatch/-/commit/ed7722230c3106e99eb5b084e1afc4492527c1bc" rel="noopener nofollow ugc">commit 2</a>).<br>
In the last palstimatch release (1.10.0) support for ITK 5.3 and DCMTK 3.6.8 was added.<br>
I can compile it Ubuntu and Arch Linux now.</p>
<p>Paolo</p>

---

## Post #11 by @Mik (2024-11-14 17:16 UTC)

<p>Plastimatch compiles successfully with ITK-5.4 and DCMTK-3.6.8. Linking errors in SlicerRT are the same.<br>
Typical output:<br>
<code>/usr/bin/ld: can't find -lofstd: Not such file or directory</code>.</p>

---

## Post #12 by @Mik (2024-11-15 11:11 UTC)

<p>I’ve compiled SlicerRT master successfully on Linux!</p>
<p>I had to comment DCMTK libraries in logic of DicomRtImportExport and DicomSroImportExport modules.</p>
<p>SuperBuild is also compiled without problems.</p>

---

## Post #13 by @Mik (2024-11-15 11:52 UTC)

<p><a href="https://github.com/SlicerRt/SlicerRT/pull/259" rel="noopener nofollow ugc">Pull request</a>  in SlicerRT for testing</p>

---

## Post #14 by @cpinter (2024-11-15 14:03 UTC)

<p>Thank you very much! I integrated the PR with some minor changes. I’m doing a clean build as well to make sure it will work on the factory. Good to know it works on Linux too!</p>

---

## Post #15 by @cpinter (2024-11-16 14:58 UTC)

<p>Just confirming that SlicerRT builds again on all platforms!</p>
<p>Thank you for helping!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c382f04ce2efcf6ae77e8fc457521f41685b34b.png" data-download-href="/uploads/short-url/hITzUMmPYbMBvsqgj4mwtFrNfrZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c382f04ce2efcf6ae77e8fc457521f41685b34b_2_690x66.png" alt="image" data-base62-sha1="hITzUMmPYbMBvsqgj4mwtFrNfrZ" width="690" height="66" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c382f04ce2efcf6ae77e8fc457521f41685b34b_2_690x66.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c382f04ce2efcf6ae77e8fc457521f41685b34b_2_1035x99.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c382f04ce2efcf6ae77e8fc457521f41685b34b.png 2x" data-dominant-color="CED0C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1063×102 23.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
