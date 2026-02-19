---
topic_id: 8647
title: "Visualization Bug In Subject Hierarchy"
date: 2019-10-02
url: https://discourse.slicer.org/t/8647
---

# Visualization bug in subject hierarchy

**Topic ID**: 8647
**Date**: 2019-10-02
**URL**: https://discourse.slicer.org/t/visualization-bug-in-subject-hierarchy/8647

---

## Post #1 by @Alex_Vergara (2019-10-02 07:40 UTC)

<p>OS: MacOS 10.14.6<br>
Slicer version: r28525</p>
<p>The subject hierarchy folder contains several children that are not displayed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8032a8c7912382485db056b4acde4ba78d6154f9.png" data-download-href="/uploads/short-url/ii5Ev7nwPbULHu7AMq7hq7Vet17.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8032a8c7912382485db056b4acde4ba78d6154f9.png" alt="image" data-base62-sha1="ii5Ev7nwPbULHu7AMq7hq7Vet17" width="438" height="500" data-dominant-color="E6E8EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">523×597 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can see a lot of children but only few displayed, If I show all nodes you can see they are there:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b572899f207790c844050aae8f1b96363052d96.png" data-download-href="/uploads/short-url/aKuxTAT9r3yPEDFOFxGtewEiyFM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b572899f207790c844050aae8f1b96363052d96_2_216x500.png" alt="image" data-base62-sha1="aKuxTAT9r3yPEDFOFxGtewEiyFM" width="216" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b572899f207790c844050aae8f1b96363052d96_2_216x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b572899f207790c844050aae8f1b96363052d96_2_324x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b572899f207790c844050aae8f1b96363052d96_2_432x1000.png 2x" data-dominant-color="DEDEDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">533×1229 60.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Even when you save the scene they are there:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adbf13a60143f5f69708ba4437a5a1e688e29ec1.png" data-download-href="/uploads/short-url/oN1YUv2ClOfFTI3HoJ5ndG8s5ax.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adbf13a60143f5f69708ba4437a5a1e688e29ec1_2_689x471.png" alt="image" data-base62-sha1="oN1YUv2ClOfFTI3HoJ5ndG8s5ax" width="689" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adbf13a60143f5f69708ba4437a5a1e688e29ec1_2_689x471.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/adbf13a60143f5f69708ba4437a5a1e688e29ec1_2_1033x706.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adbf13a60143f5f69708ba4437a5a1e688e29ec1.png 2x" data-dominant-color="E0E1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1196×817 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So this is not a critical bug, but it is very annoying, in the 25/9 release the bug was even worse as no volume were displayed at all, this was corrected but not entirely.</p>

---

## Post #2 by @lassoan (2019-10-02 11:27 UTC)

<p>Fixes have been integrated since then. Please try with latest preview version (r28531) and let us know if you still find any issues.</p>

---

## Post #3 by @Alex_Vergara (2019-10-03 07:49 UTC)

<p>The problem remains, see<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aac35996b311a1ae58464c832c59f8f5ae11b18.png" data-download-href="/uploads/short-url/8n2Ejeoiu004PULVMl44xewdnHW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aac35996b311a1ae58464c832c59f8f5ae11b18_2_690x259.png" alt="image" data-base62-sha1="8n2Ejeoiu004PULVMl44xewdnHW" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aac35996b311a1ae58464c832c59f8f5ae11b18_2_690x259.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3aac35996b311a1ae58464c832c59f8f5ae11b18_2_1035x388.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3aac35996b311a1ae58464c832c59f8f5ae11b18.png 2x" data-dominant-color="E2E2E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1187×446 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have recreated everything since the beginning and so it is not because of the old configuration.</p>
<p>I can share the scene with you for you to study what is the offending part.</p>

---

## Post #4 by @cpinter (2019-10-03 13:49 UTC)

<p>Yes please, the scene would be helpful.</p>

---

## Post #5 by @Alex_Vergara (2019-10-03 14:01 UTC)

<p>get it here <a href="https://drive.google.com/open?id=1lHh5lHeKBQY9t49J_kKZIOF0XG1qN-ut" rel="nofollow noopener">https://drive.google.com/open?id=1lHh5lHeKBQY9t49J_kKZIOF0XG1qN-ut</a></p>

---

## Post #6 by @cpinter (2019-10-03 14:05 UTC)

<p>Thanks, got it! Other than the obvious issue with the Results item is there anything else that is not how it’s supposed to be?</p>

---

## Post #7 by @cpinter (2019-10-03 14:06 UTC)

<p>By the way it seems to load fine for me:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d006f6b00987f724d59982a660a04fb9f208d5.png" data-download-href="/uploads/short-url/oSEn4Pzc7pBjoeFWyqLReZaUip.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d006f6b00987f724d59982a660a04fb9f208d5_2_590x499.png" alt="image" data-base62-sha1="oSEn4Pzc7pBjoeFWyqLReZaUip" width="590" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/02d006f6b00987f724d59982a660a04fb9f208d5_2_590x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d006f6b00987f724d59982a660a04fb9f208d5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02d006f6b00987f724d59982a660a04fb9f208d5.png 2x" data-dominant-color="D7D5D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">878×743 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @cpinter (2019-10-03 14:07 UTC)

