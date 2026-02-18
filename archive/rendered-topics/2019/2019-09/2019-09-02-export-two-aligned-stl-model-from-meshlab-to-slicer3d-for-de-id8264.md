# Export two aligned STL model from Meshlab to SLICER3D for deviation Measurement

**Topic ID**: 8264
**Date**: 2019-09-02
**URL**: https://discourse.slicer.org/t/export-two-aligned-stl-model-from-meshlab-to-slicer3d-for-deviation-measurement/8264

---

## Post #1 by @ss_sabz (2019-09-02 16:44 UTC)

<p>Hi:</p>
<p>I need to find Deviation between two STL model points, So i found this link:</p>
<p><a href="https://www.researchgate.net/post/how_to_compare_quantify_populate_two_stl_models_having_shape_difference_to_see_result_as_color_stl_file_and_bar_telling_plus_and_minus_changes" rel="noopener nofollow ugc">How to compare/quantify (populate) two .stl models having shape difference to see result as color stl file and bar telling plus and minus changes?</a></p>
<p>I one part of if t Mr <strong>P.G. Makhija</strong> (from  Modern Dental College &amp; Research Centre, Indore, INDIA) said:</p>
<blockquote>
<p>Thanks Petr Henys and Olivier Etienne for your kind suggestions. I was<br>
able to do the job with help of Meshlab first by aligning meshes and<br>
then analysing them with Slicer3D software’s shape population viewer<br>
module. The problem is solved for me for the time being. Thanks.</p>
</blockquote>
<p>So i have used the <a href="http://www.meshlab.net/" rel="noopener nofollow ugc">MESHLAB</a> Software and aligned two Stl file together like this:<br>
<a href="https://i.stack.imgur.com/tZ7Es.png" rel="noopener nofollow ugc"><img src="https://i.stack.imgur.com/tZ7Es.png" alt="enter image description here" width="690" height="388"></a><br>
<a href="https://i.stack.imgur.com/HnX00.png" rel="noopener nofollow ugc"><img src="https://i.stack.imgur.com/HnX00.png" alt="enter image description here" width="690" height="388"></a></p>
<p>i can import the separated <strong>stl</strong> file in sliver like this:</p>
<p><a href="https://i.stack.imgur.com/r5QJ9.png" rel="noopener nofollow ugc"><img src="https://i.stack.imgur.com/r5QJ9.png" alt="enter image description here" width="690" height="388"></a></p>
<p>But according two  Mr <strong>P.G. Makhija</strong> point View i can not export aligned two <strong>stl</strong> file from <a href="http://www.meshlab.net/" rel="noopener nofollow ugc">MESHLAB</a> to <a href="https://slicer.org" rel="noopener nofollow ugc">SLICER3D</a>?</p>
<p>I will appreciate your help with this situation.</p>
<p>My similar question link via stack exchange:</p>
<p><a href="https://engineering.stackexchange.com/questions/29929/export-two-aligned-stl-model-from-meshlab-to-slicer3d-for-deviation-measurement" rel="noopener nofollow ugc">Export two aligned STL model from Meshlab to SLICER3D for deviation Measurement</a></p>

---

## Post #2 by @steffen-o (2019-09-04 14:00 UTC)

<p>I don’t really know if I understand your question but you should use “Matrix:freeze current Matrix” in Meshlab after the alignment by right click on the transformed model (with an asterisk) . It’s like "Harden Transform in 3DSlicer. Otherwise, the tranformation matrix is not appied to the model.</p>

---

## Post #3 by @tsehrhardt (2019-09-05 12:03 UTC)

<p>Do what steffen-o suggested: freezing the matrix for the aligned models before exporting.</p>
<p>You can also run the deviation in Meshlab 2016 using Filters --&gt; Sampling --&gt; Distance from Reference Mesh. This allows you to generate the signed distances and will even store the distance values in the Measured Mesh as a vertex quality which you can then use to colorize the model (Filters --&gt; Color Creation and Processing --&gt; Colorize by Vertex Quality) and also export as a colorized PLY if you want.</p>

---
