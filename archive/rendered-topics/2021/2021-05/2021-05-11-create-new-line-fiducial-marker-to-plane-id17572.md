---
topic_id: 17572
title: "Create New Line Fiducial Marker To Plane"
date: 2021-05-11
url: https://discourse.slicer.org/t/17572
---

# Create new line: Fiducial marker to Plane

**Topic ID**: 17572
**Date**: 2021-05-11
**URL**: https://discourse.slicer.org/t/create-new-line-fiducial-marker-to-plane/17572

---

## Post #1 by @mcastr (2021-05-11 19:32 UTC)

<p>Operating system:Windows 10/ 64<br>
Slicer version:4.11.20200930<br>
Expected behavior:Unk<br>
Actual behavior: Is there a way for a line to be projected from a point to a plane at a designated angle? For example on a skull, a plane bisecting the skull along the midline and placing a fiducial maker at the external auditory meatus, a line to be drawn from the fiducial marker at 90 degrees to the plane. Ideally, the newly drawn line would have an output of a linear measure.</p>

---

## Post #2 by @lassoan (2021-05-13 06:08 UTC)

<p>You can look up a formula on the web and adapt it to Slicer by getting inputs from markups and setting results in markups.</p>
<p>For example, a complete working implementation that takes a markups plane <code>P</code> and a markups line <code>L</code> as input, it takes the first control point of the line and sets its second control point to the projected position on the plane.</p>
<pre><code class="lang-python">plane = getNode('P')
line = getNode('L')

