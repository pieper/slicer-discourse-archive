# Free Form Deformation Registration

**Topic ID**: 22058
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/free-form-deformation-registration/22058

---

## Post #1 by @Vir (2022-02-18 21:57 UTC)

<p>Hello .<br>
I’m trying to register two lung CT volume from the same patient (baseline and post ) using the B-spline free form deformation algorithm where my initial transformation is a composition of Affine and Initial B-spline followed by the regular b-spline algorithm .<br>
So my question is is there any documentation for registration about this method using 3D Slicer .</p>
<p>Thank you for your help.</p>

---

## Post #2 by @lassoan (2022-02-19 00:10 UTC)

<p>Would you like to know how you can do affine+bspline image registration in Slicer? See instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#automatic-image-registration">here</a>.</p>

---

## Post #3 by @Vir (2022-02-19 17:56 UTC)

<p>Thank you<br>
So I was following the instructions , but it mentions</p>
<ul>
<li>Select Preset: <code>generic (all)</code> performs deformable registration; <code>generic rigid (all)</code> performs rigid registration</li>
</ul>
<p>Can you please tell me what generic (all ) means , to perform deformable registration as I’m not able to locate this .</p>
<p>Thank you</p>

---

## Post #4 by @lassoan (2022-02-19 19:58 UTC)

<p>These registration settings are available in <a href="https://github.com/lassoan/SlicerElastix#slicerelastix"><code>General registration (Elastix)</code> module</a> (provided by SlicerElastix extension) in the “Inputs” section:</p>
<p>                    <a href="https://raw.githubusercontent.com/lassoan/SlicerElastix/master/Screenshot01.jpg" target="_blank" rel="noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/lassoan/SlicerElastix/master/Screenshot01.jpg" width="690" height="441">
          </a>

</p>

---

## Post #5 by @Vir (2022-02-19 20:16 UTC)

<p>Thank you very much . I didn’t installed the extension for the Elastix module and that why I was unable to locate it .</p>

---
