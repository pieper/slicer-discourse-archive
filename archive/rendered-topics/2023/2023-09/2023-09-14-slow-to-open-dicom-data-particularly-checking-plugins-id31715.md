# Slow to open DICOM data, particularly Checking Plugins

**Topic ID**: 31715
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/slow-to-open-dicom-data-particularly-checking-plugins/31715

---

## Post #1 by @Markb (2023-09-14 15:02 UTC)

<p>Hi. I’m currently using Slicer 5.2.2 to do quite a lot data manipulation using python scripts, and I am not surprised that some of these tasks take a while. However, I am surprised how much slower 5.2.2 is at opening DICOM data compared with 4.11.</p>
<p>I’ve already built the DICOM database, so they are being loaded from that, and not by Add Data or anything. It literally takes 5-10 minutes for Slicer to “check” a variety of plugins, and then a few minutes more to actually load the data. 4.11 used to zoom through the checks within a few seconds, and then load the DICOM data itself in a minute or so.</p>
<p>The only other difference between the systems is 4.11 was running on Ubuntu on a virtual machine on my laptop, and 5.2.2 is running on the same virtual machine but on a server now with twice the RAM and three times the cores. If anything, I would have expected it to be faster just from the increased server power.</p>
<p>I’ve looked at the log messages and nothing obvious jumps out, but I can’t find a way to copy them all and post them in this message. Any suggestions?</p>

---

## Post #2 by @pieper (2023-09-14 18:08 UTC)

<p>Thanks for reporting this.  We want dicom loading to be as fast as possible, but perhaps a regression crept in.  Can you see what examine steps seem to be taking a long time in the progress dialog?  Can you try turning off some of the plugins (options in the lower left of the dicom module) and see if that helps.  It would be good if you could compare the different slicer versions on the same machine with the same data.</p>

---

## Post #3 by @Markb (2023-09-17 20:57 UTC)

<p>Sorry for the delay in getting back to you, it’s been a hectic few days. It seems to sit on Checking DICOMPETSUVPlugin at 27% for quite a while but even after that is sits on quite a few other plugins for a while. I’ve disable all plugins and it takes a while to get through DICOMenhance, ImageSequence etc. but maybe not as slow as the extensions. Unticking all of the plugins in the bottom left doesn’t seem to load the data, with nothing showing in the loaded data window nor viewing windows, although the progress bar doesn’t show either. Interesting, CPU usage actually seems pretty low regardless of which of the tests I was running.</p>
<p>I’ve uploaded a screenshot of the log when opening up a PET/CT/RTSTRUCT dataset with only the native DICOM plugins installed, all other extensions disabled (although I think I need an extension for the RTSTRUCT file when doing this for real). It actually took a couple more minutes than the last entry on the log shown here.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1b551fe5939a5624fd429cf3e8691bc9eecb2c1.png" data-download-href="/uploads/short-url/rDCCYNIqDiWbpIjRZSc4XmjqwVj.png?dl=1" title="slicerlog" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1b551fe5939a5624fd429cf3e8691bc9eecb2c1_2_690x98.png" alt="slicerlog" data-base62-sha1="rDCCYNIqDiWbpIjRZSc4XmjqwVj" width="690" height="98" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1b551fe5939a5624fd429cf3e8691bc9eecb2c1_2_690x98.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1b551fe5939a5624fd429cf3e8691bc9eecb2c1_2_1035x147.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1b551fe5939a5624fd429cf3e8691bc9eecb2c1_2_1380x196.png 2x" data-dominant-color="D6D6D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerlog</span><span class="informations">1382×198 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To compare against the previous version, I’ve just got to rebuild the DICOM database and I’ll leave that running overnight, to report back tomorrow.</p>

---

## Post #4 by @jamesobutler (2023-09-17 21:08 UTC)

