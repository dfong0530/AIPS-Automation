import random

def generate_draft(Employee_Name, Company_Name, Site_Location):
    
    #Modify possible_subjects and possible_drafts when switching versions

    possible_subjects = ["Quick Question", f"Exploring POS Optimization Opportunities for {Company_Name}", "HERE TO HELP"]
    
    possible_drafts = [f"Hello {Employee_Name},\n\nHope you are doing well. My name is David. I’m a college student majoring in computer science and business, and I’m currently working on a school project, where I need to create software to optimize a task. I found {Company_Name} on {Site_Location}, and was wondering if I could schedule a 15 minute zoom meeting with you to discuss your POS System,inventory management process, and any bottlenecks.\n\nI understand that your time is precious, and I'm flexible with scheduling to accommodate your availability.\n\nDavid", 
                        
                       f"Dear {Employee_Name},\n\nI hope this message finds you well.\n\nMy name is David, and I'm on the initial stages of a software startup focused on enhancing POS systems for small businesses. Our goal is to streamline operations, improve inventory management, and resolve common bottlenecks. Would you be available for a brief, 15-minute Zoom call? During this meeting, I'd love to learn more about your current POS and inventory management systems, identify any challenges you're facing, and explore possible solutions to those challenges. \n\nI understand the value of your time and would be happy to accommodate your schedule for this conversation.\n\nThank you for considering this opportunity. I look forward to the possibility of working together and providing value for {Company_Name} \n\nDavid",


                       f"{Employee_Name}, \n\nIn an era where every second and dollar counts, inefficient POS systems can become a silent drain on resources. They often require more time and money to maintain than expected, impacting both operational efficiency fiscal resources. \n\nI'm David, a co-founder of a startup (AIPS) focused on automating POS systems for small businesses like {Company_Name}. Our software could significantly streamline your POS and inventory management, resolving inefficiencies you might not have been aware about. \n\nWould you be open to a brief, 15-minute Zoom call to discuss this? I'm eager to learn about your specific needs and explore how we can add value. \n\nI understand your time is valuable, and I'm flexible in scheduling this discussion at your convenience. \n\nThank you for considering this opportunity, and I look forward to helping your company optimize your POS system. \n\nBest Regards,\nDavid"
                       ]

    r = random.randint(0, 2)
    email = [r, possible_subjects[r], possible_drafts[r]]

    return email



#    #Company_Name,Employee_Name,Employee_Email_Address,Phone_Number,Did_Email,Did_Call,Site_Location,Email_Version,Respond_Positive
def updateRow(row, version, emailChoice):

    row[4] = "Yes"
    row[7] = version + "." +  str(emailChoice)

