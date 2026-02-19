---
topic_id: 16904
title: "Custom Color Maps Disappearing On Mac Big Sur"
date: 2021-04-01
url: https://discourse.slicer.org/t/16904
---

# Custom color maps disappearing (on MAC big sur)

**Topic ID**: 16904
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/custom-color-maps-disappearing-on-mac-big-sur/16904

---

## Post #1 by @lucaxx85 (2021-04-01 13:09 UTC)

<p>Dear experts,<br>
I’m working with Slicer 4.11 on MAC big sur (not sure if it’s relevant, but MAC always give lots of troubles to us). I’ve created some custom color maps and copied them in the share/Slicer-4.11/ColorFiles folder. I’ve also deleted many unusable color LUTs, to free up space in the selection menu.</p>
<p>In an apparently random fashion, it already occurred twice that the menu stopped showing us the custom color LUTs, but restarted showing us the old ones. However, in the slicer folder, the shown ones are not present and our custom ones are indeed present!<br>
The only way to have them back again appears to be deleting them and re-copying them in this folder.</p>
<p>Are we doing anything wrong? Are there other ways to load color LUTs?</p>
<p>Also, I had to do this because there are no standard nor even barely usable maps for nuclear medicine images. Are there other ways to import standard LUTs?</p>

---

## Post #2 by @lassoan (2021-04-03 01:38 UTC)

<p>You can load your LUTs in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file">application startup file</a> and if you set a singleton tag on them then closing the scene will not wipe them.</p>
<p>Adding colormap files to where the default colormap files are stored should work, too. They will be treated the same way as all the existing file-based colormaps (such as magma, viridis, …). You may not be able to remove built-in procedural and generated color tables.</p>
<p>If you have a few color tables that you would like to see in Slicer then we may just add it to the Slicer core. There are well over a hundred color tables, so adding a few should not matter much.</p>

---

## Post #3 by @lucaxx85 (2021-04-04 16:18 UTC)

<p>Thanks Andras!<br>
Two of the color LUTs I’ve added are even downloadable from the NEMA website. The third one is <em>the</em> one used by all doctors in my unit for reading PET studies on all consoles by different vendors.<br>
If I can provide them to this community let me know.</p>

---

## Post #4 by @lassoan (2021-04-06 13:17 UTC)

<p>Yes, if we are allowed to use them without restrictions then please upload them somewhere and post the link here and we’ll most probably be able to add them to the built-in lookup tables.</p>

---

## Post #5 by @lucaxx85 (2021-04-06 14:11 UTC)

<p>Thanks!<br>
The three I’ve added are the “PET” and the “HOT_METAL_BLUE” from the NEMA “well known color palettes” page (with linear interpolation to 256 levels) and the “rainbow” from the FIJI PET-CT plugin. The main difference between the “rainbow” used for nuclear medicine reading and the ones already present in Slicer is that it starts from black.<br>
These links are the original ones I’ve downloaded. I can pass them to you in the slicer format also (but I’m not sure I’ve done them correctly concerning the first two columns.</p>
<p><a href="https://sourceforge.net/projects/bifijiplugins/files/extraLUT/" class="onebox" target="_blank" rel="noopener nofollow ugc">https://sourceforge.net/projects/bifijiplugins/files/extraLUT/</a><br>
<a href="http://dicom.nema.org/medical/Dicom/2017d/output/chtml/part06/chapter_B.html" class="onebox" target="_blank" rel="noopener nofollow ugc">http://dicom.nema.org/medical/Dicom/2017d/output/chtml/part06/chapter_B.html</a></p>

---

## Post #6 by @lassoan (2021-04-13 21:51 UTC)

<p>I’ve submitted a pull request that adds these 3 color maps:</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5587" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">

      <details class="onebox-details">
        <summary class="onebox-details-summary">
          <h4>
            <a href="https://github.com/Slicer/Slicer/pull/5587" target="_blank" rel="noopener">ENH: Added new color nodes for PET image display: PET-Rainbow2, PET-DICOM, and PET-HotMetalBlue</a>
          </h4>
        </summary>
        <p class="onebox-details-body">See discussion at:
https://discourse.slicer.org/t/custom-color-maps-disappearing-on-mac-big-sur/16904/5

![image](https://user-images.githubusercontent.com/307929/114625805-c9c7e600-9c80-11eb-9a29-72cae6875aa9.png)
</p>
      </details>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:new-pet-luts</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-04-13" data-time="21:50:58" data-timezone="UTC">09:50PM - 13 Apr 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 90 additions and 63 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5587/files" target="_blank" rel="noopener">
          <span class="added">+90</span>
          <span class="removed">-63</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2021-04-14 01:38 UTC)

<p>The pull request has been merged, the new colormaps will be available in the Slicer Preview Release from tomorrow.</p>

---
