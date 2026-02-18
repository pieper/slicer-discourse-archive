# Change value of label for segmentation

**Topic ID**: 21772
**Date**: 2022-02-03
**URL**: https://discourse.slicer.org/t/change-value-of-label-for-segmentation/21772

---

## Post #1 by @codeenthusiast (2022-02-03 05:55 UTC)

<p>Operating system: MacOS<br>
Slicer version: 4.11</p>
<p>Hi there, I am developing a script to perform radiomics extraction from a set of images with associated segmentations.</p>
<p>Unfortunately, the label values are inconsistent in the segmentations and therefore, I am getting an error when running the script as all label values must be the same. I have read in another forum post <a href="https://discourse.slicer.org/t/how-to-change-the-label-value-of-binary-labelmap-volume/12511/9" class="inline-onebox">How to change the label value of binary labelmap volume? - #9 by lassoan</a> in changing the label value.</p>
<p>However, I am getting an error where it is stating that read_segmentation_info and segmentation_info are not defined. Could you please advise? Thank you!</p>

---

## Post #2 by @ebrahim (2022-02-03 12:10 UTC)

<p>The example you are looking at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-segmentation-files-in-python-outside-slicer" rel="noopener nofollow ugc">was added here</a> in the script repository, which is probably the better place to look.</p>
<blockquote>
<p>However, I am getting an error where it is stating that read_segmentation_info and segmentation_info are not defined. Could you please advise? Thank you!</p>
</blockquote>
<p>Those come from the <code>slicerio</code> package. The <a href="https://pypi.org/project/slicerio/" rel="noopener nofollow ugc">slicerio page here</a> is also useful and shows you what was the intended meaning of those objects that were not defined.</p>

---

## Post #3 by @codeenthusiast (2022-02-03 12:56 UTC)

<p>Thank you Ebrahim. Yes, I was able to reference the slicerio library and sort out the issue. Thanks again.</p>

---
