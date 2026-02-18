# DICOM database update is requested after new Slicer version, but appears to be impossible

**Topic ID**: 35821
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/dicom-database-update-is-requested-after-new-slicer-version-but-appears-to-be-impossible/35821

---

## Post #1 by @fedorov (2024-04-29 21:49 UTC)

<p>I installed the latest nightly, and experienced this situation where DICOM Browser would request me to update the database, but trying to perform the update operation does not appear to have any effect.</p>
<p>Fortunately for me, I did not have a need to keep the database, and just created a new one, which showed up empty. After adding one study to that new database, my prior content re-appeared.</p>
<p>I do not know if this is expected behavior, and I could not find similar posts.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38b4d92fb010f7ce17487a80825f0cc1e5234b6d.gif" alt="2024-04-29_17-42-48" data-base62-sha1="85EcF1vBSKOTdt2j1LGdxO7oAfb" width="690" height="350" class="animated"></p>

---

## Post #2 by @pieper (2024-04-29 21:56 UTC)

<p>That sounds like a regression.  <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> <a class="mention" href="/u/lassoan">@lassoan</a> maybe related to the visual browser?</p>

---

## Post #3 by @lassoan (2024-04-29 22:08 UTC)

<p>Until <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> can check this, the easiest is to create a new database.</p>

---

## Post #4 by @Davide_Punzo (2024-04-29 22:36 UTC)

<p>Definitely it can be a regression from my last PR, thanks for reporting <a class="mention" href="/u/fedorov">@fedorov</a> !!<br>
Unfortunately the bug was not flagged either by the automated and manual tests. I would be curious to see if the database update works by using the new browser in your case. I clearly remember testing manually the feature, but I’m not sure that I tested it on both browsers.</p>
<p>Anyway, in any case, I’ll fix it asap, but I’m currently in vacation and I’ll be back on Monday (and I’ll make it a priority).</p>

---

## Post #5 by @lassoan (2024-04-30 02:04 UTC)

<p>Im wondering if we should keep offering this feature. It works by reimporting the DICOM files, which was OK when the database was just a cache of DICOM tags. However, the database now contains information that cannot be derived from the DICOM files (where was it retrieved from). So, we would need to improve the update process to preserve all these information; or not do it anymore (but automatically create a new empty database whenever the schema changes).</p>

---

## Post #6 by @pieper (2024-04-30 11:35 UTC)

<p>I don’t like the idea of users losing their databases.</p>
<p>Schema changes should be very rare and they shouldn’t cause problems for users who don’t use new features.  Maybe these extra fields should be stored separately if they are still subject to change.</p>

---

## Post #7 by @Davide_Punzo (2024-04-30 15:09 UTC)

<p>The new field for the allowed/denied connections should not be an issue. For databases with the old schema when updated those fields would be simply empty and then the visual browser would use the server settings as default.</p>
<p>On the long term not sure what is the way to go. I generally agree with you, but at the same time losing the database at schema change would not be ideal as Steve pointed out</p>

---

## Post #8 by @pieper (2024-04-30 19:10 UTC)

<p>Thanks for working on this <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> and <a class="mention" href="/u/lassoan">@lassoan</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>On <a class="mention" href="/u/fedorov">@fedorov</a> 's original report, is there another bug that prevents him from updating the schema?  Not clear to me why this would be in a loop when the schema update feature used to work.</p>

---

## Post #9 by @Davide_Punzo (2024-04-30 22:26 UTC)

<p>Not sure, it should work (at least on the visual DICOM browser I know its working). Andrey also wrote that after adding a new study, the previous content re appeared. So probably the update was done successfully, but then something went wrong (maybe some update signals are broken).</p>
<p>On Monday I will investigate the issue on the default browser and I will let you know!</p>

---

## Post #10 by @Davide_Punzo (2024-04-30 22:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="35821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>So, we would need to improve the update process to preserve all these information;</p>
</blockquote>
</aside>
<p>Ah yes this would be nice to implement</p>

