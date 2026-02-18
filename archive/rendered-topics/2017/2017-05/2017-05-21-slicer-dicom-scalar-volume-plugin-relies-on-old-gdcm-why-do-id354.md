# Slicer DICOM Scalar volume plugin relies on (old) GDCM: why do we not use DCMTK?

**Topic ID**: 354
**Date**: 2017-05-21
**URL**: https://discourse.slicer.org/t/slicer-dicom-scalar-volume-plugin-relies-on-old-gdcm-why-do-we-not-use-dcmtk/354

---

## Post #1 by @fedorov (2017-05-21 04:30 UTC)

<p>This question came up several times, and I would like to document the answer - why do we rely on GDCM series reader in this code: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/vtkITKArchetypeImageSeriesScalarReader.cxx#L96">https://github.com/Slicer/Slicer/blob/master/Libs/vtkITK/vtkITKArchetypeImageSeriesScalarReader.cxx#L96</a></p>
<p>Arguably, this is one of the most important pieces of Slicer, since absolutely every user wants their DICOM series to be loaded correctly. We should really strive for the scalar volume loader to be very robust!</p>
<p>This example can be used to demonstrate the GDCM reader is the default IO for ImageSeriesReader: <a href="https://github.com/fedorov/itk-gdcm-dcmtk-readers/blob/master/ReadReader.cxx">https://github.com/fedorov/itk-gdcm-dcmtk-readers/blob/master/ReadReader.cxx</a></p>
<p>Arguably, DCMTK is a more widely used, more frequently updated, and stronger project as compared to GDCM. Switching to DCMTK IO is simple. A recent example demonstrates how GDCM is the culprit in failing to parse user data: <a href="https://discourse.slicer.org/t/error-with-dce-mri-loading-in-dicom-browser/327/30">ERROR with DCE MRI loading in DICOM Browser</a>.</p>
<p>Please respond here if you know of a good reason to stick to GDCMImageIO for scalar volumes!</p>

---

## Post #2 by @lassoan (2017-05-21 11:37 UTC)

<p>I don’t know a good reason why GDCM is used and I agree that it would be much better to use DCMTK.</p>
<p>There may be differences in what mechanisms are implemented in GDCM and DCMTK for addressing some inconsistencies/common problems in DICOM images (what fields are used for storing image spacing, dealing with multiframe volumes, etc.), so some regressions are quite likely, but we should be able to address them when they come up. Maybe we should create a stable release before we switch?</p>

---

## Post #3 by @pieper (2017-05-21 17:40 UTC)

<p>It’s purely a legacy thing, and I agree we should use the DCMTK code wherever possible.  I had worked on replacing that GDCM code a couple times, but I realized that it includes a lot of workarounds for special cases that aren’t really documented anywhere.  So as <a class="mention" href="/u/lassoan">@lassoan</a> says we are likely to see regressions on corner cases.  We won’t know how many until we try.</p>
<p>It’s a common issue with DICOM software that debugging is done on data that cannot be shared publically.  To the extent possible I’d like to see us create a comprehensive collection of examples of the data we do support so we can perform regression testing.</p>
<p>Also, we could expose a user option to use the GDCM code as a fallback.</p>

---

## Post #4 by @fedorov (2017-05-21 19:00 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>it includes a lot of workarounds for special cases that aren’t really documented anywhere</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> do you mind putting the pointer to those special cases that are important for reading scalar volumes here for completeness?</p>
<p>I am talking specifically about the scalar volume reader here. The individual files have already been sorted, it has already been confirmed they belong to the same volume, and have consistent spacing by the time that reader is called. I am fine if I am proven naive, but I thought all that reader needs to do is to assemble a volume, no?</p>
<p>As an aside, one level up, in the ArchetypeImageSeriesReader, I see this (8 years old by Xiaodong!) code <a href="https://github.com/Slicer/Slicer/blame/master/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L390">https://github.com/Slicer/Slicer/blame/master/Libs/vtkITK/vtkITKArchetypeImageSeriesReader.cxx#L390</a>, which on the surface is intended to do something similar to what MultiVolumePlugin is doing. Is it exercised anywhere really? Is this something that later was reimplemented in DICOM to NRRD converter, but was never cleaned up from the core?</p>
<p>I am very tempted to abandon that ArchetypeReader altogether for ScalarVolume DICOM plugin, and have a CLI like this to make a volume out of instances that belong to the same series: <a href="https://github.com/fedorov/itk-gdcm-dcmtk-readers/blob/master/ReadDCMTK.cxx" class="inline-onebox">itk-gdcm-dcmtk-readers/ReadDCMTK.cxx at master · fedorov/itk-gdcm-dcmtk-readers · GitHub</a>. I still have not seen specific examples why this would fail.</p>

