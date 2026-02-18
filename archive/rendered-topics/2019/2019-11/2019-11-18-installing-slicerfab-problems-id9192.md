# Installing SlicerFab 'problems'

**Topic ID**: 9192
**Date**: 2019-11-18
**URL**: https://discourse.slicer.org/t/installing-slicerfab-problems/9192

---

## Post #1 by @STUDIO_FREDERIK_DE_W (2019-11-18 14:03 UTC)

<p>Hi,</p>
<p>My name is Fred and new to the 3DSlicer community, so hello y’all!<br>
The first ‘problem’ i ran into is installing Slicerfab ( mac, mojave). I followed the guidelines and tried several ways to install the extension but nothing seemed to work. Any advice on this?<br>
///<br>
Since i am new to the community; a short intro to myself and my interests.<br>
I am an artist with interests in art/sci/tech crossovers and want to explore DDMM aka data driven material modelling. My main softwares are C4D and Houdini. After some searching on the internet if luckily found 3DSLICER and want to dig into it to produce some amazing artworks in collaboration with stratasys an their multicolour/material printers. I am always open for collabs so feel to reach out (<a href="http://f.d.w.angelfireATgmail.com" rel="nofollow noopener">f.d.w.angelfireATgmail.com</a>). The themes i am currently conceptually exploring are FUTURE FOSSILS and POST-NATURE CAMOUFLAGE. Cheers! Fred</p>

---

## Post #2 by @pieper (2019-11-18 14:47 UTC)

<p>Hi Fred -</p>
<p>Welcome!  Sounds like interesting work and I hope you find Slicer useful for this.  Be aware that the SlicerFab / bitmap printing stuff is very experimental and involves having the right printer capabilities, so it can be difficult to debug (e.g. I don’t have a printer that works with these files).</p>
<p>Still, SlicerFab should work to create the bitmaps.  I just tested on windows with the current nightly build and the extension is working.  Note that the default slice spacing takes a long time to generate.  Changing it so something like 1mm is good for debugging and then change it to match your actual printer when generating the actual files.</p>

---
