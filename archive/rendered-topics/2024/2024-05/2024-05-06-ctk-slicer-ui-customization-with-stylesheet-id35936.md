---
topic_id: 35936
title: "Ctk Slicer Ui Customization With Stylesheet"
date: 2024-05-06
url: https://discourse.slicer.org/t/35936
---

# CTK/Slicer UI customization with stylesheet

**Topic ID**: 35936
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/ctk-slicer-ui-customization-with-stylesheet/35936

---

## Post #1 by @Davide_Punzo (2024-05-06 08:01 UTC)

<p>Hey <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>I just wanted to bring to your attention this draft PR</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/commontk/CTK/pull/1202">
  <header class="source">

      <a href="https://github.com/commontk/CTK/pull/1202" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/commontk/CTK/pull/1202" target="_blank" rel="noopener nofollow ugc">ENH: Example how to use dynamic properties and stylesheets</a>
      </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>Punzo:qpaletteToStyleSheet</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-05-06" data-time="07:46:38" data-timezone="UTC">07:46AM - 06 May 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
            <img alt="Punzo" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
            Punzo
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 58 additions and 0 deletions">
          <a href="https://github.com/commontk/CTK/pull/1202/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+58</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Bare bones example how to use dynamic properties and stylesheets in CTK to repla<span class="show-more-container"><a href="https://github.com/commontk/CTK/pull/1202" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ce QPalette hard coded colors.
This would allow slicer customizations to replace the colors by simply defining them in the styleSheet.

hey @sjh26, @lassoan @jcfr @pieper @cpinter  I would appreciate a lot if you can provide feedback. Then if you agree on a solution, I can apply the solution to all the CTK classes that uses the QPalette.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Reference:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/commontk/CTK/issues/1162#UIcustomization">
  <header class="source">

      <a href="https://github.com/commontk/CTK/issues/1162#UIcustomization" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/issues/1162#UIcustomization" target="_blank" rel="noopener nofollow ugc">Roadmap list of issues/enhancements for Visual DICOM Browser</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-01-09" data-time="10:12:01" data-timezone="UTC">10:12AM - 09 Jan 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/Punzo" target="_blank" rel="noopener nofollow ugc">
          <img alt="Punzo" src="https://avatars.githubusercontent.com/u/7985338?v=4" class="onebox-avatar-inline" width="20" height="20">
          Punzo
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">RoadMap (items are not listed in priority):

&lt;a href="#long-termENH" id="long-<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">term ENH"&gt;**long-termENH:**&lt;/a&gt;
- [ ]  implementing send in C++ in CTK (i.e. adding ctkDICOMSendJob, ctkDICOMSendWorker and ctkDICOMSend with underlining DIMSE DcmStorageSCU). This would allow to use the background/parallel operations infrastructure for SEND as well.
- [ ] add DICOMweb
- [ ] handle jobs queue in the scheduler by file (so we can restart the jobs/workers at application restart)
- [ ] add data streaming from visual browser series widgets to Slicer volume nodes.
- [ ] add support for DICOM frame set (reference https://discourse.slicer.org/t/new-frame-set-table-in-the-dicom-database/35012)

&lt;a href="#UIcustomization" id="UIcustomization"&gt;**UI customization:**&lt;/a&gt;
- [ ] visual DICOM browser (and in general CTK) uses Qpalette to change colors dynamically. This does not go well when customizing CTK/Slicer by `styleSheet`. Probably we should use the styleSheet approach everywhere. For example, the background yellow warning on filters does not work when applying a custom styleSheet. Discuss with Sam for a good design. Ideally the solution should:
1) use one unique style file containing the stylesheet for all the CTK classes
2) change color of qt widgets in CTK dynamically with the Property Selector, e.g.: https://wiki.qt.io/Dynamic_Properties_and_Stylesheets
3) custom Slicer apps should be able to change the style by simply rewriting and reloading the style file


&lt;a href="#MinorENHs" id="MinorENHs"&gt;**Issues and minor ENH:**&lt;/a&gt;

