# Slicer Transform vs elastix Transform

**Topic ID**: 2507
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/slicer-transform-vs-elastix-transform/2507

---

## Post #1 by @brhoom (2018-04-03 20:41 UTC)

<p>It is not clear the relation between them, here is what I did:</p>
<ul>
<li>Transform manually an image imgf using Slicer Transforms module, only one translation t_x in LR and one rotation θ_x in LR
<ul>
<li>t_x=10 mm , θ_x= 45 degrees</li>
<li>the rotation matrix mSlicer= [[1,0,0,0],[0,.71,-.71,0],[0,.71,71,0],[0,0,0,1]]</li>
<li>save the transformed image as imgm</li>
</ul>
</li>
<li>Use elastix to register imgm to imgf again using rigid transform parameters, ensure the are aligned
<ul>
<li>(TransformParameters θ_x , θ_y , θ_z , t_x , t_y , t_z)</li>
<li>get the matrix from the angles (I used an external script).</li>
<li>mE= [[ 1.,-0.,0.,t_x],[ 0.,0.71,0.71,t_y],[-0.,-0.71,0.71,t_z],[0.,0.,0.,1.]]</li>
</ul>
</li>
<li>mE is not similar to mS, there is problem of the sign as well.</li>
</ul>
<p>What I am missing?</p>

---

## Post #2 by @lassoan (2018-04-03 22:02 UTC)

<p>Elastix can only return the transform as a displacement field. It does not return parameters such as translation or rotation.</p>
<p>We plan to work with Elastix developers to add the possibility to retrieve linear or bspline transforms, but it is not available yet.</p>

---

## Post #3 by @brhoom (2018-04-04 08:42 UTC)

<p>Thanks Andras for your concern,</p>
<p>still not clear, what do you mean by transform as displacement field?</p>
<p>This is what elastix returns:<br>
<code>(TransformParameters θ_x , θ_y , θ_z , t_x , t_y , t_z)</code><br>
3 angles in radians and 3 translations in mm.<br>
Aren’t these the 3D rigid transform 6 parameters?<br>
Please correct me if I am wrong, in your extension, you saved the result of elastix registration transform as a big hdf5 transform file, which includes each point in the moving image and its displacement<br>
<code>point_0, dis_x0, dis_y0, dis_z0, point_1, dis_x1, dis_y1, dis_z1, ..., point_n, dis_xn, dis_yn,dis_zn</code><br>
How did you compute the displacement field from the above 6 parameters?</p>

---

## Post #4 by @brhoom (2018-10-15 15:57 UTC)

<blockquote>
<p>We plan to work with Elastix developers to add the possibility to retrieve linear or bspline transforms, but it is not available yet.</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> its been a while, any update on this?</p>

---

## Post #5 by @lassoan (2018-10-16 14:32 UTC)

<p>We have not yet started the project that requires this feature, so there is no updates so far.</p>

---

## Post #6 by @Alex_Vergara (2019-02-25 13:49 UTC)

<p>Again, We need this feature, any update on this? I cant use elastix the way it is now without this feature.<br>
Actually is the input transformation what I am missing. I need that the Moving volume may have already associated a transformation, So I will just modify it.<br>
Hmm, I realize this is a whole new request, I will make the new thread.</p>

---
