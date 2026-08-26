# Burst – Von Mises Derivation

Von Mises Envelope for Tubulars

$$Y_{p}=\sqrt{\frac{1}{2}\left[{\left({\sigma }_{z}-{\sigma }_{\theta }\right)}^{2}+{\left({\sigma }_{\theta }-{\sigma }_{r}\right)}^{2}+{\left({\sigma }_{r}-{\sigma }_{z}\right)}^{2}\right]+3{\tau }^{2}}$$

Drop torque and expand	

$$Y_{p}=\sqrt{{\sigma }_{z}^{2}+{\sigma }_{\theta }^{2}+{\sigma }_{r}^{2}-{\sigma }_{z}{\sigma }_{\theta }-{\sigma }_{\theta }{\sigma }_{r}-{\sigma }_{r}{\sigma }_{z}}$$

For simple 2D solution in thin wall, assume no radial stress and simplify to

$$Y_{p}=\sqrt{{\sigma }_{z}^{2}-{\sigma }_{z}{\sigma }_{\theta }+{\sigma }_{\theta }^{2}}$$

Rewrite as function of ${\sigma }_{z}$, 			

$$f\left({\sigma }_{z}\right)=\frac{1}{2}{\sigma }_{\theta }\pm \frac{1}{2}\sqrt{4Y_{p}^{2}-3{\sigma }_{\theta }^{2}}$$

First find extremes of envelope. Differentiate with respect to hoop stress and solve for 0 to determine inflection point. Similar, if term under radical is 0, then that implies an extreme also. 

$$f\prime \left({\sigma }_{z}\right)=\frac{1}{2}+\frac{3}{2}\frac{-{\sigma }_{\theta }}{\sqrt{4Y_{p}^{2}-3{\sigma }_{\theta }^{2}}}=0$$
or
$${\sigma }_{\theta }=\frac{1}{\sqrt{3}}Y_{p}=0.5774{\ast Y}_{p}$$

Substitute into $$f\prime \left({\sigma }_{z}\right)$$		

$${\sigma }_{z}=\frac{1}{2}\frac{1}{\sqrt{3}}Y_{p}+\frac{1}{2}\sqrt{3}Y_{p}$$

or

$${\sigma }_{z}=1.1547{\ast Y}_{p}$$		

Note when radical is 0:	$${\sigma }_{\theta }=\frac{1}{2}{\sigma }_{z}$$	These two equations yield the point of maximum tensile stress 

Special note! 	1.1547 = sqrt(4/3) 	&	 ½*1.1547 = 0.5774

2D envelope is symmetrical, reciprocate for maximum hoop stress.		
$${\sigma }_{\theta }=1.1547{\ast Y}_{p}$$  &   $${\sigma }_{z}=0.5774{\ast Y}_{p}$$

For case of σθ = σz insert into original equation	 $${\sigma }_{z}=\frac{1}{2}{\sigma }_{z}\pm \frac{1}{2}\sqrt{4Y_{p}^{2}-3{\sigma }_{z}^{2}}$$	or	 $${\sigma }_{z}=Y_{p}={\sigma }_{\theta }$$

Create curve with following points, symmetrical about x=y
- Maximum tensile stress	$${\sigma }_{z}=1.1547{\ast Y}_{p}$$		&	$${\sigma }_{\theta }=0.5774{\ast Y}_{p}$$
- Maximum hoop stress	$${\sigma }_{\theta }=1.1547{\ast Y}_{p}$$		&	$${\sigma }_{z}=0.5774{\ast Y}_{p}$$
- σθ = σz = Yp
- σθ = 0, σz = Yp
- σz = 0, σθ = Yp
- Min extrema	 $${\sigma }_{z}=0.5774{\ast Y}_{p}$$, $${\sigma }_{\theta }=0.5774{\ast Y}_{p}$$

|Tensile    |Hoop	|Pressure	|Tension	|
|-----------|-------|-----------|-----------| 
|95	|0	0|	|1476916|	
|109.6965	|54.853	|6615	|1705395|	
|95	|95	|11456	|1476916|	
|54.853	|109.6965	|13228	|852771|	
|0	|95	|11456	|0|	
|-54.853	|54.853	|6615	|-852771|
|-95	|0	|0	|-1476916|	
|-109.6965	|-54.853	|-6615	|-1705395|	
|-95	|-95	|-11456	|-1476916|	
|-54.853	|-109.6965	|-13228	|-852771|	
|0	|-95	|-11456	|0|	
|54.853	|-54.853	|-6615	|852771|	
|95	|0	|0	|1476916|

