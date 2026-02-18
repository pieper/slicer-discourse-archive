# Potential JAX-based physics for real-time simulation in Slicer?

**Topic ID**: 44142
**Date**: 2025-08-20
**URL**: https://discourse.slicer.org/t/potential-jax-based-physics-for-real-time-simulation-in-slicer/44142

---

## Post #1 by @Bruce_Hu (2025-08-20 07:08 UTC)

<p>Hello Slicer community,</p>
<p>I’m a developer interested in physics simulation. My project, <a href="https://github.com/pal-robotics/brax_training_viewer" rel="noopener nofollow ugc">brax viewer</a>, visualizes <strong>JAX</strong>-based physics engines in real time, which is a new open-source package developed as part of Google Summer of Code. Briefly, JAX is an extremely fast, differentiable computation package that runs on GPU.</p>
<p>I am looking for a way for my viewer to be used with Slicer. So I share it with the community and have been browsing some relevant discussions. In threads like the one on <a href="https://discourse.slicer.org/t/method-to-deform-rib-cartilage-with-elevation-of-the-sternum-in-pectus-excavatum/35426">biomechanics simulation for pectus excavatum</a>, Blender can animate deformation, and tools like OpenSIM or FEBio can simulate but require patient-specific material properties for precision.</p>
<h4><a name="p-127747-could-jax-engines-be-used-to-reverse-estimate-these-material-properties-in-real-time-1" class="anchor" href="#p-127747-could-jax-engines-be-used-to-reverse-estimate-these-material-properties-in-real-time-1" aria-label="Heading link"></a>Could JAX engines be used to reverse-estimate these material properties in real-time?</h4>
<p>There are two relevant physics simulation engines suited for this problem:</p>
<ul>
<li><strong><a href="https://mujoco.readthedocs.io/en/stable/mjx.html" rel="noopener nofollow ugc">MJX</a></strong> for rigid body dynamics</li>
<li><strong><a href="https://github.com/deepmodeling/jax-fem" rel="noopener nofollow ugc">JAX-FEM</a></strong> for Finite Element Method</li>
</ul>
<p>JAX has two advantages:</p>
<ul>
<li>Speed: Because JAX runs natively on the GPU, it’s fast enough for real-time simulation. It can also host many environments in parallel, which is ideal for robot trajectory exploration.</li>
<li>Differentiability: The entire simulation is differentiable, making it powerful for optimization problems like material property estimation and learning-based robot training.</li>
</ul>
<p>Based on <a href="https://discourse.slicer.org/t/access-mrmlscene-from-terminal-using-pythonslicer/21981">this discussion</a>, Slicer’s WebServer and OpenIGTLink seem to be good interfaces.</p>
<p>Thank you for your time and any thoughts you have! I am open to any suggestions.</p>

---

## Post #2 by @RafaelPalomar (2025-08-20 15:30 UTC)

<p><a class="mention" href="/u/bruce_hu">@Bruce_Hu</a>, this sounds interesting, thanks for sharing. We have a 3D Slicer extension integrating the SOFA framework ( <a href="https://github.com/Slicer/SlicerSOFA" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerSOFA: 3D Slicer extension to enable simulations using the SOFA framework</a> ). A common pattern to integrate simulation libraries in 3D Sicer is using <code>numpy.array</code> objects as a common language to transfer data between the foreign library and 3D Slicer. This is what is used in SlicerSOFA and more recently <a class="mention" href="/u/pieper">@pieper</a> has succesfully demoed integration with <a href="https://github.com/NVIDIA/warp" rel="noopener nofollow ugc">NVIDIA Warp</a>.</p>
<p><a class="mention" href="/u/bruce_hu">@Bruce_Hu</a>, what do you think is the advantage of using Brax viewer with streamed slicer data vs. integrating JAX directly in Slicer? 3D Slicer has already a wealth of functionality for visualization.</p>

---

## Post #3 by @pieper (2025-08-20 18:11 UTC)

