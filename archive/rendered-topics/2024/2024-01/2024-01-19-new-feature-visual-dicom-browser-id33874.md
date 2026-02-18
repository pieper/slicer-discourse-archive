# New Feature: visual DICOM browser

**Topic ID**: 33874
**Date**: 2024-01-19
**URL**: https://discourse.slicer.org/t/new-feature-visual-dicom-browser/33874

---

## Post #1 by @Davide_Punzo (2024-01-19 15:32 UTC)

<h2><a name="p-105735-description-1" class="anchor" href="#p-105735-description-1" aria-label="Heading link"></a>Description</h2>
<p>The visual DICOM browser provides a new user interface for quick viewing and retrieval of patient images stored on remote DICOM servers. The new tool is optimized for clinical workflows where the focus is on all the images of a single patient - as opposed to the existing DICOM browsing experience, which was more suitable for bringing together images from many patients.</p>
<p>Both server and local content are located at the same place and are visualized by thumbnails. All data is retrieved in the background using classic DIMSE networking (most commonly used protocols in hospitals), in multiple concurrently running threads. The currently supported operations are:</p>
<ul>
<li>Browsing and filtering with thumbnails of content of local DICOM database and multiple remote DICOM servers.</li>
<li>Query/Retrieve data from servers (DIMSE <code>C-FIND</code>, <code>C-GET</code>, <code>C-MOVE</code> SCU). All the operations are done in background and in parallel. Downloaded data is automatically cached in the local DICOM database. A unique feature is the possibility to retrieve images using C-GET protocol (suitable for cases when many Slicer instances are running in docker containers) with a clinical PACS that only supports C-MOVE protocol (most clinical PACS), via a proxy server (such as the free Orthanc).</li>
<li>Import data from local files.</li>
<li>Receive data sent from remote PACS (DIMSE <code>C-STORE</code> SCP).</li>
<li>Send data to remote PACS (DIMSE <code>C-STORE</code> SCU).</li>
<li>Quick browsing of all DICOM metadata and pixel data.</li>
<li>Remove data from local database (not from server).</li>
</ul>
<div class="md-table">
<table>
<thead>
<tr>
<th>Visual DICOM Browser</th>
<th>Settings</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e.png" data-download-href="/uploads/short-url/zsJIMVnPVCUwTBzwM37eg4Y1mNg.png?dl=1" title="ScreenshotVisualDICOMBrowser" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_616x500.png" alt="ScreenshotVisualDICOMBrowser" data-base62-sha1="zsJIMVnPVCUwTBzwM37eg4Y1mNg" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_616x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_924x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_1232x1000.png 2x" data-dominant-color="BCBDBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotVisualDICOMBrowser</span><span class="informations">1577×1280 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2da5998f58e4cf668dabe7f4468f7668ed7dee7.png" data-download-href="/uploads/short-url/u5i53fxMCqJajpLkItqIa8SH8y3.png?dl=1" title="ScreenshotSettings" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2da5998f58e4cf668dabe7f4468f7668ed7dee7_2_690x173.png" alt="ScreenshotSettings" data-base62-sha1="u5i53fxMCqJajpLkItqIa8SH8y3" width="690" height="173" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2da5998f58e4cf668dabe7f4468f7668ed7dee7_2_690x173.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2da5998f58e4cf668dabe7f4468f7668ed7dee7_2_1035x259.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2da5998f58e4cf668dabe7f4468f7668ed7dee7_2_1380x346.png 2x" data-dominant-color="F0F3F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScreenshotSettings</span><span class="informations">1914×481 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
</tr>
</tbody>
</table>
</div><p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0183828f41c36e77c90ec9db178737f6251ad92.mp4">
  </div><p></p>
