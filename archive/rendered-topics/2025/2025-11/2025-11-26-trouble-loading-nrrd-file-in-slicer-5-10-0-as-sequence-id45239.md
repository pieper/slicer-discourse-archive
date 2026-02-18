# Trouble loading .nrrd file in Slicer 5.10.0 as sequence

**Topic ID**: 45239
**Date**: 2025-11-26
**URL**: https://discourse.slicer.org/t/trouble-loading-nrrd-file-in-slicer-5-10-0-as-sequence/45239

---

## Post #1 by @gchampa (2025-11-26 16:27 UTC)

<p>when I try and import my .nrrd files as sequences (which they work in slicer 5.8.1) i get an error that slicer cannot read it. They will import as volume but then there is no way to change the colour map, i have tried the way you do in slicer 5.8.1. When i change the colour map it only change the legend bar. The only time the actual colours change is when i click on the presets, it always automatically imports as the rainbow scheme.</p>

---

## Post #2 by @pieper (2025-11-26 19:40 UTC)

<p>Thanks for reporting.  Perhaps it’s related to <a href="https://github.com/Slicer/Slicer/issues/7185">these changes</a>, <a class="mention" href="/u/cpinter">@cpinter</a> ?</p>
<p><a class="mention" href="/u/gchampa">@gchampa</a> can you share a sample dataset that loads differently between the two versions?</p>

---

## Post #3 by @cpinter (2025-11-27 11:42 UTC)

<p>It seems quite likely that it is related.</p>
<p><a class="mention" href="/u/gchampa">@gchampa</a> Please include the entire message, because without that we don’t have any chance to make concrete suggestions.</p>
<p>Also, given that this is about reading a certain data file, if you can share the file, or any file that produces the same issue, then we’ll have everything to investigate and suggest a solution. Thank you!</p>

---

## Post #4 by @gchampa (2025-12-12 19:28 UTC)

<p>yup ive added the nrrd file to onedrive: <a href="https://mcgill-my.sharepoint.com/:u:/g/personal/grace_champagne_mail_mcgill_ca/IQBgYLdpa_qMSYQd-yaGhnA4AXIPAievgsqk5uZ43Q32H48?e=gnaDpH" rel="noopener nofollow ugc">dose_distribution</a> and the output when I try to upload as sequence is</p>
<blockquote>
<p>- Error: Loading /home/gchampagne/Simulations/dose_distribution.nrrd - Error reading file.</p>
<p>- Error: Loading /home/gchampagne/Simulations/dose_distribution.nrrd - Failed to read node dose_distribution (vtkMRMLSequenceNode1) from filename=‘/home/gchampagne/Simulations/dose_distribution.nrrd’</p>
</blockquote>

---

## Post #5 by @gchampa (2025-12-12 19:34 UTC)

<p>I have uploaded how the same file loads into both versions of slicer. Again, in 5.8.1 i load in as a sequence (the format I want) and in 5.10.0 it will not load as sequence so I load as volume. You can see that even though grey scale is selected, it is showing colour in 5.10.0 and when I selected other colours nothing changes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a66b922bac7c6e484c3b94a0b3fcd3636230e0f5.jpeg" data-download-href="/uploads/short-url/nKdJfyD2YaJJUnup17E0sJJPWPr.jpeg?dl=1" title="Screenshot from 2025-12-12 14-30-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a66b922bac7c6e484c3b94a0b3fcd3636230e0f5_2_690x465.jpeg" alt="Screenshot from 2025-12-12 14-30-46" data-base62-sha1="nKdJfyD2YaJJUnup17E0sJJPWPr" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a66b922bac7c6e484c3b94a0b3fcd3636230e0f5_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a66b922bac7c6e484c3b94a0b3fcd3636230e0f5_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a66b922bac7c6e484c3b94a0b3fcd3636230e0f5_2_1380x930.jpeg 2x" data-dominant-color="8BA1D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-12-12 14-30-46</span><span class="informations">1444×974 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f4b99fa75a9d7b8da23837110a0436a86022922.png" data-download-href="/uploads/short-url/krEfJcjGo3a9Ti23VhGoRFzG0Wm.png?dl=1" title="Screenshot from 2025-12-12 14-32-33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f4b99fa75a9d7b8da23837110a0436a86022922_2_690x465.png" alt="Screenshot from 2025-12-12 14-32-33" data-base62-sha1="krEfJcjGo3a9Ti23VhGoRFzG0Wm" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f4b99fa75a9d7b8da23837110a0436a86022922_2_690x465.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f4b99fa75a9d7b8da23837110a0436a86022922_2_1035x697.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8f4b99fa75a9d7b8da23837110a0436a86022922_2_1380x930.png 2x" data-dominant-color="89888C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2025-12-12 14-32-33</span><span class="informations">1444×974 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2025-12-12 20:10 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>These are the errors generated in 5.10 when this data is loaded as a sequence:</p>
<pre><code class="lang-auto">Switch to module:  "Data"
Could not find list kind axis in image file


