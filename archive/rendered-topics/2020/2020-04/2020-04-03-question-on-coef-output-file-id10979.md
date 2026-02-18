# Question on .coef output file

**Topic ID**: 10979
**Date**: 2020-04-03
**URL**: https://discourse.slicer.org/t/question-on-coef-output-file/10979

---

## Post #1 by @hcc (2020-04-03 15:50 UTC)

<p>Hello,</p>
<p>Really like the SPHARM-PDM tool, and thanks in advance for your time with this query.</p>
<p>I have the .coef file of coefficients, but it seems that they only contain coefficients for positive and zero m values. For example, for SPHARM degree 15 (which I take to mean it goes up to l=15), I get a (256x3) set of numbers, and for degree 3 I get (16x3). From the answer on the Github page (pasted below), the columns are the (x, y, z) coordinates, and accounting for one row for the m=0 coefficients, and two rows (one real, one imaginary) for the other m values, this matches the total number of rows only if I count m values of 0 and above. Could you please let me know what I have misunderstood here? Many thanks.</p>
<p>On the issues section on Github there is a reply that says the coeffs are ordered like:</p>
<pre><code class="lang-cpp">GetCoefAt(unsigned int l, unsigned int m, unsigned int coord, double *coef)
{
  if( m == 0 )
  {
    coef[0] = m_Coefs[l * l][coord];
    coef[1] = 0;
  }
  else
  {
    coef[0] = m_Coefs[l * l + 2 * m - 1][coord];
    coef[1] = m_Coefs[l * l + 2 * m][coord];
  }
}
</code></pre>

---

## Post #2 by @hcc (2020-04-11 23:44 UTC)

<p>Hi guys, I just wondered if anyone could help with this one please?<br>
Many thanks.</p>

---

## Post #3 by @styner (2020-04-17 17:57 UTC)

<p>Hi, yes, that correct. Only the positive m are used in our SPHARM implementation. See also</p>
<ol>
<li>Styner M, Oguz I, Xu S, Brechbühler C, Pantazis D, Levitt JJ, Shenton ME, Gerig G. Framework for the Statistical Shape Analysis of Brain Structures using SPHARM-PDM. Open Science Workshop at MICCAI - Insight Journal. 2006. PMCID: PMC3062073<br>
Also look at Table 1</li>
</ol>
<p>So we are only using the positive “m” coeffs with both the real and the imaginary part (i.e. we do not compute the negative “m” coeffs, where m is the order within a given degree).</p>
<p>Martin</p>

---

## Post #4 by @hcc (2020-04-25 17:23 UTC)

<p>Great, thank you very much for your help. And then for reconstruction am I right in thinking I take the real parts of the {x, y, z} series? And that this would come out fully real in the limit of spharm degree -&gt; infinity</p>

---

## Post #5 by @styner (2020-04-27 19:54 UTC)

<p>Best look at the reconstruction code in the GitHub:<br>
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
<br>
(generate a mesh from a SPHARM object, calls Evaluate)</p>
<p><a href="https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Numerics/SphericalHarmonicPolynomial.txx" rel="nofollow noopener">https://github.com/NIRALUser/SPHARM-PDM/blob/master/Libraries/Shape/Numerics/SphericalHarmonicPolynomial.txx</a> (look at function Evaluate)</p>
<p>Best<br>
Martin</p>

---
