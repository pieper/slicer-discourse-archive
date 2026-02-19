---
topic_id: 6214
title: "Slicerrt Does Not Build Due To Missing Itk Remote Module"
date: 2019-03-19
url: https://discourse.slicer.org/t/6214
---

# SlicerRT does not build due to missing ITK remote module

**Topic ID**: 6214
**Date**: 2019-03-19
**URL**: https://discourse.slicer.org/t/slicerrt-does-not-build-due-to-missing-itk-remote-module/6214

---

## Post #1 by @cpinter (2019-03-19 21:25 UTC)

<p>SlicerRT does not build for a few days, since ITK was upgraded to version 5. The dashboard currently shows a trivial Plastimatch configuration error (saying that only ITK 3 and 4 are supported),the bigger problem is with an ITK remote that apparently has been removed woth this change. The error I get once bypassing the configuration problem is this:</p>
<p><code>3&gt;LINK : fatal error LNK1104: cannot open file 'ITKBioCell.lib' [C:\d\_Extensions\SlicerRT_D\inner-build\PlmBspline\plastimatch_slicer_bsplineLib.vcxproj]</code></p>
<p>I found that I can include this missing remote with a CMake variable, for which I made a branch:</p>
<p><a href="https://github.com/cpinter/Slicer/commit/d67b9911ad20546f556bc914adb6e2f2f83ed21b" class="onebox" target="_blank" rel="noopener">https://github.com/cpinter/Slicer/commit/d67b9911ad20546f556bc914adb6e2f2f83ed21b</a></p>
<p>However, it does not help. When I build ITK like this, there is no apparent binary file created from the BioCell module (moved btw from Modules/Segmentation to Modules/Remote).</p>
<p>Has anyone encountered the same issue? Does anyone have any ideas how this could be fixed? Thanks!</p>

---

## Post #2 by @phcerdan (2019-03-19 21:52 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>If I enable BioCell in ITK, I can see the library <code>libitkBioCell-5.0.a</code> in both, the build and install tree:</p>
<p>build tree:</p>
<pre><code class="lang-bash">╭─ buildITK/ 
╰─ find . | grep BioCell 
./Utilities/Doxygen/Modules/BioCell.dox
./lib/libitkBioCell-5.0.a
./lib/cmake/ITK/Modules/BioCell.cmake
./Modules/Remote/BioCell
./Modules/Remote/BioCell/src
./Modules/Remote/BioCell/src/CMakeFiles
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir/itkBioGene.cxx.o
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir/itkBioGenome.cxx.o
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir/Labels.json
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir/itkBioGeneNetwork.cxx.o
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir/itkBioCellularAggregateBase.cxx.o
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir/itkBioCellBase.cxx.o
./Modules/Remote/BioCell/src/CMakeFiles/BioCell.dir/Labels.txt
./Modules/Remote/BioCell/src/cmake_install.cmake
./Modules/Remote/BioCell/ITKKWStyleFiles.txt
./Modules/Remote/BioCell/CMakeFiles
./Modules/Remote/BioCell/CMakeFiles/BioCell.cmake
./Modules/Remote/BioCell/cmake_install.cmake
./Modules/Core/Common/BioCellExport.h

</code></pre>
<p>install tree:</p>
<pre><code class="lang-bash">╭─ /tmp/ITK_INSTALL 
╰─ find . | grep BioCell
./include/ITK-5.0/BioCellExport.h
./include/ITK-5.0/itkBioCellularAggregate.hxx
./include/ITK-5.0/itkBioCellularAggregateBase.h
./include/ITK-5.0/itkBioCellBase.h
./include/ITK-5.0/itkBioCell.h
./include/ITK-5.0/itkBioCell.hxx
./include/ITK-5.0/itkBioCellularAggregate.h
./lib/libitkBioCell-5.0.a
./lib/cmake/ITK/Modules/BioCell.cmake
</code></pre>

---

## Post #3 by @phcerdan (2019-03-19 21:55 UTC)

