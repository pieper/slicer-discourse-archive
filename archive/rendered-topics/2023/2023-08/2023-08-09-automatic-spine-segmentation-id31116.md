# Automatic spine segmentation

**Topic ID**: 31116
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/automatic-spine-segmentation/31116

---

## Post #1 by @drvarunagarwal (2023-08-09 02:22 UTC)

<p>Hi,</p>
<p>Is there any option for vertebrae segmentation? Please advise</p>

---

## Post #2 by @Thibault_Pelletier (2023-08-09 06:02 UTC)

<p>Hi <a class="mention" href="/u/drvarunagarwal">@drvarunagarwal</a>,</p>
<p>As <a class="mention" href="/u/pieper">@pieper</a> said, TotalSegmentator or the equivalent MONAI Label bundle can handle it for CT images. The list of handled classes is given here : <a href="https://github.com/wasserth/TotalSegmentator#class-details" class="inline-onebox" rel="noopener nofollow ugc">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104 important anatomical structures in CT images</a>.<br>
You can test it out easily by downloading the TotalSegmentator extension from the Extension Manager.</p>
<p>Best,<br>
Thibault</p>

---

## Post #3 by @rbumm (2023-08-09 06:47 UTC)

<p>TotalSegmentator may miss some parts of the costovertebral junction.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e2bec8c124cf4fdd3c5c9f562355e58525d832d.png" alt="image" data-base62-sha1="4iUqIhMowIlnQMQezlrBvXo2hn7" width="321" height="287"></p>
<p>If you need full details of the spine you will probably want to threshold the spine or use intensity masked grow from seeds. And cut away structures that you do not need.<br>
You can solidify the vertebra with <a href="https://gist.github.com/lassoan/0f45db8bae792ea19ccad36ceefbf52d">this Python code</a>.</p>

---

## Post #4 by @lassoan (2023-08-12 16:55 UTC)

<p>More recent versions of TotalSegmentator model may work better, but if you want to robustly segment the vertebrae and discs then you may need to use a more specialized model. <a class="mention" href="/u/ron">@Ron</a> has been working on such a spine segmentation model - he may provide more details.</p>

---
