# DICOM information table with no complete information

**Topic ID**: 15250
**Date**: 2020-12-28
**URL**: https://discourse.slicer.org/t/dicom-information-table-with-no-complete-information/15250

---

## Post #1 by @Ash_Alarfaj (2020-12-28 16:10 UTC)

<p>Problem report for Slicer 4.11.20200930 win-amd64: [in dicom the older versions showed a better table with series date  ] I can not control the table width, no series date<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5961d686392828012f34e3cb8a45e6f18aba1a05.png" data-download-href="/uploads/short-url/cKI6VI3gjD7s7HjeY9nc1xHHaGV.png?dl=1" title="Screenshot  dicom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5961d686392828012f34e3cb8a45e6f18aba1a05_2_690x463.png" alt="Screenshot  dicom" data-base62-sha1="cKI6VI3gjD7s7HjeY9nc1xHHaGV" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5961d686392828012f34e3cb8a45e6f18aba1a05_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/5961d686392828012f34e3cb8a45e6f18aba1a05_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5961d686392828012f34e3cb8a45e6f18aba1a05.png 2x" data-dominant-color="EBF0F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot  dicom</span><span class="informations">1377×925 29.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-12-28 16:30 UTC)

<p>You can now control what fields you want to show in the DICOM browser, what order, format, sorting, and width. This also means that if open an old database then it might be possible that column setup is taken from there, which is not ideal (has the problem you described). I would recommend to create a new DICOM database and import your data sets again. It should just take a few minutes. Let us know if you encounter any problems or need hp with customizing the columns.</p>

---

## Post #3 by @Ash_Alarfaj (2020-12-28 17:32 UTC)

<p>Hi Andras</p>
<p>the problem still exists, I think there is a bug, I am happy to continue my work in slicer 10.2. as Dicom table looks like this, also I could control the table columns width. I am using windows version slicer10.2</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8260e1502ad5cfcfed5cd26a557d43f5e47ebea.png" data-download-href="/uploads/short-url/qh3nZMOpTnge7wZ5CsNLFFX833k.png?dl=1" title="dicom10.2.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8260e1502ad5cfcfed5cd26a557d43f5e47ebea_2_690x388.png" alt="dicom10.2.png" data-base62-sha1="qh3nZMOpTnge7wZ5CsNLFFX833k" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8260e1502ad5cfcfed5cd26a557d43f5e47ebea_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8260e1502ad5cfcfed5cd26a557d43f5e47ebea_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b8260e1502ad5cfcfed5cd26a557d43f5e47ebea_2_1380x776.png 2x" data-dominant-color="F1F2F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dicom10.2.png</span><span class="informations">1920×1080 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-12-28 18:00 UTC)

<p>Do not use Slicer-4.10.2. The DICOM browser in Slicer-4.11.20209030 is vastly superior.</p>
<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="1" data-topic="15250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>I can not control the table width</p>
</blockquote>
</aside>
<p>You can. Drag-and-drop the <em>right</em> side of any wide column. By default these are the manually resizable columns (the others are either very short, so there is no need for manual size adjustment; or very long and so it is set to use the maximum remaining space):</p>
<ul>
<li>Patient: Patient ID, Last Study Date, Date added</li>
<li>Study: Study ID, Date added</li>
<li>Series: Date added</li>
</ul>
<p>Column resize is not enabled by default for other columns because it should not be necessary (there is one auto-fit column that takes up the unused space). If you want to try if you prefer manual resizing then copy-paste this into the Python console, for example for series description:</p>
<pre data-code-wrap="python"><code class="lang-python">dicomBrowser = slicer.modules.dicom.widgetRepresentation().self().browserWidget.dicomBrowser
dicomDatabase = dicomBrowser.database()
dicomDatabase.setFormatForField('Series', 'SeriesDescription', '{"resizeMode":"interactive"}')
</code></pre>
<p>Series Date is intentionally hidden by default:</p>
<ul>
<li>It is a type 3 (optional) field, often not set</li>
<li>Study date is a type 2 (required) field, it is already shown by default in Study table</li>
<li>Series table is already crowded with several new, very informative fields (Size, Count, Date added), therefore adding more fields would make leave less space for Series description</li>
</ul>
<p>Anyway, you can customize all the columns to make it fit your workflow. For example, run this to show the series date column:</p>
<pre data-code-wrap="python"><code class="lang-python">dicomBrowser = slicer.modules.dicom.widgetRepresentation().self().browserWidget.dicomBrowser
dicomDatabase = dicomBrowser.database()
dicomDatabase.setVisibilityForField('Series', 'SeriesDate', True)
</code></pre>
<p>Column visualization preferences are stored in the DICOM database, therefore you need to set it only once. Also if you use a separate DICOM database for each project you work on, you can use a different column layout for each. You can find many more examples of how to customize columns in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_table_columns_in_DICOM_browser">script repository</a>.</p>

