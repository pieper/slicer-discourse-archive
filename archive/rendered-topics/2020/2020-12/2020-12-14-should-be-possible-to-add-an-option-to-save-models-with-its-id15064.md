# Should be possible to add an option to save models with its transform hardened?

**Topic ID**: 15064
**Date**: 2020-12-14
**URL**: https://discourse.slicer.org/t/should-be-possible-to-add-an-option-to-save-models-with-its-transform-hardened/15064

---

## Post #1 by @apparrilla (2020-12-14 22:22 UTC)

<p>Hi everyone,</p>
<p>Many times I have scene completed with many models properly located with trasnforms and I should like to save them as STL to manage outside Slicer. I shouldn´t like to harden them because sometimes a little position fix is needed later.</p>
<p>It should be very usefull to be able to save models with/without transform in Save Panel as:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/affc111a9ad5e3dbdbe2bb168fd9dd2cacc2fee8.png" data-download-href="/uploads/short-url/p6PBH5nR2kRbATH8FIe5CUjwMNq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affc111a9ad5e3dbdbe2bb168fd9dd2cacc2fee8_2_690x183.png" alt="image" data-base62-sha1="p6PBH5nR2kRbATH8FIe5CUjwMNq" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affc111a9ad5e3dbdbe2bb168fd9dd2cacc2fee8_2_690x183.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affc111a9ad5e3dbdbe2bb168fd9dd2cacc2fee8_2_1035x274.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/affc111a9ad5e3dbdbe2bb168fd9dd2cacc2fee8_2_1380x366.png 2x" data-dominant-color="363535"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2409×642 36.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks on advance!</p>
<p>OS: Win10</p>

---

## Post #2 by @lassoan (2020-12-15 00:52 UTC)

<p>Scene save is primarily for data saving. There are various modules that are better suited for data export.</p>
<p>For example, you can export models from the Data module’s subject hierarchy tree using right-click menu if you install Slicer Morph extension. If needed, the behavior can be tuned (e.g., make sure transform is applied, allow export an entire folder, etc).</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #3 by @muratmaga (2020-12-15 17:32 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="1" data-topic="15064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>It should be very usefull to be able to save models with/without transform in Save Panel as:</p>
</blockquote>
</aside>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> eluded, if you install SlicerMorph extension, there will be an <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ExportAs/ExportAs.md">ExportAs plugin added to the data module</a>.</p>
<p>If you do want to retain the transform and the model, you clone both, harden  the cloned pair and use the ExportAs.</p>

---

## Post #4 by @apparrilla (2020-12-15 23:47 UTC)

<p>Clone models and harden transforms is the way I´m working nowadays using Scene Save. The trouble is when many models have to be experted from the scene.<br>
I´ve install Slicer Morph extension and export models directly in Data Module is a really usefull way to save data as STL.<br>
If the plugin should add the option I´ve proposed, it should be even better solution for this task.</p>
<p>Thanks both <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>

---

## Post #5 by @lassoan (2020-12-16 02:18 UTC)

<p>Note that you can customize entire Slicer’s behavior to make you highly productive using short Python code snippets. For example, the entire “Export as” feature is essentially <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ExportAs/ExportAs.py#L51-L79">30 lines of Python code</a>. You can start from that and modify it to fit your needs (e.g., clone the node and harden the transform). If it works well for you then you can contribute it back to SlicerMorph (and in some form the export feature will be integrated into the Slicer core).</p>

---

## Post #6 by @apparrilla (2020-12-16 09:16 UTC)

<p>Ok. Working on it. Give a while… I´ll post it when it works…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c83d0e59da9d9f571b6c7ff1136f30ac82799bc4.png" data-download-href="/uploads/short-url/szoiYChZ17mu9S2QiBlc3KY9B76.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c83d0e59da9d9f571b6c7ff1136f30ac82799bc4_2_339x250.png" alt="image" data-base62-sha1="szoiYChZ17mu9S2QiBlc3KY9B76" width="339" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c83d0e59da9d9f571b6c7ff1136f30ac82799bc4_2_339x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c83d0e59da9d9f571b6c7ff1136f30ac82799bc4_2_508x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c83d0e59da9d9f571b6c7ff1136f30ac82799bc4_2_678x500.png 2x" data-dominant-color="293036"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1157×853 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you!</p>

---

## Post #7 by @apparrilla (2020-12-16 21:11 UTC)

<p>Good night! I´m a bit in trouble with this task.</p>
<p>Code added to extension:</p>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
itemIDToClone = shNode.GetItemByDataNode(node)
clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
clonedNode = shNode.GetItemDataNode(clonedItemID)
transformLogic = slicer.vtkSlicerTransformLogic()
transformLogic.hardenTransform(clonedNode)
fileName = qt.QFileDialog.getSaveFileName(slicer.util.mainWindow(),"Export As...", clonedNode.GetName(), writerFormat)
extension = slicer.vtkDataFileFormatHelper.GetFileExtensionFromFormatString(writerFormat)
if not fileName.endswith(extension):
   fileName = fileName + extension
 if fileName == "":
   return
writerType = slicer.app.coreIOManager().fileWriterFileType(clonedNode)
success = slicer.app.coreIOManager().saveNodes(writerType, {"nodeID": clonedNode.GetID(), "fileName": fileName})
if success:
  logging.info(f"Exported {clonedNode.GetName()} to {fileName}")
else:
  slicer.util.errorDisplay(f"Could not save {clonedNode.GetName()} to {fileName}")
