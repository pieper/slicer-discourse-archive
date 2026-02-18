# File edited in preview version 4.11.0 now lacks all segments. Please help!

**Topic ID**: 12591
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/file-edited-in-preview-version-4-11-0-now-lacks-all-segments-please-help/12591

---

## Post #1 by @tessamontague (2020-07-17 04:20 UTC)

<p>Operating system: OS X<br>
Slicer version: 4.11.0<br>
Expected behavior: I was using the stable version of Slicer (4.10.2) to annotate an MRI brain (months of work) but the paint tool was very laggy, so I downloaded the preview version 4.11.0 to see if it improved things. Once it seemed to be working well, I saved the file, hoping to eventually return to editing it with the stable version since I am collaborating with others who use the stable version.</p>
<p>Actual behavior: However, now when I open the mrml file in the stable 4.10.2 release, all of the segments are missing except for 1 of them. If I go to Data, I can see that the segments are there, but they don’t show up in the Segment Editor. I see the same thing if I open this file on a different computer, so somehow the file has been saved differently using 4.11.0, so it no longer displays the information correctly on 4.10.2.</p>
<p>I’d really appreciate any help getting my file to display correctly in the stable version 4.10.2. It seems like there is a bug in the preview version of slicer with how it saves files.</p>

---

## Post #2 by @lassoan (2020-07-17 04:26 UTC)

<p>Scenes that you save in a Slicer version are only guaranteed to work in that version or later versions. You can of course still save data in a format that is compatible with older versions.</p>
<p>For example, you can export segmentation to a labelmap node and you can load that labelmap into Slicer-4.10.2 and convert it to segmntation. However, since infrastructure so dramatically improved since Slicer-4.10.2, if you do a lot of segmentations, I would recommend to upgrade to a recent Slicer-4.11 version.</p>

---

## Post #3 by @tessamontague (2020-07-17 15:55 UTC)

<p>Thank you for the response. I’m afraid I’m not very experienced with 3D Slicer and I’m failing to get this to work.</p>
<p>In version 4.11.0 I went to &gt; Segmentations &gt; Export/import models and labelmaps</p>
<ul>
<li>Export</li>
<li>Labelmap</li>
<li>Export to new labelmap</li>
</ul>
<blockquote>
<p>Advanced</p>
</blockquote>
<ul>
<li>All exported segments</li>
<li>my reference volume</li>
</ul>
<blockquote>
<p>Export to files</p>
</blockquote>
<ul>
<li>STL</li>
<li>Scale 1.00</li>
<li>Coordinate system LPS<br>
<em>Export</em></li>
</ul>
<p>Now in Version 4.10.2 I add the original MR data (.nii.gz) (“volume”) and I add the labelmaps (.stl) (“model”).</p>
<p>To convert the labelmaps to segments I go to &gt; Data</p>
<ul>
<li>right click on one of the labelmaps</li>
<li>select “convert model to segmentation node”</li>
</ul>
<p>However, the label maps don’t seem to have preserved their positioning/scale on the original map, so when I view the data in Four-up and toggle slice visibility in 3D view, the labelmaps are not overlaid on the 3D volume and the scale is wrong.</p>
<p>How do I save the labelmaps so that they preserve their position and size?</p>
<p>thank you very much</p>

---

## Post #4 by @lassoan (2020-07-17 16:28 UTC)

<p>I would not recommend to export segmentation as STL, as it is a lossy storage format for segmentations created by Segment Editor (which uses binary labelmap representation). Instead:</p>
<p>Simple export/import:</p>
<ul>
<li>In Slicer Preview Release: right-lick on the segmentation in Data module and choose “Export visible segments to binary labelmap”</li>
<li>In old Slicer release: load the segmentation file by drag-and-dropping to application window and clicking OK</li>
</ul>
<p>Export/import with preserving colors:</p>
<ul>
<li>In Slicer Preview Release:
<ul>
<li>right-lick on the segmentation in Data module and choose “Export visible segments to binary labelmap”</li>
<li>save the exported labelmap and the corresponding color table (.nrrd and .ctbl file)</li>
</ul>
</li>
<li>In old Slicer release:
<ul>
<li>load the color table file by drag-and-dropping to application window and clicking OK</li>
<li>load the segmentation file by drag-and-dropping to application window, check “Show options”, scroll to the right, and select the color table that you loaded (at the bottom of the list) and clicking OK</li>
</ul>
</li>
</ul>

---

## Post #5 by @tessamontague (2020-07-17 16:52 UTC)

<p>Ah ok thank you. The only thing is when I do that the segmentations are a single file, and they’re not aligned on the original volume and editable like they were in the original version (or on 4.11.0). I think I solved the issue a different way:</p>
<ul>
<li>
<p>the alignment was fixed by changing the coordinate system to RAS when I exported the segments to labelmaps</p>
</li>
<li>
<p>I imported the labelmaps as segments (quicker than my method above):</p>
</li>
</ul>
<blockquote>
<p>Add data &gt; choose file</p>
</blockquote>
<ul>
<li>
<p>change “model” to “segmentation”</p>
</li>
<li>
<p>once I had imported all of the segmentations they were each in separate segmentations rather than as options under a single “Segmentation”. To solve this I did:</p>
</li>
</ul>
<blockquote>
<p>Segmentations<br>
Active segmentation - “add new segmentation” - name it “Segmentation”<br>
copy/move segments</p>
</blockquote>
<ul>
<li>select each segment from the dropdown menu, click on it, then use &lt;+ to add it to Segmentation</li>
<li>once all of the segments have been added go to &gt; Data. All of the segments should be under “Segmentations” so delete the individual files.</li>
<li>to edit them, go to Segment editor, change “Segmentation : Segmentation”, and select your master volume. Then select a segment to edit and say yes to converting to binary map</li>
</ul>
<p>The disadvantage here is you have to recolor all of the segments yourself.</p>
<p>Thanks for your help!</p>

---

## Post #6 by @lassoan (2020-07-17 16:58 UTC)

<p>For segments edited in Segment Editor, you lose details if you export them to STL and then import them. For this reason alone, I would strongly recommend exporting to labelmap.</p>

---

## Post #7 by @tessamontague (2020-07-17 18:16 UTC)

<p>Ah yes, I see what you mean.</p>
<p>Great that worked, thank you!</p>
<p>For anyone else that has this problem, after following your instructions to load the color map and segmentation file, you go to &gt; Data then right-click on Segmentation-label &gt; convert labelmap to segmentation node, and everything is restored.</p>
<p>Thanks again!</p>

---
