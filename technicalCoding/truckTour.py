""" 
Suppose there is a circle. There are petrol pumps on that circle. Petrol pumps are numbered to
 (both inclusive). You have two pieces of information corresponding to each of the petrol pump: (1)
the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the
next petrol pump.
Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol
pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the
truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.
"""


def truckTour(petrolpumps):
    # Write your code here
    start = 0
    end = 1
    
    petrol = petrolpumps[start][0] - petrolpumps[start][1]
    
    while end != start or petrol < 0:
        while petrol < 0 and start != end:
            petrol -= petrolpumps[start][0] - petrolpumps[start][1]
            start = (start + 1) % n
            if start == 0:
                return -1
        petrol += petrolpumps[end][0] - petrolpumps[end][1]
        end = (end + 1) % n
    return start