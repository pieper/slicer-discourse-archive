# Errors with GenParaMesh

**Topic ID**: 8377
**Date**: 2019-09-10
**URL**: https://discourse.slicer.org/t/errors-with-genparamesh/8377

---

## Post #1 by @ytaneja (2019-09-10 21:46 UTC)

<p>Hello,</p>
<p>Whenever I run the GenParaMesh step with my segmentation (which has successfully gone through the SegPostProcess step), it results in this error through Slicer 4.8.1, Slicer 4.10.2, and Slicer SALT 2.0.0. I realize this issue has come up before, and it was determined to be due to windows 10 (it apparently works on Linux): <a href="https://discourse.slicer.org/t/paratospharmmesh-completed-with-errors-on-win10/4814/8" class="inline-onebox">ParaToSPHARMMesh completed with errors on win10</a></p>
<p>Below is the message that comes each time once I cancel the seemingly infinite operation after letting it run for over a day:</p>
<p>GenParaMesh standard output:<br>
Euler Number ok = 2</p>
<p>flag = 0 iterations performed: 524<br>
flag = 0 iterations performed: 535<br>
initially active: {}.<br>
fromC[expr_] := expr /. (mant_Real)<em>e + (expon_Integer) :&gt; mant</em>10^expon;</p>
<p>Any help is appreciated, thank you!<br>
Yash</p>

---

## Post #2 by @styner (2019-09-10 22:13 UTC)

<p>Thanks Yash,<br>
Not sure what the problem is (and I think it’s quite possibly different from the ParaToSPHARM error you referenced). Could you provide a screenshot of your segmentation (e.g. using the SALT Dataimporter visualization, or simply the mesh generated with Slicer from the label file). It would be good to look at the mesh to ensure it does not have holes/handles. (A Euler number of 2 does not guarantee spherical topology, but a Euler number other than 2 guarantees non-spherical topology).</p>
<p>You can also run the GenParaMesh step with 0 iterations, and the tool should provide you with the initial spherical mapping. Visualizing that initial spherical parametrization is quite indicative of potential issues.</p>
<p>Best<br>
Martin</p>

---

## Post #3 by @bpaniagua (2019-09-11 11:59 UTC)

<p>Hi Yash,</p>
<p>Additionally to the questions asked by Martin, what is the format of your segmentations?<br>
Does SegPostProcess finish succesfully?</p>
<p>THanks,<br>
Bea</p>

---

## Post #4 by @ytaneja (2019-09-11 21:43 UTC)

<p>The SegPostProcess did finish successfully, but Martin is right: even though the Euler number was 2, it did not guarantee spherical topology. I went on to change my segmentation method and got everything to work.</p>
<p>Thank you both for your help!</p>

---

## Post #5 by @bpaniagua (2019-09-12 13:02 UTC)

<p>Great to hear things worked!<br>
Just curious, can you please let us know how did you change your segmentation?</p>

---

## Post #6 by @ytaneja (2019-09-12 17:58 UTC)

<p>Yes, at first the segmentation was of cartilage and it appeared to be rather flat, even though it passed through the SegPostProcess. To fix this, I changed the segmentation to be of cartilage <em>and</em> bone, allowing it to complete all steps properly, ensuring spherical geometry.</p>

---