&lt;a href="#Logic" id="Logic"&gt;**Logic:**&lt;/a&gt;
- [ ] add a writing lock static variable in the ctkDICOMDatabase class
- [ ] smart managing of the inserts and memory when retrieving a series. i.e. we could have a customizable `framesBatchLimit` variable.
- [ ] add infrastructure to set the maximum number of concurrent workers per server (now it is just per type of job).
- [ ] the retry time delay value should be higher and exponential with a factor 2/3 (with some randomness), i.e. each subsequent retry should have a larger delay. Current default parameter is a fixed 100ms (not enough for a server to recover). Instead of using the Maximum number of retries (current default is 3), we should use the maximum waiting time (the one defined in the GUI in the server settings) -&gt; timout warning in the UI (check the string if it is clear).
- [ ] Automatic prefetch of the full series (now the current behaviour) could be disabled and the retrieve could it be done only when the selected series are manually loaded. 
- [ ]  While waiting for download of a complete sequence, we can still do some user actions, but not all. I suspect that it is because we pump the event loop with app-&gt;processEvents(), but that might be unintentional. We might want to call processEvents with flags that disable user interaction, or even better, show a model popup with a "Cancel" button.
- [x] Stopping/Deleting many jobs (&gt;100) makes the scheduler hanging for ~2 sec. This because the deleting is done one job at the time and then a signal is emitted to queue new jobs. In Addition this methods are thread safe by a mutex which is expensive. Probably the best action would be to delete all the jobs togheter in only 1 call.
- [x] The SCU release association (DCTMK) should be protected by a mutex, because the method in DMTCK is not thread safe and in past we had crashes for it. I had also to force the release of the association at cancel operation of worker for query and retrieve. This because the DCTMK cancel operation can fail (but returns always good() == true) and in some cases we can have eternal zombies workers. The release is done in the hanlde overriden methods of SCU.

&lt;a href="#Settings" id="Settings"&gt;**Settings:**&lt;/a&gt;
- [x] servers should be in a "Servers" collapsible section, the same way as "Storage" (instead of the "Servers" label)
- [x] Add debug option to activate the output from DCMTK (global logger to terminal). 
- [x] Style of "Apply changes" and "Discard changes" should be the same as Add/verify/remove host.  
- [x] Verify host: change response string. C-ECHO connection verified/failed.  Add a "Verification" column in the "Servers" table (unknown, in progress, success, failure). C-ECHO should be run in background by the scheduler (need to implement related job and worker classes).
- [x] server settings should be more human readeable in the qt settings file.
- [x] Change in the UI the column names Proxy and Protocol with additional Retrieve (Retrieve Proxy etc....)
- [x] Apply warning yellow background to modified fields.
- [x] MedicalConnection server node, should have the Query/Retrieve/Storage checkboxes to be checked as default.
- [x] After clicking Apply, the row selection should be preserved
- [x] Hide restore defaults button (it can be shown only for testing)
- [x] Verify host should work on the current modified server settings (or it should be disabled until the user apply or discard the changes).
- [x] MedicalConnection server node, should actually *NOT* have the Query/Retrieve/Storage checkboxes to be checked as default.
- [x] verification column should be updated only from jobs which started after clicking the verify button.
- [x] Closing the application while echo workers are running make it crash. steps: run a verify server with wrong parameters and a timeout of 30 sec. The destructor of the scheduler will wait only 10 sec (hardcoded). The destructor has to wait for all jobs closing properly (echo job will not terminate before the server timeout parameter).


