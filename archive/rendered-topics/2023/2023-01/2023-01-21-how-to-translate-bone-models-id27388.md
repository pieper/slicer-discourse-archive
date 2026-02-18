# How to translate bone models?

**Topic ID**: 27388
**Date**: 2023-01-21
**URL**: https://discourse.slicer.org/t/how-to-translate-bone-models/27388

---

## Post #1 by @roshans17 (2023-01-21 03:55 UTC)

<p>Hi,</p>
<p>I recently had a question about displaying iv files on to slicer. This was solved with the amazing help of <a class="mention" href="/u/lassoan">@lassoan</a> (<a href="https://github.com/PerkLab/SlicerSandbox/commit/14753dfb8f53e59609a5e0a46a25d02dbab2cff4" rel="noopener nofollow ugc">source</a>). He made an iv file displayer in the sandbox extension which works perfectly. I currently want to learn how to allow the user to transform the bones in the x, y, or z axis. I was wondering what the best way to go about this would be. I was going to create a new module to help me accomplish this but am struggling as to how I would access the polydata that is in the sandbox extension that displays the iv files right now.</p>
<p>PS: This might seem like a basic question but I am incredibly new to slicer and don’t understand its architecture that well so any advice/materials that could help me understand the big-level architecture would be much appreciated too</p>
<p>Thank you in advance.</p>

---

## Post #2 by @roshans17 (2023-01-25 21:14 UTC)

<p>Hi all,</p>
<p>Any thoughts about the question posted above? Replying to the post for visibility purposes. Thank you in advance.</p>

---

## Post #3 by @lassoan (2023-01-26 23:16 UTC)

<p>You can apply a transform to the model node to transform it. You can enable interactive editing of the transform in 3D views, but I would recommend to position/orient it using landmark registration.</p>

---

## Post #5 by @roshans17 (2023-01-31 05:05 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. If I were to create my own module, how would I be able to access the modelNode located on the ImportOpenInventor.py file on the new module python script?</p>
<p>I notice that I am able to apply a transformation matrix via the transform tab but I want our lab to be able to feed our own specific transformation files that will manipulate the bones in the motions we want. I saw this function on the docs and was wondering if it would be useful for my purposes modelNode = slicer.util.getNode(“MyModel”)</p>
<p>Any thoughts?</p>

---

## Post #6 by @roshans17 (2023-02-15 23:30 UTC)

<p>My question may be more specific and answerable if I give some context to the problem I am trying to solve. I am trying to transform 15 nodes (bones) by passing in a file that has their respective transformation matrix. An example of the .dat file that stores the 15 transformation matrix can be found here: <a href="https://drive.google.com/file/d/1p7kUwzsx4JR1FxGTpEW8VcZY47IruXKv/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">14727_Motion01R.dat - Google Drive</a></p>
<p>We have 10 other .dat files that house their own set of 15 transformation matrices. Together, the files and the matrices housed within them represent a full movement. Ultimately, I would like to be able to insert these 10 files and then be able to visualize the movement in slicer. I have played around with the transforms module, however, I do not believe that this module has the features I am looking for.</p>
<p>Any help would be much appreciated. Thank you in advance.</p>

---

## Post #7 by @lassoan (2023-04-13 12:48 UTC)

<p>You can already load/save/record/replay transformation sequences and apply them to model nodes. We use the sequence file format for this, which is a simple text file that you should be able to create from your .dat file. The specification is available <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">here</a>.</p>
<p>Example file: <strong>test.igs.nrrd</strong></p>
<pre><code class="lang-auto">NRRD0004
dimension: 3
kinds: domain domain list
sizes: 0 0 5
space dimension: 2
Seq_Frame0000_Timestamp:=3.114000000000033
Seq_Frame0000_StylusToReferenceTransform:=1 0 0 0 0 1 0 0 0 0 1 5.645142857142858 0 0 0 1
Seq_Frame0000_StylusToReferenceTransformStatus:=OK
Seq_Frame0001_Timestamp:=3.19399999999996
Seq_Frame0001_StylusToReferenceTransform:=1 0 0 0 0 1 0 0 0 0 1 6.143761904761904 0 0 0 1
Seq_Frame0001_StylusToReferenceTransformStatus:=OK
Seq_Frame0002_Timestamp:=3.254000000000133
Seq_Frame0002_StylusToReferenceTransform:=1 0 0 0 0 1 0 0 0 0 1 6.487333333333334 0 0 0 1
Seq_Frame0002_StylusToReferenceTransformStatus:=OK
Seq_Frame0003_Timestamp:=3.314000000000078
Seq_Frame0003_StylusToReferenceTransform:=1 0 0 0 0 1 0 0 0 0 1 6.760428571428571 0 0 0 1
Seq_Frame0003_StylusToReferenceTransformStatus:=OK
Seq_Frame0004_Timestamp:=3.394000000000041
Seq_Frame0004_StylusToReferenceTransform:=1 0 0 0 0 1 0 0 0 0 1 6.92252380952381 0 0 0 1
Seq_Frame0004_StylusToReferenceTransformStatus:=OK
</code></pre>
<p>The <code>.igsio.nrrd</code> file reader and other useful modules for calibration and tracking provided by <strong>SlicerIGT extension</strong>.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> When I read the file above then an empty image file is added to the scene as well. Is it possible to prevent that by changing the .igs.nrrd file content or it would need a change in the reader?</p>

---

## Post #8 by @Sunderlandkyl (2023-04-13 13:54 UTC)

<p>Probably it would need a change in the reader.</p>

---
