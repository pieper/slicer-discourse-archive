---
topic_id: 46117
title: "Odd behavior after adding a moving mask in the ANTs extension"
date: 2026-02-10
url: https://discourse.slicer.org/t/46117
last_bumped: 2026-03-04T17:52:15.661Z
---

# Odd behavior after adding a moving mask in the ANTs extension

**Topic ID**: 46117
**Date**: 2026-02-10
**URL**: https://discourse.slicer.org/t/odd-behavior-after-adding-a-moving-mask-in-the-ants-extension/46117

---

## Post #1 by @sulli419 (2026-02-10 20:05 UTC)

<p>I’ve been using the ANTs extension for registering two single-label volumes to eachother with good results.  In an attempt to improve registration robustness, I started incorporating fixed and moving masks (FM, MM), but this is yielding some unexpected results.  To simplify the issue I’m just focusing on a single stage affine transform. The affine transform with the fixed mask alone looks very reasonable; but if I add a moving mask to this same affine configuration (along with the fixed) the registration is much poorer.  For now, the moving mask is essentially just a bounding box with zeros at the edges.</p>
<p>When working properly, the largest components of the final affine transform are a Z translation (shift) and a Z scaling (expansion).  Something about showing the MM (in addition to FM) loses this info.  As a test, I ran a “good” FM only registration but also included a 2nd dummy affine stage (following the correct/complete one), where there are zero convergence steps, but now both the FM and MM are shown.  This somehow changes the 3-3 matrix value (Z scaling factor) from 1.2 (ideal) to ~1.  If this dummy step only has the FM, the “affine erasure” doesn’t happen.</p>
<p>Trouble shooting I created a MM that is “all 1s”, expecting that it should work the same as a having no moving mask but this wasn’t the case, the all 1s MM worsened the quality.</p>
<p>Any chance this is a bug? Might the image origin of the moving mask be getting read improperly?  Perhaps I’m just ignorant of how masks interact by design in ANTs.</p>
<p>If it’s any help I’m including an image<br>
Red: Fixed volume (my tissue); Yellow: Moving volume (atlas); Green: fixed mask; Purple: moving mask</p>
<p>**Note, this doesn’t show the dimensions of the zero values.  For example, how large the virtual space of the fixed volume is.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0.jpeg" data-download-href="/uploads/short-url/tPdzGRT0m1TRxw6K90ytkXjKDWE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0_2_215x499.jpeg" alt="image" data-base62-sha1="tPdzGRT0m1TRxw6K90ytkXjKDWE" width="215" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0_2_215x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0.jpeg 2x" data-dominant-color="9387A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">320×744 34.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @sulli419 (2026-02-20 00:00 UTC)

<p>I’ve been troubleshooting this issue for days.  I’m not sure if something changed in my ANTs, but now I am convinced that even the “fixed mask” (for hiding parts of the fixed volume) is not working.</p>
<p>To make things easier I started playing with the demo MR data here.  I am finding that the registration is identical, irrespective of if I add the fixed mask in ANTs.  However, if I add the fixed mask in the Elastix extension, it changes the registration, as expected.</p>
<p>Can anyone confirm that the fixed or moving masks are working for them in the ANTs extension?  Wonder it is a version issue, or maybe something was corrupted as I was tinkering with parameters, etc.</p>
<p>I should add, if anyone has some simple positive controls to test for masking I’d gladly run them and share the results here.</p>
<p>Thanks!</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/stnava/BasicBrainMapping">
  <header class="source">

      <a href="https://github.com/stnava/BasicBrainMapping" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/aab0123cee48174388635671b0141cc9/stnava/BasicBrainMapping" class="thumbnail">

  <h3><a href="https://github.com/stnava/BasicBrainMapping" target="_blank" rel="noopener nofollow ugc">GitHub - stnava/BasicBrainMapping: A simple and "fast" brain registration example</a></h3>

    <p><span class="github-repo-description">A simple and "fast" brain registration example</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @sulli419 (2026-02-20 01:50 UTC)

<p>On the off chance this is a clue, I noticed that the masks have to be in the labelmap format to be seen in the “moving mask” dropdown menu.  Does this sound correct or point to the issue?  If recall correctly, I think Elastix can also use scalar volumes.</p>

---

## Post #4 by @drnoorfatima (2026-02-20 10:37 UTC)