<p>As a PET dataset, this report may be what you observed <a class="mention" href="/u/pieper">@pieper</a> and reported at the following issue linked below.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/QIICR/Slicer-PETDICOMExtension/issues/21">
  <header class="source">

      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/issues/21" target="_blank" rel="noopener nofollow ugc">github.com/QIICR/Slicer-PETDICOMExtension</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/issues/21" target="_blank" rel="noopener nofollow ugc">Very slow loading when many studies in the DICOM database</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-08-06" data-time="21:34:29" data-timezone="UTC">09:34PM - 06 Aug 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener nofollow ugc">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I downloaded all the studies from IDC with the PET modality (about 1700 studies)<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> and loaded them into the Slicer dicom database.  I installed the PET DICOM extensions in Slicer 5.0.3-2023-08-03.

I'm able to examine the series and see that the PET SUV Plugin correctly identifies that the PET series and is selected to load, but when I try to load it appears that Slicer is in an infinite loop, or at least something very very slow.

If I export the same study from the database to a directory by itself, and then import that directory into a newly created database the study loads quickly.  I take this to mean that the plugin is looping over all studies in the database or something similarly inefficient.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It appears development on QIICR repos has ceased? From a user perspective it would be nice to be informed in the Slicer extensions index which extensions are actually being maintained or the last time they were updated as a metric for that.</p>

---

## Post #5 by @Markb (2023-09-17 21:52 UTC)

<p>That’s an interesting idea. For comparison, I have around 100 studies, with between 4 and 25 series each (some series are edited duplicates). I’m only loaded the same original data each time though (the RTSTRUCT, the CT and the PET data).</p>
<p>Just to check, I opened a second instance of Slicer and tried to load just the RTSTRUCT and CT, but it didn’t seem to be any quicker. System resources were barely dented, so having both open at the same time hopefully wouldn’t have affected the test too much.</p>
<p>I’ve added a log below for when loading the PET/CT/RTSTRUCT with extensions etc. I’ll be honest, 50 minutes is longer than I expected, I’m sure previously it was 20-30.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6ddbb2f292628cf75c05a1b8260679fd7b44a793.png" data-download-href="/uploads/short-url/fFQKkpt7Z0mn1qOQ19CTJ2wm9Uf.png?dl=1" title="slicerlog" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6ddbb2f292628cf75c05a1b8260679fd7b44a793_2_690x229.png" alt="slicerlog" data-base62-sha1="fFQKkpt7Z0mn1qOQ19CTJ2wm9Uf" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6ddbb2f292628cf75c05a1b8260679fd7b44a793_2_690x229.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6ddbb2f292628cf75c05a1b8260679fd7b44a793_2_1035x343.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6ddbb2f292628cf75c05a1b8260679fd7b44a793_2_1380x458.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerlog</span><span class="informations">1475×491 75.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2023-09-18 02:26 UTC)

<p>How many patients/studies/series are you selecting at once? When you select a lot then some plugins try to make sense of the complete selection as a whole, which may take a long time.</p>
<p>Have you installed some more extensions after you imported a large data set? That can hugely increase the first examination time (checking of how the series can be loaded) because the new extensions may declare new DICOM tags, therefore all the DICOM files must be parsed again.</p>
<p>If you tell us what data set you are working on and what extensions you have installed then we can have a look if some performance regression has crept in.</p>

---

## Post #7 by @Markb (2023-09-18 07:37 UTC)

<p>Just the one study, with three series (RTSTRUCT, CT and PET). There are around 100 studies/patients in the database, all personally anonymised directly from a couple of Siemens PET scanners.</p>
<p>I’m pretty sure I installed the extensions after building the database though, as I forgot I needed some of them when moving from one setup to another. All of the patients have been opened at least once now though, and reopening the same patient doesn’t speed it up</p>
<p>Unfortunately, I left it building the database for 4.11 overnight, but when I’ve come back to the vmachine this morning, I can’t get into it as my ubuntu version has suddenly started prompting for a password and  the expected password isn’t working.</p>

---

## Post #8 by @Markb (2023-09-18 07:54 UTC)

<p>Actually, whilst killing my system trying to build the 4.11 database, I realised that my 5.2 database was actually stored in a networked location, albeit a very fast internal network connection, due to local space constraints on the vmachine. I’ll pump up the partition size and rebuild 5.2, then test and report back.</p>

