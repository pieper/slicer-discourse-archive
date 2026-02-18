# Improve TotalSegmentator pre-segmentation speed

**Topic ID**: 27238
**Date**: 2023-01-14
**URL**: https://discourse.slicer.org/t/improve-totalsegmentator-pre-segmentation-speed/27238

---

## Post #1 by @rbumm (2023-01-14 10:05 UTC)

<p>Interesting to see that Jakob has implemented a “roi_subset” option in the latest version of the TotalSegmentator program, which allows for generating only the organs/structures that you would want to see or save.</p>
<p>Tested</p>
<p>python TotalSegmentator -i “C:\input.nii.gz” -o “C:\segmentation” --roi_subset lung_upper_lobe_right lung_middle_lobe_right lung_lower_lobe_right</p>
<p>from the command line and it works great, reducing the time needed to save the structures from 34 s (104 segmentations) to 6.6 s (3 segmentations).</p>

---

## Post #2 by @lassoan (2023-01-14 16:19 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="27238">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Interesting to see that Jakob has implemented a “roi_subset” option in the latest version of the TotalSegmentator program</p>
</blockquote>
</aside>
<p>I’ve asked him to implement this feature because because fast pre-segmentation saving took 1.5 minutes on my computer, because all structures were saved. He implemented it within a day!</p>
<p>We now just need to update the Slicer extension to use this new parameter. <a class="mention" href="/u/rbumm">@rbumm</a> it would be nice if you could give it a try. It could be implemented by changing the <code>requiresPreSegmentation</code> property in the <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/TotalSegmentator/TotalSegmentator.py#L308">tasks descriptions</a> from a Boolean flag to a list of segment names that are required and pass that to the pre-segmentation.</p>

---

## Post #3 by @rbumm (2023-01-14 16:54 UTC)

<p>Sure, I will give it a try.</p>
<p><code> --roi-subset</code> can actually be set and has benefits during any TotalSegmentation and would not only be useful for tasks in which requirePreSegmentation is True. Should we better add it as another, independent self.tasks entry in the <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/b27e1d65949d83bca4c9ee4e41fe353ab2a0ff3d/TotalSegmentator/TotalSegmentator.py#L283">extension class logic</a>?</p>

---

## Post #4 by @rbumm (2023-01-14 17:13 UTC)

<p>The next question is how we would implement the selection of organs/structures in the TotalSegmentator extension UI. Maybe a ListWidget with MultiSelect?</p>

---

## Post #5 by @rbumm (2023-01-15 17:30 UTC)

<p>Will be up for testing on TotelSegmentator extension GitHub in some minutes (new branch).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87b5c28ae71e3dfccfd6720c172606903048d0bb.png" data-download-href="/uploads/short-url/jmxSoBA40gAmPCtFPr1WGPwQFHJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87b5c28ae71e3dfccfd6720c172606903048d0bb_2_690x315.png" alt="image" data-base62-sha1="jmxSoBA40gAmPCtFPr1WGPwQFHJ" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87b5c28ae71e3dfccfd6720c172606903048d0bb_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87b5c28ae71e3dfccfd6720c172606903048d0bb_2_1035x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/87b5c28ae71e3dfccfd6720c172606903048d0bb_2_1380x630.png 2x" data-dominant-color="A4A4AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1905×870 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2023-01-15 20:37 UTC)

<p>I don’t think we need (and therefore we probably shouldn’t) add GUI for segment selection, because we know exactly what segments are needed from the pre-segmentation step; and for the full segmentation we don’t need segment selection (as it would complicate the GUI and in most cases it would slow down segment saving, because loading a few segments one-by-one takes longer than loading 100 segments all at once).</p>
<p>Let’s continue the discussion in the comment section of your pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/lassoan/SlicerTotalSegmentator/pull/11">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/11" target="_blank" rel="noopener">github.com/lassoan/SlicerTotalSegmentator</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/11" target="_blank" rel="noopener">ENH: add the TotalSegmentator roi_subset option</a>
      </h4>

    <div class="branches">
      <code>lassoan:main</code> ← <code>rbumm:roi_subset_dev_branch</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-01-15" data-time="17:39:02" data-timezone="UTC">05:39PM - 15 Jan 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/rbumm" target="_blank" rel="noopener">
            <img alt="rbumm" src="https://avatars.githubusercontent.com/u/18140094?v=4" class="onebox-avatar-inline" width="20" height="20">
            rbumm
          </a>
        </div>

        <div class="lines" title="1 commits changed 2 files with 58 additions and 10 deletions">
          <a href="https://github.com/lassoan/SlicerTotalSegmentator/pull/11/files" target="_blank" rel="noopener">
            <span class="added">+58</span>
            <span class="removed">-10</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">- choose organ/structure from a sorted QListWidget
- multilselect is possible</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @rbumm (2023-01-16 10:59 UTC)

<p>Agreed, but let me just my response from GitHub</p>
<p><em>Thank you for your comments. I think implementing this in the GUI would be helpful because many users would just focus on 3-5 organs/structures of interest when using TS. Ideally, you would want to be able to save your selection of choice (f.e. liver only) for future use. It is very helpful to have the roi_subset option in the logic when I call the logic from Lung CT Segmenter, because it saves nearly a minute of saving time (I could just ask for lobes and airways).</em></p>
<p>here to enable a good discussion.</p>

---
