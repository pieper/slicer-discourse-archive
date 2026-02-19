---
topic_id: 31406
title: "Problems Using Importosirixroi From The Sandbox Extension"
date: 2023-08-28
url: https://discourse.slicer.org/t/31406
---

# Problems using ImportOsirixROI from the Sandbox extension

**Topic ID**: 31406
**Date**: 2023-08-28
**URL**: https://discourse.slicer.org/t/problems-using-importosirixroi-from-the-sandbox-extension/31406

---

## Post #1 by @fedorov (2023-08-28 19:11 UTC)

<p>I’ve just had a conversation with Dr. Ron Summers from NCI, who has been trying to use the <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/ImportOsirixROI">ImportOsirixROI function from the Sandbox extension</a>. It is failing with the following error:</p>
<pre><code class="lang-auto">"[...]/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/Sandbox/lib/Slicer-5.4/qt-scripted-modules/ImportOsirixROI.py", line 284, in importOsirixRoiFileToSegmentation

[CRITICAL][Stream] 28.08.2023 11:25:17 [] (unknown:0) -     inputRoiData = plistlib.readPlist(inputRoi)

[CRITICAL][Stream] 28.08.2023 11:25:17 [] (unknown:0) - AttributeError: module 'plistlib' has no attribute 'readPlist'
</code></pre>
<p>I have never used that extension. Can someone from the Sandbox extension team help here? <a class="mention" href="/u/lassoan">@lassoan</a> is this something you maintain?</p>

---

## Post #2 by @rsummers (2023-08-28 19:29 UTC)

<p>Just to provide some background, I’m trying to import a flood-filled segmentation from Osirix into Slicer, and then output the segmentation as a NIFTI file.</p>

---

## Post #3 by @jamesobutler (2023-08-29 01:13 UTC)

<p>It appears the <code>readPlist</code> method was removed from plistlib as mentioned in the Python 3.9 release notes <a href="https://docs.python.org/3.9/whatsnew/3.9.html#removed" class="inline-onebox" rel="noopener nofollow ugc">What’s New In Python 3.9 — Python 3.9.17 documentation</a> after having being marked deprecated in Python 3.4. The <code>load</code> method is the new method <a href="https://docs.python.org/3.9/library/plistlib.html#plistlib.load" class="inline-onebox" rel="noopener nofollow ugc">plistlib — Generate and parse Apple .plist files — Python 3.9.17 documentation</a>. This should be an easy upgrade to the new API.</p>
<p>Slicer upgraded to Python 3.9 back in January 2022, so it appears this SlicerSandbox code has been broken for well over 1.5 years now.</p>

---

## Post #4 by @fedorov (2023-09-01 17:49 UTC)

<p>I submitted the issue so this does not get lost.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/issues/22">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/issues/22" target="_blank" rel="noopener">github.com/PerkLab/SlicerSandbox</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PerkLab/SlicerSandbox/issues/22" target="_blank" rel="noopener">readPlist removed in python 3.9 - unable to use ImportOsirix ROI</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-01" data-time="17:49:32" data-timezone="UTC">05:49PM - 01 Sep 23 UTC</span>
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
    <p class="github-body-container">As discussed in https://discourse.slicer.org/t/problems-using-importosirixroi-fr<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">om-the-sandbox-extension/31406, `ImportOsirixROI` functionality appears to be broken.

```
"[...]/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/Sandbox/lib/Slicer-5.4/qt-scripted-modules/ImportOsirixROI.py", line 284, in importOsirixRoiFileToSegmentation

[CRITICAL][Stream] 28.08.2023 11:25:17 [] (unknown:0) -     inputRoiData = plistlib.readPlist(inputRoi)

[CRITICAL][Stream] 28.08.2023 11:25:17 [] (unknown:0) - AttributeError: module 'plistlib' has no attribute 'readPlist'
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2023-09-01 21:10 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> thanks for reporting and <a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks for the investigation.</p>
<p><a class="mention" href="/u/rsummers">@rsummers</a> It may be a simple fix, but I would like to test it with your data to make sure that I use the new plistlib API correctly. Could you upload some anonymized test segmentation to somewhere and post the link here?</p>

---

## Post #6 by @Mathematinho (2023-10-20 15:30 UTC)

<p>I wonder if there is a temporary work around with and older version. I tried couple older version but none works.</p>

---

## Post #7 by @mattflick (2023-11-13 18:36 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I’ve been attempting to update the script used to import Osirix ROIs to utilize the new plistlib methods (load and loads) in the relevant lines of code. Unfortunately this does not appear to be working when I run the script through the 3D slicer GUI, so I am wondering if you have made any progress on fixing this issue? The updated script I’ve tried is available here, in case it is helpful: <a href="https://github.com/flickmatt/3D-Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - flickmatt/3D-Slicer</a></p>
<p>Thank you for your help.</p>

---

## Post #8 by @lassoan (2023-11-13 21:32 UTC)

<p>Thanks for the update <a class="mention" href="/u/mattflick">@mattflick</a>. Could you provide an example file that I can test with? (I only seem to have .json files and not binary plist files)</p>

---
