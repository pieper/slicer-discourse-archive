# Save segmentation with orig values as nii.gz when classes missing

**Topic ID**: 42504
**Date**: 2025-04-09
**URL**: https://discourse.slicer.org/t/save-segmentation-with-orig-values-as-nii-gz-when-classes-missing/42504

---

## Post #1 by @Deep_Learning (2025-04-09 15:29 UTC)

<p>I have several binary masks saved as nii.gz.  Let’s say that I have 3 classes 1,2 and 3. But 2 is missing.  I want to load nii.gz into slicer as a segmentation along with the volume.  And manually paint the second class.   Then save as nii.gz.  The new class should have value 2 and the other values should be unchanged.</p>
<p>When I load the file, the segmentation loads as Segment_1 and Segment_3.   I add a segment. Slicer names it Segment_2.<br>
All good up to this point…<br>
Now when I export to binary label mask and save as Newfile.nii.gz,  I believe that my classes are mixed up.  I load Newfile.nii.gz as a volume and mouse over.   Now instead of 1,2,3 (or 1,3,4) I have 1,3,2.  Class 3 has a value =2 and Class 2 has a value=3.</p>
<p>Any suggestions?</p>

---

## Post #2 by @muratmaga (2025-04-09 15:32 UTC)

<p>Slicer flattens the segmentations into labelmap in the order your segments are. So if your segment order is like:</p>
<p>Segment_1<br>
Segment_3<br>
Segment_2</p>
<p>Segment_2 will get index of 3.</p>
<p>If you want to get it index of 2, move one segment up before you export. Or better yet, use a color table that defines the indices, that way order doesn’t matter.</p>

---

## Post #3 by @Deep_Learning (2025-04-09 15:57 UTC)

<p>I tried moving one up.  I do not think that it changed anything.  The problem is that I have a bunch of classes and more than one are missing (sometimes).</p>
<p>Is it possible to load a segmentation and then save it with the same values?  Assuming some are missing?</p>
<p>My work around right now is to save only the new class.  Then I can add that class into the orig file.</p>

---

## Post #4 by @muratmaga (2025-04-09 16:39 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="3" data-topic="42504">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>I do not think that it changed anything. T</p>
</blockquote>
</aside>
<p>How do you know? It does changes things.</p>
<p>If you want Slicer to export your labelmap with specific numbers, you should really use a color table. That gives you full control over what the indices will be.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-csv-file-format-csv">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-csv-file-format-csv" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-csv-file-format-csv" target="_blank" rel="noopener nofollow ugc">Colors — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Deep_Learning (2025-04-09 19:59 UTC)

<p>“move one segment up before you export.”   This refers to the order in subject heirarchy?  Or is it only the move up/down in the Segmentation Module.   Want to check before I try again.  I just dragged it up in the  subject heirarchy.  May not be the same thing…  That was the first thing that I tried… That’s why I wrote "I do not think that it changed anything. "</p>

---

## Post #6 by @muratmaga (2025-04-09 20:31 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="5" data-topic="42504">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>“move one segment up before you export.” This refers to the order in subject heirarchy? Or is it only the move up/down in the Segmentation Module.</p>
</blockquote>
</aside>
<p>In the <code>Segmentations</code> or <code>Segment editor</code> module. Right click on the segment you want to move up, and choose “Move Segment One Up” (or something like that) from the context menu. But SH should follow that.</p>

---

## Post #7 by @Deep_Learning (2025-04-10 13:37 UTC)

<p>That works.  But I would need also need to add empty segments.</p>

---

## Post #8 by @muratmaga (2025-04-10 14:50 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="7" data-topic="42504">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>But I would need also need to add empty segments.</p>
</blockquote>
</aside>
<p>That’s because you want to skip indices for labels that are not there. As I said, if you want to have full control, use a color table.</p>
<p>It can go something like<br>
1 Segment_1<br>
2 Segment_2<br>
3 Segment_3</p>
<p>And it doesn’t matter if you have if you didn’t have Segment_1 and Segment_2. Segment_3 will get index number of 3.</p>

---