---

## Post #5 by @fedorov (2025-10-09 15:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="15250">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Column resize is not enabled by default for other columns because it should not be necessary (there is one auto-fit column that takes up the unused space).</p>
</blockquote>
</aside>
<p>I ran into the same issue, many years ago, and here we are - 5 years later, and fortunately I remembered this strange UI trick to help <a class="mention" href="/u/rkikinis">@rkikinis</a> who was confused the same way as me and as <a class="mention" href="/u/ash_alarfaj">@Ash_Alarfaj</a> (and also by another user in this thread <a href="https://discourse.slicer.org/t/new-dicom-browser-is-ready/8819/13" class="inline-onebox">New DICOM browser is ready - #13 by lassoan</a>)… Sorry, but this is not a good UI design.</p>

---

## Post #6 by @lassoan (2025-10-09 15:57 UTC)

<p>This is standard spreadsheet/table editing behavior, but I agree that it is not intuitive. A better behavior would be to make the field shorter, fixed-size, and more readable (e.g., “just now”, “5 minutes ago”, “2 hours ago”, etc.) but that would require some design changes in CTK (what we display would not be the same as the value in the database). I would not invest time into this now, as <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> will make the patient list in the reworked visual DICOM browser much better than this.</p>

---

## Post #7 by @fedorov (2025-10-09 16:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="15250">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would not invest time into this now, as <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> will make the patient list in the reworked visual DICOM browser much better than this.</p>
</blockquote>
</aside>
<p>Sounds reasonable. What is the recommended mechanism to communicate feedback about Visual DICOM Browser? Is there a single place/document?</p>
<p>We did look into it today with <a class="mention" href="/u/rkikinis">@rkikinis</a> as well, and definitely there’s feedback to communicate…</p>

---

## Post #8 by @Davide_Punzo (2025-10-09 16:43 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> here it is the current To Do roadmap:</p>
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

<p>You can use the same issue to provide feedback, it would be very welcome!</p>
<p>At the same time, I am currently working on a full refactoring of the UI. The previous widget-based implementation had several limitations both in UI design and perfomances. I am switching into a model/view/delegate design which solves the perfomances issues for large datasets and it will also allow me to fully customize the UI (for example the patient tab was really not optimal).</p>
<p>As soon as I have the new implementation (probably in few weeks) I will create a PR in CTK/Slicer and it will be very nice indeed to receive feedback.</p>
<p>dev branch is <a href="https://github.com/Punzo/CTK/commits/visualDICOMBrowserUIRefactor/" class="inline-onebox" rel="noopener nofollow ugc">Commits · Punzo/CTK · GitHub</a></p>
<p>and this is the UML diagram:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/231d040ea8fcf7bb41ff7b682175e30f70f07d25.jpeg" data-download-href="/uploads/short-url/50CSpCXhaLIsg0lbN3pBzJUSSIR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/231d040ea8fcf7bb41ff7b682175e30f70f07d25_2_690x231.jpeg" alt="image" data-base62-sha1="50CSpCXhaLIsg0lbN3pBzJUSSIR" width="690" height="231" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/231d040ea8fcf7bb41ff7b682175e30f70f07d25_2_690x231.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/231d040ea8fcf7bb41ff7b682175e30f70f07d25_2_1035x346.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/231d040ea8fcf7bb41ff7b682175e30f70f07d25_2_1380x462.jpeg 2x" data-dominant-color="E1EBEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×643 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The UI at series and study levels will not change too much (but the PR will improve on a lot of small things), while at patient level will change. I will share screenshots asap.</p>

---
