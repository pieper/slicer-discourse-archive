---
topic_id: 23915
title: "Autosegmentation Of Problematic Lung Ct"
date: 2022-06-17
url: https://discourse.slicer.org/t/23915
---

# Autosegmentation of problematic Lung CT

**Topic ID**: 23915
**Date**: 2022-06-17
**URL**: https://discourse.slicer.org/t/autosegmentation-of-problematic-lung-ct/23915

---

## Post #1 by @rbumm (2022-06-17 17:26 UTC)

<p>During the preparation for the MONAILabel workshop, I noticed that in the public ML Task06_lung dataset there are several datasets with strange contrasts that display very “dark” initially.<br>
Example: lung_049</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/244cb4d1c826feca4e4bb7a57121487c2a8ec947.jpeg" alt="image" data-base62-sha1="5b7wX0YqZ3knrbZFHz1GVu6546b" width="643" height="355"></p>
<p>These data are difficult for both manually assisted as well as AI segmentation. How do you guys handle these data? Could preprocessing help here?</p>

---

## Post #2 by @lassoan (2022-06-17 18:13 UTC)

<p>This has been discussed here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/issues/447">
  <header class="source">

      <a href="https://github.com/Project-MONAI/MONAILabel/issues/447" target="_blank" rel="noopener">github.com/Project-MONAI/MONAILabel</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Project-MONAI/MONAILabel/issues/447" target="_blank" rel="noopener">Setting default window width (WW) and default window level (WL)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-10-08" data-time="11:49:34" data-timezone="UTC">11:49AM - 08 Oct 21 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2022-04-24" data-time="14:33:12" data-timezone="UTC">02:33PM - 24 Apr 22 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/masadcv" target="_blank" rel="noopener">
          <img alt="masadcv" src="https://avatars.githubusercontent.com/u/3410225?v=4" class="onebox-avatar-inline" width="20" height="20">
          masadcv
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          backlog
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">We have had some feedback from clinical partners regarding setting of window for<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> highlighting different organs.
The window/levels are defined typically by window width (WW) and window level (WL). This is then used in the following formula to set the min/max levels for CT images.
w_min = WL - WW/2
w_max = WL+WW/2

More info about this can be found here: https://radiopaedia.org/articles/windowing-ct?lang=gb

There are known WL/WW values for different organs/tissues (as listed in the above link). 

For example, a lung window is typically defined as WW=1500 and WL=-600. This has the following effect on visualizing the image volume:

Before applying lung window:
![image](https://user-images.githubusercontent.com/3410225/136550503-66fc1ba3-14f2-405a-8e06-afad4c3fc47f.png)

After applying lung window (WW=1500, WL=-600):
![image](https://user-images.githubusercontent.com/3410225/136550684-ba7a0ca4-9757-4de9-96c5-d132a8b30165.png)

You can notice that it highlights tissues/lesions inside lung better. The above is just one example, the values for WW/WL can vary for different organs and institute.

In 3D Slicer, the above can be achieved as:
```
WL=-600; WW=1500
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
volumeNode.GetDisplayNode().SetAutoWindowLevel(False)
volumeNode.GetDisplayNode().SetWindowLevelMinMax(WL-WW/2, WL+WW/2)
```

Does this sound like something we can pass as argument from an app as default, given that we know the target organ/tissue and its WL/WW. In cases where these are not present, we can skip updating the above. In other cases where the user wants to change these, there is a window level button that can be used to adjust manually. 

cc: @tvercaut</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Add a comment there, describing why it is a problem for you.</p>

---