---

## Post #9 by @jamesobutler (2023-09-18 12:04 UTC)

<p><a class="mention" href="/u/markb">@Markb</a> can you actually test with Slicer 5.4.0? That is the latest stable version of the code. Slicer 5.2.x is technically unsupported now with no future updates planned for it.</p>

---

## Post #10 by @Markb (2023-09-19 07:55 UTC)

<p>Hi James.</p>
<p>I’ve downloaded 5.4 and pointed it at the same database, and it seemed to recognise the patients straightaway. However, when loading the data, it said it couldn’t load the CT data. I haven’t added any of the extensions as yet, I just wanted to see what the raw time “out of the box” was, and as the image below shows, it was only a couple of minutes. Not sure if the non-loading of the CT slowed or sped that up though or whether there is something related that causes 5.2 to keep attempting something etc.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9490cee7159bb185239867e6a0c24a4d328a7cf8.png" data-download-href="/uploads/short-url/lcgUMj9BzpXx2U2Ejfy8J3LOE8E.png?dl=1" title="slicerlog" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9490cee7159bb185239867e6a0c24a4d328a7cf8_2_690x346.png" alt="slicerlog" data-base62-sha1="lcgUMj9BzpXx2U2Ejfy8J3LOE8E" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9490cee7159bb185239867e6a0c24a4d328a7cf8_2_690x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9490cee7159bb185239867e6a0c24a4d328a7cf8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9490cee7159bb185239867e6a0c24a4d328a7cf8.png 2x" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerlog</span><span class="informations">892×448 67.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ll try again now with the extensions added in</p>

---

## Post #11 by @Markb (2023-09-19 08:26 UTC)

<p>Adding the extensions definitely made a difference. Still an issue loading the CT but as the image below shows, nearly 15 minutes on a single step at the beginning</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab80813991d43f611d3b070223ccbf471ac972e0.png" data-download-href="/uploads/short-url/otaXZKOEZYROrLPzUw663g5A4EM.png?dl=1" title="slicerlog" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab80813991d43f611d3b070223ccbf471ac972e0_2_690x347.png" alt="slicerlog" data-base62-sha1="otaXZKOEZYROrLPzUw663g5A4EM" width="690" height="347" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab80813991d43f611d3b070223ccbf471ac972e0_2_690x347.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab80813991d43f611d3b070223ccbf471ac972e0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab80813991d43f611d3b070223ccbf471ac972e0.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerlog</span><span class="informations">895×451 70.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Extensions I have are: DCMQI, PETDICOMExtension, PetSpectAnalysis, SlicerDevelopmentToolbox and SlicerRT (not sure if all are needed anymore to be fair, some might be when I was creating python scripts for automating certain tasks)</p>

---

## Post #12 by @pieper (2023-09-19 20:53 UTC)

<p>In looking at the code I also found another issue that may slow things down:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/QIICR/Slicer-PETDICOMExtension/issues/22">
  <header class="source">

      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/issues/22" target="_blank" rel="noopener">github.com/QIICR/Slicer-PETDICOMExtension</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/issues/22" target="_blank" rel="noopener">PixelData should not be precached</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-19" data-time="20:49:36" data-timezone="UTC">08:49PM - 19 Sep 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The dicom module uses the plugin's `tags` member to know which fields to put int<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">o the TagCache database:

https://github.com/Slicer/Slicer/blob/bc6482c9a4abaabe3f93b0bfee31d5a8a2c4ae97/Modules/Scripted/DICOM/DICOM.py#L176-L185

But the PETSUV plugin includes PixelData in the `tags` member:

https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/DICOMPETSUVPlugin/DICOMPETSUVPlugin.py#L65

This probably leads to a large tag cache and poor performance, although I haven't timed it.

Possibly related to https://github.com/QIICR/Slicer-PETDICOMExtension/issues/21</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I haven’t worked on PET/CT in a while but I plan to in the coming months so I may get to these, or at least add some profiling to narrow down where the time is being spent.  If anyone has a chance to work on it sooner that would be great.</p>

---
