# Geometry all messed up in latest 5.7.0 pre-release?

**Topic ID**: 36072
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/geometry-all-messed-up-in-latest-5-7-0-pre-release/36072

---

## Post #1 by @Peng_Wang (2024-05-10 19:17 UTC)

<p>Previously aligned volumes no longer aligned in the pre-release version. It’s kind of obvious and since it’s “pre-release” I wonder if it is a known issue.</p>
<p>Steps to expose the bug: load a volume and place a fiducial. Using the Orient Scalar Volume module and perform some random orientation a couple of times and you will find the volume shifted.</p>

---

## Post #2 by @muratmaga (2024-05-10 19:20 UTC)

<p>which specific version of the preview release are you using?</p>

---

## Post #3 by @lassoan (2024-05-10 19:24 UTC)

<p>What is your reason for using the Orient Scalar Volume?<br>
What do you mean by “perform some random orientation”?<br>
What is your overall goal?</p>

---

## Post #4 by @Peng_Wang (2024-05-10 20:23 UTC)

<p>I am using the latest Linux pre-release download from the website (2024-05-03).</p>
<p>I am not using Orient Scalar Volume for any particular purpose I just found out the bug can be easily observed this way. Just choose some different orientation and hit apply and sometimes the volume shifted.</p>
<p>I compared to load a same volume in v5.6.2 and v5.7.0 and they show different transformation matrix and scan order between these 2 versions. Sometimes after I  transformed a volume and when I saved and reload the scene the volume also shifted.</p>
<p>I found there is a new Center of transformation option under Transform module and there is possibly some rework to the transformation and this bug could be resulting from that.</p>
<p>Trust me I have used Slicer for a long time. There is definitely something fundamentally wrong with current developmental release.</p>

---

## Post #5 by @muratmaga (2024-05-10 20:48 UTC)

<aside class="quote no-group" data-username="Peng_Wang" data-post="4" data-topic="36072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peng_wang/48/65535_2.png" class="avatar"> Peng_Wang:</div>
<blockquote>
<p>Trust me I have used Slicer for a long time. There is definitely something fundamentally wrong with current developmental release.</p>
</blockquote>
</aside>
<p>We trust you, but you need to more concretely describe the steps, and provide screenshots of it for us to undertand and reproduce the issue. If we can’t reproduce, it is hard to fix.</p>

---

## Post #6 by @Peng_Wang (2024-05-10 20:55 UTC)

<p>I am providing two volumes. You will find them aligned together in v5.6.2 but not in v5.7.0.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fo/ov5uhfi6n91ctfmmkkh1k/AGq11Ea5RIfPVo5WQhjSp8Q?rlkey=i81lf60sprg0v2g7wr5pn9wcy&amp;dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fo/ov5uhfi6n91ctfmmkkh1k/AGq11Ea5RIfPVo5WQhjSp8Q?rlkey=i81lf60sprg0v2g7wr5pn9wcy&amp;dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-folder-dropbox-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/scl/fo/ov5uhfi6n91ctfmmkkh1k/AGq11Ea5RIfPVo5WQhjSp8Q?rlkey=i81lf60sprg0v2g7wr5pn9wcy&amp;dl=0" target="_blank" rel="noopener nofollow ugc">SlicerTest</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also I tested them in MRView from MRTrix and they also aligned.</p>

---

## Post #7 by @lassoan (2024-05-12 11:53 UTC)

<p>If you use NIFTI format then all bets are off. In this format the image oroentation can be defined in redundant and inconsistent ways, which is interpreted differently in each software. It is really a shame that we need to deal with such basic issues, but many people in the neuroimaging community just uses a few software, so they are not aware of these serious issues around NIFTI; and many newcomers to the medical imaging field don’t know just how bad NIFTI is, so it remains widely used and it wastes everyone’s time.</p>
<p>Slicer uses ITK toolkit to read NIFTI images and so it will load such images the same way as every other ITK-based software. It seems that you would expect ITK to load your images differently, so the best would be to post it to the <a href="https://discourse.itk.org">ITK forum</a>. They will explain why ITK loads your images differently compared to MRTrix. Maybe invite MRTrix developers to the discussion, too, and let them come to an agreement. If major imaging libraries resolved inconsistencies in NIFTI images the same way then NIFTI users would suffer less.</p>

---

## Post #8 by @pieper (2024-05-12 14:27 UTC)

<p>Thanks for reporting <a class="mention" href="/u/peng_wang">@Peng_Wang</a> - I can reproduce this by comparing 5.6.1 to recent preview build.  In this case I don’t think nifti is to blame, but something has changed in Slicer, presumably with the latest version of ITK.</p>
<p>It’s a serious regression, so we should get to the bottom of this asap.<br>
I’ve filed an issue here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7742">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7742" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7742" target="_blank" rel="noopener">Incorrect geometry after running Orient Scalar Volume </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2024-05-12" data-time="14:23:56" data-timezone="UTC">02:23PM - 12 May 24 UTC</span>
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
    <p class="github-body-container">## Summary

Running the CLI module cases the result volume to be in the wrong <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">place.

## Steps to reproduce

1) Download Sample data (MRHead)
2) Run OrientScalarVolume with default LPS output into new volume
3) Put put one volume in foreground and one in background and see the shift