---

## Post #11 by @Davide_Punzo (2024-05-06 08:30 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> I tried to reproduce this issue, but I could not.<br>
Specifically I have tried to update with latest Slicer a database created with Slicer-5.6.2-linux-amd64, i.e. DICOM database from version 0.7.0 to 0.8.1</p>
<p>Here a video:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c679837445f9bddae819b8e3fdfd193789acedb1.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e02ab65acaa86aa36fb0eec52326fc7e1ce8c42e.jpeg">
  </div><p></p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> which OS are you using? <a class="mention" href="/u/pieper">@pieper</a> could you please try to reproduce this on MacOS? and <a class="mention" href="/u/lassoan">@lassoan</a> could you try Windows as well, please?</p>
<p>we have also an automated test for this: <a href="https://github.com/commontk/CTK/blob/master/Libs/DICOM/Core/Testing/Cpp/ctkDICOMDatabaseTest3.cpp" class="inline-onebox" rel="noopener nofollow ugc">CTK/Libs/DICOM/Core/Testing/Cpp/ctkDICOMDatabaseTest3.cpp at master · commontk/CTK · GitHub</a></p>
<p>but the CTK CI is run on linux.</p>

---

## Post #12 by @cpinter (2024-05-06 08:49 UTC)

<p>I did an update of a medium sized (~35 patients) database with the versions you mention yesterday on Windows (Slicer 5.7 from March 28), and it worked. The displayed name column content did not show during the update, but did do at the end.</p>
<p>I remember adding a ticket or commenting on one recently related to this (after doing some debugging, which showed a problem related with the displayed field generators - btw I implemented those back in the day), but can’t find it in CTK or Slicer. In any case, just letting know that the update worked for me too.</p>

---

## Post #13 by @Davide_Punzo (2024-05-06 09:10 UTC)

<blockquote>
<p>I did an update of a medium sized (~35 patients) database with the versions you mention yesterday on Windows (Slicer 5.7 from March 28), and it worked. The displayed name column content did not show during the update, but did do at the end.</p>
</blockquote>
<p>ok perfect thanks for testing and let me know <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<blockquote>
<p>I remember adding a ticket or commenting on one recently related to this (after doing some debugging, which showed a problem related with the displayed field generators - btw I implemented those back in the day), but can’t find it in CTK or Slicer. In any case, just letting know that the update worked for me too.</p>
</blockquote>
<p>ok if you find again the issue, please ping me, I will try to have a look!</p>

---

## Post #14 by @pieper (2024-05-06 10:59 UTC)

<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> it looks like the <code>Count</code> column is empty after the update.  Can you test if this is a side-effect of updating the database or is it something that happens if you start with a fresh database (i.e. is the count populated in a new database).</p>

---

## Post #15 by @fedorov (2024-05-06 15:03 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="11" data-topic="35821">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> which OS are you using?</p>
</blockquote>
</aside>
<p>I am on macOS Sonoma 14.4.</p>

---

## Post #16 by @Davide_Punzo (2024-05-07 09:27 UTC)

<blockquote>
<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> it looks like the <code>Count</code> column is empty after the update. Can you test if this is a side-effect of updating the database or is it something that happens if you start with a fresh database (i.e. is the count populated in a new database).</p>
</blockquote>
<p>it is a general bug. I have investigated it and the issue is that:</p>
<ol>
<li>in dcdeftag.h we have this definition:<br>
<code> #define DCM_SeriesInstanceUID                    DcmTagKey(0x0020, 0x000e)</code></li>
<li>While in the metadata of that specific DICOM in my video the seriesIstanceUID tag is <code>"0020,000E"</code></li>
<li>this create the issue in ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule::getDisplayedFieldsForInstance:<br>
<a href="https://github.com/commontk/CTK/blob/7ed1da357b9e7e2462b4b764882612484c6fa051/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp#L67" class="inline-onebox" rel="noopener nofollow ugc">CTK/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp at 7ed1da357b9e7e2462b4b764882612484c6fa051 · commontk/CTK · GitHub</a></li>
</ol>
<p>because the return of <code>cachedTagsForInstance[dicomTagToString(DCM_SeriesInstanceUID)]</code> is an empty string (because <code>dicomTagToString(DCM_SeriesInstanceUID)</code> return “0020,000e” instead of “0020,000E”) and this creates issues when updating the tables.</p>
<p>I am not sure if this is a new regression, but I will check out differences in the CTK commits after Slicer version 5.6.2 and see if I can find where the regression happened.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> not sure what is the best way to fix the issue. Maybe we should fix the dicoms at loading/fetching time to have lowercase in the tags, instead of putting a lot of <code>if</code> exceptions everytime we use <code>dicomTagToString</code> to check lowercase vs uppercase</p>

