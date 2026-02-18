# Renaming segments based on .txt file

**Topic ID**: 24198
**Date**: 2022-07-06
**URL**: https://discourse.slicer.org/t/renaming-segments-based-on-txt-file/24198

---

## Post #1 by @coco (2022-07-06 08:30 UTC)

<p>Dear all,<br>
I’m new to Slicer which I learning and finding fantastic, steep learning curve though. So I hope this is not too obvious but I have a lot of segments which are numbered and I would like to rename them based on a txt file, is this possible ?</p>
<p>I previously found this thread</p><aside class="quote" data-post="1" data-topic="16575">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akshay_pillai/48/8301_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-rename-segments-in-a-segmentation-node/16575">How to rename segments in a segmentation node?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Operating system: Windows 10 
Slicer version:4.11 
How can I change the names of segments in a segmentation. I can do this manually in the GUI but I want to know if there is any way to do this programmatically. I can’t see any mrml node ids for each individual segment.
  </blockquote>
</aside>
<p>
but I am not sure how this would address my point.</p>
<p>Thanks for your help<br>
best</p>

---

## Post #2 by @lassoan (2022-07-06 15:19 UTC)

<p>This is a good question. If you have a color table (specifying name and color for each label value) then load that first into the application and then when you load the segmentation select this color table as <code>Color node</code> in the <code>Options</code> section.</p>
<p>Specification of the color table file format is available <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-file-format-txt-ctbl">here</a>.</p>

---

## Post #3 by @coco (2022-07-08 07:12 UTC)

<p>Unfortunately, I have in excess of 800 segments so the color table would not be convenient. I have these segments (and apologies if I am mixing terms such as segments and objects) under a seg.nrrd. file where all segments are within one file or +800 single .obj files so I guess my best best is to rename the individual files which can be easily done using a text file and a bit of command lines.<br>
Thanks</p>

---

## Post #4 by @muratmaga (2022-07-08 16:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Specification of the color table file format is available here.</p>
</blockquote>
</aside>
<p>There is no link attached. I am also curious to learn this…</p>

---

## Post #5 by @lassoan (2022-07-08 16:55 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>There is no link attached. I am also curious to learn this…</p>
</blockquote>
</aside>
<p>Good catch, I’ve fixed the link above.</p>
<aside class="quote no-group" data-username="coco" data-post="3" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/8797f3/48.png" class="avatar"> coco:</div>
<blockquote>
<p>Unfortunately, I have in excess of 800 segments so the color table would not be convenient</p>
</blockquote>
</aside>
<p>You might have misunderstood how a color table can be created or used. It is just a text file that you should be able to very easily create using Excel or any text editor, from the list of segment names that you already have. You can then load it into the scene and select it when loading the segmentation to use it for naming segments.</p>
<p>You can of course modify segment names in the <code>.seg.nrrd</code> file as well, as segment names are stored in plain text. To allow easier editing, you can save the segmentation file in <code>.seg.nhdr</code> format, which has the header in a separate text file.</p>
<p>If you have your segmentation in .obj files then you can load all of them into Slicer and import them into a segmentation (for example, you can put them into a folder in Data module, right-click on the folder, and choose “Convert models to segmentation node”).</p>

---

## Post #6 by @muratmaga (2022-07-08 17:19 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="5" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You might have misunderstood how a color table ca be created or used. It is just a text file that you should be able to very easily create using Excel or any text editor, from the list of segment names that you already have. You can then load it into the scene and select it when loading the segmentation to use it for naming segments.</p>
</blockquote>
</aside>
<p>I am also interested in this, but it is not clear how the matching is done. I saved that ctbl file and loaded into the Slicer session. Then, I created a random segmentation from MRhead with three segments (which went segment_1, segment_2), saved the segmentation and reloaded the seg_nrrd file with the color table option. Instead of artery, bone and connective_tissue it came back with segment_1, segment_2.</p>
<p>Do the colors have to match exactly? Or is it the order of the segments?</p>

---

## Post #7 by @lassoan (2022-07-08 17:39 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>reloaded the seg_nrrd file</p>
</blockquote>
</aside>
<p>If you you load a .seg.nrrd file then you already have the segment names in the file, so the color table is not needed - it will not be used.</p>
<p>If you export the segmentation into a simple labelmap file (.nrrd) that does not have any of the segmentation metadata then the color table will be used. Labelmap voxel values are matched to color table index. Number of segments or entries in the color table does not matter. Order in color table probably does not matter but in all files that Slicer creates and that I have seen so far have entries listed in ascending order based on color index.</p>

---

## Post #8 by @muratmaga (2022-07-08 17:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you you load a .seg.nrrd file then you already have the segment names in the file, so the color table is not needed - it will not be used.</p>
</blockquote>
</aside>
<p>We are working on segmentations by multiple users/groups. The goal is to use the results for ML training. Maintaining consistency and ordering of the labels/segments has been a challenge to say the least. We haven’t used the terminology as our terms are very different than what’s available.</p>
<p>Is that what you would suggest?</p>

---

## Post #9 by @lassoan (2022-07-08 18:36 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Maintaining consistency and ordering of the labels/segments has been a challenge to say the least. We haven’t used the terminology as our terms are very different than what’s available.</p>
</blockquote>
</aside>
<p>We recognized several years ago that it was not going to be possible to aggregate data from multiple sources, collected for various purposes and rely on a single mapping of label value → content. That’s why terminology support was introduced. It was probably too much ahead of its time and users just start to realize now why it is essential to use it.</p>
<p>Our proposed solution is to use seg.nrrd file for archiving data, which specifies the meaning of each label value (and volume layer, if there are overlapping segments) by using a coded term. Then, when the data is loaded from the seg.nrrd file, the user can choose what label values will be assigned to each term, for example using <a href="https://pypi.org/project/slicerio/">slicerio</a>. The slicerio Python package that can be pip-installed in any Python environment, which makes seg.nrrd file easily usable as a source data in any data preparation workflows.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="8" data-topic="24198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We haven’t used the terminology as our terms are very different than what’s available.</p>
</blockquote>
</aside>
<p>For users convenience, in the Slicer installer package we included two terminologies with some commonly used terms. However, this does not mean that you must use these terms and you could not use any other terms.</p>
<p>You can use any other terminology (TA2, TA98, MeSH, FMA, …) or if you find that any term is missing then you can specify your own. If you define your own terms it can make sense to add it to your Slicer extension so that your users can access it easily. The terminology file format should be self-explaining but you can learn more about it in <a href="https://qiicr.gitbook.io/dcmqi-guide/opening/coding_schemes">DCMQI project documentation</a>. You can use <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveAnnulusAnalysis/Resources/SlicerHeartSegmentationCategoryTypeModifier.json">terminology file in the SlicerHeart project</a> as a simple example.</p>

---
