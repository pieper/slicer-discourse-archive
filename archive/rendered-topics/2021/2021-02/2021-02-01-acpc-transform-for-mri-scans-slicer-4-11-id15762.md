# ACPC Transform for MRI scans- Slicer 4.11

**Topic ID**: 15762
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/acpc-transform-for-mri-scans-slicer-4-11/15762

---

## Post #1 by @shebaelena (2021-02-01 01:55 UTC)

<p>Hi,</p>
<p>I am trying to do an ACPC transform on Slicer 4.11, and have been unable to determine how to do so. I recently updated from an older version in which I used to be able to complete the transform, but lately it had not been registering the final step (i.e. the actual realignment of the MRI scan) following the fiducial list creation and the “Apply” step.</p>
<p>These are the instructions I was using a few years back: <a href="https://www.slideserve.com/jacoba/slicer3-tutorial-registration-library-case-15-ac-pc-alignment" class="inline-onebox" rel="noopener nofollow ugc">PPT - Slicer3 Tutorial: Registration Library Case 15 AC-PC Alignment PowerPoint Presentation - ID:5393167</a></p>
<p>Any help would be greatly appreciated.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-02-01 05:55 UTC)

<p>In latest Slicer Stable Release (Slicer-4.11), you need to specify both the ACPC line and the Midline curve by placing markups fiducial points.</p>
<p>To make the behavior more intuitive, I’ll improve latest Slicer Preview Release (Slicer-4.13) to take a markups line and a markups curve instead. The updated Slicer Preview Release will be available for download tomorrow or the day after.</p>

---

## Post #3 by @shebaelena (2021-02-01 22:02 UTC)

<p>Thank you so much for your response! I did have to specify both ACPC and Midline with fiducial points in the last version, but I couldn’t figure out how to do so with the new setup. Is there any way you could upload instructions/screenshots here for how to assign the fiducials to a list and then apply the transform properly?</p>
<p>Thank you in advance!!</p>

---

## Post #4 by @shebaelena (2021-02-07 19:42 UTC)

<p>Hi Andras,</p>
<p>Thank you for the new release! I was able to create the two fiducial lists, but I wasn’t sure where to go from there, since I couldn’t find any specific module for an “ACPC Transform.” I’ve attached a few screenshots of what I tried:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5e7d2f4341f78095b7f5a177048f30425de5a18.jpeg" data-download-href="/uploads/short-url/nFFsJ435uW3U1Ackgikyh2KHyVW.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e7d2f4341f78095b7f5a177048f30425de5a18_2_690x412.jpeg" alt="1" data-base62-sha1="nFFsJ435uW3U1Ackgikyh2KHyVW" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e7d2f4341f78095b7f5a177048f30425de5a18_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e7d2f4341f78095b7f5a177048f30425de5a18_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a5e7d2f4341f78095b7f5a177048f30425de5a18_2_1380x824.jpeg 2x" data-dominant-color="616060"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">2752×1644 344 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would also definitely be willing to write up some instructions with screenshots for how to do the transformation in the newest version for the next person!</p>
<p>Thank you so much,<br>
Alexis</p>

---

## Post #5 by @lassoan (2021-02-10 04:29 UTC)

<p>I did a quick recording of how ACPC alignment works in latest Slicer Preview Release:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="sdrRv3JrgTU" data-video-title="acpcdemo" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=sdrRv3JrgTU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/sdrRv3JrgTU/maxresdefault.jpg" title="acpcdemo" width="" height="">
  </a>
</div>

<p>It would be great if you could create a nice description/tutorial of how to use it (with a few screenshots). Slicer documentation is now in markdown format, which is the format that this forum uses, so you can write this as a new post in this topic and I will move it to the Slicer documentation when it is ready.</p>

---

## Post #6 by @shebaelena (2021-02-11 23:44 UTC)

