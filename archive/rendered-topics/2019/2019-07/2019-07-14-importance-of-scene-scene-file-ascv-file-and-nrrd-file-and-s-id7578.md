# Importance of Scene SCENE file, ASCV file and NRRD file and SCENE PNG file and ROI file

**Topic ID**: 7578
**Date**: 2019-07-14
**URL**: https://discourse.slicer.org/t/importance-of-scene-scene-file-ascv-file-and-nrrd-file-and-scene-png-file-and-roi-file/7578

---

## Post #1 by @NoobForSlicer (2019-07-14 22:10 UTC)

<ul>
<li>So let’s say you have a a big volume, you transform it &gt;&gt; and click “Harden the transformation”</li>
</ul>
<ol>
<li>What does that do to the transformation actually and what could be the consequences of not hardening the transformation?</li>
</ol>
<ul>
<li>
<p>After that you &gt;&gt; crop the big volume<br>
Suddenly a new volume appears in the Data module.</p>
</li>
<li>
<p>You go to save but &gt;&gt;&gt; for you it is important that &gt; the new cropped volume has a) same position (menaing that 3D file exported later using only that little cropped volume, will be synced and will match the big volume you’ve been cropping. For example you can crop  5 files  however once they are segmented and exported &gt;&gt;&gt;&gt;&gt; they should match their position and relations to one another)</p>
</li>
</ul>
<ol start="2">
<li>
<p>Which files are important for that, which ones should I checked in the saved box? I have deleted everything besides NRRD file and then I closed all slicer files and opened just NRRD and then I just segmented and opened it and I did so with few cropped NRRD files and &gt;&gt;&gt; in the end their positions were okay and they were still in their original places. So I guess it is okay to check  only  NRRD file upon saving?</p>
</li>
<li>
<p>How can this be done if Linear transformation was not saved at all along with the cropped NRRD file?</p>
</li>
<li>
<p>What is the purpose of linear transformation file then ?</p>
</li>
<li>
<p>What other information will scene file hold and NRRD file won’t ? How can this be done without SCENE file? Shouldn’t Scene file hold information such as position of the NRRD in relation to the 0 points on xyz axis?  Will this somehow trick me down the road in some way that I am not getting here?</p>
</li>
</ol>
<p>So far exporting only the NRRD files and segmenting them&gt;&gt;&gt; putting them together then in some 3d program and they all appear to be nicely in their places. AM I missing something here? I just find it hard to believe I can ignore all the other files and I am affraid I might be making some big mistake.</p>
<p>Please let me know if you can answer my 5 questions, I hope they aren’t too much.</p>

---

## Post #2 by @ljod (2019-07-14 22:42 UTC)

<p>The short answer is the harden transform applies it to your data using image resampling, and the nrrd header contains the voxel origin or spatial position of each volume. Once you harden, the additional transform file is no longer applied. But it is important to re-create the series of steps you took, if this is for scientific research.</p>

---

## Post #3 by @NoobForSlicer (2019-07-14 23:17 UTC)

<p>What does it mean re-create the series of steps I took?</p>
<p>What steps and how to “re-create them”?<br>
In which volume? With new cropped volume? You mean that I should redo the transformation on the cropped NRRD file as well?</p>
<p>Hmm or you’re just referring I have to speficy what I did in the paper to be published?</p>

---

## Post #4 by @NoobForSlicer (2019-07-14 23:35 UTC)

<p>And what is the difference between NRRD and  NHRD… I’ve been saving NRRD and worked nicely so far… Is there some difference?</p>

---

## Post #5 by @pieper (2019-07-15 13:10 UTC)

<p><a href="http://teem.sourceforge.net/nrrd/format.html" class="onebox" target="_blank" rel="nofollow noopener">http://teem.sourceforge.net/nrrd/format.html</a></p>

---

## Post #6 by @ljod (2019-07-15 13:25 UTC)

<p>Just meant it is good to save your steps for scientific documentation.</p>

---

## Post #7 by @NoobForSlicer (2019-07-15 13:43 UTC)

<p>ohh okay yes of course!! Thank you guys soo much! Great!! NRRD contains positions and stuff because it would cause major headache for researchers trying to split files or crop files.</p>
<p>This way it is ensured, positions of cropped files are preserved in relation to the old big volume.</p>

---

## Post #8 by @NoobForSlicer (2019-07-15 13:44 UTC)

<p>waow incredible read! Thanks a lot! I can deepen  my knowledge starting from the basis of what Lauren told me</p>

---
