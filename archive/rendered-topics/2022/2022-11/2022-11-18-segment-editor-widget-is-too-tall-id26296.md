# Segment Editor widget is too tall

**Topic ID**: 26296
**Date**: 2022-11-18
**URL**: https://discourse.slicer.org/t/segment-editor-widget-is-too-tall/26296

---

## Post #1 by @FUFU (2022-11-18 08:07 UTC)

<p>Hello! I’m new here but I also have a question about the viewing of the slices. My company has developed a plug-in. When running 3D-SLicer 4.8, the resulview looks like this.  Everything is fine</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44a9227efa2ec938b21bee70e3ae20048826b39a.jpeg" data-download-href="/uploads/short-url/9NoPVqKYXbB7iFuteq3yx0mO91E.jpeg?dl=1" title="6cf9efc2854e4a0b7545ccba7e6ad83" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44a9227efa2ec938b21bee70e3ae20048826b39a_2_657x500.jpeg" alt="6cf9efc2854e4a0b7545ccba7e6ad83" data-base62-sha1="9NoPVqKYXbB7iFuteq3yx0mO91E" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44a9227efa2ec938b21bee70e3ae20048826b39a_2_657x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44a9227efa2ec938b21bee70e3ae20048826b39a_2_985x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44a9227efa2ec938b21bee70e3ae20048826b39a.jpeg 2x" data-dominant-color="ADADAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">6cf9efc2854e4a0b7545ccba7e6ad83</span><span class="informations">1128×858 71.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But because slicer’s upgrade deleted the editor module and changed it into the segmentation module,The height of the SegmentEditor section is much larger than that of the previous editor, which makes the resultview section much smaller</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea5e5b1851afb112d0525521eb6ed135630c908.png" data-download-href="/uploads/short-url/8Wd2fMRzhokG4Mc8UibonoKz2ac.png?dl=1" title="1564cca0e34a1b71bcf83e627af80bd" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea5e5b1851afb112d0525521eb6ed135630c908_2_357x499.png" alt="1564cca0e34a1b71bcf83e627af80bd" data-base62-sha1="8Wd2fMRzhokG4Mc8UibonoKz2ac" width="357" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea5e5b1851afb112d0525521eb6ed135630c908_2_357x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3ea5e5b1851afb112d0525521eb6ed135630c908_2_535x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea5e5b1851afb112d0525521eb6ed135630c908.png 2x" data-dominant-color="DBDDE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1564cca0e34a1b71bcf83e627af80bd</span><span class="informations">576×805 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This makes it difficult for the company’s annotator to use the resultview section.I wanted to change this by adjusting the code, but found that the size of the resultview widget is due to slicer’s window being scaled.And there is no api in qt.QTableView() that cannot resize a resultview</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b09b25657885c8e12e9460fbb7a07f3fcfb0c024.png" data-download-href="/uploads/short-url/pckqTiKfG1Hfsic6kmtomX66IFS.png?dl=1" title="1668758406149" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b09b25657885c8e12e9460fbb7a07f3fcfb0c024.png" alt="1668758406149" data-base62-sha1="pckqTiKfG1Hfsic6kmtomX66IFS" width="690" height="424" data-dominant-color="333233"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1668758406149</span><span class="informations">707×435 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
We need some ways to change the height of review. Thank you!!</p>

---

## Post #2 by @jamesobutler (2022-11-18 12:14 UTC)

<p>You may want to consider putting the segment editor effect list to the left of the “result view” to be similar to how the segment editor effect List is positioned to the left of the segment table view.</p>
<p>Or you can set the effectColumnCount to be say 6 or whatever amount you would like instead of the default 2. See the examples provided in the commit message body at the link below:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/5a44b5e47650ea7b954dbfa52bb28da10cd19a32">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/5a44b5e47650ea7b954dbfa52bb28da10cd19a32" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/5a44b5e47650ea7b954dbfa52bb28da10cd19a32" target="_blank" rel="noopener nofollow ugc">ENH: Improve configurability of Segment Editor effect list</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-09-20" data-time="13:23:26" data-timezone="UTC">01:23PM - 20 Sep 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 3 files with 38 additions and 8 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/5a44b5e47650ea7b954dbfa52bb28da10cd19a32" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+38</span>
          <span class="removed">-8</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Improve visual appearance of effect buttons by making all the same width.
Make e<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/5a44b5e47650ea7b954dbfa52bb28da10cd19a32" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ffectColumnCount a property so it can be set in Qt Designer.

Examples of how to customize Segment Editor appearance:

editor = getModuleGui('SegmentEditor').editor

# Text below (two-column)
editor.effectButtonStyle = qt.Qt.ToolButtonTextUnderIcon
editor.setEffectColumnCount(2)

# Text below (three-column)
editor.effectButtonStyle = qt.Qt.ToolButtonTextUnderIcon
editor.setEffectColumnCount(3)
findChild(editor,"EffectsGroupBox").setMaximumWidth(200)

# Text beside
editor.setEffectColumnCount(1)
editor.effectButtonStyle = qt.Qt.ToolButtonTextBesideIcon</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2022-11-19 17:36 UTC)

<p>You can also put the Segment Editor widget and the table in collapsible widgets. You can even put the widgets in a button group and make them exclusive, which means that when you open one it automatically collapses the other.</p>
<p>But probably it is much better to switch to a view layout that has a table view and display your table there.</p>

---

## Post #5 by @FUFU (2022-11-28 08:01 UTC)

<p>Thanks! But that table is very important to me, so I’d rather not fold it</p>

---

## Post #6 by @lassoan (2022-11-28 14:05 UTC)

<p>If you always want to see the table then I would recommend to switch to a view layout that has a table view and display your table there.</p>

---

## Post #8 by @FUFU (2022-12-01 01:41 UTC)

<p>If you have this problem, try using a few lines of my code.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/684431fd2d4bea35d373868033766567f725699f.png" alt="1669858854962" data-base62-sha1="eSnLpbMzeuwsdd9cnNCMzjuQkrB" width="606" height="213"></p>

---

## Post #9 by @FUFU (2022-12-01 01:45 UTC)

<p>It to everyone. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @FUFU (2022-12-01 03:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f258bb87ab46ad4e5d2cce07710ba97454c55a2.png" data-download-href="/uploads/short-url/i8N4Ym5PklJxSGpOZAMifhqh5V8.png?dl=1" title="1669863997635" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f258bb87ab46ad4e5d2cce07710ba97454c55a2.png" alt="1669863997635" data-base62-sha1="i8N4Ym5PklJxSGpOZAMifhqh5V8" width="316" height="500" data-dominant-color="F3F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1669863997635</span><span class="informations">488×771 6.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thank you for your very effective advice!!!</p>

---
