# Tracking how the values in GLCM, GLSZM matrices are populated

**Topic ID**: 13808
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/tracking-how-the-values-in-glcm-glszm-matrices-are-populated/13808

---

## Post #1 by @Ankita_Singh (2020-10-02 01:07 UTC)

<p>Hello,</p>
<p>I am interested in understanding how the values in GLCM and GLSZM are computed for each gray level. I know that there are C++ functions calculate_glcm and calculate_glszm that compute these matrices. Using these functions and adding some more lines of code, can I, for example, track step-by-step how size zones are calculated for each gray level in the GLSZM? Is it possible?</p>
<p>Thank you<br>
Ankita</p>

---

## Post #2 by @JoostJM (2020-10-10 13:36 UTC)

<p>The actual algortihm filling the matrices of the various feature classes is programmed into the C-extension of PyRadiomics. In the earliest versions, we did have python implementations, but due to unsatisfactory performance we have since moved to C-only calculation of the matrices.</p>
<p>Depending on your specific aim, there are several possibilities. If you need to influence the process or extract intermediate results, you can revisit the history of the repository, extracting the python implementations of the matrix calucaltion (though this does not support voxel-based radiomics).<br>
Moreover, the python algorithms were slightly different to make optimum use of optimized numpy calls.</p>
<p>However, if you are seeking a conceptual view of how the matrices are filled, I suggest to start with the C-source code included in the repository. Here you have 2 options. Option 1 is to read the current version, which is more complex to allow for voxel-based calculation and to support both 2D and 3D input. Alternatively, you can read the C-extensions of an earlier version, which required 3D input and could therefore have less complex algorithms. The last version of PyRadiomics with this earlier version of the C-extensions can be found <a href="https://github.com/Radiomics/pyradiomics/tree/12b512fc5fc7e8e317273ddd4b72552695380676">here</a>.</p>

---

## Post #3 by @JoostJM (2020-10-10 13:45 UTC)

<p>If you have a need of some specific intermediate information, we may be able to help give you some pointers on how to implement this if necessary.</p>

---

## Post #4 by @Ankita_Singh (2020-10-11 21:31 UTC)

<p>Hi Joost,</p>
<p>Thank you very much for your help. I will look into the two options and see which one works best for my case.</p>
<p>I had one question from what you mentioned above:</p>
<blockquote>
<p>we did have python implementations, but due to unsatisfactory performance we have since moved to C-only calculation of the matrices.</p>
</blockquote>
<p>What do you exactly mean by ‘unsatisfactory performance’? Is that in terms of computational efficiency?</p>

---

## Post #5 by @Ankita_Singh (2020-10-14 07:51 UTC)

<p>Hi Joost,</p>
<p>In the <a href="https://github.com/Radiomics/pyradiomics/blob/master/radiomics/src/cmatrices.c" rel="noopener nofollow ugc">cmatrices.c</a> file, there is a function <a href="https://github.com/Radiomics/pyradiomics/blob/master/radiomics/src/cmatrices.c#L94" rel="noopener nofollow ugc">calculate_glszm</a> which, as I understand, calculates the size zones for each gray-level and this is stored in temp_data. Later, the function <a href="https://github.com/Radiomics/pyradiomics/blob/master/radiomics/src/cmatrices.c#L281" rel="noopener nofollow ugc">fill_glszm</a> is used to create glszm. I couldn’t locate how fill_glszm is called in the C implementation. Could you please let me know how that is done?</p>
<p>Thank you.</p>

---

## Post #6 by @JoostJM (2020-11-18 18:54 UTC)

<p>It’s called here: <a href="https://github.com/Radiomics/pyradiomics/blob/master/radiomics/src/_cmatrices.c#L437">https://github.com/Radiomics/pyradiomics/blob/master/radiomics/src/_cmatrices.c#L437</a></p>

---

## Post #7 by @JoostJM (2020-11-18 18:56 UTC)

<p>Yes, when comparing time required for matrix calculation in C and in Python only, there was a 300-1000 fold faster calculation in C</p>
<p>note: this only applies to the actual calculation of the matrices. Though overall the time gain was less dramatic, it was still quite significant (in the order of: “instead of a week it just took a couple of minutes”)</p>

---