![Von Mises Envelope](\images\vme_1.svg)
 
# Combined loading burst with radial stresses
Von Mises Envelope for Tubulars		
$Y_{p}=\sqrt{\frac{1}{2}\left[{\left({\sigma }_{z}-{\sigma }_{\theta }\right)}^{2}+{\left({\sigma }_{\theta }-{\sigma }_{r}\right)}^{2}+{\left({\sigma }_{r}-{\sigma }_{z}\right)}^{2}\right]+3{\tau }^{2}}$

Drop torque and expand			
$Y_{p}=\sqrt{{\sigma }_{z}^{2}+{\sigma }_{\theta }^{2}+{\sigma }_{r}^{2}-{\sigma }_{z}{\sigma }_{\theta }-{\sigma }_{\theta }{\sigma }_{r}-{\sigma }_{r}{\sigma }_{z}}$

Use Lame equation to relate hoop and radial stresses.

${\sigma }_{\theta }=-\left(\frac{R_{i}^{2}R_{o}^{2}\left(P_{o}-P_{i}\right)}{R_{o}^{2}-R_{i}^{2}}\right)\frac{1}{r^{2}}+\left(\frac{P_{i}R_{i}^{2}-P_{o}R_{o}^{2}}{R_{o}^{2}-R_{i}^{2}}\right)$,
${\sigma }_{r}=\left(\frac{R_{i}^{2}R_{o}^{2}\left(P_{o}-P_{i}\right)}{R_{o}^{2}-R_{i}^{2}}\right)\frac{1}{r^{2}}+\left(\frac{P_{i}R_{i}^{2}-P_{o}R_{o}^{2}}{R_{o}^{2}-R_{i}^{2}}\right)$	    

Assume Po = 0 for burst scenarios. r = radius within the cylinder, use Ri 

$\frac{{\sigma }_{\theta }}{\left(\frac{R_{o}^{2}}{r^{2}}+1\right)}=\left(\frac{P_{i}R_{i}^{2}}{R_{o}^{2}-R_{i}^{2}}\right)$, 
${\sigma }_{r}=\frac{P_{i}R_{i}^{2}\left(1-\frac{R_{o}^{2}}{r^{2}}\right)}{R_{o}^{2}-R_{i}^{2}}$,
substitute	${\sigma }_{r}=\frac{\left(1-\frac{R_{o}^{2}}{r^{2}}\right)}{\left(\frac{R_{o}^{2}}{r^{2}}+1\right)}{\sigma }_{\theta }$		or	${\sigma }_{r}=C{\sigma }_{\theta }$

Rewrite and substitute σr into VME	
$Y_{p}=\sqrt{{\sigma }_{z}^{2}+{\sigma }_{\theta }^{2}+{\sigma }_{r}^{2}-{\sigma }_{z}{\sigma }_{\theta }-{\sigma }_{\theta }{\sigma }_{r}-{\sigma }_{r}{\sigma }_{z}}$	

$Y_{p}=\sqrt{{\sigma }_{z}^{2}+{\sigma }_{\theta }^{2}+{C^{2}\sigma }_{\theta }^{2}-{\sigma }_{z}{\sigma }_{\theta }-{\sigma }_{\theta }C{\sigma }_{\theta }-C{\sigma }_{\theta }{\sigma }_{z}}$

Simplify to	 $Y_{p}=\sqrt{{\sigma }_{z}^{2}+{\left(C^{2}-C+1\right)\sigma }_{\theta }^{2}-\left(C+1\right){\sigma }_{\theta }{\sigma }_{z}}$	note extremes are not the same as 2D

Rewrite to solve for stresses	

${\sigma }_{z}=\frac{1}{2}{\left(C+1\right)\sigma }_{\theta }\pm \frac{1}{2}\sqrt{4Y_{p}^{2}-3{\left(C^{2}-2K+1\right)\sigma }_{\theta }^{2}}$		

${\sigma }_{\theta }=\frac{{\left(C+1\right)\sigma }_{z}\pm \sqrt{4{\left(C^{2}-C+1\right)Y}_{p}^{2}-3{\left(C^{2}-2C+1\right)\sigma }_{z}^{2}}}{2\left(C^{2}-C+1\right)}$

We could differentiate as above for extremes, but if term under radical is 0 then that indicates extrema for the variable under the radical. Basically if we have too high of a hoop stress, we get an imaginary number!

$4Y_{p}^{2}=3{\left(C^{2}-2C+1\right)\sigma }_{\theta }^{2}$			or	${\sigma }_{\theta }=\frac{1}{\sqrt{3\left(C^{2}-2C+1\right)}}2Y_{p}$		maximum hoop

