# Viewing an FA image

**Topic ID**: 668
**Date**: 2017-07-11
**URL**: https://discourse.slicer.org/t/viewing-an-fa-image/668

---

## Post #1 by @Rewati_Kulkarni (2017-07-11 18:44 UTC)

<p>Operating system: Mac OSX 10.9.5<br>
Slicer version: 4.7.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I have a greyscale Fractional Anisotropy (FA) image, and I want to view it in RGB colour scheme, with white matter tract orientations too, if possible. I tried using the Volumes module, but the preset colour schemes only make the greyscale image look garish when colourful. I would like to view it the way the sample DTI downloaded from the 3D Slicer forum looks like, with a black background, and a 3D vector visualisation in RGB. Which module should I be using for this?</p>
<p>(I was able to load this FA image in another software and view it in 3d vector RGB visualisation, but I would really like to use Slicer over the other software).</p>

---

## Post #2 by @ihnorton (2017-07-11 19:53 UTC)

<p>How does the other software (which one?) provide a directionally-coded visualization? There’s no directional information available in a grayscale FA, it’s a single scalar value per voxel.</p>

---

## Post #3 by @Rewati_Kulkarni (2017-07-12 14:27 UTC)

<p>I am using FSL, and within that, FSLeyes to view the FA image. The image I<br>
have is actually called an FAV1 image, but when I checked online, I could<br>
not find a similar format listed anywhere.</p>
<p><em>Rewati Kulkarni</em></p>
<p><em>Research Assistant, Injury Biomechanics Lab.</em></p>
<p>University of Pennsylvania,<br>
Department of Bioengineering<br>
<em>+1 267-648-7960</em> | <em><a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a> <a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a></em></p>

---

## Post #4 by @Rewati_Kulkarni (2017-07-12 15:53 UTC)

<p>To explain better, I have attached the file I opened, and an image of what<br>
it looks like in FSL, when used with the 3D RGB vector visualisation<br>
option. I hope that makes what I am trying to say, clearer.</p>
<p><em>Rewati Kulkarni</em></p>
<p><em>Research Assistant, Injury Biomechanics Lab.</em></p>
<p>University of Pennsylvania,<br>
Department of Bioengineering<br>
<em>+1 267-648-7960</em> | <em><a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a> <a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a></em></p>

---

## Post #5 by @ihnorton (2017-07-12 16:03 UTC)

<p>Thanks - I don’t think attachment mail-in is supported (or the file may be too big). Please upload to something like dropbox/google drive/etc. and share the link.</p>
<p>However, based on <a href="https://git.fmrib.ox.ac.uk/fsl/fsleyes/fsleyes/blob/master/userdoc/overlays.rst#vector">this document</a> it sounds like they are storing components. I’m not sure if we have a way to visualize such an image in color right now.</p>

---

## Post #6 by @ihnorton (2017-07-12 16:04 UTC)

<p>Might be possible to glyph it using: <a href="http://apidocs.slicer.org/master/classvtkMRMLVectorVolumeDisplayNode.html">http://apidocs.slicer.org/master/classvtkMRMLVectorVolumeDisplayNode.html</a></p>

---

## Post #7 by @ihnorton (2017-07-12 16:19 UTC)

<p>Please note – if you share data, it must be anonymized (no identifiable information in the image, metadata, or even filename).</p>

---

## Post #8 by @Rewati_Kulkarni (2017-07-12 16:20 UTC)

<p>I’ve attached the google drive link to the files I tried to send earlier:</p>
<p><a href="https://drive.google.com/drive/folders/0B9ZRwZrndb2DYXl0LVpZcHdzYmc?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/0B9ZRwZrndb2DYXl0LVpZcHdzYmc?usp=sharing</a></p>
<p><em>Rewati Kulkarni</em></p>
<p><em>Research Assistant, Injury Biomechanics Lab.</em></p>
<p>University of Pennsylvania,<br>
Department of Bioengineering<br>
<em>+1 267-648-7960</em> | <em><a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a> <a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a></em></p>

---

## Post #9 by @Rewati_Kulkarni (2017-07-13 12:51 UTC)

<p>Hello Isaiah, did you have a chance to go over the files I sent you?</p>
<p><em>Rewati Kulkarni</em></p>
<p><em>Research Assistant, Injury Biomechanics Lab.</em></p>
<p>University of Pennsylvania,<br>
Department of Bioengineering<br>
<em>+1 267-648-7960</em> | <em><a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a> <a href="mailto:rewati.p.k01@gmail.com">rewati.p.k01@gmail.com</a></em></p>

---

## Post #10 by @ihnorton (2017-07-14 17:12 UTC)

<p>I took a look at the file, but I’m still unsure about the conventions it uses (what is the order of the image components, etc.). As of now we don’t have a way to display such a file.</p>

---
