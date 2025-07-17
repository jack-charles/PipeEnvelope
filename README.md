# PipeEnvelope
Von Mises and API pipe envelope calculations for OCTG

This is a simple calculator for determining the Von Mises and API stress envelope for OCTG products. This incorporates Von Mises ellipsis with corrections for burst under tension, along with API calculations for burst, collapse, and tension. Temperature derating and wall thickness/eccentricity are included. It is also possible to plot your load data against the curves.

This is useful if you have an internal Python workflow and need to validate your stresses work with the pipe being used. 

You can run demo calculations in _cli_pipeenvelope.py_ by selecting 10 at the user prompt (unlisted feature). Please note the import paths for _pipe_envelope.py_ and adjust to fit your environment.

This requires the WellEngineeringCalc.py from [here](https://github.com/jack-charles/WellEngineeringCalc)

<img width="1167" height="883" alt="pipeenvelope output" src="https://github.com/user-attachments/assets/0d54b366-c114-44ed-8977-fb944c3180e0" />

**To do**
* Add I/O to read and save files. Coming soon in CSV and JSON formats.
* Ability to add custom envelopes, such as for connections
* Anistropy calculations
* Additional wear and corrosion calculations on top of eccentricity/wall thickness.