<p>Hi!</p>
<p>I’ve been looking at this and I think the issue is actually in how the ANTs extension GUI passes mask parameters internally which explains why the same mask behaves differently depending on the stage configuration.</p>
<p>The “all 1s” mask behaving differently than no mask is a strong clue that the problem is in the extension layer, not ANTs itself.</p>
<p>There’s a way to bypass this entirely and get proper mask control, but it involves a different approach than using the extension GUI directly.</p>
<p>Happy to help if you want to discuss further!</p>

---

## Post #5 by @sulli419 (2026-02-20 17:44 UTC)

<p>Thanks for your message.  Interesting, so you are also unable to read the hide masks with the ANTs extension?  Since the extension has been around so long, I wonder if the conflict arose in a newerer version of Slicer?</p>
<p>To my more recent post, I might have been getting distracted by the odd behavior of the moving mask.  I now wonder if because it <span class="bbcode-u">isn’t reading the fixed mask</span> the moving mask was also getting misread.  Somewhere in the ANTs documentation I vaguely recall reading that if you have a moving mask a fixed mask is obligatory.</p>
<p>Maybe we could keep the Slicer specific details here, and I will DM about alternative approaches.  However, the GUI has been so useful for tracking my workflow and quality control.  If everyone has this bug I hope it can be fixed.  I’ll put in a request if you can confirm you also get the error.  I’m in the process of testing it on a different machine with a fresh install.</p>
<p>Appreciate the help</p>

---

## Post #6 by @drnoorfatima (2026-02-22 11:01 UTC)

<p>Happy to discuss alternative approaches over DM!</p>

---

## Post #7 by @sulli419 (2026-02-28 02:06 UTC)

<p>A solution.  Thanks to those who helped fix and update ATNs <a class="mention" href="/u/mhalle">@mhalle</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/simonoxen">@simonoxen</a></p>
<p>Ok, I pitched this problem in a forum where people were discussing using large documentation and code data bases for priming AI for working in slicer, which includes debugging!  Claude spotted the bug and fixed it.  Interestingly, in my hands GPT 5.2 was suggesting a similar fix with zero documentation priming, but I didn’t completely trust it.</p>
<p>It appears that what was happening is that if the user selected only one mask (either fixed or moving) it didn’t load it and ran with no warning.</p>
<p>A new slicer ants released a couple of days ago with this fixed (see link).   You can either replace the suspect .py file in your existing ANTs or install the absolute latest Slicer and then find the new extension from within the GUI</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> is an expert user, so he might add some comments about how well it’s working.  The masks seem to change the registration in fairly sensible ways, but I haven’t probed it rigorously.</p>
<p>Things I plan to check:<br>
1.) can different masks be mixed at matched at different stages (confirm at least in the CLI)?</p>
<p>2.)  Why was I getting a funny result in the old version when adding a fixed AND moving mask (since this shouldn’t trigger this bug)?  Test if this is still happening, i.e., not a separate bug to address.</p>
<aside class="quote" data-post="4" data-topic="46243">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-slicer-skill-ai-tool/46243/4">New slicer-skill ai tool</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #000000;" data-drop-close="true" class="badge-category --style-square " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
    </div>
  </div>
  <blockquote>
    This sounds very useful.  Could it be used to fixed bugs in extensions?  As an example task, I am finding the ANTs extension can no longer apply fixed masks (for hiding parts of the volume).  It would be interesting to see if Claude could nail the problem and provide a fix for the next version.
  </blockquote>
</aside>