<h2><a name="p-105735-how-to-use-2" class="anchor" href="#p-105735-how-to-use-2" aria-label="Heading link"></a>How to use</h2>
<p>The new interface is available in the <code>DICOM</code> module. To enable the new browsing experience toggle the <code>Show experimental visual DICOM browser</code> option in the dropdown menu of the <code>Show DICOM database</code> button:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a60b5a8be109f4f5ffeb606e9b9b69d9a9a7e7b1.png" data-download-href="/uploads/short-url/nGTAhO7nKzzhmoGhNAbPS2mrpgB.png?dl=1" title="SlicerActivateVisualDICOMBrowser" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a60b5a8be109f4f5ffeb606e9b9b69d9a9a7e7b1_2_690x249.png" alt="SlicerActivateVisualDICOMBrowser" data-base62-sha1="nGTAhO7nKzzhmoGhNAbPS2mrpgB" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a60b5a8be109f4f5ffeb606e9b9b69d9a9a7e7b1_2_690x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a60b5a8be109f4f5ffeb606e9b9b69d9a9a7e7b1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a60b5a8be109f4f5ffeb606e9b9b69d9a9a7e7b1.png 2x" data-dominant-color="E1E3E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerActivateVisualDICOMBrowser</span><span class="informations">835×302 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-105735-feedback-3" class="anchor" href="#p-105735-feedback-3" aria-label="Heading link"></a>Feedback</h2>
<p>We have tested the widget mostly on Linux and Windows on multiple servers (Orthanc, <a href="http://www.dicomserver.co.uk" rel="noopener nofollow ugc">www.dicomserver.co.uk</a>, and some clinical PACS). It would be great to get feedback how the browser performs in different environments.</p>
<p>Developement is still ongoing, and a comprehensive roadmap is available <a href="https://github.com/commontk/CTK/issues/1162" rel="noopener nofollow ugc">here</a>. We are looking forward to receiving error reports or any comments and suggestions for further improvements.</p>
<h2><a name="p-105735-for-developers-4" class="anchor" href="#p-105735-for-developers-4" aria-label="Heading link"></a>For developers</h2>
<p>Example scripts for accessing the widget logic from Python can be found <a href="https://github.com/commontk/CTK/pull/1165#issue-2078249761" rel="noopener nofollow ugc">here</a></p>
<h2><a name="p-105735-references-5" class="anchor" href="#p-105735-references-5" aria-label="Heading link"></a>References</h2>
<p><a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerVisualDICOMBrowser/" rel="noopener nofollow ugc">PW40 Project</a><br>
<a href="https://github.com/commontk/CTK/pull/1142" rel="noopener nofollow ugc">CTK PR1</a><br>
<a href="https://github.com/commontk/CTK/pull/1165" rel="noopener nofollow ugc">CTK PR2</a><br>
<a href="https://github.com/Slicer/Slicer/pull/7525" rel="noopener nofollow ugc">Slicer PR</a><br>
<a href="https://github.com/commontk/CTK/issues/1162" rel="noopener nofollow ugc">Roadmap</a></p>

---

## Post #2 by @fedorov (2024-01-19 18:40 UTC)

<p>Are there plans to support this interface for DICOMweb accessible servers?</p>
<p>I do not work with DIMSE servers, but would be very interested to try this out with DICOMweb!</p>

---

## Post #3 by @Davide_Punzo (2024-01-19 18:56 UTC)

