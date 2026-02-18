# How to visualize wall of trachea that is obstructed by tracheostomy tube lying alongside it

**Topic ID**: 27408
**Date**: 2023-01-22
**URL**: https://discourse.slicer.org/t/how-to-visualize-wall-of-trachea-that-is-obstructed-by-tracheostomy-tube-lying-alongside-it/27408

---

## Post #1 by @mdear (2023-01-22 21:53 UTC)

<p>Hello again.</p>
<p>My inability to visualize all aspects of the tracheal wall is handicapping my efforts to produce novel custom shaped tracheostomy tubes for my son by annealing off-the-shelf Shiley Medtronics tubes.  In an effort to improve I’ve approached the radiology department of our local children’s hospital, but I’m also posting here to seek the wisdom of the community.</p>
<p>I’ve been having pretty good success with visualizing only the air inside the trachea to get an idea where the tracheal wall is sitting.  I then visualize and segment bone (it appears the density of a tracheostomy tube is fairly similar to bone).  Those two categories usually give me all the visibility I need.</p>
<p>However, this strategy breaks down when there is an object (such as a tracheostomy tube) lying alongside the tracheal wall such that no air sits against that portion of the wall.  I can’t tell where the object starts and the tracheal wall stops.</p>
<p>I tried to segment the tracheal wall by density alone, but I failed utterly since the density of the tracheal wall doesn’t appear to be much different from other surrounding tissue.  A recent bronchoscope shows that I was off by a few millimeters and the novel “S” shaped tube is subjecting the tracheal wall to gentle but still repetitive stress leading to unhealthy tissue that is easily seen.  I don’t feel I can alter its shape until I can better visualize all aspects of the tracheal wall (I only have bits and pieces at present and I’m trying to base my designs off evidence instead of guesswork).</p>

---

## Post #2 by @rbumm (2023-01-23 20:22 UTC)

<p>Could you not 3D-scan the unblocked tracheostomy tube, bring it to the exact same position in Slicer, then subtract the tube segment from the trachea, just leaving the tracheal wall in place?</p>

---
