---
topic_id: 35549
title: "Slicer Rejects Modified Header"
date: 2024-04-17
url: https://discourse.slicer.org/t/35549
---

# Slicer rejects modified Header

**Topic ID**: 35549
**Date**: 2024-04-17
**URL**: https://discourse.slicer.org/t/slicer-rejects-modified-header/35549

---

## Post #1 by @GaryPlayer (2024-04-17 02:41 UTC)

<p>I am trying to add space directions to an nrrd file that was created using pynrrd.  If I modify the header of the nrrd file, I am getting an error in Slicer:</p>
<p>ITK exception info: error in unknown:  Could not create IO object for reading file xxxxxxxxxxxxxxxxxxxxxxxxx (edited out user file)<br>
Tried to create one of the following:<br>
BMPImageIO<br>
etc…</p>
<p>I have tried to duplicate an example where I load in a nrrd file to slicer, set the spacing directions and save.  I then looked at the header in pynrrd, but if I modify the header exactly as Slicer saves, i get the above error.  I cannot tell via the error log where to dig further.  Our graders need this info to match up our images and segmentataions, and doing 1000+ by hand is simply not feasible.  I’d like to figure out if somehow I am creating the nrrd file wrong by modifying the header.  The header is a dictionary, so I simply add the proper matrix and user nrrd.write(filename, image, header=mynewheader)</p>
<p>ANy guidance would be greatly appreciated.</p>

---

## Post #2 by @lassoan (2024-04-17 02:48 UTC)

<p>I would recommend to copy the entire header from the source image. If you still have problems then please upload the script and an example nrrd file somewhere and post the link here so that we can have a look.</p>

---

## Post #3 by @GaryPlayer (2024-04-17 17:37 UTC)

<p>Using some old fashioned grind it out, anyone landing here from search the solution was if you want to modify ‘space directions’ you need to also have the following elements in the header<br>
‘space origin’<br>
‘space’</p>
<p>If you are missing one, it produces the error above (essentially ‘this is not an nrrd file’)</p>
<p>A minor thought would be to have the error message be a little better (it is a valid nrrd file, just missing proper header elements) but that is probably a very low priority and I don’t know how many people are like us playing with the header info.</p>

---

## Post #4 by @lassoan (2024-04-18 15:40 UTC)

<p>I agree. While the file was unusable (it does not make sense to specify axis orientation in physical space if you don’t tell what that physical space is), a meaningful error message would have been useful. I’ve added more detailed error message now - see <a href="https://discourse.slicer.org/t/slicer-rejects-modified-header/35549/2">here</a>.</p>

---