Algorithm vtkITKImageSequenceReader (0x7ff026ffe020) returned failure for request: vtkInformation (0x600003a46400)
  Debug: Off
  Modified Time: 379967
  Reference Count: 1
  Registered Events: (none)
  Request: REQUEST_DATA
  FROM_OUTPUT_PORT: 0
  ALGORITHM_AFTER_FORWARD: 1
  FORWARD_DIRECTION: 0




vtkMRMLVolumeSequenceStorageNode::ReadDataInternal: Error reading file.


vtkMRMLStorageNode::ReadData: Failed to read node dose_distribution (vtkMRMLSequenceNode1) from filename='/Users/amaga/Downloads/dose_distribution.nrrd'


AddSequence: error reading /Users/amaga/Downloads/dose_distribution.nrrd


static void qSlicerIOManager::showLoadNodesResultDialog(bool, vtkMRMLMessageCollection *) Errors occurred while loading nodes: "- Error: Loading /Users/amaga/Downloads/dose_distribution.nrrd - Error reading file.\n- Error: Loading /Users/amaga/Downloads/dose_distribution.nrrd - Failed to read node dose_distribution (vtkMRMLSequenceNode1) from filename='/Users/amaga/Downloads/dose_distribution.nrrd'\n"
</code></pre>

---

## Post #7 by @cpinter (2025-12-12 20:42 UTC)

<p>Thank you!</p>
<p>The most help would be if we could have the actual file for testing.</p>
<p>If that’s not possible, then maybe pasting the nrrd file header would give us some clue (since the error says list kind axis could not be found, seeing what those axes are defined as would certainly help).</p>

---

## Post #8 by @lassoan (2025-12-14 21:38 UTC)

<p><a class="mention" href="/u/gchampa">@gchampa</a> Is this a 4D file? How did you create this file? Previous versions of Slicer made random guesses about files that had more than 3 dimensions, which sometimes were correct sometimes not. Slicer-5.10 requires unambiguous definition of axes (spatial, vector component, time, etc), mostly by relying on proper setting of the <code>kinds</code> field in NRRD files.</p>
<p>If you copy here the NRRD image header then we can give you more specific advice.</p>

---

## Post #9 by @muratmaga (2025-12-15 00:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="45239">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>here the NRRD image header th</p>
</blockquote>
</aside>
<p>This is the header from the file provided:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: double
dimension: 4
space: left-posterior-superior
sizes: 2 201 201 201
space directions: none (1,0,0) (0,1,0) (0,0,1)
centerings: ??? cell cell cell
kinds: 2-vector space space space
labels: "" "x" "y" "z"
endian: little
encoding: gzip
space origin: (-100,-100,-100)
Executable:=RapidBrachyMC
Writer:=Teem
distance_unit:=mm
dose_unit:=Gy

</code></pre>

---

## Post #10 by @lassoan (2025-12-15 02:05 UTC)

<p>I see the issue now. The image was attempted to be loaded as a 3D+t sequence, while it is a 3D+component volume. Since Slicer supports loading/saving of 5D data, the axis kinds checks had to be made more reliable (so that for example we can distinguish a 3D+component+time image from a 3D+time+component image).</p>
<p>The fix is simple: specify the axis kinds to match the actual data content. In this case, use <code>list</code> instead of <code>2-vector</code>. You can save a numpy array into a nrrd file like this:</p>
<pre data-code-wrap="python"><code class="lang-python">import numpy as np
import nrrd

img = np.zeros([201,201,201, 2])

header = {
    'space': 'left-posterior-superior',
    'kinds': ['domain', 'domain', 'domain', 'list'],
    'labels': ["", "", "", "time"],
    'units': ["", "", "", "s"],
    'space origin': [-137.16099548, -36.80649948, -309.71899414],
    'space directions': [[1.953125, 0., 0.], [0., 1.953125, 0.], [0., 0., 1.953125], [np.nan, np.nan, np.nan]],
    'axis 3 index type': 'numeric',
    'axis 3 index values': "1.2 1.4"
}

nrrd.write("c:/tmp/test.seq.nhdr", img, header)
</code></pre>
<p>The resulting file header will look like this:</p>
<pre data-code-wrap="txt"><code class="lang-txt">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: double
dimension: 4
space: left-posterior-superior
sizes: 201 201 201 2
space directions: (-1.9531249999999998,0,0) (0,-1.9531249999999998,0) (0,0,1.9531249999999998) none
kinds: domain domain domain list
labels: "" "" "" "time"
units: "" "" "" "s"
endian: little
encoding: gzip
space origin: (137.16099548000003,36.806499479999999,-309.71899414000001)
data file: test.seq.raw.gz
DataNodeClassName:=vtkMRMLScalarVolumeNode
axis 3 index type:=numeric
axis 3 index values:=1.2 1.4
</code></pre>
<p>For more information, check out <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/sequences.html#volume-sequence-file-format-seq-nrrd">full specification of the sequence file format</a> and examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-a-4d-volume-in-python-outside-slicer">script repository</a>.</p>

---
