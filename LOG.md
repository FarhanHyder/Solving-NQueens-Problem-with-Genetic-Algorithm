##### 07/28/2019
Well, the current problem is - it works only if i am lucky enough.
I think the reason might be that I am only selecting the best (fitness) ones, 
so there is no diversity after a few epochs. 
<br>
Solution? Well let's try a new `selection method`.
- selected chromosomes will be a% according to the fitness score, b% selected randomly
    - why? hope, doing so will help to prevent diversity

<br>    
Other suggestions? Yeah. The current code design is very messy and confusing.
Better if I start this whole using a different DS. 