point = np.zeros(3)
planeOrigin = np.zeros(3)
planeNormal = np.zeros(3)
plane.GetOriginWorld(planeOrigin)
plane.GetNormalWorld(planeNormal)
line.GetNthControlPointPositionWorld(0, point)
distanceFromPlane = np.dot(np.subtract(point, planeOrigin), planeNormal)
line.SetNthControlPointPositionWorld(1, *(point-planeNormal*distanceFromPlane))
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/259a360904776ee668dd7700b62c57c70ba21067.png" alt="image" data-base62-sha1="5mE3QKQwq9p7ICXGZhJz2VoHd4P" width="615" height="362"></p>
<p>You can add an observer to the plane and line and make the line’s endpoint update automatically if the line’s starting point or the plane is adjusted (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#define-edit-a-circular-region-of-interest-in-a-slice-viewer">this example</a>).</p>

---

## Post #3 by @mcastr (2021-07-19 14:44 UTC)

<p>I will try this. Thank you!</p>

---

## Post #4 by @jumbojing (2022-12-28 15:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="17572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">plane = getNode('P')
line = getNode('L')

point = np.zeros(3)
planeOrigin = np.zeros(3)
planeNormal = np.zeros(3)
plane.GetOriginWorld(planeOrigin)
plane.GetNormalWorld(planeNormal)
line.GetNthControlPointPositionWorld(0, point)
distanceFromPlane = np.dot(np.subtract(point, planeOrigin), planeNormal)
line.SetNthControlPointPositionWorld(1, *(point-planeNormal*distanceFromPlane))
</code></pre>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<blockquote>
<p>According to  <img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20"> your code , I got the following function, which can project the point cloud to the specified plane:</p>
</blockquote>
<p>根据您给的代码, 我得到了下面这个函数, 可以将点云投影到指定的平面:</p>
<pre><code class="lang-auto">def projPla(pm: XYZ,
            norm: XYZ,
            ps: XYZ,
            # modName: str=''
            ) -&gt;XYZ:
    '''projPla 点射面

    将点投射的平面

    Args:
        pm (arr): 平面上的点
        norm (arr): 平面法向量
        p0 (arr): 投射源点阵

    Returns:
        - 投射点阵

    Note:
        -
    '''
    pss = []
    for p in ps:
        v = np.subtract(p, pm)
        p2Pla = np.dot(v, norm)
        pss.append(p-norm*p2Pla)
    return np.asarray(pss)
</code></pre>
<p>aa = projPla(pm, norm = np.array([0,1,0]), ps = arr[0::9])</p>
<pre><code class="lang-auto">
![图片|455x336](upload://xatW7Xyug8DU9qB5l9hytromAvI.png)


&gt; However, when norm=[0,0,1] or [1,0,0], an exception occurs, as shown in the following figure:
可是, 当norm = [0,0,1]或者[1,0,0]时却出现了异常如下图:

![图片|397x500](upload://6zoSBy6NJ1JydhrD7GTOsh83NCf.png)



原来的点阵在投影时成了一条很窄的类似直线的形状

&gt; The original points cloud becomes a very narrow line like shape during projection. what's wrong?</code></pre>

---

## Post #5 by @jumbojing (2022-12-28 16:02 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="4" data-topic="17572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p><code>shape</code></p>
</blockquote>
</aside>
<pre><code class="lang-auto">arr=array([[-4.93960810e+00,  7.01684875e+01, -7.48282654e+02],
       [-4.71345520e+00,  7.01748428e+01, -7.49177856e+02],
       [-5.63638353e+00,  7.01358185e+01, -7.44255371e+02],
       [-3.81400299e+00,  7.01904144e+01, -7.51793884e+02],
       [-5.54661322e+00,  7.01026306e+01, -7.41144470e+02],
       [-2.60454869e+00,  7.01987686e+01, -7.54090820e+02],
       [-4.79960060e+00,  7.00572891e+01, -7.37660828e+02],
       [-1.85518825e+00,  7.02044754e+01, -7.55565002e+02],
       [-3.73253250e+00,  7.00230179e+01, -7.35644897e+02],
       [-3.09748203e-01,  7.01931992e+01, -7.56368774e+02],
       [-2.07208180e+00,  6.99935226e+01, -7.34821350e+02],
       [ 1.62125003e+00,  7.01665115e+01, -7.56150818e+02],
       [-4.43809509e-01,  6.99708328e+01, -7.34618469e+02],
       [ 3.03206897e+00,  7.01364746e+01, -7.54967896e+02],
       [ 1.39871228e+00,  6.99509354e+01, -7.34950439e+02],
       [ 3.92218852e+00,  7.01042480e+01, -7.52932800e+02],
       [ 3.02136064e+00,  6.99405594e+01, -7.35936707e+02],
       [ 4.64894152e+00,  7.00833206e+01, -7.51794067e+02],
       [ 4.10499763e+00,  6.99445190e+01, -7.37652466e+02],
       [ 5.83407831e+00,  7.00866241e+01, -7.53570801e+02],
       [ 4.76213551e+00,  6.99688416e+01, -7.40820862e+02],
       [ 7.59368277e+00,  7.00687408e+01, -7.53996399e+02],
       [ 5.29720736e+00,  6.99932251e+01, -7.43844666e+02],
       [ 9.85618973e+00,  7.00391693e+01, -7.53905396e+02],
       [ 6.18222475e+00,  6.99629135e+01, -7.41989746e+02],
       [ 1.11831875e+01,  7.00229416e+01, -7.53960144e+02],
       [ 7.05674744e+00,  6.99254150e+01, -7.39423584e+02],
       [ 1.32680683e+01,  6.99938354e+01, -7.53695557e+02],
       [ 8.51561928e+00,  6.98925323e+01, -7.38023621e+02],
       [ 1.47315636e+01,  6.99666748e+01, -7.52856750e+02],
       [ 1.01131620e+01,  6.98743820e+01, -7.38224731e+02],
       [ 1.53441133e+01,  6.99283218e+01, -7.49886108e+02],
       [ 1.16029158e+01,  6.98721085e+01, -7.39833740e+02],
       [ 1.46470222e+01,  6.99058533e+01, -7.46848816e+02],
       [ 1.25617809e+01,  6.98832474e+01, -7.42093201e+02],
       [ 1.36347218e+01,  6.98939819e+01, -7.44453247e+02]])  # arr = arr[0::9]
</code></pre>

---

## Post #6 by @esomjai (2023-03-20 12:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="17572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">plane = getNode('P')
line = getNode('L')

point = np.zeros(3)
planeOrigin = np.zeros(3)
planeNormal = np.zeros(3)
plane.GetOriginWorld(planeOrigin)
plane.GetNormalWorld(planeNormal)
line.GetNthControlPointPositionWorld(0, point)
distanceFromPlane = np.dot(np.subtract(point, planeOrigin), planeNormal)
line.SetNthControlPointPositionWorld(1, *(point-planeNormal*distanceFromPlane))
</code></pre>
</blockquote>
</aside>
<p>I am experiencing issues with applying this code in Slicer 5.2.2.<br>
I am also quite new to the program, therefore the language. I am currently working on facial DICOM files and their landmarking. I established a frankfort horizontal plane as a reference for further measurements. I am struggling to project a specified point orthogonally to the plane - tried to compute coordinated with MatLab but failed (not even intersecting the plane). I will also need to establish the point(s) where different lines intersect the plane (not in 90°) for angle  measurements as well. Can this be done using visual modules?<br>
Many thanks,<br>
Eszter</p>

---

## Post #7 by @lassoan (2023-03-20 15:05 UTC)

<p>You need to have a plane node by the name <code>P</code> and a line node by the name <code>L</code> in the scene. The script updates the second point of the line to make the line orthogonal to the plane. I’ve just tried the code snippet in Slicer-5.2.2 and it worked perfectly.</p>

---
