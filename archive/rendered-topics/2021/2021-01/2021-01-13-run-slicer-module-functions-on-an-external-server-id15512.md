# Run Slicer module functions on an external server

**Topic ID**: 15512
**Date**: 2021-01-13
**URL**: https://discourse.slicer.org/t/run-slicer-module-functions-on-an-external-server/15512

---

## Post #1 by @sthirumal (2021-01-13 19:25 UTC)

<p>I’ve created a Module in Slicer that includes some functions that are very computationally intensive. Given we already have a more computationally powerful server available to us, is there a way that we can run these functions on that server rather than the local computer?</p>

---

## Post #2 by @pieper (2021-01-13 22:51 UTC)

<p>Yes, maybe - can you describe how the computationally complex modules are implemented?  (Are they in C++ or python?  loadable or cli modules?  do they interact with the scene or process bulk data like volume or model?)</p>

---

## Post #3 by @sthirumal (2021-01-14 19:47 UTC)

<p>Hi Steve, sure! It’s a loadable module implemented in python. It processes bulk data of a large number of loaded volumes. It essentially is extracting values of each pixel in each volume and performing some function on those values, so the higher number of volumes the longer it takes. The output is a table of the extracted data.</p>

---

## Post #4 by @pieper (2021-01-14 19:51 UTC)

<p>This <a href="https://github.com/pieper/SlicerProcesses">SlicerProcesses</a> proof of concepts shows how to route data to helper processes, and if you prefix the command line with ssh to a machine where Slicer is installed it can run (many kinds of processing could be run headless).  Then you would get the results back in your local Slicer for viewing.</p>

---

## Post #5 by @sthirumal (2021-01-14 20:42 UTC)

<p>I’ll take a look, thanks so much!</p>

---
