# New frame set table in the DICOM database?

**Topic ID**: 35012
**Date**: 2024-03-22
**URL**: https://discourse.slicer.org/t/new-frame-set-table-in-the-dicom-database/35012

---

## Post #1 by @lassoan (2024-03-22 01:19 UTC)

<p>I’ve come across a serious limitation in our current database structure: the <a href="https://groups.google.com/g/comp.protocols.dicom/c/ewGSfDcodJE">frame set</a> (see also <a href="https://www.dclunie.com/pixelmed/software/javadoc/com/pixelmed/dicom/FrameSet.html">here</a>) level is completely missing. We treat series as displayable set of frames, which is wrong for image modalities such as ultrasound and not always optimal for fluoroscopy and in many other cases. It is common to have dozens of ultrasound acquisitions in a single series that we currently cannot browse. We can switch to advanced mode and browser loadables (results of “Examine” step) but that’s very limited (e.g., no thumbnails) and slow.</p>
<p>I’m wondering if we should add a “FrameSet” table to the database. We would store each loadables item in a table, provide thumbnail and metadata for those and not for each series.</p>
<p>What do you think <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>, <a class="mention" href="/u/cpinter">@cpinter</a>?</p>

---

## Post #2 by @Davide_Punzo (2024-03-22 09:09 UTC)

