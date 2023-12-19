# Doc_automation  
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

# Flags  
- --master or -m : uses the collect_data_master() function that uses predefined officer name and license no, takes a single line argument seperated by "," 

# Screenshot  
<img src="https://github.com/Adnan525/doc_automation/blob/main/doc_automation.PNG" alt="master function screenshot">  
  
<img src="https://github.com/Adnan525/doc_automation/blob/main/collect_data.JPG" alt="collect_data">  
  
<img src="https://github.com/Adnan525/doc_automation/blob/main/collect_data_master.JPG" alt="collect_data_master">  