<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/netstim/SlicerANTs/pull/15">
  <header class="source">

      <a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc">github.com/netstim/SlicerANTs</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc">BUG: Fix masks silently ignored when only one mask is provided (#15)</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>mhalle:fix/allow-single-mask</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-02-23" data-time="04:07:42" data-timezone="UTC">04:07AM - 23 Feb 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/mhalle" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/649467?v=4" class="onebox-avatar-inline" width="20" height="20">
            mhalle
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 5 additions and 5 deletions">
          <a href="https://github.com/netstim/SlicerANTs/pull/15/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+5</span>
            <span class="removed">-5</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

- **Fixed**: `getMasksCommand()` required both fixed AND moving mask<span class="show-more-container"><a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">s to generate the `--masks` flag. Providing only a fixed mask (the common use case for hiding parts of the volume during registration) silently dropped the mask entirely — no `--masks` flag was emitted and no warning was shown.
- **Fix**: When only one mask is provided, `NULL` is passed as the ANTs placeholder for the missing mask, allowing either mask to be used independently.

### Before (broken)
```
# User selects only a fixed mask → no --masks flag generated at all
```

### After (fixed)
```
# Fixed only:  --masks [$fixedMask,NULL]
# Moving only: --masks [NULL,$movingMask]
# Both:        --masks [$fixedMask,$movingMask]
# Neither:     no flag (unchanged)
```

## Test plan

- [ ] Load two volumes and a label map mask in Slicer
- [ ] In ANTs Registration, select only a fixed mask (leave moving mask as None)
- [ ] Run registration and verify the `--masks` flag appears in the generated command with `NULL` for the moving mask
- [ ] Repeat with only a moving mask selected
- [ ] Verify both masks together still works as before
- [ ] Verify no masks selected still omits the `--masks` flag

🤖 Generated with [Claude Code](https://claude.com/claude-code)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @sulli419 (2026-03-01 18:53 UTC)

<p>Reposting because I might have accidentally deleted</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/netstim/SlicerANTs/pull/15">
  <header class="source">

      <a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc">github.com/netstim/SlicerANTs</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc">BUG: Fix masks silently ignored when only one mask is provided (#15)</a>
      </h4>

    <div class="branches">
      <code>master</code> ← <code>mhalle:fix/allow-single-mask</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-02-23" data-time="04:07:42" data-timezone="UTC">04:07AM - 23 Feb 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/mhalle" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/649467?v=4" class="onebox-avatar-inline" width="20" height="20">
            mhalle
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 5 additions and 5 deletions">
          <a href="https://github.com/netstim/SlicerANTs/pull/15/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+5</span>
            <span class="removed">-5</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

- **Fixed**: `getMasksCommand()` required both fixed AND moving mask<span class="show-more-container"><a href="https://github.com/netstim/SlicerANTs/pull/15" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">s to generate the `--masks` flag. Providing only a fixed mask (the common use case for hiding parts of the volume during registration) silently dropped the mask entirely — no `--masks` flag was emitted and no warning was shown.
- **Fix**: When only one mask is provided, `NULL` is passed as the ANTs placeholder for the missing mask, allowing either mask to be used independently.

### Before (broken)
```
# User selects only a fixed mask → no --masks flag generated at all
```

### After (fixed)
```
# Fixed only:  --masks [$fixedMask,NULL]
# Moving only: --masks [NULL,$movingMask]
# Both:        --masks [$fixedMask,$movingMask]
# Neither:     no flag (unchanged)
```

## Test plan

- [ ] Load two volumes and a label map mask in Slicer
- [ ] In ANTs Registration, select only a fixed mask (leave moving mask as None)
- [ ] Run registration and verify the `--masks` flag appears in the generated command with `NULL` for the moving mask
- [ ] Repeat with only a moving mask selected
- [ ] Verify both masks together still works as before
- [ ] Verify no masks selected still omits the `--masks` flag

🤖 Generated with [Claude Code](https://claude.com/claude-code)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group quote-modified" data-username="sulli419" data-post="7" data-topic="46117">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>A solution. Thanks to those who helped fix and update ANTs <a class="mention" href="/u/mhalle">@mhalle</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/simonoxen">@simonoxen</a></p>
<p>Ok, I pitched this problem in a forum where people were discussing using large documentation and code data bases for priming AI for working in slicer, which includes debugging! Claude spotted the bug and fixed it. Interestingly, in my hands GPT 5.2 was suggesting a similar fix with zero documentation priming, but I didn’t completely trust it.</p>
<p>It appears that what was happening is that if the user selected only one mask (either fixed or moving) it didn’t load it and ran with no warning.</p>
<p>A new slicer ants released a couple of days ago with this fixed (see link). You can either replace the suspect .py file in your existing ANTs or install the absolute latest Slicer and then find the new extension from within the GUI</p>
<p><a class="mention" href="/u/mikebind">@mikebind</a> is an expert user, so he might add some comments about how well it’s working. The masks seem to change the registration in fairly sensible ways, but I haven’t probed it rigorously.</p>
<p>Things I plan to check:<br>
1.) can different masks be mixed at matched at different stages (confirm at least in the CLI)?</p>
<p>2.) Why was I getting a funny result in the old version when adding a fixed AND moving mask (since this shouldn’t trigger this bug)? Test if this is still happening, i.e., not a separate bug to address.</p>
</blockquote>
</aside>

---

## Post #9 by @sulli419 (2026-03-02 19:12 UTC)

<p>Sharing more of my notes on this post after running some quality tests in slicer.  I think everything is in order.</p>
<p>I took some dummy T1 MRI data of the head and registered two volumes to eachother with quick syn (rigid, affine, SyN).  I created masks for the brain and everything but the brain (~skull) for each volume.  This allowed me to hide various parts and see if the reg worked as predicted.</p>
<p>With “link across stages” selected for the masks, I am now able to select just one mask (either fixed or moving) and it works predictably, e.g., if I mask/hide everything but the skull with <em>either</em> a fixed or moving mask, the skull reg looks great but the brain is poorer.  Same from brain but not skull.</p>
<p><strong>The CLI that shows up under the double arrow of the ANTs GUI shows this, as expected</strong><br>
<em>All_Command_lines_OK<br>
Using single precision for computations.<br>
Reading mask(s).<br>
Registration stage 0<br>
No fixed mask<br>
Moving mask = C:/Users/sulliste/AppData/Local/Temp/1/Slicer/BBJFC_vtkMRMLLabelMapVolumeNodeE.nrrd<br>
Registration stage 1<br>
No fixed mask<br>
Moving mask = C:/Users/sulliste/AppData/Local/Temp/1/Slicer/BBJFC_vtkMRMLLabelMapVolumeNodeE.nrrd<br>
Registration stage 2<br>
No fixed mask<br>
Moving mask = C:/Users/sulliste/AppData/Local/Temp/1/Slicer/BBJFC_vtkMRMLLabelMapVolumeNodeE.nrrd</em></p>
<p>Next I tested if single masks can be applied at certain stages but not others, for example, just a fixed mask at the affine stage (2nd).  Now the the same CLI readout looks wrong, only applying at stage 0 (rigid) (?).</p>
<p><em>Reading mask(s).<br>
Registration stage 0<br>
Fixed mask = C:/Users/APOM/AppData/Local/Temp/Slicer/FJEE_vtkMRMLLabelMapVolumeNodeC.nrrd<br>
No moving mask</em></p>
<p>I thought maybe this is just a readout error so dug deeper…<br>
Each time the ANTs extension runs it creates a report in the slicer data module.  To see it, click the tab “all nodes” in the main data module, then at the bottom tick “show hidden nodes” and it will look something like the image I shared.  I expanded my last run “…CLI_13” by right clicking then “edit properties”.  Under the command dropdown it shows this info.  Note in bold that the mask is only applied to affine, as I intended:<br>
*–dimensionality 3 --use-histogram-matching 0 --winsorize-image-intensities [0.005,0.995] --float $useFloat --verbose 1 --interpolation Linear --output [$outputBase,$outputVolume] --write-composite-transform 1 --collapse-output-transforms 1 --transform Rigid[0.1] --metric MI[$inputVolume01,$inputVolume02,1,32,Regular,0.25] --convergence [1000x500x250x0,1e-6,10] --smoothing-sigmas 4x3x2x1vox --shrink-factors 12x8x4x2 <strong>–transform Affine[0.1] --metric MI[$inputVolume01,$inputVolume02,1,32,Regular,0.25] --convergence [1000x500x250x0,1e-6,10] --smoothing-sigmas 4x3x2x1vox --shrink-factors 12x8x4x2 **–masks [$inputVolume03,NULL] –</strong>*<em>transform SyN[0.1,3,0] --metric MI[$inputVolume01,$inputVolume02,1,32,Regular,0.25] --convergence [100x100x70x50x0,1e-6,10] --smoothing-sigmas 5x3x2x1x0vox --shrink-factors 10x6x4x2x1</em></p>
<p>Yet to confirm single stage reg is perfectly predictable, but <strong>long story short, it seems to be applying correctly.</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20a846c253df42c0798c32b76b60ca138f226f77.png" data-download-href="/uploads/short-url/4ETOc2Dkt811j1saW8wmtpqcOq3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20a846c253df42c0798c32b76b60ca138f226f77.png" alt="image" data-base62-sha1="4ETOc2Dkt811j1saW8wmtpqcOq3" width="580" height="273"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">580×273 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @sulli419 (2026-03-04 17:52 UTC)

<p>I take it back!  The new version indeed fixes the single masking bug if you link them across all stages.  <span class="bbcode-u">BUT probing to see if I can apply various masks in any (many) permutations, i.e., differently at each stage, show it isn’t working.</span>  So my previous concern (below) was justified!  I have a new .py script that seems to have fixed this issue.  Testing it more and plan to place another git pull request.</p>
<p>”Next I tested if single masks can be applied at certain stages but not others, for example, just a fixed mask at the affine stage (2nd). Now the the same CLI readout looks wrong, only applying at stage 0 (rigid) (?).</p>
<p><em>Reading mask(s).<br>
Registration stage 0<br>
Fixed mask = C:/Users/APOM/AppData/Local/Temp/Slicer/FJEE_vtkMRMLLabelMapVolumeNodeC.nrrd<br>
No moving mask”</em></p>

---
