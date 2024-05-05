def create_recommendations_flowchart(further_recommendations):
    if further_recommendations.lower() == 'yes':
        print("Avoid aerobic bacterial culture and antimicrobial susceptibility testing on nasal secretions for acute bacterial URI.")
        print("Consider tests for FCV, FHV-1, or C. felis.")
        print("If chronic URTD develops, conduct a more extensive workup for an underlying cause.")
    elif further_recommendations.lower() == 'no':
        print("No further recommendations needed.")
    else:
        print("Invalid input for further recommendations.")

def ask_for_further_recommendations():
    further_recommendations = input("Do you want further recommendations? (yes/no): ")
    if further_recommendations.lower() == 'yes':
        print("Follow further recommendations.")
        create_recommendations_flowchart(further_recommendations)
    elif further_recommendations.lower() == 'no':
        print("End.")
    else:
        print("Invalid input.")

def diagnose_urt(cat_signs):
    if cat_signs.lower() == 'yes':
        vaccinated = input("Has the cat been vaccinated against respiratory diseases? (yes/no): ")
        if vaccinated.lower() == 'yes':
            thorough_exam = input("Perform a thorough ocular, oral, and otic examination? (yes/no): ")
            if thorough_exam.lower() == 'yes':
                lower_respiratory = input("Is there evidence of concurrent lower respiratory disease based on thoracic auscultation? (yes/no): ")
                if lower_respiratory.lower() == 'yes':
                    retrovirus_testing = input("Evaluate for the presence of feline leukemia virus antigen and feline immunodeficiency virus antibodies? (yes/no): ")
                    if retrovirus_testing.lower() == 'yes':
                        nasal_discharge = input("Are nasal discharges serous, lacking mucopurulent or purulent components? (yes/no): ")
                        if nasal_discharge.lower() == 'yes':
                            print("Antimicrobial treatment is not recommended. End.")
                        elif nasal_discharge.lower() == 'no':
                            period_of_observation = input("If purulent or mucopurulent discharge is present without clear evidence of the cause, a period of observation without immediate antimicrobial use.\n Did clinical signs persist or worsen after the observation period? (yes/no): ")
                            if period_of_observation.lower() == 'yes':
                                print("Consider antimicrobial treatment.")
                                antimicrobial_choice = input("Consider using Doxycycline or Amoxicillin (PO). Proceed with antimicrobial treatment Doses? (yes/no): ")
                                if antimicrobial_choice.lower() == 'yes':
                                    print("Use Doxycycline @ 5 mg/kg, PO, q12h or Amoxicillin @ 22 mg/kg, PO, q12h.")
                                elif antimicrobial_choice.lower() == 'no':
                                    print("No antimicrobial treatment is recommended.")
                                    ask_for_further_recommendations()
                                else:
                                    print("Invalid input.")
                            elif period_of_observation.lower() == 'no':
                                print("No antimicrobial treatment is recommended.")
                                ask_for_further_recommendations()
                            else:
                                print("Invalid input.")
                        else:
                            print("Invalid input.")
                    elif retrovirus_testing.lower() == 'no':
                        print("End.")
                    else:
                        print("Invalid input.")
                elif lower_respiratory.lower() == 'no':
                    print("End.")
                else:
                    print("Invalid input.")
            elif thorough_exam.lower() == 'no':
                print("End.")
            else:
                print("Invalid input.")
        elif vaccinated.lower() == 'no':
            print("End.")
        else:
            print("Invalid input.")
    elif cat_signs.lower() == 'no':
        print("No treatment needed.")
        ask_for_further_recommendations()
    else:
        print("Invalid input.")

# Example usage:
cat_signs_input = input("Is the cat exhibiting signs of Upper Respiratory Tract Disease (URTD) with a duration of ≤10 days? (yes/no): ")
diagnose_urt(cat_signs_input)
