# doc_automation  
The program uses the given template to generate a new file using the following input -  
- Replacement officer name  
- Start time  
- Finish Time  
- Patrol times  
  
# Time generation  
Patrol time generation "p_time" is a dictionalry with keys -  "day_1" and "day_2". So far I've covered -  
- If 0000 found, all value goes to day 2  
- If 23 found then is_23 var becomes True  
- When is_23 is True and the next val is not 23, e.g 00, 01 etc is_0 becomes True  
- When both is_23 and is_0 is True, we go to "day_2"