---

## Post #5 by @pieper (2017-05-21 19:23 UTC)

<p>I’m not arguing with you Andrey, and given that we now have significant<br>
experience on the topic I’m sure that as Andras suggested and I agreed we<br>
should try it out and fix any issues we run into.</p>
<p>You are right that the DICOMScalarVolumePlugin does a lot of consistency<br>
checking in an attempt to be sure the Archetype reader has the best chance<br>
of success.  The reason I still used Archetype reader is so that it can<br>
deal with the encodings, pixel representations, lookup tables, etc.</p>
<p>As I also mentioned, the GDCM-based code does not clearly document which<br>
things, so I can’t give you a direct pointers to everything.  But it<br>
doesn’t take long looking at the ITK GDCM code to find all kinds of<br>
heuristics and workaround for various non-standard data files (I pasted a<br>
few quick examples below).</p>
<p>// There isn’t a definitive way to check for DICOM files;</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L129" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L129" target="_blank" rel="nofollow noopener">Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L129</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="119" style="counter-reset: li-counter 118 ;">
<li>catch( ExceptionObject &amp; )</li>
<li>  {</li>
<li>  return false;</li>
<li>  }</li>
<li>
</li>
<li>//</li>
<li>// sniff for the DICM signature first at 128</li>
<li>// then at zero, and if either place has it then</li>
<li>// ask GDCM to try reading it.</li>
<li>//</li>
<li class="selected">// There isn't a definitive way to check for DICOM files;</li>
<li>// This was actually cribbed from DICOMParser in VTK</li>
<li>bool dicomsig(false);</li>
<li>for(long int off = 128; off &gt;= 0; off -= 128)</li>
<li>  {</li>
<li>  file.seekg(off,std::ios_base::beg);</li>
<li>  if(file.fail() || file.eof())</li>
<li>    {</li>
<li>    return false;</li>
<li>    }</li>
<li>  char buf[5];</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>// In general this should be relatively safe to assume</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L269" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L269" target="_blank" rel="nofollow noopener">Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L269</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="259" style="counter-reset: li-counter 258 ;">
<li>
</li>
<li>
</li>
<li>void GDCMImageIO::InternalReadImageInformation()</li>
<li>{</li>
<li>// ensure file can be opened for reading, before doing any more work</li>
<li>std::ifstream inputFileStream;</li>
<li>// let any exceptions propagate</li>
<li>this-&gt;OpenFileForReading( inputFileStream, m_FileName );</li>
<li>inputFileStream.close();</li>
<li>
</li>
<li class="selected">// In general this should be relatively safe to assume</li>
<li>gdcm::ImageHelper::SetForceRescaleInterceptSlope(true);</li>
<li>
</li>
<li>gdcm::ImageReader reader;</li>
<li>reader.SetFileName( m_FileName.c_str() );</li>
<li>if ( !reader.Read() )</li>
<li>  {</li>
<li>  itkExceptionMacro(&lt;&lt; "Cannot read requested file");</li>
<li>  }</li>
<li>const gdcm::Image &amp;   image = reader.GetImage();</li>
<li>const gdcm::File &amp;    f = reader.GetFile();</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<pre><code>        // Stupid file: CT-MONO2-8-abdo.dcm
        // The spacing is something like that: [0.2\0\0.200000]
        // I would need to throw an expection that VM is not compatible
</code></pre>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L445-L448" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L445-L448" target="_blank" rel="nofollow noopener">Kitware/ITK/blob/master/Modules/IO/GDCM/src/itkGDCMImageIO.cxx#L445-L448</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="445" style="counter-reset: li-counter 444 ;">
<li>// Stupid file: CT-MONO2-8-abdo.dcm</li>
<li>// The spacing is something like that: [0.2\0\0.200000]</li>
<li>// I would need to throw an expection that VM is not compatible</li>
<li>m_El.SetLength( entry.GetVM().GetLength() * entry.GetVR().GetSizeof() );</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2017-05-21 20:03 UTC)

<p>The archetype reader was useful because it allowed a saved scene to refer to existing DICOM files. However, this does not work anymore (since the change that forces the file name to be the same as node name on save).</p>
<p>I think we should also consider David Gobbi’s <a href="https://github.com/dgobbi/vtk-dicom/">vtk-DICOM</a> package. It is the most comprehensive open-soruce DICOM image reading/writing solution - it can read multiframe, cine, multidimensional, compressed, gantry-tilt images and it can also write several image IODs (see more info <a href="http://dgobbi.github.io/vtk-dicom/doc/api/image_reader.html">here</a> and <a href="http://dgobbi.github.io/vtk-dicom/">here</a>). It’s small, clean, simple, supported and continuously improved by David.</p>

---

## Post #7 by @pieper (2017-05-21 20:57 UTC)

<p>vtkDICOM looks good to me as well.</p>
<p>The only downside I can see is that for some applications, like in dcmqi, we might end up duplicating some of the slice-to-volume conversion logic in something closer to native DCMTK without the VTK dependency.</p>

---

## Post #8 by @fedorov (2017-05-21 21:43 UTC)

<p>I think to expedite things and help the user, I should add an alternative scalar volume reader to the multivolume importer plugin, label its output loadable as “DCMTK scalar volume”, and use it in the multivolume either as the primary, or as a fallback when the first-order scalar volume plugin fails.</p>

---

## Post #9 by @pieper (2017-05-21 22:34 UTC)

<p>Sounds very reasonable.</p>
<p>I wonder if you could add a testing mode where both loading mechanisms are used and the user (developer) is notified if they give different results.</p>

---

## Post #10 by @fedorov (2017-05-22 18:32 UTC)

<p>For what it’s worth:</p>
<ul>
<li>this branch replaces GDCM with DCMTK image IO: <a href="https://github.com/fedorov/Slicer/tree/dcmtk-for-scalar-volume">https://github.com/fedorov/Slicer/tree/dcmtk-for-scalar-volume</a> - feel free to test any “corner cases”</li>
<li>the build of the branch above works fine, and I can load the DCE series from <a href="https://discourse.slicer.org/t/error-with-dce-mri-loading-in-dicom-browser/327/30">ERROR with DCE MRI loading in DICOM Browser</a> without problems</li>
<li>almost all of the tests are passing when I tested on linux (from the list below, most of the failing tests failed because I killed Slicer app manually, as the test was running for very long time, often without any indication of what it was doing, some of them keep doing something or showed non-responsive app window after 10 minutes and up)</li>
</ul>
<p>The following tests FAILED:<br>
440 - py_StandaloneEditorWidgetTest (Failed)<br>
601 - py_AtlasTests (Failed)<br>
615 - py_RSNAVisTutorial (Failed)<br>
616 - py_RSNAQuantTutorial (Failed)<br>
622 - py_RSNA2012ProstateDemo (Failed)<br>
623 - py_JRC2013Vis (Failed)<br>
640 - py_LandmarkRegistration (Failed)<br>
Errors while running CTest</p>

---

## Post #11 by @fedorov (2017-05-30 16:08 UTC)

<p>We thought about this a bit more and discussed the implementation plan further with <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>The following issues related to the initially considered approach of introducing a new C++ CLI that would read a DICOM series using DCMTKImageIO have been identified:</p>
<ul>
<li>there will be a need to re-implement the code that determines the scalar type from DICOM - this has to be done before the ITK reader is instantiated!</li>
<li>since in the general case we cannot assume that the directory containing DICOM files does not include files from other series, and there is a limit on the maximum length of a command line in Windows, we would need to work around this by either copying files into a temp location, or communicating the list of files via a file</li>
</ul>
<p>Based on this, and further analysis of the archetype reder code, an alternative approach has been developed:</p>
<ul>
<li>add a flag to ArchetypeScalarVolumeSeriesReader that would allow at runtime to select between GDCM and DCMTK image IO (done, see this commit in a branch referenced earlier: <a href="https://github.com/fedorov/Slicer/commit/505265f8c1c48aea3ae3619e4718b5902170dafb#diff-849c98df12f92abb7d0eb4d31e9f83a5R100">https://github.com/fedorov/Slicer/commit/505265f8c1c48aea3ae3619e4718b5902170dafb#diff-849c98df12f92abb7d0eb4d31e9f83a5R100</a>)</li>
<li>propagate the capability of setting the flag to the layer that is used by DICOMScalarVolumePlugin (currently it is using Volumes logic</li>
<li>keep GDCMImageIO as default to address the concerns expressed earlier about limited experience with DCMTKImageIO in Slicer</li>
<li>in the case when loading an image series as a scalar volume fails in <code>load()</code> of the DICOMScalarVolumePlugin (<code>None</code> returned in this line: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L298">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L298</a>) using GDCMImageIO (this is what was happening in the use case reported by the user that motivated this discussion), retry loading of the series using DCMTKImageIO</li>
</ul>
<p>By using this approach, we will not change any of the behavior in the application or its reliance on GDCM, unless GDCM fails. As such, we will be able to introduce the fix addressing the user need relatively easily, and without waiting for the next release, and without confusing the user by introducing a new type of plugin for scalar volumes.</p>
<p>If you have any concerns or suggestions, please respond. We plan to proceed with the implementation of the proposed approach very soon.</p>

---

## Post #12 by @jcfr (2017-05-30 16:51 UTC)

<blockquote>
<p>done before the ITK reader is instantiated</p>
</blockquote>
<p>May this could be added to ITK … in that case a list of readers could be returned.  <a class="mention" href="/u/thewtex">@thewtex</a> Do you think that make sense or should Slicer team proceed as described ?</p>
<blockquote>
<p>or communicating the list of files via a file</p>
</blockquote>
<p><img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=12" title=":thumbsup:" class="emoji" alt=":thumbsup:" loading="lazy" width="20" height="20"> This is a common practice. Within build system, such files are called <a href="https://msdn.microsoft.com/en-us/library/3te4xt0y.aspx">“response” files</a></p>

---

## Post #13 by @fedorov (2017-05-30 17:07 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> thanks for the response. Do you have any specific concerns with the proposed plan?</p>
<p>I think the issue of improving ITK is an important, but a separate one. I would prefer not to wait for the ITK improvements to be developed, tested and integrated to resolve this specific issue, unless there are really good reasons.</p>

---

## Post #14 by @lassoan (2017-05-30 18:18 UTC)

<p>I like the proposed solution of implementing this by making vtkITKArchetypeImageSeriesScalarReader smarter.</p>
<p>I have just a small comment: it would be a bit nicer to make the DICOM reader selector a string attribute (PreferredDICOMReader, PreferredDICOMIOMethod, PreferredIOClass, …), instead of a Boolean flag (UseGDCMImageIO), as in the future we will probably want to have more options (for example, different modes for using DCMTK or GDCM, auto-select between different readers, use other toolkits) without changing the interface.</p>
<p>It would be useful to have a way to load using DCMTK, even when GDCM returns something. For this, the DICOMScalarVolumePlugin could always offer two loadables for a series: a GDCM-based and a DCMTK-based. By default, if GDCM can interpret the image, the GDCM-based loadable would have higher confidence (so it would be selected by default).</p>

---

## Post #15 by @thewtex (2017-05-30 18:21 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="12" data-topic="354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>done before the ITK reader is instantiated</p>
<p>May this could be added to ITK … in that case a list of readers could be returned.  <a class="mention" href="/u/thewtex">@thewtex</a> Do you think that make sense or should Slicer team proceed as described ?</p>
</blockquote>
</aside>
<aside class="quote no-group">
<blockquote>
<p>I think the issue of improving ITK is an important, but a separate one. I would prefer not to wait for the ITK improvements to be developed, tested and integrated to resolve this specific issue, unless there are really good reasons.</p>
</blockquote>
</aside>
<p>Yes, I think it is a idea to have the DICOM image type code available in ITK without duplication, but it should not be a blocker to move forward. Could an issue please be created here:</p>
<p><a href="https://github.com/KitwareMedical/ITKDICOM" class="inline-onebox" rel="noopener nofollow ugc">GitHub - KitwareMedical/ITKDICOM: Better support for DICOM in ITK.</a></p>
<p>that points to the appropriate code as a reference?</p>
<p>The overall plan sounds good <img src="https://emoji.discourse-cdn.com/twitter/thumbsup.png?v=12" title=":thumbsup:" class="emoji" alt=":thumbsup:" loading="lazy" width="20" height="20"></p>
<p>Worth noting, <a class="mention" href="/u/pieper">@pieper</a> did some digging the other week and found  these DICOM datasets from GDCM:</p>
<p><a href="https://sourceforge.net/p/gdcm/gdcmdata/ci/master/tree/" class="inline-onebox" rel="noopener nofollow ugc">Grassroots DICOM / Gdcmdata / [a0bba5]</a></p>
<p>These are a good resource for regression testing.</p>

---

## Post #16 by @pieper (2017-05-30 20:55 UTC)

<p>Thanks for the review and feedback everyone.</p>
<p>I agree with <span class="mention">@lasson</span> that we should rename the methods for selecting which toolkit to use.  I also like the idea of offering the two methods as alternative loadables so the user can pick which to use in Advanced mode of the DICOM browser.</p>
<p>I’m also thinking it could make sense to write a test that checks out Matheiu’s repository (beefed up with any additional examples) and then runs both readers and compares the results.  I wouldn’t want to make this a Nightly test, but it would make sense to be able to run it when the code changes.</p>

---

## Post #17 by @pieper (2017-05-30 21:12 UTC)

<p>Since Andrey is traveling I went ahead and filed the issue on ITKDICOM:</p>
<p><a href="https://github.com/KitwareMedical/ITKDICOM/issues/7" class="onebox" target="_blank">https://github.com/KitwareMedical/ITKDICOM/issues/7</a></p>

---

## Post #18 by @pieper (2017-06-23 00:35 UTC)

<p>I just merged the topic to address this.</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/734" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/734" target="_blank">Export/Save scene as single directory zip file</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:30:59" data-timezone="UTC">10:30PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:00" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I believe it captures most (all?) of the agreed upon approaches discussed here.</p>
<p>TL;DR People should not notice anything different for now, since GDCM will still be the default reader, but if it fails to load correctly DCMTK will be used as a backup.  There’s now a settings panel for DICOM where people can choose to use DCMTK if they want to experiment.</p>
<p>There is still this known issue outstanding,</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4389" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4389" target="_blank">Some DICOM volumes load with different datatypes between DCMTK and GDCM</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:00:38" data-timezone="UTC">01:00AM - 13 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:00:38" data-timezone="UTC">01:00AM - 13 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>but report if you see other issues.</p>

---

## Post #19 by @ihnorton (2017-06-23 13:41 UTC)

<p>Any deprecation schedule, to avoid the conversation in two years about “can’t remove GDCM <strong><em>OR</em></strong> DCMTK because it might break someone’s volume”? <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>
<p>By the way, when I looked at the original issue that prompted this, I noticed that some slices of the sample data did in fact have thickness set to 0 – so GDCM wasn’t lying. I believe it worked in DCMTK because they don’t look at that tag at all (and then Slicer recalculates the spacing from IPP anyway).</p>

---

## Post #20 by @pieper (2017-06-23 15:42 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="19" data-topic="354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Any deprecation schedule, to avoid the conversation in two years about “can’t remove GDCM OR DCMTK because it might break someone’s volume”? <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>I think this is a long-term issue for the reasons I mentioned above - we don’t have a good way of knowing the impact of  any particular change because we cannot test it with users’ actual data.  For the self test I implemented code to load with both methods and compare the results.  I was thinking to make that a selectable option so that we could start experimenting about when one fails but the other works.</p>
<p>Realistically what we need is a very large regression testing suite of data that somehow defines the data that we do support.  This would allow changes to be made on at least some solid footing.</p>
<p>Unfortunately I don’t think there are any easy answers…</p>

---

## Post #21 by @lassoan (2017-06-23 15:49 UTC)

<p>I think we should deliver a stable release as soon as possible (that’s why I’m slowly chewing through all the open issues in Mantis) and after that we can change the default to DCMTK.</p>
<p>We have to be careful about how to save the user preference for DCMTK/GDCM: we should not save the user preference now to be GDCM, as user preferences are not overwritten when releases are uninstalled/installed. A solution could be to offer Default, DCMTK, and GDCM options to the user. We can then change in the code at any time what toolkit we use if “Default” is selected.</p>

---

## Post #22 by @ihnorton (2017-06-23 16:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="20" data-topic="354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Realistically what we need is a very large regression testing suite</p>
</blockquote>
</aside>
<p>Sure, but the flipside is that we’ll never get regression reports and test data if we never break anything. A hypothetical deprecation schedule might look something like:</p>
<ul>
<li>2 months, GDCM stays default, DCMTK fallback with pop-up request to report</li>
<li>+4 months, switch to DCMTK, GDCM fallback with strongly-worded pop-up request to report</li>
<li>+6 months, DCMTK default, GDCM annoying pop-up over-ride available with desperate plea to report</li>
<li>+1 year, GDCM importer available as an extension (or perhaps via emscripten)</li>
</ul>
<p>Every dependency adds build complication and potential failures, maintenance burden, etc. and we are now carrying two JSON libraries, a bunch of Python packages, etc. too.</p>

---

## Post #23 by @fedorov (2017-06-23 16:08 UTC)

<p>Given the quality of DCMTK ImageIO code, severely limited availability of DICOM test data and DICOM testing functionality in general, and other issues mentioned by <a class="mention" href="/u/pieper">@pieper</a>, I vote against deprecating GDCM IO. It is good to have both options for the situations when one approach does not work.</p>
<aside class="quote no-group" data-username="ihnorton" data-post="22" data-topic="354">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Every dependency adds build complication</p>
</blockquote>
</aside>
<p>Yes, but we introduced 0 new dependencies by the new feature introduced. Both GDCM and DCMTK are already build by Slicer/ITK.</p>

---

## Post #24 by @pieper (2017-06-23 16:25 UTC)

<p>I like the idea from <a class="mention" href="/u/lassoan">@lassoan</a> of adding a ‘Default’ reader option that we can change as needed.  I hadn’t thought of that.</p>
<p>Of course we can also add a version number to future settings keys if we want to override old behavior and ignore the old setting value.</p>
<p>This is where the selection settings are handled now in case we want to change before too many people start using it.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L41-L48" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L41-L48" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L41-L48</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="41" style="counter-reset: li-counter 40 ;">
<li>  self.tags['classUID'] = "0008,0016"</li>
<li>
</li>
<li>@staticmethod</li>
<li>def readerApproaches():</li>
<li>  """Available reader implementations.  First entry is initial default.</li>
<li>  Note: the settings file stores the index of the user's selected reader</li>
<li>  approach, so if new approaches are added the should go at the</li>
<li>  end of the list.</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L466-L468" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L466-L468" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L466-L468</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="466" style="counter-reset: li-counter 465 ;">
<li>uid = slicer.dicomDatabase.fileValue(file,self.tags['instanceUID'])</li>
<li>if uid == "":</li>
<li>  uid = "Unknown"</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