<p>Thank you so much, this was really helpful. I unfortunately am still coming across an error and haven’t been able to figure out why it’s happening despite trying multiple scans. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ea6af305b210f0da80704b4087c992c9d86b2b.jpeg" data-download-href="/uploads/short-url/rFso9rF0WGRc8WzgxWpCa0nkj2j.jpeg?dl=1" title="Slicer 2-11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1ea6af305b210f0da80704b4087c992c9d86b2b_2_517x327.jpeg" alt="Slicer 2-11" data-base62-sha1="rFso9rF0WGRc8WzgxWpCa0nkj2j" width="517" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1ea6af305b210f0da80704b4087c992c9d86b2b_2_517x327.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1ea6af305b210f0da80704b4087c992c9d86b2b_2_775x490.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1ea6af305b210f0da80704b4087c992c9d86b2b_2_1034x654.jpeg 2x" data-dominant-color="403D44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer 2-11</span><span class="informations">2374×1504 448 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>It seems like a Read Data error (pasted below). I understand if this is too particular to resolve, and can certainly still write up instructions for others given that my issue is only with the last ‘Apply’ step. Also, just to clarify, which topic would you prefer that I use?</p>
<p>ACPC Transform standard error:</p>
<p>ERROR: In /Volumes/D/P/S-0/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonStorageNode.cxx, line 105</p>
<p>vtkMRMLMarkupsJsonStorageNode (0x7f954730f650): vtkMRMLMarkupsJsonStorageNode::ReadDataInternal failed: error opening the file '/var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/BAHCB_vtkMRMLMarkupsLineNodeC.json</p>
<p>ERROR: In /Volumes/D/P/S-0/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonStorageNode.cxx, line 1049</p>
<p>vtkMRMLMarkupsJsonStorageNode (0x7f954730f650): vtkMRMLMarkupsStorageNode::ReadDataInternal failed: error opening the file '/var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/BAHCB_vtkMRMLMarkupsLineNodeC.json</p>
<p>Failed to read ACPC line from file /var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/BAHCB_vtkMRMLMarkupsLineNodeC.json</p>
<p>ERROR: In /Volumes/D/P/S-0/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonStorageNode.cxx, line 105</p>
<p>vtkMRMLMarkupsJsonStorageNode (0x7f95473163a0): vtkMRMLMarkupsJsonStorageNode::ReadDataInternal failed: error opening the file '/var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/BAHCB_vtkMRMLMarkupsFiducialNodeB.json</p>
<p>ERROR: In /Volumes/D/P/S-0/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsJsonStorageNode.cxx, line 1049</p>
<p>vtkMRMLMarkupsJsonStorageNode (0x7f95473163a0): vtkMRMLMarkupsStorageNode::ReadDataInternal failed: error opening the file '/var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/BAHCB_vtkMRMLMarkupsFiducialNodeB.json</p>
<p>Failed to read midline points from file /var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/BAHCB_vtkMRMLMarkupsFiducialNodeB.json</p>
<p>At least ACPC line or midline points must be specified</p>
<p>ACPC Transform standard output:</p>
<p>vtkDebugLeaks has found no leaks.</p>

---

## Post #7 by @lassoan (2021-02-12 01:53 UTC)

<p>Which Slicer version do you use?</p>
<p>Try the following: enable “Preserve CLI module data files” in menu → Edit → Application settings → Developer and restart Slicer, run the module, then check if the referenced json file (such as <code>    /var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/BAHCB_vtkMRMLMarkupsLineNodeC.json</code> in your examples above) exist.</p>

---

## Post #8 by @shebaelena (2021-02-12 17:55 UTC)

<p>I’m currently using the latest preview release-- 4.13.0-2021-02-04. Unfortunately, I’m still getting the same error across the scans with the json files. Would you advise trying with an earlier version?</p>

---

## Post #9 by @lassoan (2021-02-13 03:34 UTC)

<p>I’ve tested the module with the latest Slicer Preview Release (4.13.0-2021-02-11 (revision 29702 / 6942d70)) and it worked well. Please try this version (or the newest Slicer Preview Release).</p>
<p>If you still keep having problems then check if your user has write access to “Temporary directory” (in menu: Edit → Application Settings → Modules). Based on your logs that you previously posted, it is probably <code>/var/folders/j1/s687l10s5qxfrs8rwnbv_rpw0000gn/T/Slicer-alexisgiff/</code>.</p>

