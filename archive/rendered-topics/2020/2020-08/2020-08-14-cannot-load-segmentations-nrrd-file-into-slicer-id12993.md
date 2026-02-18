# Cannot load segmentations (nrrd file) into slicer

**Topic ID**: 12993
**Date**: 2020-08-14
**URL**: https://discourse.slicer.org/t/cannot-load-segmentations-nrrd-file-into-slicer/12993

---

## Post #1 by @Bo_Lan (2020-08-14 01:10 UTC)

<p>Hi all, so I saved my segmentations (under an nrrd file) and my segmentation scene just half an hour ago and restarted my computer. It appeared that the segmentations were saved when I saved them half an hour ago, however my latest scene, which I also saved do not have the segmentations anymore or the template data. When I open up the template and the segmentations in a new slicer window, only the template data loads but not the segmentations.</p>
<p>I see that the segmentations still show up on my storage folder as a nrrd file and still have space in them. They also indicate that they were last edited 30 minutes ago (when I saved them). However, whenever I load them in slicer nothing shows up, and I have gone to data, segment editor, and segmentations modules to find nothing. However, when I load other data, it does show up. I have been fine for the past two months saving it the same way. I am worried that I have lost my segmentations, is there a solution to this?</p>

---

## Post #2 by @lassoan (2020-08-14 02:20 UTC)

<p>Please send the application log of a load attempt (menu: Help / Report a bug).</p>
<p>It would be also very interesting to see the log of that session when you saved the segmentation file. In Help / Report a bug, you can select previous sessions (logs of the last 10-20 sessions are saved), maybe you can still find it.</p>
<p>Can you share the segmentation file? (upload somewhere and post the link, maybe send it in a private message)</p>

---

## Post #3 by @Bo_Lan (2020-08-14 02:29 UTC)

<p>Hi Dr. Lasso,</p>
<p>Thank you for the response. In Help/Report a bug, I went to the last session, but the only options I have appear to be copy and paste and open in new window, which just appears to be a bunch of code and I am quite illiterate in coding besides basic C++. Also I do not even know for sure if it the last session is still the session before my data was lost as I have tried reopening my segmentations about 10 times and restarted each time so it may be over ten sessions. I would be happy to send you the segmentation file in a private message.</p>

---

## Post #4 by @lassoan (2020-08-14 03:57 UTC)

<p>The file was just a few-hundred kB and filled with just zeros. Other then using an old version (latest stable 4.10.2) there is nothing special about the configuration or workflow (file was saved to desktop; OS: Windows).</p>
<p>The problem seems to be similar to the one described in “<a href="https://discourse.slicer.org/t/segments-disappeared/12698" class="inline-onebox">Segments disappeared!</a>”. Maybe there were some instability in how Slicer-4.10.2 saved segmentations. It may make sense to use a recent Slicer-4.11 version and create backups (instead of always just overwriting the previous version). If data corruption occurs then save logs of the last session (where the data was saved) using menu: Help / Report a bug.</p>

---

## Post #5 by @Bo_Lan (2020-08-14 22:00 UTC)

<p>Hi Dr. Lasso, I just also realized I exported my original segmentations to binary labelmap and saved them in the nifti format the day before my segmentations disappeared. While I do cannot restore by going to help/report a bug, is there anyway to restore my segmentations by converting the nifti back to nrrd? The nifti is able to show up on slicer, but it shows up as a volume and I am unable to edit the image as segmentations.</p>

---

## Post #6 by @lassoan (2020-08-14 22:22 UTC)

<p>You can load the nifti file as segmentation by choosing “Segmentation” in Description column in Add data window. You may need Slicer-4.11 for this.</p>
<p>In Slicer-4.10, you need to load the nifti file as labelmap volume by checking labelmap option in Add data window. Then you can convert it to segmentation node by right-clicking on it in Data module.</p>

---

## Post #7 by @Bo_Lan (2020-08-18 21:43 UTC)

<p>Thank you Dr. Lasso, this solved the problem!</p>

---