## Environment
- Slicer version: Slicer-5.7.0-2024-05-10, does not happen in 5.6.1
- Operating system: tested on mac</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It’s easy to reproduce and the CLI uses nrrd, so there’s something else going on.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8813621ea170e1ac4fc446f1c9020b1e3020b7b.jpeg" data-download-href="/uploads/short-url/xaPBESKEvksX1zDMQI5PxFlui0P.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8813621ea170e1ac4fc446f1c9020b1e3020b7b_2_690x454.jpeg" alt="image" data-base62-sha1="xaPBESKEvksX1zDMQI5PxFlui0P" width="690" height="454" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8813621ea170e1ac4fc446f1c9020b1e3020b7b_2_690x454.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8813621ea170e1ac4fc446f1c9020b1e3020b7b_2_1035x681.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8813621ea170e1ac4fc446f1c9020b1e3020b7b_2_1380x908.jpeg 2x" data-dominant-color="BDC0C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1266 212 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2024-05-12 14:32 UTC)

<aside class="quote no-group" data-username="Peng_Wang" data-post="6" data-topic="36072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/peng_wang/48/65535_2.png" class="avatar"> Peng_Wang:</div>
<blockquote>
<p>I am providing two volumes. You will find them aligned together in v5.6.2 but not in v5.7.0.</p>
</blockquote>
</aside>
<p>While all the problems with NIFTI format still holds, I agree that in this case something else is going on with <code>IntraOp2T1_Warped</code>. The file uses a left-handed image coordinate system, which is uncommon, but it is still valid. It gets normalized to a right-handed coordinate, which would be good, but this normalization seems to be computed incorrectly.</p>

---

## Post #10 by @lassoan (2024-05-12 14:37 UTC)

<p>The culprit is probably this change:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7627/files">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7627/files" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7627/files" target="_blank" rel="noopener">ENH: Improve vtkMRMLVolumeArchetypeStorageNode for left handed volumes</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>Thibault-Pelletier:enh_improve_left_handed_volume_loading</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-03-13" data-time="16:37:26" data-timezone="UTC">04:37PM - 13 Mar 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Thibault-Pelletier" target="_blank" rel="noopener">
            <img alt="Thibault-Pelletier" src="https://avatars.githubusercontent.com/u/58782295?v=4" class="onebox-avatar-inline" width="20" height="20">
            Thibault-Pelletier
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 102 additions and 3 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7627/files" target="_blank" rel="noopener">
            <span class="added">+102</span>
            <span class="removed">-3</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">* Automatically flip left handed volumes when loading into 3D Slicer to make the<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7627" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">m compatible with all algorithms. Fixes flipped normals in segmentation node for left handed volumes.

See related discussion here : 
https://discourse.slicer.org/t/slicer-segmentation-inverted-normals-for-closed-surface-representation/34762</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I should have suspected that it was wrong, because images should only be ever transformed with homogeneous transformation matrices, never with just flipping.</p>

---

## Post #11 by @Peng_Wang (2024-05-12 22:15 UTC)

<p>The problem is not only with the volume <code>IntraOp2T1_Warped</code>. Sometimes when I load back the volume saved by Slicer itself it also shifted. Also as shown by Pieper above you can reproduce the bug using Orient Scalar Volume not dealing with any on-disk files.</p>
<p>PS. Also I tried with the latest ITK-SNAP 4.2 (Apr 22, 2024) it also displayed the volumes correctly.</p>
<p>PPS. I remember this problem only showed in recent build. Using the download page url offset parameter I am trying to pinpoint the problematic build:</p>
<p>it’s somewhere in between [revision 32753 built 2024-03-15 ] and [revision 32789 built 2024-04-02 ].</p>
<p>As I suspected it’s also when the “Center of Transformation” started to show up in the Transform module.</p>

---

## Post #12 by @lassoan (2024-05-13 11:58 UTC)

<p>The problem is the change that I pointed out <a href="https://discourse.slicer.org/t/geometry-all-messed-up-in-latest-5-7-0-pre-release/36072/10">above</a>. When an image with left-handed IJK coordinate system is encountered then the K axis is automatically flipped to turn it into a right-handed coordinate system. However, the computation of the new image origin was incorrect. I’ll submit a pull request with the fix today.</p>

---

## Post #13 by @lassoan (2024-05-13 12:52 UTC)

<p>The fix is available in this pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7746">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7746" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7746" target="_blank" rel="noopener">Fix reading of images that have left-handed IJK coordinate system</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-lefthanded-image-reading</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-05-13" data-time="12:51:38" data-timezone="UTC">12:51PM - 13 May 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="3 commits changed 6 files with 153 additions and 49 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7746/files" target="_blank" rel="noopener">
            <span class="added">+153</span>
            <span class="removed">-49</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fix regression introduced in https://github.com/Slicer/Slicer/pull/7627 that ima<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7746" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ge origin is not computed correctly when flipping K axis of an image to make it right-handed.

Fixes issue discussed in https://discourse.slicer.org/t/geometry-all-messed-up-in-latest-5-7-0-pre-release/36072/12</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Probably it will be available in the Slicer Preview Release within a few days.</p>

---

## Post #14 by @Peng_Wang (2024-05-13 17:52 UTC)

<p>When I looked at my other problematic volumes they are indeed left-handed too. And when Slicer save them they remained left-handed. So thank you, this should fix it.</p>

---

## Post #15 by @lassoan (2024-05-13 18:17 UTC)

<p>The fix has been merged, so Slicer Preview Release that is downloaded tomorrow or later will include it.</p>

---
