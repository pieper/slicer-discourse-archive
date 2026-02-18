# How to change the name of a folder in the subject hierarchy

**Topic ID**: 23360
**Date**: 2022-05-10
**URL**: https://discourse.slicer.org/t/how-to-change-the-name-of-a-folder-in-the-subject-hierarchy/23360

---

## Post #1 by @koeglfryderyk (2022-05-10 14:47 UTC)

<p>I want to change the name of a folder in the Subject hierarchy in the ‘Data’ module.</p>
<p>I tried using <code>SetItemName()</code> like this:<br>
<code>subject_hierarchy_node.SetItemName(296, 'new_name')</code><br>
but this only changed the name in the ‘Subject hierarchy item information’ and not in the folder name in the hierarchy tree.</p>
<p>Here you can see that I wanted to change the name of the ‘NewFolder’ folder to ‘new_name’ but the name ‘NewFolder’ did not change:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d653ea7c0577a824d3a298924ce66494ceb9786c.png" data-download-href="/uploads/short-url/uA1Y099gDmMoMRKWWbyppiP4Tgw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653ea7c0577a824d3a298924ce66494ceb9786c_2_690x303.png" alt="image" data-base62-sha1="uA1Y099gDmMoMRKWWbyppiP4Tgw" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653ea7c0577a824d3a298924ce66494ceb9786c_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653ea7c0577a824d3a298924ce66494ceb9786c_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d653ea7c0577a824d3a298924ce66494ceb9786c_2_1380x606.png 2x" data-dominant-color="BCBCBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1780×782 80.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer 5.10-2022-05-08 MacOS</p>

---

## Post #2 by @cpinter (2022-05-10 15:46 UTC)

<p>I just checked and this call works for me in Slicer 5.1 on Windows. I call <code>shNode.SetItemName(18, 'NewName')</code> and <code>NewName</code> appears in the tree.</p>
<p>Can someone else using MacOS try it?</p>

---

## Post #3 by @lassoan (2022-05-12 12:08 UTC)

<p>This should work well. Could your provide the complete list of steps that reproduces the issue? (start Slicer, go to Data module, right-click on…)</p>

---

## Post #4 by @koeglfryderyk (2022-05-12 14:13 UTC)

<p>I tried it again today and it worked - maybe I have made a mistake before that I didn’t realise. Thanks for your responses!</p>

---