<p>Welcome <a class="mention" href="/u/bruce_hu">@Bruce_Hu</a> - it sounds like you are into some interesting things and I hope you’ll find Slicer useful for your work.  Now is an exciting time for simulation and medical imaging and as <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> says, we are actively exploring a lot of options.</p>
<p>You may already know of this, but the <a href="https://newton-physics.github.io/newton/guide/overview.html">Newton Physics</a> project also looks interesting in this space.</p>
<p>In addition to the WebServer and OpenIGTLink, you may want to explore RPyC and shared memory as in <a href="https://github.com/SlicerTMS/SlicerTMS/tree/rpyc-simnibs/Experiments">the client and server examples here</a>.  There’s some description of our <a href="https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/ImprovementsOfSlicertms/">electromagnetic simulation examples and visualizations here</a>.  Note that we preferred the client-server model for <a href="https://simnibs.github.io/simnibs/build/html/documentation/command_line/simnibs_python.html">SimNIBS</a> because, like JAX-FEM, it is GPL.  But it’s also an option for decoupling simulation from UI processes in general.</p>
<p>As a general rule we also like the option we like being able to have the option of installing all the packages in the Slicer python interpreter for portability, although that’s not always possible.  It does seem to work well for Warp in my experience.</p>
<aside class="quote no-group" data-username="Bruce_Hu" data-post="1" data-topic="44142">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bruce_hu/48/79365_2.png" class="avatar"> Bruce Shouyue Hu:</div>
<blockquote>
<p>Could JAX engines be used to reverse-estimate these material properties in real-time?</p>
</blockquote>
</aside>
<p>Yes, this is a great idea and definitely something that would be valuable.  We often have 4D datasets and other data that could be used for this purpose.</p>

---

## Post #4 by @Bruce_Hu (2025-08-23 01:24 UTC)

<p>Thanks, <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>. You’re right, the goal is definitely to integrate JAX directly and use Slicer’s own visualization, not build a separate one. Using <code>numpy</code> as the common language is ideal, since <code>jax.numpy</code> mirrors <code>numpy</code>’s API.</p>
<p>Two reasons to integrate JAX are:</p>
<ol>
<li>Integrated Reinforcement Learning Pipeline<br>
Robots can be trained directly within the Slicer environment for autonomous systems.<br>
JAX can be used for simulation - <a href="https://mujoco.readthedocs.io/en/stable/mjx.html" rel="noopener nofollow ugc">MJX</a>, and reinforcement learning trainer - <a href="https://github.com/google/brax" rel="noopener nofollow ugc">Brax</a>. (In soft dynamics simulation, SOFA, and NVIDIA Warp seems more suitable than MJX.)</li>
<li>Accelerated Scientific Compute Backend<br>
JAX is highly optimized for high-throughput computation and cleanly supports different hardware (CPU/GPUs/TPUs). However, its I/O, compilation, and asynchronous architecture are unique, so it requires careful design for integration with the Slicer server (non-blocking, real-time visualization).</li>
</ol>

---

## Post #5 by @RafaelPalomar (2025-08-23 17:41 UTC)

<p><a class="mention" href="/u/bruce_hu">@Bruce_Hu</a>, thanks for the reply. It is great to see the number of alternatives and the potential to make them work in 3D Slicer. If you have the time and interest I would suggest you join one of the developer meetings to have a discussion on this. These meetings are open and happen on Tuesdays at 10 am EST; usually they are announced at <a href="https://discourse.slicer.org/c/community/hangout/20" class="inline-onebox">Weekly meetings - 3D Slicer Community</a> the same day or the day before.</p>
<p>One idea could be to have an extension offering an API and tools to interact with simulations in Slicer through different back-ends.</p>
<p>Thanks for the discussion!</p>

---

## Post #6 by @Bruce_Hu (2025-08-23 19:46 UTC)

<p>Thank you for the reply, <a class="mention" href="/u/pieper">@pieper</a>!</p>
<p>I think the server-client model works well with <code>JAX</code>’s asynchronous execution, and my <code>Brax Viewer</code> follows this design too.</p>
<p>Thanks for the suggestion to <code>Newton Physics</code> and <code>RPyC</code>. It’s nice to see <code>Newton</code>’s support for <code>MuJoCo</code>, as it is widely used in reinforcement learning frameworks like <code>Brax</code> for training algorithms. I will definitely look into these.</p>
<p>I understand that a direct installation is ideal for portability. <code>JAX</code>’s installation is automated by <code>pip install jax[device]</code>, where device can be CUDA/TPU. So there could be a direct integration method.</p>
<p>And regarding licenses, is Apache 2.0 good for direct integration?  <code>JAX</code>, <code>Brax</code> and my <code>Brax Viewer</code> are all Apache 2.0.</p>

---

## Post #7 by @pieper (2025-08-23 19:58 UTC)

<p>Yes, we definitely prefer Apache 2 (see, for example, comments <a href="https://discourse.slicer.org/t/rpy2-pip-installation-fails/4883/14">here</a> on why we avoid GPL code).  It seems to be a common thought, since Warp and Newton are recent Apache examples too.</p>
<p>As Rafael suggests, discussing these topics at a developer call would be a chance to get us all better up to speed on the options these packages provide and to think about how we can apply them in various medical image computing contexts.</p>

---
