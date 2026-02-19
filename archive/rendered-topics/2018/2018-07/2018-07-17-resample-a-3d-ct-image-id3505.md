---
topic_id: 3505
title: "Resample A 3D Ct Image"
date: 2018-07-17
url: https://discourse.slicer.org/t/3505
---

# Resample a 3D CT Image

**Topic ID**: 3505
**Date**: 2018-07-17
**URL**: https://discourse.slicer.org/t/resample-a-3d-ct-image/3505

---

## Post #1 by @Alex_Vergara (2018-07-17 15:35 UTC)

<p>Hello!<br>
I have read this <a href="https://discourse.slicer.org/t/resampling-a-3d-ct-image/618">discussion</a> but couldn’t found the answer I look for. I want to perform a resample similar to the BRAINS resample plugin, BUT not doing interpolation, instead the resample shall average the HU values that lay in a reference voxel.</p>
<p>I have the CT image to wrap, the SPECT image as voxel size reference. So I want to resample the CT such as in each new voxel appear the average HU number of all the CT voxels that are contained. Just add an option to average instead of interpolate. Is there a way to do this now?</p>
<p>Regards</p>

---

## Post #2 by @Alex_Vergara (2018-07-18 09:42 UTC)

<p>After some deep research in the wikis, I move forward to the source code itself and I found this description of the Windowed Sinc Filtered interpolation</p>
<pre><code class="lang-auto">/**
 * \class WindowedSincInterpolateImageFunction
 * \brief Use the windowed sinc function to interpolate
 * \author Paul A. Yushkevich
 *
 * \par THEORY
 *
 * This function is intended to provide an interpolation function that
 * has minimum aliasing artifacts, in contrast to linear interpolation.
 * According to sampling theory, the infinite-support sinc filter,
 * whose Fourier transform is the box filter, is optimal for resampling
 * a function. In practice, the infinite support sinc filter is
 * approximated using a limited support 'windowed' sinc filter.
 *
 * \par
 * This function is based on the following publication:
 *
 * \par
 * Erik H. W. Meijering, Wiro J. Niessen, Josien P. W. Pluim,
 * Max A. Viergever: Quantitative Comparison of Sinc-Approximating
 * Kernels for Medical Image Interpolation. MICCAI 1999, pp. 210-217
 *
 * \par
 * In this work, several 'windows' are estimated. In two dimensions, the
 * interpolation at a position (x,y) is given by the following
 * expression:
 *
 * \par
 * \f[
 *   I(x,y) =
 *     \sum_{i = \lfloor x \rfloor + 1 - m}^{\lfloor x \rfloor + m}
 *     \sum_{j = \lfloor y \rfloor + 1 - m}^{\lfloor y \rfloor + m}
 *     I_{i,j} K(x-i) K(y-j),
 * \f]
 *
 * \par
 * where m is the 'radius' of the window, (3,4 are reasonable numbers),
 * and K(t) is the kernel function, composed of the sinc function and
 * one of several possible window functions:
 *
 * \par
 * \f[
 *   K(t) = w(t) \textrm{sinc}(t) = w(t) \frac{\sin(\pi t)}{\pi t}
 * \f]
 *
 * \par
 * Several window functions are provided here in the itk::Function
 * namespace. The conclusions of the referenced paper suggest to use the
 * Welch, Cosine, Kaiser, and Lanczos windows for m = 4,5. These are based
 * on error in rotating medical images w.r.t. the linear interpolation
 * method. In some cases the results achieve a 20-fold improvement in
 * accuracy.
 *
 * \par USING THIS FILTER
 *
 * Use this filter the way you would use any ImageInterpolationFunction,
 * so for instance, you can plug it into the ResampleImageFilter class.
 * In order to initialize the filter you must choose several template
 * parameters.
 *
 * \par
 * The first (TInputImage) is the image type, that's standard.
 *
 * \par
 * The second (VRadius) is the radius of the kernel, i.e., the
 * \f$ m \f$ from the formula above.
 *
 * \par
 * The third (TWindowFunction) is the window function object, which you
 * can choose from about five different functions defined in this
 * header. The default is the Hamming window, which is commonly used
 * but not optimal according to the cited paper.
 *
 * \par
 * The fourth (TBoundaryCondition) is the boundary condition class used
 * to determine the values of pixels that fall off the image boundary.
 * This class has the same meaning here as in the NeighborhoodItetator
 * classes.
 *
 * \par
 * The fifth (TCoordRep) is again standard for interpolating functions,
 * and should be float or double.
 *
 * \par CAVEATS
 *
 * There are a few improvements that an enthusiasting ITK developer
 * could make to this filter. One issue is with the way that the kernel
 * is applied. The computational expense comes from two sources:
 * computing the kernel weights K(t) and multiplying the pixels in the
 * window by the kernel weights. The first is done more or less
 * efficiently in \f$ 2 m d \f$ operations (where d is the
 * dimensionality of the image). The second can be done
 * better. Presently, each pixel \f$ I(i,j,k) \f$ is multiplied by the
 * weights \f$ K(x-i), K(y-j), K(z-k) \f$ and added to the running
 * total. This results in \f$ d (2m)^d \f$ multiplication
 * operations. However, by keeping intermediate sums, it would be
 * possible to do the operation in \f$ O ( (2m)^d ) \f$
 * operations. This would require some creative coding. In addition, in
 * the case when one of the coordinates is integer, the computation
 * could be reduced by an order of magnitude.
 *
 * \sa LinearInterpolateImageFunction ResampleImageFilter
 * \sa Function::HammingWindowFunction
 * \sa Function::CosineWindowFunction
 * \sa Function::WelchWindowFunction
 * \sa Function::LanczosWindowFunction
 * \sa Function::BlackmanWindowFunction
 * \ingroup ImageFunctions ImageInterpolators
 * \ingroup ITKImageFunction
 */
</code></pre>
<p>Specially this part $$I(x,y) =  \sum_{i = \lfloor x \rfloor + 1 - m}^{\lfloor x \rfloor + m}  \sum_{j = \lfloor y \rfloor + 1 - m}^{\lfloor y \rfloor + m}  I_{i,j} K(x-i) K(y-j)$$</p>
<p>which makes me realize the WindowedSinc filter is what I was searching for actually. So for resampling CT just take any of the filters following BSpline.</p>
<p>By the way, the forum maintainers shall really look at this <a href="https://github.com/kasperpeulen/discourse-mathjax" rel="nofollow noopener">discourse-mathjax plugin</a></p>

---

## Post #3 by @cpinter (2018-07-18 12:28 UTC)

<p>Excellent! Glad you managed to find the solution yourself.</p>
<p>You say you took a good look at the wikis. Any suggestion where it would be best to add the information you just discovered? Thanks!</p>

---

## Post #4 by @Alex_Vergara (2018-07-18 13:08 UTC)

<blockquote>
<p><a class="mention" href="/u/cpinter">@cpinter</a><br>
Excellent! Glad you managed to find the solution yourself.<br>
You say you took a good look at the wikis. Any suggestion where it would be best to add the information you just discovered? Thanks!</p>
</blockquote>
<p>Yeah! of course. In the <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/BRAINSResample" rel="noopener nofollow ugc">BRAINS tool wiki</a> there is nothing descriptive of what is actually being performed. I would have written something about what the interpolation method actually do, or at least the references. The text that appears in the itk source file is a lot more descriptive than that wiki page.</p>
<p>By the way, there must appear in some place that using windowed sinc interpolation is strongly recommended for resampling CT images. SPECT/PET images has a different approach. I don’t know about MRI.</p>

---
