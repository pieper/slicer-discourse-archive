# View controller bar is thicker in Slicer-5.6.0

**Topic ID**: 33238
**Date**: 2023-12-05
**URL**: https://discourse.slicer.org/t/view-controller-bar-is-thicker-in-slicer-5-6-0/33238

---

## Post #1 by @rbumm (2023-12-05 16:28 UTC)

<p>The bars of the view windows are bigger than before - they take too much space - will this also be addressed?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7bbb515d40ffccaebc175976cb531384df3f004.png" data-download-href="/uploads/short-url/uMsOFMcVM7YCzlQulQGVZ3w0tpy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7bbb515d40ffccaebc175976cb531384df3f004_2_690x370.png" alt="image" data-base62-sha1="uMsOFMcVM7YCzlQulQGVZ3w0tpy" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7bbb515d40ffccaebc175976cb531384df3f004_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7bbb515d40ffccaebc175976cb531384df3f004_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7bbb515d40ffccaebc175976cb531384df3f004_2_1380x740.png 2x" data-dominant-color="4D4B53"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1427×767 26.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2023-12-05 16:31 UTC)

<p>The larger slice view controller buttons is by design and has been present in Slicer 5.5-Preview builds since September 13th.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7219">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7219" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7219" target="_blank" rel="noopener nofollow ugc">ENH: Remove fixed size buttons in view controller for better restyling</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:view-controller-button-styling</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-07" data-time="22:07:11" data-timezone="UTC">10:07PM - 07 Sep 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="3 commits changed 4 files with 1 additions and 10 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7219/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-10</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">If restyling ToolButtons as a whole through QSS with a fixed vertical size set, <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7219" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">but a variable width allowed, the fixed size specification in qMRMLViewControllerBar was still forcing these buttons to be 15px wide.

| `main` | This PR |
|--------|----------|
|![image](https://github.com/Slicer/Slicer/assets/15837524/37f1351e-a30d-4c19-a063-52df2a026466)|![image](https://github.com/Slicer/Slicer/assets/15837524/a113dd03-010a-4bb2-83ff-81f32ed4454a)|

Now these buttons are sized based on their contents which in this case is their icon. This results in a slightly different spacing and sizing as previously the FixedSize call was actually cutting off part of the ToolButton's normal margin/padding. However I think the end result is near identical and functionally acts the same. This change ultimately allows for better ways of restyling QToolButtons through QSS.

---------------------------------------
I could also issue a separate change to allow these QToolButton's in the slice view controller to be their default size based on their normal 24px icons (remove any fixed size or iconSize specifications for these QToolButtons). This will result in the buttons being the same size as those in the Slice controller floating pop-up widget which I think is more consistent and the larger size buttons make the accessibility better to avoid mis-clicks and speeds up the time it takes to click successfully. It would look like the following:

| `main` | Default size for 24px icon |
|--------|----------|
![image](https://github.com/Slicer/Slicer/assets/15837524/cd5ae01d-a8c6-4136-b9fc-ad7e0e0cd7d1)|![image](https://github.com/Slicer/Slicer/assets/15837524/db7f8720-ebab-4996-b1c9-45593bc6a451)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jamesobutler (2023-12-05 18:23 UTC)

<p>We had discussed a comfort and cozy mode, but I don’t have full plans of how that will consistently be applied across the entire application for a common user experience.</p>

---

## Post #4 by @lassoan (2023-12-05 20:17 UTC)

<p>I hoped that I would get used to the thicker view controller bars, because the difference is not all that much and the larger size makes the pushpin icon a bit easier to click. However, after several months of use on a large monitor, I still feel that these bars take up too much space.</p>
<p>If I run this line of code to hide the slice view controllers it feels like a breath of fresh air:</p>
<pre data-code-wrap="python"><code class="lang-python">slicer.util.setViewControllersVisible(False)
</code></pre>
<p>We can already display a vertical scrollbar to browse slices:</p>
<pre><code class="lang-auto">for slice in ['Red', 'Yellow', 'Green']:
    sw = slicer.app.layoutManager().sliceWidget(slice)
    sw.setSliceOffsetSliderOrientation(qt.Qt.Vertical)
    sw.sliceController().setVisible(False)
    #sw.setSliceOffsetSliderOrientation(qt.Qt.Horizontal)
    #sw.sliceController().setVisible(True)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08088f23e129b6a3d137a27301d892ae93f9faba.jpeg" data-download-href="/uploads/short-url/1949LXOjT0HPICv5YSa9K2bswDU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08088f23e129b6a3d137a27301d892ae93f9faba_2_690x397.jpeg" alt="image" data-base62-sha1="1949LXOjT0HPICv5YSa9K2bswDU" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08088f23e129b6a3d137a27301d892ae93f9faba_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08088f23e129b6a3d137a27301d892ae93f9faba_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08088f23e129b6a3d137a27301d892ae93f9faba_2_1380x794.jpeg 2x" data-dominant-color="434247"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1105 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If we implemented display of view color (e.g., as a colored frame) and some view information as corner annotations, and make the slice view controller available (e.g., in the context menu) then we could remove the slice view controller bars completely.</p>

---

## Post #5 by @pieper (2023-12-05 22:45 UTC)

<p>+1 for uncluttering the views and displaying things only when needed, so long as it doesn’t introduce multiple clicks to do simple things.  It would be nice too if the drag handles weren’t so prominent.  Maybe if they only showed up when the mouse is over the drag area.  This kind of behavior is nice in a lot of interfaces to remove clutter, but we should use it carefully to avoid lots of stuff flashing in and out of view as you mouse around.</p>

---

## Post #6 by @lassoan (2023-12-05 23:13 UTC)

<p>Fully agree. There should be a lot of possibilities to declutter without impacting usability.</p>
<p>We could keep a vertical slider for slice browsing and buttons above it for resetting FOV and maximize view. We could display layout name, color, slice offset, etc. in corner annotations.</p>
<p>The rest of the options (that are shown when the pushpin icon is clicked) could be added as right-click menu, or maybe by clicking on certain corner annotations, or perhaps properties of the current view (where the user last clicked in) could be editable in the DataProbe… We should look at other examples that users like and see what makes sense to adopt.</p>
<p>Maybe we could create a project about this for the upcoming project week?</p>

---
