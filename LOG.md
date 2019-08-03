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


##### 08/02/2019
update: the NQueens.py is separated and tested to be working properly.
<br>
new changes?: Re-engineering the whole DS. 
The program should be divided into following classes.
- NQueens
- Chromosome 
    - need to check and store selection(maybe not) and mutation rate
- Epoch (more like the current Chromosome_Collection class)
- Main
    - this is where the magic happens
    - insures the whole genetic algorithm process
    - maybe name it Nucleus?
 
<br>
Testing: Like whatever I did before for testing, was so childish.
Need to step my game up in testing. 

##### 08/03/2019
update: NQueens has 100% test coverage. Wohooo!
new selection method under study: Roulette Wheel Selection