Substitute back into tensile stress equation for associated tensile

${\sigma }_{z}=\frac{1}{2}\left(C+1\right)\frac{2Y_{p}}{\sqrt{3\left(C^{2}-2C+1\right)}}\pm \frac{1}{2}\sqrt{4Y_{p}^{2}-3\left(C^{2}-2C+1\right)\frac{4Y_{p}^{2}}{3\left(C^{2}-2C+1\right)}}=\frac{\left(C+1\right)Y_{p}}{\sqrt{3\left(C^{2}-2C+1\right)}}$			

Similarly for maximum tensile

$4{\left(C^{2}-C+1\right)Y}_{p}^{2}=3{\left(C^{2}-2C+1\right)\sigma }_{z}^{2}$	or	${\sigma }_{z}=\sqrt{\frac{\left(C^{2}-C+1\right)}{3\left(C^{2}-2C+1\right)}}2Y_{p}$	max tensile

${\sigma }_{\theta }=\frac{\left(C+1\right)\sqrt{\frac{\left(C^{2}-C+1\right)}{3\left(C^{2}-2C+1\right)}}2Y_{p}\pm \sqrt{4{\left(C^{2}-C+1\right)Y}_{p}^{2}-3\left(C^{2}-2C+1\right)\frac{\left(C^{2}-C+1\right)}{3\left(C^{2}-2C+1\right)}4Y_{p}^{2}}}{2\left(C^{2}-C+1\right)}=\frac{\left(C+1\right)}{\left(C^{2}-C+1\right)}\sqrt{\frac{\left(C^{2}-C+1\right)}{3\left(C^{2}-2C+1\right)}}Y_{p}$	

For case of σθ = σz 	${\sigma }_{z}=\frac{1}{2}{\left(C+1\right)\sigma }_{z}\pm \frac{1}{2}\sqrt{4Y_{p}^{2}-3{\left(C^{2}-2C+1\right)\sigma }_{z}^{2}}$		or	${\sigma }_{z}=\sqrt{\frac{1}{\left(C^{2}-2C+1\right)}}Y_{p}$

For case of σz or σθ = 0	$Y_{p}=\sqrt{{\left(C^{2}-C+1\right)\sigma }_{\theta }^{2}}$	or	${\sigma }_{z}={\sigma }_{\theta }=\sqrt{\frac{1}{\left(C^{2}-C+1\right)}}Y_{p}$

Summarize equations
- Max hoop and associated tension		${\sigma }_{\theta -max}=\frac{1}{\sqrt{3\left(C^{2}-2C+1\right)}}2Y_{p}$		${\sigma }_{z}=\frac{\left(C+1\right)Y_{p}}{\sqrt{3\left(C^{2}-2C+1\right)}}$
- Max tension and associated hoop		${\sigma }_{z-max}=\sqrt{\frac{\left(C^{2}-C+1\right)}{3\left(C^{2}-2C+1\right)}}2Y_{p}$		${\sigma }_{\theta }=\frac{\left(C+1\right)}{\left(C^{2}-C+1\right)}$\sqrt{\frac{\left(C^{2}-C+1\right)}{3\left(C^{2}-2C+1\right)}}Y_{p}$	
- σθ = σz		${\sigma }_{z}=\sqrt{\frac{1}{\left(C^{2}-2C+1\right)}}Y_{p}$
- σz = 0		${\sigma }_{z}=\sqrt{\frac{1}{\left(C^{2}-C+1\right)}}Y_{p}$
- Torque (not plotted for ellipse)	$\tau =\frac{2\bullet Torque\bullet r}{\pi (R_{o}^{4}-R_{i}^{4})}$	use r = Ro 
- Uniaxial Burst (Barlow’s)		${Burst}_{uniaxial}=Y_{p}\ast \frac{(OD-ID)}{OD}$
- Temperature Derating		$Y_{p,\ \ adj\ Temp}=Y_{p}\left(1-0.0003\left(Temperature-75\right)\right)$


