# A bit of confusion about the slicer coordinate system

**Topic ID**: 29883
**Date**: 2023-06-07
**URL**: https://discourse.slicer.org/t/a-bit-of-confusion-about-the-slicer-coordinate-system/29883

---

## Post #1 by @ma1282029525 (2023-06-07 02:28 UTC)

<p>The itk coordinate system is lps, and the slider is ras. However, why does the cursor on the slider display coordinates that are not actually ras? For example, the dicom coordinates are (1, 1, 1), while the actual coordinates in the slider are (-1, -1, 1), and the slider cursor displays coordinates that are (1, -1, 1)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f79f254a5662cf3415d96394fa85a859c06525df.png" data-download-href="/uploads/short-url/zkyTZXRkzbCxrToiLLTIaIf0tTF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f79f254a5662cf3415d96394fa85a859c06525df.png" alt="image" data-base62-sha1="zkyTZXRkzbCxrToiLLTIaIf0tTF" width="690" height="68" data-dominant-color="ECECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1017×101 5.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffaa64221e959f2447cb6bb1201ea933bb93211.jpeg" data-download-href="/uploads/short-url/2hmaUClL1rDeG3i8sGQotpEpKqR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ffaa64221e959f2447cb6bb1201ea933bb93211_2_690x409.jpeg" alt="image" data-base62-sha1="2hmaUClL1rDeG3i8sGQotpEpKqR" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ffaa64221e959f2447cb6bb1201ea933bb93211_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ffaa64221e959f2447cb6bb1201ea933bb93211_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffaa64221e959f2447cb6bb1201ea933bb93211.jpeg 2x" data-dominant-color="3A774B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1214×720 74.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
such as this</p>

---

## Post #2 by @ma1282029525 (2023-06-07 02:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7fbaa1580a8d18f08c6f69b4fc9e2d9863215a1.png" data-download-href="/uploads/short-url/sx8cImzDo1sNkVL1hLRaw8Kg34Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7fbaa1580a8d18f08c6f69b4fc9e2d9863215a1_2_690x229.png" alt="image" data-base62-sha1="sx8cImzDo1sNkVL1hLRaw8Kg34Z" width="690" height="229" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7fbaa1580a8d18f08c6f69b4fc9e2d9863215a1_2_690x229.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7fbaa1580a8d18f08c6f69b4fc9e2d9863215a1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7fbaa1580a8d18f08c6f69b4fc9e2d9863215a1.png 2x" data-dominant-color="87BAD9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1008×335 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @ma1282029525 (2023-06-07 02:30 UTC)

<p>Why is R the opposite</p>

---

## Post #4 by @jamesobutler (2023-06-07 10:34 UTC)

<p>Here is a good explanation about the usage of the RAS and LPS coordinate system by Slicer:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#on-use-of-lps-ras-coordinate-systems" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#on-use-of-lps-ras-coordinate-systems</a></p>

---

## Post #5 by @muratmaga (2023-06-07 16:57 UTC)

<aside class="quote no-group" data-username="ma1282029525" data-post="3" data-topic="29883" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ma1282029525/48/66047_2.png" class="avatar"> ma1282029525:</div>
<blockquote>
<p>Why is R the opposite</p>
</blockquote>
</aside>
<p>in summary RAS to LPS transition (or vice versa) involves negating the signs of the first two coordinates (not just R. In your case both R and A had inverse signs).</p>

---

## Post #6 by @ma1282029525 (2023-06-12 01:50 UTC)

<p>I’m referring to the slider. The slider yellow is -0.5, Green is 212, RED is -99, and it doesn’t correspond to either RAS or LPS.</p>

---

## Post #7 by @muratmaga (2023-06-12 17:58 UTC)

<p>I am speculating, but that’s probably related to some other radiological convention being used. Reported measurements are still consistent, but as you said it is neither RAS, nor LPS, but LAS (look at the wording on the title bars Green is A, Red is S, and yellow is L).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dff17eb3f74b6252af62b64a4d04aea86f4b1635.jpeg" data-download-href="/uploads/short-url/vX5SkXcGHKWh61G9xtk9eqxPOOp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dff17eb3f74b6252af62b64a4d04aea86f4b1635_2_690x336.jpeg" alt="image" data-base62-sha1="vX5SkXcGHKWh61G9xtk9eqxPOOp" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dff17eb3f74b6252af62b64a4d04aea86f4b1635_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dff17eb3f74b6252af62b64a4d04aea86f4b1635_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/dff17eb3f74b6252af62b64a4d04aea86f4b1635_2_1380x672.jpeg 2x" data-dominant-color="9B9BA1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2664×1300 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @jamesobutler (2023-06-12 19:36 UTC)

<p>In Edit-&gt;Application Settings you can change whether patient right is screen left or not.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58170b7a1a10ddacde79884c1a0f1d5fb401d008.png" alt="image" data-base62-sha1="czhodWuDrfAqQdUAYgVs4b2Ca9y" width="679" height="208"></p>
<p>That work came out of the following PR if you are curious about the conversation that led to it.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5536">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5536" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/5536" target="_blank" rel="noopener nofollow ugc">ENH: Make default slice view orientations configurable</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:configurable-slice-view-orientation</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2021-03-19" data-time="01:32:04" data-timezone="UTC">01:32AM - 19 Mar 21 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 10 files with 188 additions and 51 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/5536/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+188</span>
            <span class="removed">-51</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">User can choose between radiology and neurology view directions (patient left/ri<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5536" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ght on screen right).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @cpinter (2023-06-19 12:55 UTC)

<p>Just a small observation here: when I called the first versions of Subject hierarchy “Patient hierarchy” it was deemed not appropriate because Slicer is not strictly for use in humans. Just as demonstrated here in this topic - the images are pre-clinical. In the same spirit I don’t think we should call these options “patient right is screen left” etc, but use the word “subject”. <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #10 by @pieper (2023-06-19 18:26 UTC)

<p>I’m okay with changing to consistently use “subject”.  We do use Patient in the DICOM module, since that’s what’s used in the standard, but I don’t think it shows up much anywhere else in the program.</p>

---

## Post #11 by @lassoan (2023-06-19 20:01 UTC)

<p>I agree when it’s not DICOM then “subject” would be better than “patient”. It is my fault, I just haven’t considered this when I introduced the name of the new setting.</p>

---

## Post #12 by @jamesobutler (2023-06-19 21:23 UTC)

<p>For pre-clinical images that use DICOM as the file format, is it standard to use “Patient” instead of “Subject” or “Animal”? I’m not familiar with the usage of pre-clinical image metadata in DICOM format.</p>

---

## Post #13 by @pieper (2023-06-19 22:08 UTC)

<p>Yes, I remember David Clunie telling me they always use patient, even if it’s just a normal control subject or even a phantom.  Legacy I guess, but it’s the standard.</p>

---

## Post #14 by @muratmaga (2025-01-24 20:54 UTC)

<p>I would rather have the standard terms radiology vs neurology convention used.</p>
<p><a href="https://nipy.org/nibabel/neuro_radio_conventions.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://nipy.org/nibabel/neuro_radio_conventions.html</a></p>
<p>And I second replace patient with subject.</p>

---
