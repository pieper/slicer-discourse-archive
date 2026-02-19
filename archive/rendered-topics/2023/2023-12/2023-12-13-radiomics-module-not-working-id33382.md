---
topic_id: 33382
title: "Radiomics Module Not Working"
date: 2023-12-13
url: https://discourse.slicer.org/t/33382
---

# Radiomics module not working?

**Topic ID**: 33382
**Date**: 2023-12-13
**URL**: https://discourse.slicer.org/t/radiomics-module-not-working/33382

---

## Post #1 by @ogdenk (2023-12-13 16:18 UTC)

<p>I have been using the Radiomics module for several years now and it has worked properly.  The latest version for which it still works for me is 5.4.0.  In newer versions it does not work, the output is blank.  I have not changed my computer platform so it is not a hardware issue.  Is this a known issue, or is there something else locally I might need to address?  Any help is appreciated!</p>
<p>Kent</p>

---

## Post #2 by @pieper (2023-12-13 17:28 UTC)

<p>Yes, it’s not currently working on all platforms (mac is broken, others might work on the new 5.6.1).  Using the older release is probably the best workaround for the time being.</p>

---

## Post #3 by @ogdenk (2023-12-13 17:37 UTC)

<p>Ok, thank you for the information!  As long as it is not my computer . . .</p>
<p>Kent</p>

---

## Post #4 by @Numan_Kutaiba (2024-01-03 20:00 UTC)

<p>It’s a problem because I can’t use Total Segmentator unless I use the newer version. So right now I don’t have a version with both radiomics and Total Segmentator both working at the same time!</p>

---

## Post #5 by @ogdenk (2024-01-03 20:04 UTC)

<p>I agree, I have two versions of Slicer installed because of this issue. My original comment meant that I don’t have a computer issue, it’s a software issue.</p>
<p>Kent</p>

---

## Post #6 by @pieper (2024-01-03 21:41 UTC)

<p>There’s a fix for windows and linux that needs to be reviewed (I don’t have access to that repo to merge it but maybe <a class="mention" href="/u/fedorov">@fedorov</a> does?).</p>
<p>In the meantime, it would be great if people could be testing the fix.  It should just be a matter of replacing the lines of code or the whole file:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/pull/857">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/pull/857" target="_blank" rel="noopener">github.com/AIM-Harvard/pyradiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/AIM-Harvard/pyradiomics/pull/857" target="_blank" rel="noopener">SafeLoadRemove Error in Slicer</a>
      </h4>

    <div class="branches">
      <code>AIM-Harvard:master</code> ← <code>DanXieJY:SafeLoadRemove</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-12-06" data-time="19:28:57" data-timezone="UTC">07:28PM - 06 Dec 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/DanXieJY" target="_blank" rel="noopener">
            <img alt="DanXieJY" src="https://avatars.githubusercontent.com/u/113625444?v=4" class="onebox-avatar-inline" width="20" height="20">
            DanXieJY
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 3 additions and 1 deletions">
          <a href="https://github.com/AIM-Harvard/pyradiomics/pull/857/files" target="_blank" rel="noopener">
            <span class="added">+3</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I recently found the SlicerRadiomics extension does not work in 3D Slicer and be<span class="show-more-container"><a href="https://github.com/AIM-Harvard/pyradiomics/pull/857" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">low is the issue that I decribed in.
https://github.com/AIM-Harvard/SlicerRadiomics/issues/80

I tried to modify the code with the help of @pieper :
1. Add the code below to the top of the file:
`from ruamel.yaml import YAML`
2. Add the code below before line 353:
`yaml = YAML(typ='safe', pure=True) `
3. Change what was in line 353 to:
`settingsSchema = yaml.load(schema)['mapping']['setting']['mapping']`</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @fedorov (2024-01-03 23:05 UTC)

<p>I’ve just merged it - hope this fixes it! Coincidentally, I also just today noticed the extension is missing from Slicer.</p>

---

## Post #8 by @pieper (2024-01-03 23:39 UTC)

<p>Thanks Andrey <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>The extension built on windows and linux but there was a runtime error.  On mac there’s a build error so no extension is available.</p>

---

## Post #9 by @miklontzas (2024-01-14 18:13 UTC)

<p>Any update for Mac users? is the extension back? if not which is the latest working version of slicer that we can use to have a working radiomics plugin?</p>

---

## Post #10 by @pieper (2024-01-14 18:43 UTC)

<p>I don’t think there’s any progress on the mac version of pyradiomics.  The build system needs work.  Unless someone else knows off the top of their head you’ll need to test to see when there was a working version and report back if you can.</p>

---

## Post #11 by @miklontzas (2024-01-14 19:16 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>! I tried building Slicer 5.4.0 from source but I cannot install the extension… <a class="mention" href="/u/fedorov">@fedorov</a> is there a plan for a future fix for the most recent version of slicer?</p>

---

## Post #12 by @pieper (2024-01-14 21:43 UTC)

<p>It may be hard to build older slicers, but you should still be able to get the application and install extensions for released binaries at this link:  <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482">https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482</a></p>

---

## Post #13 by @miklontzas (2024-01-14 21:56 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>! Managed to download and install version 5.0.3 from the link you gave. I also downloaded the radiomics extension for this version which seems to work perfect. will stick there until a new version of the plugin is released to work with the latest version of slicer</p>

---

## Post #14 by @fedorov (2024-01-15 15:19 UTC)

<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> is there a plan for a future fix for the most recent version of slicer?</p>
</blockquote>
<p>The error seems to be in pyradiomics, not in the SlicerRadiomics extension itself. I submitted an issue, but I am not sure if pyradiomics is being maintained. I suggest following up in that issue.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/issues/865">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/issues/865" target="_blank" rel="noopener">github.com/AIM-Harvard/pyradiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/AIM-Harvard/pyradiomics/issues/865" target="_blank" rel="noopener">[BUG] unable to build package on mac</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-01-15" data-time="15:18:31" data-timezone="UTC">03:18PM - 15 Jan 24 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/fedorov" target="_blank" rel="noopener">
          <img alt="fedorov" src="https://avatars.githubusercontent.com/u/313942?v=4" class="onebox-avatar-inline" width="20" height="20">
          fedorov
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">pyradiomics build fails on mac as part of Slicer preview build

https://slicer<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">.cdash.org/viewBuildError.php?buildid=3271763

![image](https://github.com/AIM-Harvard/pyradiomics/assets/313942/e8798f80-dd0c-4213-9da8-06416b18667b)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @jamesobutler (2024-01-15 15:41 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> is there a reason for SlicerRadiomics to build pyradiomics from source?</p>
<p>Latest pyradiomics (3.1.0) does have a Python whl file for macOS. <a href="https://pypi.org/project/pyradiomics/#files" class="inline-onebox" rel="noopener nofollow ugc">pyradiomics · PyPI</a>. This seems to indicate that it isn’t so much a problem with pyradiomics as it was possible for it to build a whl file successfully and upload to PyPI for macOS.</p>
<p>Therefore SlicerRadiomics could instead install from whl instead of build from source.</p>

---

## Post #16 by @fedorov (2024-01-15 20:42 UTC)

<p>That’s a great idea! I don’t remember why we are building it from source in SlicerRadiomics, but indeed I should experiment with switching to pip install. Thank you!</p>

---
