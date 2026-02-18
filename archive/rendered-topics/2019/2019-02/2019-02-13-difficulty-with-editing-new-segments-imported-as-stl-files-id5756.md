# Difficulty with editing new segments imported as stl files

**Topic ID**: 5756
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/difficulty-with-editing-new-segments-imported-as-stl-files/5756

---

## Post #1 by @cricar01 (2019-02-13 13:39 UTC)

<p>Operating system: Mac High Sierra 10.13.6<br>
Slicer version: 3D Slicer 4.11.0<br>
Expected behavior: Import stl file, convert from model to segment, edit the segment normally<br>
Actual behavior: Unable to edit imported segment</p>
<p>Hi, there! I have been working on an independent project with 3D slicer to better understand the pulmonary vascular anatomy, and so far it has been a huge success and very fun. However, I have run into a new problem and can’t seem to find the answer on the online forums (or at least I don’t seem to be asking the right questions). I would be so grateful if you could offer some help!</p>
<p>So far, I have created detailed segmentations of the airway, pulmonary artery, pulmonary vein, and fissures based of a de-identified CT scan. However, now that I am going to print these segmentations, they are far too complex and I am needing to go back and simplify them a bit. The issue is, whenever I take the stl file (ie airway.stl), drag and drop into a new scene in 3D slicer, create a new transform from that model, then create a new segment based on that transform, the segment editor buttons are all greyed out so I can’t click on them. When I drag and drop the stl file into my old scene that has all the saved airway, PA, PV, and fissure segments, I can get it to come up as a new segment and the buttons are clickable, but when I go to edit my new segment it changes that whole segment, not just the area I was working on.</p>
<p>I have attached some pics below if that helps at all.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26d574505dc6d09ce0e4f84deac610ec9733792f.png" data-download-href="/uploads/short-url/5xxsZTIaGCbi5Hrz44MHnbP4yzZ.png?dl=1" title="02%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26d574505dc6d09ce0e4f84deac610ec9733792f_2_690x406.png" alt="02%20PM" data-base62-sha1="5xxsZTIaGCbi5Hrz44MHnbP4yzZ" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26d574505dc6d09ce0e4f84deac610ec9733792f_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26d574505dc6d09ce0e4f84deac610ec9733792f_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26d574505dc6d09ce0e4f84deac610ec9733792f_2_1380x812.png 2x" data-dominant-color="C2C4DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02%20PM</span><span class="informations">1677×987 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> !</p>
<p>This is my data showing that I imported the airway.stl model, made a transform, and then made a segmentation from that transform successfully.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07ef74749f470be0dc784656ec422aa5d9985d0d.png" data-download-href="/uploads/short-url/18cn4cjuVgpZmToHfYJ7OIwHIG9.png?dl=1" title="21%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07ef74749f470be0dc784656ec422aa5d9985d0d_2_690x406.png" alt="21%20PM" data-base62-sha1="18cn4cjuVgpZmToHfYJ7OIwHIG9" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07ef74749f470be0dc784656ec422aa5d9985d0d_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07ef74749f470be0dc784656ec422aa5d9985d0d_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07ef74749f470be0dc784656ec422aa5d9985d0d_2_1380x812.png 2x" data-dominant-color="C1C4DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21%20PM</span><span class="informations">1676×988 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see here, when I go to edit this segment, all the edit buttons are greyed out.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e491ebb98c99f37e650912b815cb47fbfd8aa43e.png" data-download-href="/uploads/short-url/wC1uOZ55uapSc2OIM3cCHuChj0q.png?dl=1" title="43%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e491ebb98c99f37e650912b815cb47fbfd8aa43e_2_690x464.png" alt="43%20PM" data-base62-sha1="wC1uOZ55uapSc2OIM3cCHuChj0q" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e491ebb98c99f37e650912b815cb47fbfd8aa43e_2_690x464.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e491ebb98c99f37e650912b815cb47fbfd8aa43e_2_1035x696.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e491ebb98c99f37e650912b815cb47fbfd8aa43e_2_1380x928.png 2x" data-dominant-color="C0C4DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">43%20PM</span><span class="informations">1600×1078 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In this example, I added PAsmoothed.stl to my existing scene with the other segments, and the segment editor buttons are still lit up, but chaos breaks loose when I try to edit it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9fda83f328a0de94f319c000d64e6d2ce2fec52.png" data-download-href="/uploads/short-url/sOTqDwaWUEP6ARFqWetjxRXGKNY.png?dl=1" title="04%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9fda83f328a0de94f319c000d64e6d2ce2fec52_2_690x463.png" alt="04%20PM" data-base62-sha1="sOTqDwaWUEP6ARFqWetjxRXGKNY" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9fda83f328a0de94f319c000d64e6d2ce2fec52_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9fda83f328a0de94f319c000d64e6d2ce2fec52_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9fda83f328a0de94f319c000d64e6d2ce2fec52_2_1380x926.png 2x" data-dominant-color="C1C5DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04%20PM</span><span class="informations">1600×1074 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do you see how the branches of the vessel are weirdly shrunken? All I tried to do was delete the left half of the image with the scissor tool just as an experiment, and this was the result.</p>
<p>Again, if you are able to get back to me with some guidance that would be greatly appreciated. Thanks so much!</p>