---

## Post #10 by @shebaelena (2021-02-15 23:58 UTC)

<p>Hi Andras,</p>
<p>I tried again with the latest preview release and the same issue is occurring- I’ve attached a photo below of the Modules tab in the menu. The directory that seems to be having issues is the one that is selected, so I’m not sure if there’s anything else I can change.</p>
<p>Thank you,<br>
Alexis</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8d84c02f3303eddf96ad73fa1022d45ea12bae0.jpeg" data-download-href="/uploads/short-url/xdQbBr0sb1DgL7dL2OrN3Eb6ETK.jpeg?dl=1" title="Screen Shot 2021-02-15 at 6.56.28 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8d84c02f3303eddf96ad73fa1022d45ea12bae0_2_690x486.jpeg" alt="Screen Shot 2021-02-15 at 6.56.28 PM" data-base62-sha1="xdQbBr0sb1DgL7dL2OrN3Eb6ETK" width="690" height="486" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8d84c02f3303eddf96ad73fa1022d45ea12bae0_2_690x486.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8d84c02f3303eddf96ad73fa1022d45ea12bae0_2_1035x729.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8d84c02f3303eddf96ad73fa1022d45ea12bae0_2_1380x972.jpeg 2x" data-dominant-color="353437"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-15 at 6.56.28 PM</span><span class="informations">2240×1578 392 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @lassoan (2021-02-16 00:18 UTC)

<p>Could you attach the complete application logs of a failed execution (in menu: Help / Report a bug)? Preferably upload the log to somewhere (such as <a href="https://pastebin.com/">pastebin</a>, or to dropbox, onedrive, …) and post just the link here. Thank you!</p>

---

## Post #12 by @shebaelena (2021-02-17 17:09 UTC)

<p>For some reason, the log window is completely empty when I bring it up after trying the transform. I’m not sure if I’m doing something wrong, but I just completed the module and then went to Report a bug. Here is what I am seeing:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a9d051bbd384889d5c6086b42b14b57e81e3c51.jpeg" data-download-href="/uploads/short-url/huGFeCXaR1gC0kbpj0vUNGdvidb.jpeg?dl=1" title="Screen Shot 2021-02-17 at 12.07.28 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9d051bbd384889d5c6086b42b14b57e81e3c51_2_517x307.jpeg" alt="Screen Shot 2021-02-17 at 12.07.28 PM" data-base62-sha1="huGFeCXaR1gC0kbpj0vUNGdvidb" width="517" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9d051bbd384889d5c6086b42b14b57e81e3c51_2_517x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9d051bbd384889d5c6086b42b14b57e81e3c51_2_775x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9d051bbd384889d5c6086b42b14b57e81e3c51_2_1034x614.jpeg 2x" data-dominant-color="302E2F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-17 at 12.07.28 PM</span><span class="informations">2512×1496 438 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thank you so much for all your help.</p>

---

## Post #13 by @lassoan (2021-02-17 17:11 UTC)

<p>This further confirms that the temporary folder that is set in application settings is not writable for your user. I’ve updated temporary folder check at startup 1-2 days ago to deal with such issues. It would be great if you could try if you the latest Slicer Preview Release works correctly.</p>

---

## Post #14 by @shebaelena (2021-02-17 17:41 UTC)

<p>Hi Andras,</p>
<p>It works!! Thank you so much for all the help. I really appreciate it. For the tutorial of this process, which topic should I put it under?</p>

---

## Post #15 by @lassoan (2021-02-17 18:28 UTC)

<p>Awesome!</p>
<p>Regarding module documentation/tutorial: Since the Slicer documentation uses the same markdown format as this forum, the simplest is if you can write the tutorial as a new post in this topic. When it is ready, I’ll move it over to <a href="https://slicer.readthedocs.io/en/latest/">readthedocs</a>.</p>

