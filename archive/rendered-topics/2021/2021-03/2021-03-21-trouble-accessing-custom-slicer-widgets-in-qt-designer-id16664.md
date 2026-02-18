# Trouble accessing custom Slicer widgets in QT Designer

**Topic ID**: 16664
**Date**: 2021-03-21
**URL**: https://discourse.slicer.org/t/trouble-accessing-custom-slicer-widgets-in-qt-designer/16664

---

## Post #1 by @jmhuie (2021-03-21 00:39 UTC)

<p>I am trying to edit the GUI of my module with QT Designer, but I noticed that I cannot see any of the custom CTK or MRML widgets. I copied (and edited) the UI file from the Segment Cross-Section Area module, which is why there are qMRMLNodeComboBoxes and such. See photo.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67d00f037245b55907bede475eefb67d9402f6d1.png" data-download-href="/uploads/short-url/eOmWt5guagJC7WULPIFMZwzKzWV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67d00f037245b55907bede475eefb67d9402f6d1_2_690x431.png" alt="image" data-base62-sha1="eOmWt5guagJC7WULPIFMZwzKzWV" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67d00f037245b55907bede475eefb67d9402f6d1_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67d00f037245b55907bede475eefb67d9402f6d1_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/67d00f037245b55907bede475eefb67d9402f6d1_2_1380x862.png 2x" data-dominant-color="E8E8E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3584×2240 586 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have tried reading <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/QtDesigner" rel="noopener nofollow ugc">this wiki page</a> but unfortunately, I just don’t fully understand. I think part of the issues is the fact that I am using a Mac. The “Edit UI” button, which is supposed to open Designer, doesn’t work. That is a known problem it seems. So instead, I downloaded QT Designer version 5.9.6 directly from <a href="https://build-system.fman.io/qt-designer-download" rel="noopener nofollow ugc">here</a>. Not sure if the version matters.</p>
<p>Because I am completely new to this, I’m not sure what is going on. My best guess is that because I downloaded Designer separately, it’s not automatically reading in the QTplugins folder. I could not figure out how to get it to do that.</p>
<p>Any help would be greatly appreciated. Thanks!</p>

---

## Post #2 by @pieper (2021-03-21 16:59 UTC)

<p>Yes, this is a known issue and there are some workarounds:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4700#issuecomment-681022893" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4700#issuecomment-681022893" target="_blank" rel="noopener">QT Designer does not start on MacOS</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:05:20" data-timezone="UTC">01:05AM - 13 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
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
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
