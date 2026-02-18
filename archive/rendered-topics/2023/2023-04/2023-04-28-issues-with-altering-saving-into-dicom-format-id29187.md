# Issues with altering/saving into DICOM format

**Topic ID**: 29187
**Date**: 2023-04-28
**URL**: https://discourse.slicer.org/t/issues-with-altering-saving-into-dicom-format/29187

---

## Post #1 by @Benjamin_Lee (2023-04-28 14:45 UTC)

<p>Sorry if this question is very entry level, but I have spent an entire day trying to figure this out.<br>
I am trying to rename the images in the tree structure to describe what the image shows for a dataset of about 350 thyroid ultrasound images and then save those changes to the DICOM database. All of the names are different from one another.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a0b215cd759bb3cc3b5821dcc1d91f7dd95a890.png" data-download-href="/uploads/short-url/hpE64IwFjtKw3fOffXs9N45Pa5W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a0b215cd759bb3cc3b5821dcc1d91f7dd95a890_2_690x354.png" alt="image" data-base62-sha1="hpE64IwFjtKw3fOffXs9N45Pa5W" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a0b215cd759bb3cc3b5821dcc1d91f7dd95a890_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a0b215cd759bb3cc3b5821dcc1d91f7dd95a890_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a0b215cd759bb3cc3b5821dcc1d91f7dd95a890.png 2x" data-dominant-color="353B41"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1273×654 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The problems I am having are that the save button only allows me to save to .mrml or .nrrd format, I need them in DICOM format. Also not sure I understand the .mrml concept, when I just save the .mrml file but deselect the .nrrd files, it fails to load when I try to reload the project after restarting Slicer.</p>
<p>The other problem is that the “export to DICOM” option only allows me to export a subtree at a time rather than the whole database. Also when I export just a series this disrupts the database structure and outputs all separate scalar volumes, or bundles of the series at best, not the original hierarchy. Also when I click on the “Export entire scene” button nothing happens. All the options go grey and nothing happens. The python interactor gives this error:</p>
<p>Traceback (most recent call last):<br>
File “”, line 2, in <br>
TypeError: <strong>init</strong>() missing 1 required positional argument: ‘referenceFile’</p>
<p>However everything is grayed out so there is no way I can select a reference file.</p>
<p>Ideally I’d like to use these labels later to sort the images by sagittal vs transverse view, calipered measurements vs. unmarked, etc. and possibly other labels to sort these images to use in a machine learning context and also upload to the National Cancer Imaging Archive. Is there a better place in the DICOM file metadata to put these tags? for example “thyroid nodule no. 2 Sagittal view”.<br>
I’m very new to Slicer, please advise.<br>
Thanks,</p>

---

## Post #2 by @lassoan (2023-04-28 14:58 UTC)

<aside class="quote no-group" data-username="Benjamin_Lee" data-post="1" data-topic="29187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin_lee/48/65817_2.png" class="avatar"> Benjamin_Lee:</div>
<blockquote>
<p>I need them in DICOM format</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Benjamin_Lee" data-post="1" data-topic="29187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin_lee/48/65817_2.png" class="avatar"> Benjamin_Lee:</div>
<blockquote>
<p>Ideally I’d like to use these labels later to sort the images by sagittal vs transverse view, calipered measurements vs. unmarked, etc. and possibly other labels to sort these images to use in a machine learning context and also upload to the National Cancer Imaging Archive. Is there a better place in the DICOM file metadata to put these tags? for example “thyroid nodule no. 2 Sagittal view”.</p>
</blockquote>
</aside>
<p>Do you mean TCIA? Have you discussed with them about this already?</p>
<p>DICOM files are not meant to be modified. You could make new instances by modifying some fields in the original files, but then you would have a data set quite that is different from what users normally get from their clinical workflow. It means that if anyone develops some machine learning tool on this manipulated data set, it will not work an any clinical data set.</p>
<p>Instead, you could add additional DICOM information objects, such as structured reports with segmentations, measurements, etc. to add more descriptive data to these image series.</p>
<aside class="quote no-group" data-username="Benjamin_Lee" data-post="1" data-topic="29187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin_lee/48/65817_2.png" class="avatar"> Benjamin_Lee:</div>
<blockquote>
<p>Also not sure I understand the .mrml concept, when I just save the .mrml file but deselect the .nrrd files, it fails to load when I try to reload the project after restarting Slicer.</p>
</blockquote>
</aside>
<p>The scene file is just an index. All bulk data (images, models, etc.) are stored in additional data files. If you don’t save the data files then you won’t be able to load them.</p>
<p>If you want to save everything in a single file then click the small “package” icon in the save data window.</p>
<aside class="quote no-group" data-username="Benjamin_Lee" data-post="1" data-topic="29187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin_lee/48/65817_2.png" class="avatar"> Benjamin_Lee:</div>
<blockquote>
<p>when I click on the “Export entire scene” button nothing happens</p>
</blockquote>
</aside>
<p>Which Slicer version are you using?</p>

---

## Post #3 by @Benjamin_Lee (2023-04-28 16:03 UTC)

