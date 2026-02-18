# Path explorer (Slicer IGT) does not save Trajectory

**Topic ID**: 13132
**Date**: 2020-08-22
**URL**: https://discourse.slicer.org/t/path-explorer-slicer-igt-does-not-save-trajectory/13132

---

## Post #1 by @Michele_Bailo (2020-08-22 14:59 UTC)

<p>OS: MacOS 10.15.6 and Windows 10<br>
Slicer version:4.11.0-2020-08-15<br>
Expected behavior: I find it extremely helpful and interesting to study trajectories with 3D slicer (e.g. for stereotactic procedures, research purposes,…), so I would like to be able to save the planned trajectory and load it again the next time I use the software.<br>
Actual behavior: Unfortunately, every time I reopen a scene, I do not find the previously saved Trajectory, and I have to start all over again setting the target, entry point and recreating the path.</p>
<p>Thank you very much for the incredible job you did and keep doing! What you created is outstanding!</p>
<p>Thanks again for the patience</p>

---

## Post #2 by @lassoan (2020-08-22 18:42 UTC)

<p>We can certainly fix saving of the trajectories in the scene file.</p>
<p>How do you find the usability of this module overall? For me it seems somewhat complicated that you need to define set of entry and target points and then you need to select a pair to create a trajectory from them. What would be the ideal workflow for you?</p>

---

## Post #3 by @Michele_Bailo (2020-08-23 08:27 UTC)

<p>Thank you for your extremely quick answer and solution.</p>
<p>I have to admit that it was a little strange, at the beginning, the strategy 3D Slicer adopts to create targets and entry points and then pair them in a trajectory, since it is different by most neurosurgical softwares (like Medtronic, Brainlab or Leksell surgiplan): in the latters you first create a new path, you name it, and then you set the corresponding entry point and target. Anyway, after some initial difficulties, I’ve got pretty used to the 3D slicer workflow over the time, so I can’t really say that it bothers me; moreover, when you are deciding the best path among many possible entry points and targets, it could be even convenient to switch target or entry point in just a click.</p>
<p>The main issues I found, apart from the “saving”, are the following:</p>
<ol>
<li>
<p>it is very easy to inadvertently move one of the entry points or targets while exploring and rotating the 3D view, this immediately destroys your path and you have to start all over. It would be extremely helpful to be able “lock” the trajectory directly from the “path explorer” module and, perhaps, to have an “undo” button available.</p>
</li>
<li>
<p>it would be time-saving to be able to set all the preferred appearance for trajectories and points (color, size of dots and line, size of the text,…) in the “path explorer” window, so I wouldn’t have to repeat the setting, again and again, for each new path I create</p>
</li>
<li>
<p>moving targets or entry point in an orthogonal or parallel (“in plane”) view is something I find extremely helpful when I’m looking for the best trajectory; unfortunately, in 3D slicer, unless I keep deactivating the automatic view update (and then reactivating it again afterwards) it is almost impossible to move properly the target or entry point without messing everything. The ideal thing, for me, would be for the software to automatically deactivate the view update while I’m moving a point, and then to reactivate it when the point is released in the final position. I’m not sure if I was clear enough in this last part.</p>
</li>
<li>
<p>finally, but I know I’m dreaming the impossible, it would fabulous to be able to get the x,y,z coordinates after registering  stereotactic frames localization (like the Leksell G frame) directly in Slicer, so that I would only need to type the final coordinates in the “clinically approved” software, without transferring all data and recreating the final path (usually I export the targets and entry point as RTstructures)</p>
</li>
</ol>
<p>Anyway, these are just my impressions and ideas to improve, somehow, the potential of these, already, outstanding tool.</p>
<p>Thank you very much again for all your efforts!</p>

---