<p>Hey Andrey. It’s one of our long term enh in the <a href="https://github.com/commontk/CTK/issues/1162" rel="noopener nofollow ugc">roadmap</a>. I agree that it would be critical to have also dicomweb. The issue is that the new widget is fully written in C++ at ctk level and there is no clear supported C++ dicomweb library. We will also explore other ways (e.g. python libraries )</p>
<p>During the project week (see <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/SlicerVisualDICOMBrowser/" class="inline-onebox" rel="noopener nofollow ugc">Project Description | NA-MIC Project Weeks</a>)  we plan to get feedback and discuss future plans and probably dicomweb will one of the main discussion item.</p>
<p>Ultimately it will depend on people interest and funds <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2024-01-20 13:16 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="3" data-topic="33874">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>The issue is that the new widget is fully written in C++ at ctk level and there is no clear supported C++ dicomweb library</p>
</blockquote>
</aside>
<p>We could move MITK’s  C++ DICOMweb implementation to CTK and use it in this browser. Classic DIMSE support was prioritized over DICOMweb implementation because DICOMweb is still very rarely supported by hospital PACS. If there is a confirmed need then it would not be huge work to add DICOMweb, because the framework is designed to support multiple protocols (DIMSE, DICOMweb, and custom PACS/cloud provider protocols).</p>

---

## Post #5 by @Davide_Punzo (2024-01-20 13:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="33874">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If there is a confirmed need then it would not be huge work to add DICOMweb, because the framework is designed to support multiple protocols (DIMSE, DICOMweb, and custom PACS/cloud provider protocols).</p>
</blockquote>
</aside>
<p>yes, indeed the framework is already set for it, we just need the C++ dicomweb library.</p>

---

## Post #6 by @drvarunagarwal (2024-01-26 10:42 UTC)

<p>hi,</p>
<p>I am using slicer 5.7.0</p>
<p>I am not getting this option or dropdown menu in show DICOM database button</p>
<p>Please advise how to enable</p>
<p>thanks</p>

---

## Post #7 by @Davide_Punzo (2024-01-26 12:10 UTC)

<p>Hello <a class="mention" href="/u/drvarunagarwal">@drvarunagarwal</a>,</p>
<p>I appreciate your prompt report, and I am sorry for the inconvenience.  <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>  and <a class="mention" href="/u/jcfr">@jcfr</a> are currently addressing a minor issue with the Windows binaries. For further details, please refer to the ongoing discussion at: <a href="https://discourse.slicer.org/t/slicer-build-error-on-windows-on-the-dashboard/33967" class="inline-onebox">Slicer build error on Windows on the dashboard</a></p>
<p>Meanwhile, the MacOS and Linux binaries are fully functional – I’ve personally tested the Linux version, and it works seamlessly. If you’re using either of those systems, feel free to download and use them. We anticipate resolving the Windows binary concern by early next week. Thank you for your understanding.</p>
<p>Furthermore, in today Slicer preview (Linux and MacOS) we have released a refreshed UI that comes with a dedicated Jobs list:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f97cc983707c251dcd385e7ca937ee94824e79d.mp4">
  </div><p></p>
<p>Please, let us know if you have any comments or suggestions.</p>
<p>Thanks again for your time</p>

---

## Post #8 by @Davide_Punzo (2024-01-26 12:21 UTC)

<p><a class="mention" href="/u/drvarunagarwal">@drvarunagarwal</a></p>
<p>on the other hand if you download the current 5.7.0 windows binaries</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d01333b1f98ed7cb34f1178ee269be5f8fcca82.png" alt="image" data-base62-sha1="48ApUmVX5JLl3TpbrsIa6v6oiwW" width="226" height="96"></p>
<p>you do have access to the visual DICOM browser (previous week version):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91f5d16c01423893bf1a18d07d302fcb26cae244.png" data-download-href="/uploads/short-url/kPdTy687NQRHLsXfqriWbDpKsbG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f5d16c01423893bf1a18d07d302fcb26cae244_2_690x279.png" alt="image" data-base62-sha1="kPdTy687NQRHLsXfqriWbDpKsbG" width="690" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f5d16c01423893bf1a18d07d302fcb26cae244_2_690x279.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f5d16c01423893bf1a18d07d302fcb26cae244_2_1035x418.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91f5d16c01423893bf1a18d07d302fcb26cae244_2_1380x558.png 2x" data-dominant-color="F9F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3438×1394 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please be sure to  have the binaries from 2024-01-22.<br>
It could be worth to wait anyway few more days to try the latest version.</p>

---

## Post #9 by @Davide_Punzo (2024-01-26 17:54 UTC)

<p><a class="mention" href="/u/drvarunagarwal">@drvarunagarwal</a> the current Windows version</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56169f001f210998cc99a06e6076af0b625b3d88.png" alt="image" data-base62-sha1="chzwJn50MYoZjKzHhYfCl0EwTRm" width="279" height="122"></p>
<p>includes the latest version of the visual DICOM browser.</p>

---

## Post #10 by @fedorov (2024-01-26 17:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="33874">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If there is a confirmed need then it would not be huge work to add DICOMweb</p>
</blockquote>
</aside>
<p>Just to be clear, I don’t want to say there is a confirmed need from my side. It’s just that I do not work with any DIMSE servers, and I am not going to set one up for the sake of testing this. With DICOMweb support, testing of this functionality would become trivial using, for example, Google Healthcare API.</p>

---

## Post #11 by @lassoan (2024-01-26 18:06 UTC)

<p>The browser can be tested with local DICOM files - thumbnail display, searching and filtering, etc.</p>
<p>To try the PACS connection features, you can use the <a href="https://www.medicalconnections.co.uk/kb/Public-DICOM-Server">Medical Connections DICOM test server</a>. This server is preconfigured in Slicer by default, you just need to enable Query/Retrieve for this server in the Settings section.</p>

---

## Post #12 by @fedorov (2024-01-26 18:10 UTC)

<p>In my view, one of the interesting testing scenarios would be to try it out against a database that has a non-trivial amount of heterogeneous data across the range of manufacturers/modalities etc. That’s not something that can be done using local files or that test server. But could be done with the DICOMweb server we have in IDC that has &gt;50TB of data. Or with a smaller subset of that.</p>
<p>In any case, if you guys want to test it using such a subset using other means, I am happy to answer any questions related to selecting and downloading data from IDC!</p>

---

## Post #13 by @Davide_Punzo (2024-01-26 18:18 UTC)

<p>It would be indeed very nice to test with IDC (i.e. check perfomances with very large datasets).</p>
<p>let’s talk at the project week. In general, I agree that having a DICOMweb C++ library would definitely make this new infrastructure more flexible.</p>

---

## Post #14 by @lassoan (2024-01-26 18:28 UTC)

<p>This new DICOM browser is optimized for clinical workflows (you focus on a single patient and access complete history of that patient) and not for exploring research databases (where you don’t know what patient you want to see and often want to aggregate data over multiple patients). For example, in the visual DICOM browser there is very limited set of patient search&amp;filter features, because the clinician knows the one single patient he is dealing with; while in a research database browser a big part is to find relevant set of cases.</p>
<p>But thank you <a class="mention" href="/u/fedorov">@fedorov</a> for the offer. As <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> wrote, large databases can be useful for performance testing and optimization. After DICOMweb support is added we could also see if the browser can be adapted to work conveniently for non-clinical/non-patient-oriented workflows on research databases.</p>

---

## Post #15 by @fedorov (2025-10-09 15:53 UTC)

<p>As a quick followup, we relatively recently opened public access to IDC data (now over 90TB) via <a href="https://www.dicomstandard.org/using/dicomweb">DICOMweb</a> interface. Access details are documented in this article: <a href="https://learn.canceridc.dev/data/organization-of-data/dicom-stores" class="inline-onebox">DICOM stores | IDC User Guide</a>.</p>

---

## Post #16 by @Davide_Punzo (2025-10-09 16:33 UTC)

<p>That’s great! Unfortunately we still didn’t implement dicomweb capabilities into CTK. I don’t think it’s too complicated to implement in C++, but we had always other priorities in last year. Full roadmap is at:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/commontk/CTK/issues/1230">
  <header class="source">

      <a href="https://github.com/commontk/CTK/issues/1230" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/issues/1230" target="_blank" rel="noopener nofollow ugc">Visual DICOM roadmap 2025</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2025-04-23" data-time="10:09:21" data-timezone="UTC">10:09AM - 23 Apr 25 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
          Punzo
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- [ ] **1.** Implement sending in C++ in CTK (i.e., adding `ctkDICOMSendJob`, `c<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">tkDICOMSendWorker`, and `ctkDICOMSend` with underlying DIMSE `DcmStorageSCU`). This would allow the use of the background/parallel operations infrastructure for SEND as well.
- [ ] **2.** Add DICOMweb support.
- [ ] **3.** Handle the jobs queue in the scheduler by file (so we can restart the jobs/workers at application restart).
- [ ] **4.** Add data streaming from visual browser series widgets to Slicer volume nodes.
- [ ] **5.** Add support for DICOM frame set ([GitHub issue](https://github.com/Slicer/Slicer/issues/8102), [discussion](https://discourse.slicer.org/t/new-frame-set-table-in-the-dicom-database/35012)).
- [ ] **6.** Test loading of series with an extra “localizer” slice ([discussion link 1](https://discourse.slicer.org/t/problems-during-dicom-import/9060/31?u=lassoan), [discussion link 2](https://github.com/Slicer/Slicer/blob/1f7bb55e84af9eaa8993ea3dd305413f83680721/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L290-L314)). Test also Fluoro acquisitions.
- [ ] **7.** Restore the old advanced/examine UI for loading a series in the visual DICOM browser.
- [ ] **8.** Improve the visual DICOM browser (and CTK in general) to use `styleSheet` instead of `QPalette` for dynamic color changes.  Ideally, the solution should:
  1. Use one unique style file containing the stylesheet for all CTK classes.
  2. Change the color of Qt widgets in CTK dynamically with the Property Selector (e.g., [Dynamic Properties and Stylesheets](https://wiki.qt.io/Dynamic_Properties_and_Stylesheets)).
  3. Allow custom Slicer apps to change the style by simply rewriting and reloading the style file.
- [ ] **9.** Add a writing lock static variable in the `ctkDICOMDatabase` class.
- [ ] **10.** Implement smart management of inserts and memory when retrieving a series (e.g., add a customizable `framesBatchLimit` variable).
- [ ] **11.** Add infrastructure to set the maximum number of concurrent workers per server (currently, it is per job type).
- [ ] **12.** Update retry time delay to be exponential with a factor of 2/3 (with some randomness). The current default of 100ms is insufficient for server recovery. Replace the maximum number of retries (default: 3) with a maximum waiting time (defined in the GUI server settings). Add a timeout warning in the UI and ensure the string is clear.
- [ ] **13.** Allow disabling automatic prefetch of the full series (current behavior). If the option is active, retrieval of all frames should occur only when selected series are manually loaded.
- [ ] **14.** Replace the Patients list as tabs in the tab control of the Patient widgets with the old widget from the `ctkDICOMBrowser` (first one, only the patient list). Add an option to switch between them.
- [ ] **15.** Improve UI clarity regarding querying PACS servers vs. filtering the local database.
- [ ] **16.** Address UI performance issues when importing a large number of patients (&gt;500, &gt;5000 series).
- [ ] **17.** Add a button to enable full-screen mode in the visual DICOM browser.
- [ ] **18.** Apply thumbnail size settings changes without requiring a restart.
- [ ] **19.** Add a feature for force download of series/study:
  - Add a checkable setting (default: False). If any study is 3 hours old (based on DICOM study date), force redownload every time a query is performed (not for local search).
  - Enable monitoring (right-click action) for a configurable time. Automatically fetch and update the UI if any series or instances in a series are uploaded to PACS. Add UI icons to indicate updates. For series, check if new instances have been added to the PACS.
- [ ] **20.** Add a feature to check a folder containing DICOM files when clicking the query/retrieve lens button. If files are present, import them and clean the folder. Create a lock file in the DICOM folder with the PID of the session accessing/deleting the files. Investigate using a watcher for automatic import. Treat the local folder as a "local connection" (like a server) to allow adding multiple folders in settings. Ensure the infrastructure is protocol-independent.
- [ ] **21.** Fix rendering for Segmentation DICOM objects in the `ctkThumbnail` class.
- [ ] **22.** Add an option in settings to order series in the study widget by modality.
- [ ] **23.** Automatically load the source volume when loading a segmentation.
- [ ] **24.** Show a popup warning when loading a series that is unsupported (or supported with an extension).


References: 

- old roadmap: https://github.com/commontk/CTK/issues/1162</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I am currently focusing on point (14-16) → UI refactoring and perfomances.</p>

---