<p>Another screenshot from the bottom:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d661bfc7a0596c07b81066fc447f9aa70f18a36e.png" data-download-href="/uploads/short-url/uAvBwyb6ZThMtW4skrIYtx7kg10.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d661bfc7a0596c07b81066fc447f9aa70f18a36e.png" alt="image" data-base62-sha1="uAvBwyb6ZThMtW4skrIYtx7kg10" width="317" height="500" data-dominant-color="EEEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">393×618 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Alex_Vergara (2019-10-03 14:07 UTC)

<p>Thats Odd, let me retry with r28532</p>

---

## Post #10 by @cpinter (2019-10-03 14:08 UTC)

<p>OK sounds good. If you have an issue in r28532 then I’ll check it out on Mac</p>

---

## Post #11 by @Alex_Vergara (2019-10-03 14:12 UTC)

<p>Ok thats was solved, Thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9021516595c3062e501dec064ff483c48a949864.png" data-download-href="/uploads/short-url/kz28CQcQwgbHBuOMsVWjUBUIpZW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9021516595c3062e501dec064ff483c48a949864_2_247x500.png" alt="image" data-base62-sha1="kz28CQcQwgbHBuOMsVWjUBUIpZW" width="247" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9021516595c3062e501dec064ff483c48a949864_2_247x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9021516595c3062e501dec064ff483c48a949864_2_370x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/9021516595c3062e501dec064ff483c48a949864_2_494x1000.png 2x" data-dominant-color="E7E8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">547×1103 72.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @cpinter (2019-10-03 14:21 UTC)

<p>Results still has the question mark.</p>
<p>What do you get if you paste this in the python window?</p>
<pre><code>shn=slicer.mrmlScene.GetSubjectHierarchyNode()
resultsItem = shn.GetItemByName('Results')
shn.GetItemOwnerPluginName(resultsItem)
</code></pre>
<p>It’s supposed to return ‘Folder’</p>

---

## Post #13 by @Alex_Vergara (2019-10-03 14:23 UTC)

<p>We need to have it as <code>Results</code> Level, since it must be univocally identified from the rest of folders. We are refactoring this part so we don’t need to force this, but for now it is our bug <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"><br>
The main problem is that there could be more than one Results folder and that would crash the workflow.</p>

---

## Post #14 by @cpinter (2019-10-03 14:28 UTC)

<p>You don’t need to use Level. You can use attribute instead. Like<br>
<code>shn.SetItemAttribute(resultsItem, 'Results', 1)</code><br>
then<br>
<code>shn.HasItemAttribute(resultsItem, 'Results')</code><br>
will return True</p>

---

## Post #15 by @Alex_Vergara (2019-10-03 14:29 UTC)

<p>Nice! I will try that asap!</p>

---

## Post #16 by @Alex_Vergara (2019-10-03 14:54 UTC)

<p>That does not worked out, the attribute is not set! I think it is not working for folders.</p>
<p>Ahh, the value argument must be a string!!</p>

---

## Post #17 by @cpinter (2019-10-03 14:57 UTC)

<p>It works on all kinds of items. Yes it needs to be string. Check the error log if anything strange happens. Usually it should tell you what went wrong and why.</p>

---

## Post #18 by @Alex_Vergara (2019-10-03 15:28 UTC)

<p>It is working for the Results folder thanks!</p>
<p>And I found the cause of the original problem: it is a refresh issue, the scene needs to be refreshed, but currently I have tried the <code>StartModify - EndModify</code> things and they don’t refresh the scene.</p>
<p>Basically I create the scene, no items visible<br>
save the scene to a mrb file, close current scene and load back the mrb and voila, the items magically appear.</p>
<p>Is there a way to force the scene to refresh?</p>

---

## Post #19 by @cpinter (2019-10-03 17:51 UTC)

<p>How exactly do you use StartModify / EndModify? We usually use it on individual nodes, in which case it should be OK, because on EndModify the one corresponding SH item updates itself and that’s it.</p>
<p>I recently integrated a change that allows subject hierarchy to be stable with BatchProcessing, maybe you should use that instead.</p>

---

## Post #20 by @Alex_Vergara (2019-10-23 08:24 UTC)

<p>OK<br>
Most has been fixed in the lasts versions, but still I have some issues, although I am closer to the issue identification.<br>
I can do</p>
<pre data-code-wrap="python"><code class="lang-python">    def createFolder(parentID, name):
        shNode = vtkmrmlutils.getSubjectHierarchyNode()
        folderID = shNode.CreateFolderItem(parentID, name)

        pluginHandler = slicer.qSlicerSubjectHierarchyPluginHandler().instance()
        folderPlugin = pluginHandler.pluginByName('Folder')
        folderPlugin.setDisplayVisibility(folderID, 1)

        return folderID

    def setItemFolder(itemID, folderID):
        shNode = vtkmrmlutils.getSubjectHierarchyNode()
        shNode.SetItemParent(itemID, folderID)
