We are using a collection of data from different pre-amplifier circuits acquired from old tests performed at Northeastern University's Aramaki Lab.
<p>In order for this code to show the plots according to the data taken, the python/python notebook file needs to be in the same file as all of the data files, in .csv form.<br>
<p>What we are analyzing:<br>
<p>Curve fit to the decay times:<br>
Curving fitting helps you find a formula that matches this pattern. This formula can then be used to predict future decay times or understand the behavior of the system you're studying.
To do this, you try out different mathematical curves and adjust their parameters (like slope, intercept, etc.) until the curve matches your data points as closely as possible. The curve that fits the data best is considered the best representation of the decay process, and it allows you to make predictions or draw conclusions about the decay phenomenon you're studying.
By collecting data from the pre-amp under different conditions, such as input signal strength or frequency, you can then use curve fitting techniques to determine the relationship between these input parameters and the output signal characteristics. This can help in optimizing the performance of the pre-amp, predicting its behavior under different conditions, or designing new pre-amp circuits with desired properties.
In essence, curve fitting with pre-amps allows engineers and scientists to understand and quantify how these devices amplify signals, which is crucial for various applications in fields like telecommunications, instrumentation, and signal processing.
<p>Comparing gain:<br>
Gain is the ratio of the output signal amplitude to the input signal amplitude.
By comparing gain, we can assess how effectively a pre-amplifier amplifies weak signals. A higher gain indicates that the pre-amplifier can boost the strength of incoming signals more effectively.
Comparing gain can help diagnose issues with pre-amplifiers or related components in a system. Significant deviations from expected gain values may indicate faults or inconsistencies that need to be addressed.
<p>$A_V=V_{output}/V_{input}$<br>
<p>Parasitic Capacitance:<br>
Parasitic capacitance in pre-amp refers to unintended or undesired capacitance that exists between various components within the pre-amp circuitry or between the pre-amp and its surroundings.
Designing pre-amplifiers with low parasitic capacitance is essential for maintaining signal fidelity and maximizing performance. Techniques such as proper layout design, shielding, and component placement can help minimize parasitic capacitance. Additionally, using high-quality components with low parasitic capacitance characteristics can mitigate its effects.
Voltage of the output of the amplifier:
<p>$V_0=-AV_i$<br>
The amplifier itself has high input impedance so its input current is not important – the current into the input terminal is:
<p>$ⅈ=C(1+A)((∂v_{input})/ⅆt)$<br>
<p>The capacitance at the input of the amplifier is:<br>
<p>$C_M=C(1+A)$<br>
	<p></p>This is the Miller Capacitance.<br>
<p>If the input circuit has an impedance to ground of the initial resistance, then the output is:<br>
<p>$V_0=A/(1+jwR_i C_M)V_i$<br>
<p>The bandwidth of the amplifier is limited by the high frequency roll-off:<br>
<p>$f=1/(2πR_i C_M )=1/(2πR_i C(1+A))$<br>