<p>Maybe we need to explicitly add it as a COMPONENT in the <code>find_package(ITK ...)</code></p>
<p>For example here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/322fb8552dd71d6f61b92a89cad4e8aecc102f11/Libs/vtkITK/CMakeLists.txt#L31-L47" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/322fb8552dd71d6f61b92a89cad4e8aecc102f11/Libs/vtkITK/CMakeLists.txt#L31-L47" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/322fb8552dd71d6f61b92a89cad4e8aecc102f11/Libs/vtkITK/CMakeLists.txt#L31-L47</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="31" style="counter-reset: li-counter 30 ;">
<li>set(${PROJECT_NAME}_ITK_COMPONENTS</li>
<li>  ITKAnisotropicSmoothing</li>
<li>  ITKCommon</li>
<li>  ITKConnectedComponents</li>
<li>  ITKDistanceMap</li>
<li>  ITKIOGDCM</li>
<li>  ITKIOGE</li>
<li>  ITKIOImageBase</li>
<li>  ITKImageCompose</li>
<li>  ITKImageFilterBase</li>
<li>  ITKImageFunction</li>
<li>  ITKImageGrid</li>
<li>  ITKLabelMap</li>
<li>  ITKPath</li>
<li>  ITKRegionGrowing</li>
<li>  ITKThresholding</li>
<li>  ITKVTK</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Add</p>
<pre><code class="lang-auto">BioCell
</code></pre>

---

## Post #4 by @cpinter (2019-03-20 14:11 UTC)

<p>Thanks a lot! I’ll try to do that</p>

---

## Post #5 by @cpinter (2019-03-20 20:02 UTC)

<p>I checked the lib directory again, and found an ‘ITKBioCell-5.0.lib’. The reason it was not found was that the project wanted to find an ‘ITKBioCell.lib’. I’ll work with <a class="mention" href="/u/gcsharp">@gcsharp</a> to fix the Plastimatch build within SlicerRT, and then probably issue a PR to include this remote.<br>
Thanks!</p>

---

## Post #6 by @cpinter (2019-03-21 14:08 UTC)

<p>Unfortunately there are multiple other errors too when building Plastimatch with ITKv5.</p>
<p>I wish some more testing had been done before making the switch, at least trying to build the most downloaded extensions. Now we have to scrape to have a working SlicerRT, which is by far the most downloaded extension. I already got emails about why it is not available. This is an emergency for us that I think would have been avoidable.</p>
<p>For others struggling with the same thing, here is the ITK 5 migration guide: <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ITK5MigrationGuide.md" rel="nofollow noopener">https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ITK5MigrationGuide.md</a></p>

---

## Post #7 by @lassoan (2019-03-21 14:58 UTC)

<p>Nightly Slicer will be unstable for a while due to many major changes that we are planning to do (Python3…). Can your users stay on the latest stable version?</p>

---

## Post #8 by @cpinter (2019-03-21 15:03 UTC)

<p>That’s what I told them. There are not a lot of changes in SlicerRT so they don’t lose much. But we might lose users who try the nightly and they don’t find what they want.</p>

---

## Post #9 by @jcfr (2019-05-10 23:29 UTC)

<p>3 posts were split to a new topic: <a href="/t/improve-description-of-nightly-build-on-download-slicer-org/6754">Improve description of nightly build on download.slicer.org</a></p>

---

## Post #11 by @cpinter (2019-03-21 15:28 UTC)

<p>After taking a better look, these errors, although there are many, do not seem hard to fix. At least for us what took the long time was to investigate what broke exactly and to find the time to start the fixes (deadlines etc). Doing the fixes should be now easy, and can be expected in a day or two.</p>
<p>I don’t think it is needed to revert the change unless there are multiple other extensions that rely heavily on ITK as much as SlicerRT (due to Plastimatch mainly).</p>

---

## Post #12 by @jcfr (2019-03-21 15:39 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="11" data-topic="6214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>long time was to investigate what broke exactly and to find the time to start the fixes</p>
</blockquote>
</aside>
<p>Based on your finding and implemented fixes, could you add entry to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Transition_from_ITK4_to_ITK5" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/MigrationGuide - Slicer Wiki</a></p>

---

## Post #14 by @jcfr (2019-05-10 23:30 UTC)

<p>A post was split to a new topic: <a href="/t/streamlining-maintenance-of-download-slicer-org/6755">Streamlining maintenance of download.slicer.org</a></p>

---

## Post #15 by @cpinter (2019-03-21 16:18 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="12" data-topic="6214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Based on your finding and implemented fixes, could you add entry</p>
</blockquote>
</aside>
<p>Some of the things are specific to Plastimatch (e.g. I don’t think anyone else uses BioCell), and I find that ITK migration guide is pretty good. Since there is a link already to the full migration guide I think it is enough.</p>

---

## Post #16 by @fedorov (2019-03-22 15:44 UTC)

<p>I just saw this <a href="https://discourse.itk.org/t/itk-4-13-2-has-been-released/1696">post about release of ITK 4.13.2</a>, which made me quite confused about the discussion in this thread. Quoting that post,</p>
<blockquote>
<p>The next feature pre-release for ITK 5, ITK 5 Release Candidate 2, is anticipated in <a href="https://github.com/InsightSoftwareConsortium/ITK/milestone/4">a few weeks</a></p>
</blockquote>
<p>If ITK 5 is not yet released, we only have release candidate 1, why is Slicer switching to ITK 5 now?</p>

---

## Post #17 by @pieper (2019-03-22 16:01 UTC)

<p>Part of the motivation was that <a class="mention" href="/u/phcerdan">@phcerdan</a> was available to do the troubleshooting for the needed C++ changes.  Also this has been <a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap" rel="nofollow noopener">on the roadmap for a long time</a> to upgrade all the dependencies and we planned that the nightly would be undergoing a lot of slicer5 changes (python3 is coming soon too) and that was accepted since we have a 4.10.1 already and plans for a 4.10.2 soon for people who aren’t ready to change.  I think it’s fine that we are a bit ahead of the game on ITK.  I doubt it’ll change much between RC and release.</p>

---

## Post #18 by @fedorov (2019-03-22 16:16 UTC)

<p>I think C++ changes is different from upgrading to a dependency that is in a pre-release stage. I did not find ITK 5 upgrade in the roadmap, maybe I missed it. Maybe it all makes sense to the developers closely involved, but for someone a bit on the outside, switch to a prerelease of a key dependency looks strange.</p>

---

## Post #19 by @pieper (2019-03-22 16:31 UTC)

<p>Personally I don’t think it’s strange at all that the pre-release version of Slicer would be using the almost released version of ITK.  You are right that the roadmap does not specifically callout ITK5, but it makes it clear that disruptive changes are coming…</p>

---

## Post #20 by @phcerdan (2019-03-22 16:33 UTC)

<p>Hi <a class="mention" href="/u/fedorov">@fedorov</a>, I updated the wiki with the steps taken on the transition. <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Transition_from_ITK4_to_ITK5" rel="nofollow noopener">ITKv4-&gt;ITKv5</a> and the <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ITK5MigrationGuide.md" rel="nofollow noopener">ITKv5 Migration Guide</a></p>
<p>Upgrading external modules should be a matter of upgrading to ITKv5 new threads,<br>
if the ThreadedGenerateData makes no use of <code>threadId</code> replacing:</p>
<pre><code class="lang-cpp">void ThreadedGenerateData( const OutputRegionType&amp; threadRegion, ThreadIdType threadId )
</code></pre>
<pre><code class="lang-cpp">void DynamicThreadedGenerateData( const OutputRegionType&amp; threadRegion )
</code></pre>
<p>will do.</p>
<p>In other cases, where <code>threadId</code> is involved, the ITK migration guide has examples, but to just use the ITKv4 threading system add to the ITK class constructor:</p>
<pre><code class="lang-cpp">this-&gt;DynamicMultiThreadingOff();
</code></pre>
<p>And replace</p>
<pre><code class="lang-auto">  #include &lt;itkMultiThreader.h&gt;

  itk::MultiThreader::Pointer ProcessingThreader;
</code></pre>
<p>with:</p>
<pre><code class="lang-cpp">  #include &lt;itkPlatformMultiThreader.h&gt;

  itk::PlatformMultiThreader::Pointer ProcessingThreader;
</code></pre>
<p>that will probably solve 99% of the problems upgrading to ITKv5.</p>
<p>I am sorry the upgrade forced external plugins to catch up…</p>

---

## Post #21 by @cpinter (2019-03-22 18:20 UTC)

<p>I went through the extensions on the latest nightly dashboard that did not build. These are the extensions that fail to build due to ITK and the failure seems to be related to version 5 (and not some older issue like itkFactoryRegistration):</p>
<ul>
<li>ABC</li>
<li>DSCMRIAnalysis</li>
<li>DTI-Reg</li>
<li>DTIAtlasBuilder</li>
<li>DTIProcess</li>
<li>IASEM</li>
<li>PET-IndiC</li>
<li>PETTumorSegmentation</li>
<li>PkModeling</li>
<li>ResampleDTIlogEuclidean</li>
<li>SkullStripper</li>
<li>SlicerElastix</li>
<li>SlicerVMTK</li>
<li>SPHARM</li>
<li>VirtualFractureReconstruction (also failed before for different reasons)</li>
</ul>
<p>All of these issues are related to these few things:</p>
<ul>
<li>Changed constants such as ITK_THREAD_RETURN_TYPE</li>
<li>The abovementioned multi-threading changes</li>
<li>Changed vnl functions (e.g. vnl_math_isinf or vnl_math_abs)</li>
<li>Deprecated vcl functions (e.g. vcl_cstdio.h or vcl_vector)</li>
<li>Changed image initialization ( conversion from ‘int’ to ‘const itk::SmartPointer&lt;itk::Image&lt;float, 3&gt; &gt;’ is ambiguous) - I haven’t met this one when fixing SlicerRT but I think this should be new as well</li>
</ul>
<p>I volunteer fixing SlicerElastix as I’m planning to work on it regarding the node references I’m adding to all registration modules.</p>

---

## Post #22 by @pieper (2019-03-22 18:37 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a>!  You probably know this, but <a class="mention" href="/u/lassoan">@lassoan</a> checked the elastix repo and they were actively porting to itk5 so maybe it’s just a matter of changing the superbuild hash.</p>

---

## Post #23 by @fedorov (2019-03-22 21:24 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="21" data-topic="6214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I went through the extensions on the latest nightly dashboard that did not build. These are the extensions that fail to build due to ITK and the failure seems to be related to version 5 (and not some older issue like itkFactoryRegistration):</p>
<ul>
<li>DSCMRIAnalysis</li>
<li>PET-IndiC</li>
<li>PETTumorSegmentation</li>
<li>[…]</li>
</ul>
</blockquote>
</aside>
<p><a class="mention" href="/u/chribaue">@chribaue</a> <a class="mention" href="/u/abeers">@abeers</a> FYI</p>

---

## Post #24 by @cpinter (2019-03-25 12:41 UTC)

<p>Just an update that I issued a <a href="https://github.com/SuperElastix/elastix/pull/128" rel="nofollow noopener">PR</a> to Elastix to fix the remaining build errors. Once this is integrated I’ll update the hash.</p>

---

## Post #25 by @lassoan (2019-03-25 15:44 UTC)

<p>This is great, thank you! Until they integrate the fix, you can fork the Elastix repository and use that fork for nightly builds. It would allow us to start testing Elastix build on all operating systems.</p>

---

## Post #26 by @pieper (2019-03-29 23:57 UTC)

<p>Looks like there’s a small conflict between <a class="mention" href="/u/cpinter">@cpinter</a>’s patch and the one <span class="mention">@N-Dekker</span> did.  If it doesn’t get resolved in a few days then yes, doing temporary Slicer-specific elastix fork would be a good idea.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SuperElastix/elastix/pull/128">
  <header class="source">

      <a href="https://github.com/SuperElastix/elastix/pull/128" target="_blank" rel="noopener">github.com/SuperElastix/elastix</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/SuperElastix/elastix/pull/128" target="_blank" rel="noopener">COMP: Fix ITK5 build issues</a>
      </h4>

    <div class="branches">
      <code>SuperElastix:develop</code> ← <code>cpinter:fix-itk5-build</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2019-03-22" data-time="19:41:51" data-timezone="UTC">07:41PM - 22 Mar 19 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="1 commits changed 12 files with 60 additions and 0 deletions">
          <a href="https://github.com/SuperElastix/elastix/pull/128/files" target="_blank" rel="noopener">
            <span class="added">+60</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">There were a few simple things that prevented from Elastic to build with ITK5. T<span class="show-more-container"><a href="https://github.com/SuperElastix/elastix/pull/128" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">his commit fixes these, preserving former ITK version compatibility with preprocessor ifs.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #27 by @cpinter (2019-03-31 22:36 UTC)

<p>Just returned from travelling. I’ll take care of this tomorrow. Thanks for the patience</p>

---

## Post #28 by @cpinter (2019-04-01 13:22 UTC)

<p>This pull request fixes the build issues (only tested on Windows) and adds node references from the transform to the inputs:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/lassoan/SlicerElastix/pull/14">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerElastix/pull/14" target="_blank" rel="noopener">github.com/lassoan/SlicerElastix</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/lassoan/SlicerElastix/pull/14" target="_blank" rel="noopener">Fix ITK5 build + Add node references</a>
      </h4>

    <div class="branches">
      <code>lassoan:master</code> ← <code>cpinter:add-node-references</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2019-04-01" data-time="13:22:03" data-timezone="UTC">01:22PM - 01 Apr 19 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="cpinter" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="2 commits changed 2 files with 5 additions and 3 deletions">
          <a href="https://github.com/lassoan/SlicerElastix/pull/14/files" target="_blank" rel="noopener">
            <span class="added">+5</span>
            <span class="removed">-3</span>
          </a>
        </div>
      </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
