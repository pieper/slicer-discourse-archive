# Use coefficients to reconstruct 

**Topic ID**: 8870
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/use-coefficients-to-reconstruct/8870

---

## Post #1 by @Yoda0612 (2019-10-23 04:40 UTC)

<p>I applied SHPARM-PDM extension, and then obtained the coefficients of spherical harmonic.<br>
I wonder if I can reconstruct the original mode by just use the coefficients.</p>

---

## Post #2 by @styner (2019-10-24 19:30 UTC)

<p>Yes, you can. You need to sample the spherical parametrization space and then evaluate the spherical harmonic series at those sample. SlicerSALT is doing that already for you, by using a spherical sampling scheme based on an icosahedron subdivision. The tool that does this is called ParaToSPHARMPDM, which first fits the coefficients and then generates a reconstructed surface from those coefficients.</p>
<p>Martin</p>

---

## Post #3 by @Yoda0612 (2019-10-25 06:35 UTC)

<p>Dear Martin,</p>
<p>Thank you for your response.</p>
<p>Actually, I have tried to reconstruct the shapes by the output the spherical harmonic coefficients<br>
.</p>
<p>Just generated the series of spherical harmonics for each v(phi, theta), and then multiply the coefficients.</p>
<p>However, the result shape is just like a surface.</p>
<p>Because I am trying to develop a tool to apply the spherical harmonic coefficients<br>
.</p>
<p>I wonder if I miss any other parameters.</p>
<p>Cheng</p>
<p>Martin Styner via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> 於 2019年10月25日 週五 上午4:40寫道：</p>

---

## Post #4 by @styner (2019-10-25 13:42 UTC)

<p>Not sure what may be wrong in your reconstruction code, but you can look at the code in SlicerSALT:<br>
surface reconstruction:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Algorithms/SphericalHarmonicMeshSource.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Algorithms/SphericalHarmonicMeshSource.cxx" target="_blank" rel="nofollow noopener">NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Algorithms/SphericalHarmonicMeshSource.cxx</a></h4>
<pre><code class="lang-cxx">/*=========================================================================

  Author: Christine Xu

=========================================================================*/

#include &lt;itkTriangleCell.h&gt;

#include "SphericalHarmonicMeshSource.h"

#include &lt;math.h&gt;
#include &lt;stdio.h&gt;
#include &lt;iostream&gt;

namespace neurolib
{

#define X .525731112119133606
#define Z .850650808352039932

</code></pre>

  This file has been truncated. <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Algorithms/SphericalHarmonicMeshSource.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>SPHARM reconstruction at phi/theta:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Numerics/SphericalHarmonicPolynomial.txx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Numerics/SphericalHarmonicPolynomial.txx" target="_blank" rel="nofollow noopener">NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Numerics/SphericalHarmonicPolynomial.txx</a></h4>
<pre><code class="lang-txx">/*=========================================================================

  Author: Christine Xu, Ipek Oguz, Martin Styner

=========================================================================*/
#ifndef _namicSphericalHarmonicPolynomial_txx
#define _namicSphericalHarmonicPolynomial_txx

#include "SphericalHarmonicPolynomial.h"
#include &lt;ctime&gt;
#include &lt;cstdlib&gt;

#include &lt;math.h&gt;
#include &lt;iostream&gt;
#include &lt;fstream&gt;

namespace neurolib
{
#ifndef M_PI
#define M_PI 3.1415926535897932
</code></pre>

  This file has been truncated. <a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Numerics/SphericalHarmonicPolynomial.txx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
(look at function Evaluate)</p>
<p>Martin</p>

---

## Post #5 by @Yoda0612 (2019-10-28 04:54 UTC)

<p>Dear Martin,</p>
<p>Thanks a lot.</p>
<p>Originally, I implemented my code by Python and apply scipy.special.sph_harm and np.linalg.lstsq to solve the coefficients.</p>
<p>It might have some differences in the details.</p>
<p>I think I can start to modify my code by reference your code.</p>
<p>Regards</p>
<p>Cheng</p>
<p>Regards</p>
<p>Cheng</p>
<p>Martin Styner via 3D Slicer Community <a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a> 於 2019年10月25日 週五 下午10:52寫道：</p>

---