&lt;a href="#VisualbrowserUI" id="VisualbrowserUI"&gt;**Visual browser UI:**&lt;/a&gt;
&lt;a href="#Patientselection" id="Patientselection"&gt;**Patient selection:**&lt;/a&gt;
- [x] By default show all local content.
- [x] Display patient name in "Patient information" section (while there are many patient names listed above, it is not that clear which one is actually selected; it is also not possible to select and copy-paste that name). Left-align field names and values (for example, "ID:" label is on the left - which is good; but then the actual ID value is floating somewhere in the middle of the screen).
- [x] Hitting enter in a search field should run the query (same as clicking the search button)
- [x] When hitting the search button, the patient list always jumps to the first patient, which is quite annoying, as I keep clicking it to see if new studies have become available for the current patient on the server. Current patient selection should not be lost if Search button is pressed (if the current patient is still selected by the search criteria).
- [x] Patient selection is lost when showing/hiding the browser in 3D Slicer
- [x] Having a shortcut to browser previous/next patient (Ctrl-tab/Ctrl-shift-tab) would be useful when working with a research PACS (where we are not find/explore data, without necessarily knowing patient name/id).
- [x] study sorting by date, sometimes does not work. Verify the sorting.
- [x] at least happened once: after pressing search, download of series started. Switched to a different patient, hourglass was displayed for a while and then the application crashed.
- [x] When changing patient if there are TCIA [datasets](https://github.com/dnahive/HiveSlicerVNCWidget/releases) imported from local disk and there is the test server enabled (medical connection), the UI gets stuck and there is this message logged many times:
`Failed to find patient with PatientsName= and PatientID=`
- [x] visual dicom browser does not have drop action (neither the old browser). In Slicer dropping a dicom folder will use the python code in DICOM.py and then use the old browser to import. If Slicer is using the new browser should import with the visual one.
- [x] All the DICOM import from local disk were broken for the visual dicom browser when using it in Slicer. The issue was that several methods on the DICOM module UI were using directly the old browser. Refactored to call methods of the class DICOMbrowser.py. Then it is  the DICOMbrowser that take care of calling methods from the two browsers.
- [x] importing multiple folders for the visual dicom browser is broken
- [x] when importing in Slicer this logging should not happen:
```
D: DcmDataset::read() TransferSyntax="Little Endian Explicit"
D: DcmMetaInfo::checkAndReadPreamble() TransferSyntax="Little Endian Explicit"
```
This happens when detailed logging in DICOM settings is checked. It is logging printed by DCMTK. Detailed logging is already as default set to false.

- [x] We need to be able to select the enabled severs on a patient basis.


&lt;a href="#Filtering" id="Filtering"&gt;**Filtering:**&lt;/a&gt;
- [x] when doing a search without filter (i.e. show all local database), if there is nothing in the local database, the yellow warning background fo the filter gets bugged (always on, even if doing a new search)
- [x] Filter at the moment is both query and filter the local database (this could be confusing). Add an advanced menu under the query button to disable the query/retrieve.
- [ ] Filter local database could leave studies or patients empty (these should be filtered out). See also next two issues for more detailed info.
- [ ]  I don't get some updates (study list remains empty) when setting filter criteria to "Everything from last year". I see "ctkDICOMQuery: the number of responses of the query task at patients level surpassed the maximum value of permitted results (i.e. 25)." message in the log - can it be the root cause? Or maybe just that this filter does not filter out patients. It is confusing that some filter boxes filter patients, while others let all patients displayed, even those that don't have matching studies/series/modality/date.
- [ ] The logic behind "Study" and "Series" textboxes in "Patient search" section is not clear. If I type there something then still all the patients are shown, just studies or series list is empty. When the study filter is set then patients that don't have any matching studies should not show up. Similarly, those patients and studies shold not show up that don't have any series that matches the filter criteria.
- [ ] Patients list as tabs in the tab control of the Patient widgets is not optimal. We should use the old widget from the ctkDICOMBrowser (first one, only the patient list). We could have an option to switch between them. 

&lt;a href="#Thumbnailsserieswidgets" id="Thumbnailsserieswidgets"&gt;**Thumbnails &amp;&amp; series widgets:**&lt;/a&gt;
- [x] on right click menu we will need an addittion action: force redownload. (for series and studies)
- [ ] additional feature for force download (add checkable settings, default False): if any series is 3 hours old (also this should be a CTK settings variable), force redownload every time we use a search.
- [ ] additional feature for force download: enable monitoring (right click action) for a time (configurable). If any series or instance in series gets uploaded in PACs, in this case, will be automatically fetched and the UI updated (some UI icons to give the warning that it is updating). For series, we should check also if new instances have been added in the PACs to the series.
- [ ] additonal feature: add a check (when clicking the query/retrieve lense button) to a folder containing dicom files, if there are files import them and clean the folder. Create a lock file in the dicom folder and we put there the PID of the session of the user, when is accessing the DICOM files/deleting them. 
Check also if using a watcher we can automatically do the import.
The local folder should be a "local connection", like a server. So we could add as many we want in the settings and everything will be automatic in the infrastructure (not adding hard coded specil cases, but everything will be independednt), it is just a new "protocol" comunications.
- [x] right click delete name in the UI should be: delete from local database
- [x] text: add transparent and improve shadows. Remove N.frames and put it as the third dimension on the rowXcolumns (e.g. 100x100x5). Elide the series description and put the full text in tooltip.
- [ ] thumbnails are quite low quality, which is visible when the image contains text or simple graphics - if there is an option to use higher-order interpolation and it is not much slower then it would be nice to switch to that
- [ ] rendering for Segmentation DICOM object does not work with the ctk thumbnail class.
- [ ] Selection in series list uses blue background. If the thumbnail image has rectangular shape then the blue text that is overlaid on the thumbnail is not readable (blue text on blue background). Maybe improving the drop shadow would fix it (to make it 4 directions instead of just 1, maybe larger offset).
![image](https://github.com/commontk/CTK/assets/7985338/5d17c1e6-37c5-44c3-a14b-67a084d36dba)
- [x] Wait and load selected series sometimes did not worked and the UI got stuck.
- [ ] loading a series in visual dicom browser does not have the old advanced/examine UI
- [ ] after deselecting there is a white box around thumbnails in dark mode in Slicer
- [ ] thumbnail should not be updated by jobs that started before the last scheduler API call from the series widget. Sometimes old jobs could take more time to be killed than need jobs to run successfully. Then the stopped one should be ignored.


&lt;a href="#Errorreport" id="Errorreport"&gt;**Error report:**&lt;/a&gt;
- [x] Implement Job list status UI. See next two issues for more info.
- [x] Error reporting is inconsistent. Most often I don't see any errors (just nothing shows up), but once an error message came up as a button. But then I could not remove that message. A nice solution would be to have a "Job list" button, which could show an error notification (red or yellow circle) on it when one of the jobs failed. Clicking on it the button would show the job list (it can be a popup or a collapsing section in the GUI) that would show all the jobs (in-progress and completed) along with its status (it can be just simple list, details shown as tooltip or popup; with an option to show all jobs or only in-progress jobs, a button to clear the completed jobs, a button to cancel the selected jobs, and a button to retry the selected jobs). 
- [x] Error message like "bc2343432-234241frfd-2342341s job failed to fetch data" is quite annoying. It should tell something like "Fetching data for patient John Doe [patientid] from server MedicalConnections failed. Response not received for 30 seconds. Click here to see more details." (clicking could open the job list with that task highlighted)
- [ ] we need to stream the DCMTK logging per each job to the Job list UI, this can be implemented by instantiating an Appender with a custom ErrorHandler to the SCU logger: DCM_dcmnetLogger (name: "dcmtk.dcmnet")
- [ ] when loading a series, if it is not supported (or it is supported with an extension), we should fire a popup warning.
- [ ] big warning push button for failed jobs should be removed. We should have warning/error icons at patient/study/series widgets which should refer to the job in some way.
- [ ] then we could use the same icon on patient/study/series widget to know if we are waiting for the query (loading icon) 
- [ ] also a refresh button to refresh the query for patient/study/series widgets (if everything was success, this can be useful to query new changes in the server)
- [ ] clearing jobs push buttons should be outside from filter group box
- [ ] clear completed push button, should also remove the current "cancel" one
- [ ] status: if the user stop the jobs,  status should be "user stopped"
- [ ] status: if the job is stopped because it failed, it should be "attempt failed" (if it will retry it) / "failed" (if it is the last attempt)
- [ ] When a request fails then it leaves 4 entries in the log: 3x failed attempts + 1x final failed attempt. This is too much noise (and if the user wants to retry he would need to pay attention not to retry all 4 entries, only 1). Could you change filtering settings so that the 3 failed attempts are not displayed by default? The simplest would be to only display the 3 failed attempts only if “Show completed” is enabled in filtering settings.
- [x] Jobs and Settings group box should be encapsulated in one
- [x] Having also a splitter between the main patients navigation widget and Jobs/Settings groups would be ideal.
- [ ] clicking a row in the job list should open the corrispettive patient widget in the main navigation widget.
- [ ] Details:1) do not put the separator if only one job is selected 2) separator should be either ----- or ==== (check DCMTK and use a different one) 3) do not put spaces before ":"