---

## Post #16 by @shebaelena (2021-02-26 16:58 UTC)

<p>Hi Andras,</p>
<p>I’ve just posted the instructions! Let me know if I can make any changes.</p>
<p>Best,<br>
Alexis</p>

---

## Post #17 by @lassoan (2021-02-26 22:06 UTC)

<p>Thank you! I’ve found it - <a href="https://discourse.slicer.org/t/slicer-acpc-transformation-instructions/16244" class="inline-onebox">Slicer ACPC Transformation Instructions</a></p>

---

## Post #18 by @shebaelena (2021-02-26 16:55 UTC)

<ol>
<li>
<p>Begin by opening the ACPC module in the upper left. Under the ‘Transform Panel’, create a new markups line.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e4e357f8692ef6df5334826ae1f08534412cac8.png" data-download-href="/uploads/short-url/22yfhJ3ydfKRAX4RRemnztz5WtO.png?dl=1" title="Screen Shot 2021-02-26 at 11.40.55 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4e357f8692ef6df5334826ae1f08534412cac8_2_345x116.png" alt="Screen Shot 2021-02-26 at 11.40.55 AM" data-base62-sha1="22yfhJ3ydfKRAX4RRemnztz5WtO" width="345" height="116" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4e357f8692ef6df5334826ae1f08534412cac8_2_345x116.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4e357f8692ef6df5334826ae1f08534412cac8_2_517x174.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e4e357f8692ef6df5334826ae1f08534412cac8_2_690x232.png 2x" data-dominant-color="44494E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-26 at 11.40.55 AM</span><span class="informations">1028×346 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Use this line to define the posterior border of the anterior commissure as well as the anterior border of the posterior commissure in the axial slice. You will need to toggle between slices before you place the second point to do this. Verify in the sagittal slice that this line is accurate. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6f8a343f8db0f692c7efe450ea62d9165b63c67.jpeg" data-download-href="/uploads/short-url/zeOa1rt4MmJzP2YTUuP1jQQYV9R.jpeg?dl=1" title="Screen Shot 2021-02-24 at 9.58.17 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f8a343f8db0f692c7efe450ea62d9165b63c67_2_345x192.jpeg" alt="Screen Shot 2021-02-24 at 9.58.17 AM" data-base62-sha1="zeOa1rt4MmJzP2YTUuP1jQQYV9R" width="345" height="192" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f8a343f8db0f692c7efe450ea62d9165b63c67_2_345x192.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f8a343f8db0f692c7efe450ea62d9165b63c67_2_517x288.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f6f8a343f8db0f692c7efe450ea62d9165b63c67_2_690x384.jpeg 2x" data-dominant-color="6B6969"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-24 at 9.58.17 AM</span><span class="informations">2528×1410 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6887cfa9e6fe1f382e9e60b694f7a4e323aef15.jpeg" data-download-href="/uploads/short-url/wTof3p71l9ujMXkkDZbadvlUfJ3.jpeg?dl=1" title="Screen Shot 2021-02-24 at 9.58.44 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6887cfa9e6fe1f382e9e60b694f7a4e323aef15_2_307x250.jpeg" alt="Screen Shot 2021-02-24 at 9.58.44 AM" data-base62-sha1="wTof3p71l9ujMXkkDZbadvlUfJ3" width="307" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6887cfa9e6fe1f382e9e60b694f7a4e323aef15_2_307x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6887cfa9e6fe1f382e9e60b694f7a4e323aef15_2_460x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e6887cfa9e6fe1f382e9e60b694f7a4e323aef15_2_614x500.jpeg 2x" data-dominant-color="868484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-24 at 9.58.44 AM</span><span class="informations">1590×1294 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>To create the midline, select ‘Create New MarkupsFiducial’ from the dropdown. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc3a44e120fba33ed314ffbbc25604642b5929a8.jpeg" data-download-href="/uploads/short-url/t8GfbelU3vJEyySFgcUVP6QkYre.jpeg?dl=1" title="Screen Shot 2021-02-24 at 9.58.54 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3a44e120fba33ed314ffbbc25604642b5929a8_2_345x180.jpeg" alt="Screen Shot 2021-02-24 at 9.58.54 AM" data-base62-sha1="t8GfbelU3vJEyySFgcUVP6QkYre" width="345" height="180" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3a44e120fba33ed314ffbbc25604642b5929a8_2_345x180.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3a44e120fba33ed314ffbbc25604642b5929a8_2_517x270.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cc3a44e120fba33ed314ffbbc25604642b5929a8_2_690x360.jpeg 2x" data-dominant-color="828282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-24 at 9.58.54 AM</span><span class="informations">2494×1306 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Select at least 5 points along reliable midline structures, (e.g. third ventricle, cerebral aqueduct, etc) ideally on different slices.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/facde1792e749ad92b7b87bad112b97c3b56c60b.jpeg" data-download-href="/uploads/short-url/zMIsPPsmr7kZ8pVGIoXtPXMJHET.jpeg?dl=1" title="Screen Shot 2021-02-24 at 9.59.22 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/facde1792e749ad92b7b87bad112b97c3b56c60b_2_296x250.jpeg" alt="Screen Shot 2021-02-24 at 9.59.22 AM" data-base62-sha1="zMIsPPsmr7kZ8pVGIoXtPXMJHET" width="296" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/facde1792e749ad92b7b87bad112b97c3b56c60b_2_296x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/facde1792e749ad92b7b87bad112b97c3b56c60b_2_444x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/facde1792e749ad92b7b87bad112b97c3b56c60b_2_592x500.jpeg 2x" data-dominant-color="ADACAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-24 at 9.59.22 AM</span><span class="informations">1550×1306 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Under output transform, select ‘Create New Transform,’ and then Apply.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/519fcd27efe4da24074c0018d1dd11aa50719ed6.png" alt="Screen Shot 2021-02-26 at 11.47.56 AM" data-base62-sha1="bE52YxmQgDIxfVQQRsMsNc0DCvQ" width="207" height="69"></p>
</li>
<li>
<p>Open ‘Data’ in the dropdown to navigate to the Subject hierarchy. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a035de08f916158717739b919fe2763f69cdb620.png" alt="Screen Shot 2021-02-26 at 11.49.14 AM" data-base62-sha1="mRhNWgWPhVwD3WuhT49brvJGGDC" width="320" height="40"></p>
</li>
<li>
<p>Right click on the grid along your original MRI scan and select ‘Output transform’. Then, reselect this same scan, and select ‘Harden transform’.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/187da023a8fdd6e39f5bea079ed503fd42a38065.png" data-download-href="/uploads/short-url/3uEBRPrrPqV1oQl3GA1cCRBDXal.png?dl=1" title="Screen Shot 2021-02-26 at 11.51.18 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/187da023a8fdd6e39f5bea079ed503fd42a38065_2_344x109.png" alt="Screen Shot 2021-02-26 at 11.51.18 AM" data-base62-sha1="3uEBRPrrPqV1oQl3GA1cCRBDXal" width="344" height="109" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/187da023a8fdd6e39f5bea079ed503fd42a38065_2_344x109.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/187da023a8fdd6e39f5bea079ed503fd42a38065_2_516x163.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/187da023a8fdd6e39f5bea079ed503fd42a38065_2_688x218.png 2x" data-dominant-color="2A3038"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-26 at 11.51.18 AM</span><span class="informations">1212×386 58.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>You have now completed your AC-PC transformation!</p>

---

## Post #19 by @lassoan (2021-02-28 15:23 UTC)

<p><a class="mention" href="/u/shebaelena">@shebaelena</a> FYI, the documentation update has been <a href="https://github.com/Slicer/Slicer/pull/5492">submitted for review</a>. I’ve also added a “Center volume” option that moves the AC point to the origin, allowing transforming the volume into standard Talairach coordinate system. The changes should appear in the Slicer Preview Release within a few days.</p>

---