---

## Post #17 by @Davide_Punzo (2024-05-07 09:32 UTC)

<blockquote>
<p>I am on macOS Sonoma 14.4.</p>
</blockquote>
<p>ok, thanks. <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/pieper">@pieper</a> would be possible, when you have time, to perfom the same test that I did in <a href="https://discourse.slicer.org/t/dicom-database-update-is-requested-after-new-slicer-version-but-appears-to-be-impossible/35821/11" class="inline-onebox">DICOM database update is requested after new Slicer version, but appears to be impossible - #11 by Davide_Punzo</a> on MacOS?</p>
<p>the idea would be to understand if it an issue at OS level (i.e. performing the same test I did on linux) or if it is something related to the database that Andrey tried to update (size, type of DICOM, version of the previous schema, etc…).</p>
<p>Finally, Andrey do you still have a copy of the database before updating it? and is it something that you can share?</p>

---

## Post #18 by @Davide_Punzo (2024-05-07 09:59 UTC)

<aside class="quote no-group quote-modified" data-username="Davide_Punzo" data-post="16" data-topic="35821" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<blockquote>
<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> it looks like the <code>Count</code> column is empty after the update. Can you test if this is a side-effect of updating the database or is it something that happens if you start with a fresh database (i.e. is the count populated in a new database).</p>
</blockquote>
<p>it is a general bug. I have investigated it and the issue is that:</p>
<ol>
<li>in dcdeftag.h we have this definition:<br>
<code> #define DCM_SeriesInstanceUID                    DcmTagKey(0x0020, 0x000e)</code></li>
<li>While in the metadata of that specific DICOM in my video the seriesIstanceUID tag is <code>"0020,000E"</code></li>
<li>this create the issue in ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule::getDisplayedFieldsForInstance:<br>
<a href="https://github.com/commontk/CTK/blob/7ed1da357b9e7e2462b4b764882612484c6fa051/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp#L67" rel="noopener nofollow ugc">CTK/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorSeriesImageCountRule.cpp at 7ed1da357b9e7e2462b4b764882612484c6fa051 · commontk/CTK · GitHub</a></li>
</ol>
<p>because the return of <code>cachedTagsForInstance[dicomTagToString(DCM_SeriesInstanceUID)]</code> is an empty string (because <code>dicomTagToString(DCM_SeriesInstanceUID)</code> return “0020,000e” instead of “0020,000E”) and this creates issues when updating the tables.</p>
<p>I am not sure if this is a new regression, but I will check out differences in the CTK commits after Slicer version 5.6.2 and see if I can find where the regression happened.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> not sure what is the best way to fix the issue. Maybe we should fix the dicoms at loading/fetching time to have lowercase in the tags, instead of putting a lot of <code>if</code> exceptions everytime we use <code>dicomTagToString</code> to check lowercase vs uppercase</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> I think the issue is this commit:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/commontk/CTK/commit/84187713304e4ed5a457ee9758de1af4a22d8dbd">
  <header class="source">

      <a href="https://github.com/commontk/CTK/commit/84187713304e4ed5a457ee9758de1af4a22d8dbd" target="_blank" rel="noopener nofollow ugc">github.com/commontk/CTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/commit/84187713304e4ed5a457ee9758de1af4a22d8dbd" target="_blank" rel="noopener nofollow ugc">ENH: Update DICOM Database with URL Support and Tag Cache Optimization</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-12-13" data-time="15:57:11" data-timezone="UTC">03:57PM - 13 Dec 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener nofollow ugc">
          <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="changed 4 files with 133 additions and 37 deletions">
        <a href="https://github.com/commontk/CTK/commit/84187713304e4ed5a457ee9758de1af4a22d8dbd" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+133</span>
          <span class="removed">-37</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This generalizes the ctkDICOMDatabase code to ease hard-coded restrictions about<span class="show-more-container"><a href="https://github.com/commontk/CTK/commit/84187713304e4ed5a457ee9758de1af4a22d8dbd" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">
