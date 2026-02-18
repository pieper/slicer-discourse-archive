# How do I properly connect the qMRMLSegmentEditorWidget so that it properly updates?

**Topic ID**: 24940
**Date**: 2022-08-26
**URL**: https://discourse.slicer.org/t/how-do-i-properly-connect-the-qmrmlsegmenteditorwidget-so-that-it-properly-updates/24940

---

## Post #1 by @Kevin.Kn (2022-08-26 19:36 UTC)

<p>I am expanding an automated segmentation Tool that I have created to be a bit more user friendly for people to not go between a ton of menus in slicer.</p>
<p>I have a UI created that has the qMRMLSegmentEditorWidget added, and linked to the mrmlSceneChanged(vtkMRMLScene*) signal.</p>
<p>for my input/output volume nodes and a nodule seed placement nodes, I can update these using setCurrentNode(). When doing this with the segmentation node, I get an error saing that the setCurrentNode() doesnt exist.</p>
<p>Looking at the the documentation of qMRMLSegmentEditorWidget, the closest thing I can find is setCurrentSegmentID, but even setting that doesnt work properly, and the widget segmentation selection/volume nodes are still greyed out.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad24befc156b0b4e2ab0126db168fdb4e76933bf.png" alt="image" data-base62-sha1="oHHku49dCrAtzYdihaI7Tg9XYbJ" width="571" height="63"></p>
<p>any help would be appreciated</p>

---

## Post #2 by @lassoan (2022-08-26 20:40 UTC)

<p><code>setCurrentSegmentID</code> sets the currently selected segment (not the segmentation node). All segment editor parameters are stored in the segment editor node and you can modify them via methods in that node. There are several examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-segment-editor-effects-from-script-qmrmlsegmenteditorwidget">script repository</a>.</p>

---

## Post #3 by @Kevin.Kn (2022-08-29 15:44 UTC)

<p>These examples are sligtly different than what I was wanting. I already have my segmentations transferred from volumes to the scene to be ready for editing using some of the code from those examples.</p>
<p>My issue is that I want to add the segmentation editor widget to allow for ease of editing, but those menus, and that widget in general do not update when a reference volume or segmentation are available.</p>
<p>I have double checked that the scene is properly connected in QT for updates, which is why I am stuck as to why the widget is greyed out, when I used the same methods as connecting my other widgets which work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a0ce0953c170858c90200b1fd8df042ce56a281.png" data-download-href="/uploads/short-url/lYN7qQI9fv72NvmUw5yy76iF4LT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a0ce0953c170858c90200b1fd8df042ce56a281.png" alt="image" data-base62-sha1="lYN7qQI9fv72NvmUw5yy76iF4LT" width="368" height="500" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">455×617 16.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Kevin.Kn (2022-08-29 16:07 UTC)

<p>after trying implementing the linking in <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/SegmentEditor/SegmentEditor.py" class="inline-onebox" rel="noopener nofollow ugc">Slicer/SegmentEditor.py at main · Slicer/Slicer · GitHub</a> I was able to get a version of the widget that works and updates with user inputs.</p>
<p>Although I still do not get why the widget is non responsive in my scripted module when I directly link it to the MRML scene in QT</p>

---

## Post #5 by @lassoan (2022-08-31 02:53 UTC)

<p>If you set the MRML scene and then the segment editor parameter node into the widget then the GUI becomes editable.</p>

---
