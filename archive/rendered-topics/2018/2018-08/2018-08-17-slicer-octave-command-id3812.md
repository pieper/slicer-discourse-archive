# Slicer-Octave-command

**Topic ID**: 3812
**Date**: 2018-08-17
**URL**: https://discourse.slicer.org/t/slicer-octave-command/3812

---

## Post #1 by @Mazen_Alharah (2018-08-17 13:22 UTC)

<p>Hi everyone<br>
there is a way to run Octave script using Slicer ??</p>

---

## Post #2 by @ihnorton (2018-08-17 13:48 UTC)

<p>The simplest option is to create a command line script which can parse arguments and accept/write input/output as NRRD files. There is a pure-Matlab NRRD implementation <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">here</a> (if it is not compatible with Octave, the changes should hopefully be minimal).</p>
<p>Then, using the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel">Slicer Execution Model (CLI)</a>, you can define an XML file specifying input and output arguments and types, and Slicer will automatically create a wrapper and graphical interface. Recent Slicer versions will recognize <code>#!</code> at the beginning of a script as a marker that the script can be run as a CLI. There are two Python examples I know of, <a href="https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/CLI/ExtractDWIShells">here</a> and <a href="https://github.com/Radiomics/SlicerRadiomics/tree/master/SlicerRadiomicsCLI">here</a>. <s>Similar scripts and XML files could be written for Octave, provided you make the <code>octave</code> command available in the Slicer PATH.</s> [edit: we would need to broaden the functionality to make this possible, but it should be a small change if/when someone needs it]</p>
<p>A more difficult approach would be to port the <a href="https://github.com/PerkLab/SlicerMatlabBridge/">SlicerMatlabBridge</a>. This is mostly pure-Matlab, except for the <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/cli_commandserver.m">core part which communicates over OpenIGTLink</a>; that part uses Java classes. Apparently it is <a href="https://octave.org/doc/interpreter/How-to-use-Java-from-within-Octave.html#How-to-use-Java-from-within-Octave">possible to call Java from Octave</a>, but Octave does not ship with a JVM the way Matlab does, so the syntax is different and you would need to do a potentially significant amount of work to port.</p>
<p>Of course, if you are not tied to Octave for some specific reason, then using Python is a very good option for similar scientific/technical computing work – and Python is very well-supported in Slicer.</p>

---

## Post #3 by @lassoan (2018-08-17 13:51 UTC)

<p>Slicer’s MatlabBridge can run Matlab commands from Slicer, which could be usable for Octave as well. Client (Slicer) side would work as is, server (Matlab) side probably needs some tuning (how Matlab/Octave server is started and how the TCP/IP communication is implemented).</p>
<p>However, due to booming of Python ecosystem in recent years and relative stagnation of Octave, it might be a better choice to switch to Python (which runs natively in Slicer).</p>

---

## Post #4 by @Mazen_Alharah (2018-08-20 12:15 UTC)

<p>thank you for this Answer ,i think i’ll switch to Python ,it’s more easier <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=6" title=":smile:" class="emoji" alt=":smile:"></p>

---