---

## Post #2 by @cpinter (2019-02-13 14:40 UTC)

<p>In your second screenshot you cannot edit because there is no anatomical volume selected. That’s why Segment Editor is asking you to “Select master volume to enable editing”, as shown in your screenshot as well.</p>
<p>In the third case, I can see a master volume. If that “6: CHEST…” image occupies the same space in 3D as your imported STL, then you should be able to edit it. You can verify that by going to Volume Rendering and showing the CT in 3D.</p>
<p>If “chaos breaks loose” means what you described next that the vessels have shrunk, then it’s because of smoothing. When you import an STL into segmentation and edit it, then in the background the model is converted to a labelmap. Then when you show it in 3D again, then default smoothing is performed, hence the data loss.</p>
<p>You can oversample the labelmap:</p>
<ul>
<li>Use 4.10.1 or latest nightly</li>
<li>Create new segmentation node in Segmentations module</li>
<li>In Representations section make Closed surface as master (because you want to have control over the geometry of the labelmap afterwards)</li>
<li>Import model in Import/Export section</li>
<li>In Representations section long-click Create and choose Advanced create</li>
<li>Click the only path in the top part</li>
<li>Click Specify geometry button in the bottom part</li>
<li>Select your CT volume</li>
<li>Specify an oversampling factor (2 should be fine, 3 even higher resolution, but 4 may occupy too much memory)</li>
<li>Click OK</li>
<li>Go to Segment Editor and do your thing</li>
</ul>
<p>You can also disable smoothing to prevent any shrinking (but after oversampling it might not be necessary):</p><aside class="quote quote-modified" data-post="16" data-topic="883">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/option-to-disable-smoothing-of-the-segment-surfaces-in-segment-editor/883/16">Option to disable smoothing of the segment surfaces in Segment Editor</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    This is implemented now in Slicer <a href="https://github.com/Slicer/Slicer/commit/06ae9980af2c01a8f38ee2e7cfd930375f729b6d">master branch</a> and should be available in tomorrow’s nightly build. A checkbox is available directly in the “Show 3D” button’s menu: 
[image]
  </blockquote>
</aside>


---

## Post #3 by @cricar01 (2019-02-14 02:09 UTC)

<p>Dear 3D slicer forum,</p>
<p>Thanks so much for the help! I was able to make changes once I imported my CT scans and selected them as the master volume. In terms of the smoothing issue, I tried the oversampling the label map instructions, and when I went to do segment editor, an error message appeared saying that I needed to have a binary label map, and that I had closed surface selected. It would not let me make edits unless I switched back to binary label map. Am I still missing something? Not a big deal at this point though, this was a lot of help!</p>
<p>Sincerely,</p>
<p>Caroline</p>

---

## Post #4 by @cpinter (2019-02-14 13:51 UTC)

<aside class="quote no-group" data-username="cricar01" data-post="3" data-topic="5756">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/ce73a5/48.png" class="avatar"> cricar01:</div>
<blockquote>
<p>an error message appeared saying that I needed to have a binary label map, and that I had closed surface selected</p>
</blockquote>
</aside>
<p>That’s fine, as Segment Editor requires the segmentation to have Binary labelmap as master, and you had a closed surface because of the custom initialization you needed to do with the labelmap. Just click OK and edit away <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> If you want to avoid the message, then after binary labelmap conversion (with oversampling), click Make master for the labelmap.</p>

---