</code></pre>
<p>Original Scene:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab2db0fea480fea34826483541ca6872f5e970bc.png" data-download-href="/uploads/short-url/oqjxwN7m3kYKtP7OCKOwxgoe9Gs.png?dl=1" title="First" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2db0fea480fea34826483541ca6872f5e970bc_2_345x217.png" alt="First" data-base62-sha1="oqjxwN7m3kYKtP7OCKOwxgoe9Gs" width="345" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2db0fea480fea34826483541ca6872f5e970bc_2_345x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2db0fea480fea34826483541ca6872f5e970bc_2_517x325.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab2db0fea480fea34826483541ca6872f5e970bc_2_690x434.png 2x" data-dominant-color="9A9DD2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">First</span><span class="informations">2983×1879 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Add Trasnform to OriginalModel_Yellow:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28219e4f8be75e54ef954d601178cea0d84e9bc5.png" data-download-href="/uploads/short-url/5J17O00eQEGHIqRHIi3k9Du7tKB.png?dl=1" title="Third" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28219e4f8be75e54ef954d601178cea0d84e9bc5_2_345x169.png" alt="Third" data-base62-sha1="5J17O00eQEGHIqRHIi3k9Du7tKB" width="345" height="169" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28219e4f8be75e54ef954d601178cea0d84e9bc5_2_345x169.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28219e4f8be75e54ef954d601178cea0d84e9bc5_2_517x253.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28219e4f8be75e54ef954d601178cea0d84e9bc5_2_690x338.png 2x" data-dominant-color="8487B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Third</span><span class="informations">3825×1882 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Right click menu to save hardened model:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/635a1a291910dfcc8f842b586de2b23c64bda368.png" data-download-href="/uploads/short-url/eaUjnJnDvdCs2bpIo0cLoWLh9eU.png?dl=1" title="Fourth" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/635a1a291910dfcc8f842b586de2b23c64bda368_2_345x203.png" alt="Fourth" data-base62-sha1="eaUjnJnDvdCs2bpIo0cLoWLh9eU" width="345" height="203" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/635a1a291910dfcc8f842b586de2b23c64bda368_2_345x203.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/635a1a291910dfcc8f842b586de2b23c64bda368_2_517x304.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/635a1a291910dfcc8f842b586de2b23c64bda368_2_690x406.png 2x" data-dominant-color="404658"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fourth</span><span class="informations">1367×807 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But result (new cloned Mode in Red)…:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/674c5e137f826a557954bcc1caafb5b499008dc5.png" data-download-href="/uploads/short-url/eJONlYdxpKxBwcg9j3yGd6TQFIF.png?dl=1" title="Fiveth" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/674c5e137f826a557954bcc1caafb5b499008dc5_2_690x338.png" alt="Fiveth" data-base62-sha1="eJONlYdxpKxBwcg9j3yGd6TQFIF" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/674c5e137f826a557954bcc1caafb5b499008dc5_2_690x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/674c5e137f826a557954bcc1caafb5b499008dc5_2_1035x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/674c5e137f826a557954bcc1caafb5b499008dc5_2_1380x676.png 2x" data-dominant-color="8487B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fiveth</span><span class="informations">3827×1876 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Original yellow model come back to original position but is still trasnformed??? Cloned model is OK. If I import saved model, it is in hardened position as expected too.</p>
<p>What am I doing worng with OriginalModel_Yellow? I think I´m just cloning it but don´t looks like.</p>
<p>OS: Win10<br>
Slicer ver: 4.11.20200930 r29402 / 002be18 (stable)</p>
<p>Thanks!</p>

---

## Post #8 by @apparrilla (2020-12-16 23:45 UTC)

<p>Ok. I answare myself.<br>
I think is something related with Slicer version. In new 4.13 when you clone a node, new cloned node is not related to original node transform.</p>
<p>I´ve add 2 lines to code to apply transform to cloned node and when I harden it there is no change in the original node.</p>
<p>it works for me!<br>
<a class="mention" href="/u/lassoan">@lassoan</a>, who can I share modded file ExportAs.py?</p>

---

## Post #9 by @lassoan (2020-12-16 23:57 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="8" data-topic="15064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>it works for me!</p>
</blockquote>
</aside>
<p>Great, congratulations!</p>
<aside class="quote no-group" data-username="apparrilla" data-post="8" data-topic="15064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>who can I share modded file ExportAs.py?</p>
</blockquote>
</aside>
<p>The proper way of proposing changes to source code is via github (fork the repository into your github account, make the changes there, and then create a pull request). Since changes affect a single file, you can do all these steps with a few clicks on the github website: click the edit button <a href="https://github.com/SlicerMorph/SlicerMorph/blob/master/ExportAs/ExportAs.py">here</a>, make the changes in the code, and click “Propose changes” button at the bottom.</p>

---

## Post #10 by @muratmaga (2020-12-17 00:14 UTC)

<aside class="quote no-group" data-username="apparrilla" data-post="8" data-topic="15064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/apparrilla/48/9230_2.png" class="avatar"> apparrilla:</div>
<blockquote>
<p>I´ve add 2 lines to code to apply transform to cloned node and when I harden it there is no change in the original node.</p>
</blockquote>
</aside>
<p>Congrats. You can fork the SlicerMorph repo (<a href="https://github.com/SlicerMorph/SlicerMorph" class="inline-onebox">GitHub - SlicerMorph/SlicerMorph: Extension to import microCT data and conduct 3D morphometrics in Slicer</a>) make changes and submit a PR. We will review and incorporate the changes (as is or revised) <a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #11 by @apparrilla (2020-12-17 00:41 UTC)

<p>Done!<br>
Thanks to all.</p>

---
