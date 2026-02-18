# Mirror copy of a segmentation

**Topic ID**: 6143
**Date**: 2019-03-14
**URL**: https://discourse.slicer.org/t/mirror-copy-of-a-segmentation/6143

---

## Post #1 by @Lucas_Formighieri (2019-03-14 14:00 UTC)

<p>Hello,</p>
<p>I would like to know if it is possible to make a mirror copy of a segmentation. For example, I have the segmentation of the left side of a face and I want to make a “right” side of the same face.</p>
<p>Thanks,</p>
<p>Lucas</p>

---

## Post #2 by @fedorov (2019-03-14 15:00 UTC)

<p>I have not tried it, but you might be able to do this with the Surface Toolbox module, see earlier post here: <a href="https://discourse.slicer.org/t/mirror-in-surface-toolbox/3297" class="inline-onebox">Mirror in surface toolbox</a></p>

---

## Post #3 by @muratmaga (2019-03-14 19:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> This might actually be an useful addition to segment editor. We segment bilaterally symmetric structures (e.g., l/r sides of a cranial bone) and in some cases it will speed the segmentation to mirror one side to the other (provided that the axis of symmetry and the coordinate system line up).</p>

---

## Post #4 by @Lucas_Formighieri (2019-03-15 15:47 UTC)

<p>Thanks, it worked really well.</p>

---

## Post #5 by @cpinter (2019-03-15 15:53 UTC)

<p>I can see its utility too, but adding mirroring into Segment Editor will need transformation features as well, because the position of the mirrored segment is kind of undeterministic, and needs to be adjusted in virtually every case.</p>
<p>Adding transformation features into Segment Editor is a big decision, because so far the module only contained segmentation features, and delineating regions on anatomical images does not need transformation if ever, except for this new mirroring idea (which, again, I think would be useful too). Maybe the mirroring effect could allow post-mirror placement option, but I cannot see a convenient way for that right now. Ideas are welcome.</p>
<p>In the meantime the workflow is: export to model -&gt; surface toolbox -&gt; transforms -&gt; import to segmentation (quite lengthy indeed).</p>

---

## Post #6 by @cpinter (2019-03-15 16:14 UTC)

<p>What occurred to me is that in the meantime I could make model import to segmentation as easy as drag&amp;drop model into a segmentation in the Data module. It would be quite easy to do I think. Then both export and import would be possible from there.</p>

---

## Post #7 by @lassoan (2019-03-15 16:14 UTC)

<p>Cloning and mirroring are modeling tools, not segmentation tools. The main idea in segmentation that you rely on the underlying image - I would not encourage people to segment by mirroring.</p>

---

## Post #8 by @hortakc (2023-06-21 03:54 UTC)

<p>Hi Lucs Please, can you tell me how you mirror your segmentation?</p>
<p>Thanks!</p>

---