</code></pre>
<p>And then this happens<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a5c8ffad7712b0460ae071111adb200f0ec676c.png" alt="image" data-base62-sha1="8ki0shRFhz70Upxryt5pPkk3pSc" width="678" height="449"></p>
<p>BUT when I press the eye button in one node (the <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342d524a62dcc95b51fb0d099074769a12edc22b.png" alt="image" data-base62-sha1="7rzVBUoX1vFkOn4boVFjOFny5wn" width="28" height="22">, then magically</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed1d743ba80d5f49695274c3c06e8d01caa32ff.png" alt="image" data-base62-sha1="mEZ1nRvJbGsJWFaQ6gCTXFXRJpl" width="676" height="413"></p>
<p>So, whats wrong here? How can I force the shNode to refresh?</p>

---

## Post #21 by @Alex_Vergara (2019-10-23 10:02 UTC)

<p>I have solved by forcing the view to display another node</p>
<pre><code class="lang-python">    for color in ['Red', 'Yellow', 'Green']:
        slicer.app.layoutManager().sliceWidget(color).sliceLogic().GetSliceCompositeNode().SetBackgroundVolumeID(minCTID)
        slicer.app.layoutManager().sliceWidget(color).sliceLogic().GetSliceCompositeNode().SetForegroundVolumeID(minSPECTID)
</code></pre>
<p>This way the shnode is forced to refresh, I still don’t know how to do that but this trick worked out</p>

---

## Post #22 by @Alex_Vergara (2019-10-23 11:43 UTC)

<p>The above does not work for tables, charts and plots, actually now is even worse than before:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2381877a27d036a4c35a94b6f25338be12abb408.png" data-download-href="/uploads/short-url/546e2IsTTbIHHChgZbziYXO6nFK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/2381877a27d036a4c35a94b6f25338be12abb408_2_333x500.png" alt="image" data-base62-sha1="546e2IsTTbIHHChgZbziYXO6nFK" width="333" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/2381877a27d036a4c35a94b6f25338be12abb408_2_333x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/2381877a27d036a4c35a94b6f25338be12abb408_2_499x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/2381877a27d036a4c35a94b6f25338be12abb408_2_666x1000.png 2x" data-dominant-color="F6F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">678×1017 48.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So How can I create Display nodes for tables, charts and plots to be handled by the folder display node?</p>

---

## Post #23 by @lassoan (2019-10-23 13:19 UTC)

<p>Thanks for the feedback.</p>
<aside class="quote no-group quote-modified" data-username="Alex_Vergara" data-post="20" data-topic="8647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>pluginHandler = slicer.qSlicerSubjectHierarchyPluginHandler().instance() folderPlugin = pluginHandler.pluginByName(‘Folder’) folderPlugin.setDisplayVisibility(folderID, 1)</p>
</blockquote>
</aside>
<p>Why did you need to add this?</p>

---

## Post #24 by @Alex_Vergara (2019-10-23 13:31 UTC)

<p>Because otherwise the folder is created without a Display node, (No eye in the view)</p>

---

## Post #25 by @cpinter (2019-10-23 13:33 UTC)

<p>Currently this is how you can set the folder visibility from code. The generic setItemVisibility uses CreateDefaultDisplayNodes in the displayable node and since the folder does not have a displayable node, it uses a function in the plugin that creates the special folder display node that is needed. I have not found a solution for this yet (and was not a high priority either).</p>
<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> The folder visibility is considered by the displayable managers, so to fix show/hiding certain types of nodes in folders this has to be added to the corresponding displayable manager.</p>

---

## Post #26 by @lassoan (2019-10-23 13:45 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="22" data-topic="8647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>The above does not work for tables, charts and plots, actually now is even worse than before:</p>
</blockquote>
</aside>
<p>The old behavior is still available: right-click on the eye icon and choose “Show all children” or “Hide all children”.</p>
<aside class="quote no-group" data-username="cpinter" data-post="25" data-topic="8647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>fix show/hiding certain types of nodes in folders this has to be added to the corresponding displayable manager.</p>
</blockquote>
</aside>
<p>How could we apply this to for example volumes, tables, and plots? They do not have displayable managers. Should the volumes plugin observe the parent folder visibility and change visibility accordingly (perform the same action when clicking on the eye icon of the individual SH item)?</p>

---

## Post #27 by @cpinter (2019-10-23 13:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="8647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The old behavior is still available: right-click on the eye icon and choose “Show all children” or “Hide all children”</p>
</blockquote>
</aside>
<p>Very good point.</p>
<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="8647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should the volumes plugin observe the parent folder visibility and change visibility accordingly (perform the same action when clicking on the eye icon of the individual SH item)</p>
</blockquote>
</aside>
<p>Something like this would work. However I probably wouldn’t include volumes in this. Volumes did not change visibility in the past based on folder visibility, because they are so differently visualized. There is a ‘Show volumes in study’ option for this if I remember correctly.</p>

---