<p>hei Andras,</p>
<p>for the visual dicom browser I still have to implement the UI for the  advanced/examine capabilities of the default browser (last item in <a href="https://github.com/commontk/CTK/issues/1162#Thumbnailsserieswidgets" class="inline-onebox" rel="noopener nofollow ugc">Roadmap list of issues/enhancements for Visual DICOM Browser · Issue #1162 · commontk/CTK · GitHub</a>).</p>
<p>We can discuss this, but I agree we could implement a similar/enhanced UI of the default browser in the visual one with thumbnails.</p>
<p>Probably for the user knowing the concept of FrameSet is not important, so we could just provide a simple UI with thumbnails of the selected series where each new thumbnails/element comes either from:</p>
<ol>
<li>differences in geometry of the instances, … etc… (i.e. the currrent examine operation)</li>
<li>FrameSet division.</li>
</ol>

---

## Post #3 by @lassoan (2024-03-22 11:52 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="2" data-topic="35012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>We can discuss this, but I agree we could implement a similar/enhanced UI of the default browser in the visual one with thumbnails.</p>
</blockquote>
</aside>
<p>I’m only thinking about improving the visual browser, as I expect that it can replace the old browser in the future.</p>
<aside class="quote no-group" data-username="Davide_Punzo" data-post="2" data-topic="35012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>we could just provide a simple UI with thumbnails of the selected series where each new thumbnails/element comes either from:</p>
</blockquote>
</aside>
<p>Examine step provides the frame sets, so they are not two different things. I would not spend time with the old browser, we can leave it as is (show the list of series and generate framesets on-the-fly).</p>
<p>In the visual browser, the thumbnail list should always show the frameset list to the user, never the series list, so there is no need to ask the user. For this, we probably need a FrameSets table and the visual browser would display records of this table instead of the series table. The table would be populated by running “examine” for each imported (or updated) study automatically. We could store output of all plugins in the framelists table, but by default we would only show the results provided by the plugin with the highest confidence. We could add an option to the right-click menu of the thumbnail to choose outputs from a different plugin.</p>

---

## Post #4 by @pieper (2024-03-22 14:27 UTC)

<p>Yes, I think the browser should expose the logical structure of the acquisition as captured in the dicom data and support previews that make sense for the modality and use case.  I think you should do what is needed for the visual browser.</p>
<p>Longer term we should rethink the database entirely, and define a new API that better refects framesets and other DICOM concepts that aren’t currently well represented.</p>
<p>In my experiments I found that the dicomDatabase can be completely replaced by a DICOMweb client so we should factor the database out from the plugins (which currently treat it as a global singleton).  In <a href="https://github.com/Slicer/Slicer/compare/main...pieper:Slicer:virtualize-database">this branch</a> I made the database an optional argument for the ScalarVolumePlugin, and I think we can go a lot further to clean things up.  This could be a good deliverable for some funding proposal.</p>

---

## Post #5 by @Davide_Punzo (2024-03-22 14:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="35012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In the visual browser, the thumbnail list should always show the frameset list to the user, never the series list, so there is no need to ask the user. For this, we probably need a FrameSets table and the visual browser would display records of this table instead of the series table. The table would be populated by running “examine” for each imported (or updated) study automatically. We could store output of all plugins in the framelists table, but by default we would only show the results provided by the plugin with the highest confidence. We could add an option to the right-click menu of the thumbnail to choose outputs from a different plugin.</p>
</blockquote>
</aside>
<p>I agree this would be the ideal solution.</p>
<p>From dev point of view:</p>
<ol>
<li>
<p>the UI probably will need only minor refactoring (we could simply convert the series widget into a Frame sets one)</p>
</li>
<li>
<p>however for the logic (Examine step, which would be run as soon as we fetch the series and instances metadata), we would need some refactoring and probably move (at least part of) the plugins logic into CTK (C++).</p>
</li>
</ol>

---

## Post #6 by @lassoan (2024-03-22 15:33 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="5" data-topic="35012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>logic (Examine step, which would be run as soon as we fetch the series and instances metadata), we would need some refactoring and probably move (at least part of) the plugins logic into CTK (C++)</p>
</blockquote>
</aside>
<p>Yes, the logic part is the difficult one. Unfortunately, it is not an option to move all the plugin logic to C++ because many people who have the domain knowledge to create plugins will provide it in their language of preference (now mostly Python, but soon also Rust, etc.).</p>
<p>It should not be a big issue, except we need to find a robust and fast way of running these plugins in parallel in the background. Multithreading in Python is rather limited, so we may need to run Python plugins in separate processes.</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="35012">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>dicomDatabase can be completely replaced by a DICOMweb client so we should factor the database out from the plugins</p>
</blockquote>
</aside>
<p>We will have to rework the plugin/database interface anyway to be able to run the plugins in the background. I’m not sure if DICOMweb REST API is optimal or sufficient, as we still need to store additional data, such as framesets. There might be some overhead due to HTTP and fully text-based communication, which might be perceivable when inspecting geometry of large series, such as high-resolution 4D CTs. But the API could be perhaps very similar to DICOMweb so that it would be trivial to use it with a DICOMweb server.</p>

---

## Post #7 by @pieper (2024-03-22 15:44 UTC)

<p>Yes, the database API should not assume DICOMweb, but it also should not assume DIMSE or filesystem either, but rather expose the metadata in a clean and efficient way, possibly pre-cached and possibly fetched on the fly.</p>
<p>Exposing the plugins to the C++ layer should not mean migrating the code to C++, it should mean providing a clean abstract C++ class that can be specialized to use the plugins in whatever language they come in.  Running in threads or processes would be options to explore.</p>

---

## Post #8 by @Davide_Punzo (2024-03-22 16:07 UTC)

<p>btw added this feature request and the post reference in the visual dicom browser roadmap(long term section, <a href="https://github.com/commontk/CTK/issues/1162#long-termENH" class="inline-onebox" rel="noopener nofollow ugc">Roadmap list of issues/enhancements for Visual DICOM Browser · Issue #1162 · commontk/CTK · GitHub</a>)</p>

---

## Post #9 by @lassoan (2024-12-16 21:45 UTC)

<p><a class="mention" href="/u/david_clunie">@David_Clunie</a> gave a very useful information for implementation of framesets. <a href="https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_TF_Vol2.pdf">IHE RAD TF-2 Transactions standard</a> section 4.16.4.2.2.6.2 specifies a logic for determining framesets in a study. While the described logic may have some oversimplifying assumptions, it is good enough as a default implementation (and in the future we may implement plugin infrastructure for special cases).</p>
<blockquote>
<p>Each DICOM image instance is a separate FrameSet, with two exceptions:</p>
<ul>
<li>a Series of only single frame instances comprises a single FrameSet</li>
<li>the combined frames of a Concatenation comprise a single FrameSet (if Concatenations are supported, which they are not required to be)</li>
</ul>
<p>This means that when a Series contains a mixture of single frame and multi-frame images, in order to preserve sequence of images within a Series:</p>
<ul>
<li>each successive single frame image will be a separate FrameSet consisting of one frame</li>
<li>each multi-frame image will be a separate FrameSet (except for combined images of a Concatenation, if supported)</li>
</ul>
<p>Furthermore, there will never be fewer FrameSets than Series (i.e., Series will not be combined).</p>
</blockquote>
<p>The logic is simple enough that it could be possible to implement without a new database table. However, it would probably simplify the implementation if there was a 1-to-1 mapping between database table records and viewer items. Also, having a table would allow saving additional information into the database. For example, we could store how the user chose to load that frameset last time (what DICOM plugin, what interpretation), or we could use that to hide a frameset (instead of actually deleting it, thereby potentially corrupting the image series).</p>
<p>I’ve added an issue to track this feature request:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/8102">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/8102" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/8102" target="_blank" rel="noopener">DICOM visual browser should show framesets instead of series</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-12-16" data-time="21:47:08" data-timezone="UTC">09:47PM - 16 Dec 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">As described in [this discussion](https://discourse.slicer.org/t/new-frame-set-t<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">able-in-the-dicom-database/35012), the DICOM browser should show a thumbnail for each frameset, not for each series.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