<p>Sorry yes I meant TCIA. I spoke with them and they recommended talking to the Imaging Data Commons people to see what they would recommend.<br>
I think for now I may do as you suggest and simply add structured reports with descriptions in them.</p>
<p>When I select the bundle it give this error and fails to save<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0cd31313a941024c8190f2aa7050af410b39131.png" data-download-href="/uploads/short-url/pe3EJo3EpX2gxoyPhO3vr5XSGAN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0cd31313a941024c8190f2aa7050af410b39131_2_690x289.png" alt="image" data-base62-sha1="pe3EJo3EpX2gxoyPhO3vr5XSGAN" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0cd31313a941024c8190f2aa7050af410b39131_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0cd31313a941024c8190f2aa7050af410b39131_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0cd31313a941024c8190f2aa7050af410b39131_2_1380x578.png 2x" data-dominant-color="383737"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1534×644 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am using 3D Slicer 4.11.20210226</p>

---

## Post #4 by @pieper (2023-04-28 16:14 UTC)

<p><a class="mention" href="/u/benjamin_lee">@Benjamin_Lee</a> you should probably post over at <a href="https://discourse.canceridc.dev/">https://discourse.canceridc.dev/</a> where people like <a class="mention" href="/u/fedorov">@fedorov</a> are monitoring and can give advice on this topic.  I’m also involved in a couple submissions to TCIA and it’s good to get advice before starting.  We have found that writing python scripts to batch process the data is more manageable than using the Slicer GUI.</p>

---

## Post #5 by @Benjamin_Lee (2023-04-28 16:43 UTC)

<p>Update: I have updated to Slicer 5.2.2 and now the Export to DICOM function says it has exported, but the folder is empty.</p>
<p>Also the .mrb option still fails with this error:</p>
<p>[VTK] vtkMRMLScene::WriteToMRB: Failed to save C:/Users/Ben/Desktop/thyroid conventional US scan images/Labeled Images/2023-04-28-Scene.mrb: Failed to save scene to data bundle directory</p>
<p>[Qt] bool __cdecl qSlicerCoreIOManager::saveNodes(class QString,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLMessageCollection *,class vtkMRMLScene *) error: Saving failed with all writers found for file “C:/Users/Ben/Desktop/thyroid conventional US scan images/Labeled Images/2023-04-28-Scene.mrb” of type “SceneFile”</p>
<p>[Qt] void __cdecl qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int,class vtkMRMLMessageCollection *,bool) Data save error: “- Error: 0001: US [0000] (vtkMRMLSequenceNode1): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [0256] (vtkMRMLSequenceNode2): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [0512] (vtkMRMLSequenceNode3): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [0768] (vtkMRMLSequenceNode4): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [1024] (vtkMRMLSequenceNode5): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [1280] (vtkMRMLSequenceNode6): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [1536] (vtkMRMLSequenceNode7): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [1792] (vtkMRMLSequenceNode8): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [2048] (vtkMRMLSequenceNode9): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [2304] (vtkMRMLSequenceNode10): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [2560] (vtkMRMLSequenceNode11): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [2816] (vtkMRMLSequenceNode12): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [3072] (vtkMRMLSequenceNode13): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [3328] (vtkMRMLSequenceNode14): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [3584] (vtkMRMLSequenceNode15): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [3840] (vtkMRMLSequenceNode16): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [4096] (vtkMRMLSequenceNode17): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [4352] (vtkMRMLSequenceNode18): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [4608] (vtkMRMLSequenceNode19): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [4864] (vtkMRMLSequenceNode20): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [5120] (vtkMRMLSequenceNode21): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [5376] (vtkMRMLSequenceNode22): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [5632] (vtkMRMLSequenceNode23): Only single scalar component volumes can be written in this format.\n- Error: 0001: US [5888] (vtkMRMLSequenceNode24): Only single scalar component volumes can be written in this format.\n- Error: Failed to save C:/Users/Ben/Desktop/thyroid conventional US scan images/Labeled Images/2023-04-28-Scene.mrb: Failed to save scene to data bundle directory\n- Error: Failed to save scene as C:/Users/Ben/Desktop/thyroid conventional US scan images/Labeled Images/2023-04-28-Scene.mrb\n- Error: Saving failed with all writers found for file ‘C:/Users/Ben/Desktop/thyroid conventional US scan images/Labeled Images/2023-04-28-Scene.mrb’ of type ‘SceneFile’.\n”</p>

---

## Post #6 by @pieper (2023-04-28 19:13 UTC)

<p>Probably the Ultrasound images are color and are not supported for this use case.  I’m not sure Slicer has been used for this use case before.  Still best to contact the IDC team for advice - please post the exact description of the data you are planning to provide to TCIA in order to get help.</p>

---

## Post #7 by @lassoan (2023-04-30 15:43 UTC)

<p>The problem is that currently the nrrd file I/O does not support 5D (space+time+color).</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> you worked a lot on adding color video support. Do you think we could use here the storage nodes that you implemented? We need lossless storage.</p>

---
