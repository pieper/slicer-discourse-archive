# Basic question about the format of Image2ProbeTransform

**Topic ID**: 35372
**Date**: 2024-04-09
**URL**: https://discourse.slicer.org/t/basic-question-about-the-format-of-image2probetransform/35372

---

## Post #1 by @DHK (2024-04-09 00:59 UTC)

<p>Hello,</p>
<p>I have a question about the Image2ProbeTransform that is used in .mha files. As far as I can tell, all of the matrices have to be 4X4 matrices. Please correct me if I’m wrong.</p>
<p>I have an ultrasound probe with an attached markers, and its position in a reference system (Probe2ReferenceTransform) is known.</p>
<p>The thing is, the image plane itself is 2D, and while (<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CommonCoordinateSystems.html" class="inline-onebox" rel="noopener nofollow ugc">Plus applications user manual: Definition of commonly used coordinate systems</a>) says that the Z-axis is a cross product of the X-axis and Y-axis, I have been having some confusion about how I should define the transformation matrix.</p>
<p>Say that the image coordinates are in (u, v) and I want to transform it to (x,y,z) in the probe coordinates. The two are linked via</p>
<p>[x                    [a1 a2                               [p1<br>
y       =            b1 b2     *      [u       +       p2
 z]                    c1 c2]             v]               p3]</p>
<p>or [x; y; z] = [a1, a2; b1, b2; c1, c2] * [u, v] + [p1, p2, p3]. Semicolons denote new rows and commas denote new columns within a row a la MATLAB.</p>
<p>Values are</p>
<p>a1 = 0.3467;</p>
<p>a2 = -0.1316;</p>
<p>b1 = -0.2807;</p>
<p>b2 = -0.0620;</p>
<p>c1 = 0.1460;</p>
<p>c2 = -0.0394;</p>
<p>p1 = -109.1116;</p>
<p>p2 = 154.9904;</p>
<p>p3 = 5.9658;</p>
<p>I am thinking of a 4X4 Image2ProbeTransform</p>
<p>[a1, a2, 1, p1;<br>
b1, b2, 1, p2;<br>
c1, c2, 1, p3;<br>
0, 0, 0 1]</p>
<p>but it seems that while Slicer can track <em>an</em> image via this method when I put it all into a .mha file, the image gets zoomed in, pixelated, and cut up from a 2D image into an odd slice like this:</p>
<p>                    <a href="https://i.imgur.com/UPit8VT.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.imgur.com/UPit8VT.png" width="171" height="88">
          </a>

</p>
<p>I would greatly appreciate any help!</p>

---

## Post #2 by @lassoan (2024-04-09 03:18 UTC)

<p>See detailed specification in the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CoordinateSystemDefinitions.html#TransformationMatrix">PLUS toolkit documentation</a>.</p>

---