&lt;a href="#ctkDICOMVisualBrowserapplication" id="ctkDICOMVisualBrowserapplication"&gt;**ctkDICOMVisualBrowser application:**&lt;/a&gt;
- [x] the folder selector does not reflect the actual DICOM database location (it seems that the button is not updated from application settings at startup)

## Reference PR:
* https://github.com/commontk/CTK/pull/1142
* https://github.com/commontk/CTK/pull/1165
* https://github.com/Slicer/Slicer/pull/7525
* https://github.com/commontk/CTK/pull/1184
* https://github.com/commontk/CTK/pull/1191
* https://github.com/Slicer/Slicer/pull/7676
* https://github.com/commontk/CTK/pull/1201
* https://github.com/commontk/CTK/pull/1202</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<blockquote>
<p>visual DICOM browser (and in general CTK) uses Qpalette to change colors dynamically. This does not go well when customizing CTK/Slicer by <code>styleSheet</code>. Probably we should use the styleSheet approach everywhere. For example, the background yellow warning on filters does not work when applying a custom styleSheet. Discuss with Sam for a good design. Ideally the solution should:</p>
<ol>
<li>use one unique style file containing the stylesheet for all the CTK classes</li>
<li>change color of qt widgets in CTK dynamically with the Property Selector, e.g.: <a href="https://wiki.qt.io/Dynamic_Properties_and_Stylesheets" class="inline-onebox" rel="noopener nofollow ugc">Dynamic Properties and Stylesheets - Qt Wiki</a></li>
<li>custom Slicer apps should be able to change the style by simply rewriting and reloading the style file</li>
</ol>
</blockquote>

---