Solution method & notes
- Define range of σθ	\pm \frac{2Y_{p}}{\sqrt{3\left(C^{2}-2C+1\right)}} 		This ranges from maximum hoop to minimum
- Solve for σz	{\sigma }_{z}=\frac{1}{2}{\left(C+1\right)\sigma }_{\theta }\pm \frac{1}{2}\sqrt{4Y_{p}^{2}-3{\left(C^{2}-2C+1\right)\sigma }_{\theta }^{2}}	Solve for both sides of ellipse
- Convert to tension and pressure
- Tension={\sigma }_{z}\ast Area/{DF}_{tension}
- Pressure={Burst}_{uniaxial}\ast \frac{{\sigma }_{\theta }}{{\sigma }_{\theta -max}}/{DF}_{burst}	Use Barlow’s burst for uniaxial burst
- To neglect radial loads, set Ro = Ri when calculating C
- Other considerations to be made for eccentricity & corrosion (affecting Ri), anisotropy & temperature (affecting yield point), bending moments (usually included in the tensile terms), shear (additional term in VME as hoop shear – more critical for drilling than completions)
= Note that high burst loads may cause buckling and subsequent bending moments in the tubular!

Comparing VME with and without radial stresses, superimposed on API limits. Note change in shape of ellipse by considering the radial stresses.

![Envelope with radial stresses](\images\vme_2.svg)

 
# Collapse – API Derivation
API 5C3 is the industry-standard treatment of pipe collapse under multiple types of loading. Four regimes were identified and curve fit against. First corrections for temperature and tension need to be applied, then the constants are calculated. Using the constants the collapse regime can be find, whether Yield, Plastic, Transition, or Elastic, driven by the D/t ratio of the pipe. Once the adjust yield stress, constants, and regime is found, the collapse pressure may be calculated. Collapse calculated this way has an inherent safety factor due to how the curve-fits were made and the long, field-proven history of the calculations, so having a high design factor is not necessary as compared to burst.

![API Collapse](\images\vme_3.svg)

Corrections – use for transitional points, constants, and solutions
- Temperature Correction		$Y_{p,\ \ Tadj}=Y_{p}(1-0.0003\ x\ \left(temperature-75\right))$
- Combined Loading Correction	$Y_{p,\ \ adj}=\left(\sqrt{1-0.75{\left(\frac{{\sigma }_{a}}{Y_{p}}\right)}^{2}}-0.5\frac{{\sigma }_{a}}{Y_{p}}\right)Y_{p}$

Constants
- $A=2.8762+0.10679{\times 10}^{-5}\times Y_{p}+0.21301{\times 10}^{-10}\times Y_{p}^{2}-0.53132{\times 10}^{-16}\times Y_{p}^{3}$
- $B=0.02623+0.50609{\times 10}^{-6}\times Y_{p}$
- $C=-465.93+0.030867\times Y_{p}-0.10483{\times 10}^{-7}\times Y_{p}^{2}+0.36989{\times 10}^{-13}\times Y_{p}^{3}$
- $F=\frac{46.95{\times 10}^{6}{\left(\frac{\frac{3B}{A}}{2+\frac{B}{A}}\right)}^{3}}{Y_{p}\left(\frac{\frac{3B}{A}}{2+\frac{B}{A}}-\frac{B}{A}\right){\left(1-\frac{\frac{3B}{A}}{2+\frac{B}{A}}\right)}^{2}}$
- $G=\frac{FB}{A}$

Transitional Points	
- Yield to Plastic 			${\left(\frac{D}{t}\right)}_{Y\ to\ P}=\frac{\sqrt{{\left(A-2\right)}^{2}+8\left(B+\frac{C}{Y_{p}}\right)}+\left(A-2\right)}{2\left(B+\frac{C}{Y_{p}}\right)}$
- Plastic to Transition			${\left(\frac{D}{t}\right)}_{P\ to\ T}=\frac{Y_{p}\left(A-F\right)}{C+Y_{p}\left(B-G\right)}$
- Transition to Elastic			${\left(\frac{D}{t}\right)}_{T\ to\ E}=\frac{2+\frac{B}{A}}{\frac{3B}{A}}$

Solutions
- Yield, analytic solution		$P_{Y}=2Y_{p}\frac{\frac{D}{t}-1}{{\left(\frac{D}{t}\right)}^{2}}$
- Plastic, empirical solution		$P_{P}=Y_{p}\left(\frac{A}{\frac{D}{t}}-B\right)-C$
- Transition, empirical solution	$P_{T}=Y_{p}\left(\frac{F}{\frac{D}{t}}-G\right)$
- Elastic, analytic solution		$P_{E}=\frac{2E}{1-v^{2}}x\frac{1}{\left(\frac{D}{t}\right){\left(\frac{D}{t}-1\right)}^{2}}$

# Connections
While API threads have calculated data, proprietary connections rely on the provider’s testing and calculations. It is always recommended to have test data of the connections performed, and understand how extrapolations and interpolations may be conducted to link test data to actual pipe materials and body selected. API RP 5C5 / ISO 13679 is the resource for planning connection testing.