DICOM files always being on disk. Now the schema includes a `URL` field of the
SQLite database so certain file-specific operations are only performed on filePaths
while URL are handled independently. Entries in the `Images` table of the database
may now have either a `URL` or a `fileName` or both and new accessors are provided
to get `URL`s at the series and instance level.

Schema version is updated from version `0.7.0` to `0.8.0`.

Also this contains a fix to the `ctkDICOMTagCache` so that tags are always stored
internally as uppercase hex, so a string like "0010,000d" will always be turned
into "0010,000D" for storage in the database. Both forms can be used to query
tags. This avoids the situation where some cache entries were duplicated because
different code used either upper or lower case to refer to the same tag. Using
only upper case should improve storage use and improve performance by avoiding
unneeded cache misses.

Co-authored-by: Andras Lasso &lt;lasso@queensu.ca&gt;
Co-authored-by: Davide Punzo &lt;punzodavide@hotmail.it&gt; 
Co-authored-by: Jean-Christophe Fillion-Robin &lt;jchris.fillionr@kitware.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I am not sure 100%, it could be a mix of things, but my investigation points to that. This because the count display works only up to Slicer version 5.6.2 which uses the dicom schema 0.7.0, i.e just before the linked commit which modifies the lower/upper case tags stuff too.</p>
<p>Adding .toUpper() in <a href="https://github.com/commontk/CTK/blob/7ed1da357b9e7e2462b4b764882612484c6fa051/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorAbstractRule.h#L119" class="inline-onebox" rel="noopener nofollow ugc">CTK/Libs/DICOM/Core/ctkDICOMDisplayedFieldGeneratorAbstractRule.h at 7ed1da357b9e7e2462b4b764882612484c6fa051 · commontk/CTK · GitHub</a> :</p>
<pre><code class="lang-auto">
/// Utility function to convert a DICOM tag enum to string
  static QString dicomTagToString(const DcmTagKey&amp; tag)
  {
    return QString("%1,%2").arg(tag.getGroup(),4,16,QLatin1Char('0')).arg(tag.getElement(),4,16,QLatin1Char('0')).toUpper();
  }
</code></pre>
<p>fix the issue, I have created a PR in CTK (<a href="https://github.com/commontk/CTK/pull/1203" class="inline-onebox" rel="noopener nofollow ugc">BUG: Convert lower case dicom tags by Punzo · Pull Request #1203 · commontk/CTK · GitHub</a>). But I am not sure if we need to apply the fix in any another part of CTK</p>

---

## Post #19 by @pieper (2024-05-07 11:27 UTC)

<p>Ah, good catch Davide - yes, this mix of upper and lower case hex tags was a big pain.  I think we need to be very consistent and use upper case everywhere.</p>

---

## Post #20 by @Davide_Punzo (2024-05-07 11:56 UTC)

<blockquote>
<p>Ah, good catch Davide - yes, this mix of upper and lower case hex tags was a big pain. I think we need to be very consistent and use upper case everywhere.</p>
</blockquote>
<p>I agree. I had a look and I think the only missing one was this one.</p>

---
