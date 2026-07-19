# ---------------- NEXT-UP (CAREER-PATHWAY) ----------------

career_data = {
    "Pre-Medical": {
        "fsc_careers": ["Doctor", "Dentist", "Pharmacist", "Biomedical Researcher"],
        "bachelor_programs": ["MBBS", "BDS", "Pharm-D", "BS Biotechnology"],
        "ms_programs": ["MS Biotechnology", "MS Public Health (MPH)", "M.Phil Anatomy"],
        "pak_unis": ["King Edward Medical University", "Aga Khan University", "NUMS"],
        "global_unis": ["Harvard Medical School", "Oxford University", "Johns Hopkins University"],
        "scholarships": ["Chevening Scholarship", "Fulbright Program", "HEC Overseas Scholarships"]
    },
    "Pre-Engineering": {
        "fsc_careers": ["Mechanical Engineer", "Civil Engineer", "Electrical Engineer", "Aerospace Engineer"],
        "bachelor_programs": ["BE Mechanical", "BE Civil", "BE Electrical"],
        "ms_programs": ["MS Engineering Management", "MS Aerospace Engineering", "M.Phil Physics"],
        "pak_unis": ["NUST", "UET Lahore", "GIKI"],
        "global_unis": ["MIT", "Stanford University", "ETH Zurich"],
        "scholarships": ["Commonwealth Scholarship", "Erasmus Mundus", "DAAD Germany"]
    },
    "Commerce": {
        "fsc_careers": ["Chartered Accountant", "Financial Analyst", "Investment Banker"],
        "bachelor_programs": ["BBA", "BS Accounting & Finance", "BS FinTech"],
        "ms_programs": ["MS Finance", "MBA", "MS Risk Management & FinTech"],
        "pak_unis": ["IBA Karachi", "LUMS", "NUST"],
        "global_unis": ["LSE", "INSEAD", "Wharton"],
        "scholarships": ["Fulbright Program", "Chevening Scholarship", "Great Scholarships UK"]
    },
    "Arts": {
        "fsc_careers": ["Graphic Designer", "Psychologist", "Journalist", "Professor"],
        "bachelor_programs": ["BS Psychology", "Bachelor of Fine Arts", "BS English"],
        "ms_programs": ["MS Clinical Psychology", "MS Media Studies", "M.Phil Applied Linguistics"],
        "pak_unis": ["NCA", "LUMS", "Beaconhouse National University"],
        "global_unis": ["UCLA", "University of Melbourne", "Oxford University"],
        "scholarships": ["Chevening Scholarship", "Fulbright Program", "Charles Wallace Trust"]
    },
    "ICS": {
        "fsc_careers": ["Software Engineer", "Data Scientist", "AI Engineer", "Cybersecurity Expert"],
        "bachelor_programs": ["BS Computer Science", "BS Software Engineering", "BS Artificial Intelligence"],
        "ms_programs": ["MS Computer Science", "MS Data Science", "MS Cyber Security"],
        "pak_unis": ["FAST-NUCES", "NUST", "ITU Lahore"],
        "global_unis": ["MIT", "Stanford University", "Carnegie Mellon", "Waterloo"],
        "scholarships": ["Erasmus Mundus", "MEXT Japan", "Fulbright Program"]
    }
}

def get_valid_rating(text):
    """Safeguards rating choices between 1 and 5 to prevent empty inputs or values out of bounds."""
    while True:
        user_input = input(text).strip()
        if not user_input:
            print("Input cannot be empty. Please enter a number between 1 and 5.")
            continue
        try:
            value = int(user_input)
            if 1 <= value <= 5:
                return value
            print("Invalid rating scale! Choose an integer strictly between 1 and 5.")
        except ValueError:
            print("Invalid format! Please type a valid mathematical integer digit.")

def personality_quiz():
    print("\n======================================")
    print("      CAREER INTEREST ASSESSMENT")
    print("======================================")
    print("Rate yourself from 1 to 5")
    print("1 = Strongly Dislike | 3 = Neutral | 5 = Strongly Like\n")

    questions = {
        "Pre-Medical": [
            "I enjoy helping sick people: ",
            "I like Biology and Human Body: ",
            "I want to work in hospitals or healthcare: "
        ],
        "Pre-Engineering": [
            "I enjoy Mathematics and Physics: ",
            "I like machines and technology: ",
            "I enjoy solving technical problems: "
        ],
        "Commerce": [
            "I like business and money management: ",
            "I enjoy accounting and finance: ",
            "I want to become an entrepreneur: "
        ],
        "Arts": [
            "I enjoy creativity and designing: ",
            "I like writing, languages or psychology: ",
            "I enjoy public speaking or teaching: "
        ],
        "ICS": [
            "I enjoy coding/programming: ",
            "I like Artificial Intelligence and computers: ",
            "I enjoy solving logical problems: "
        ]
    }

    scores = {}
    for field, q_list in questions.items():
        scores[field] = sum(get_valid_rating(q) for q in q_list)

    best = max(scores, key=scores.get)
    print("\n======================================")
    print("YOUR INTEREST MATCH BASED ON QUIZ:", best)
    print("======================================")
    return best

def show_path(user_name, current_level, field, score_metric, actual_background):
    print(f"\n====================================")
    print(f"CAREER ROADMAP FOR {user_name.upper()}")
    print(f"====================================")

    bg_display = "Matric Science" if actual_background == "1" else ("Matric Arts" if actual_background == "2" else actual_background)
    
    print(f"Your Academic Background: {bg_display}")
    print(f"Your Evaluated Quiz Interest: {field}")
    print("------------------------------------")

    is_mismatch = False
    if current_level == "1":
        if actual_background == "2" and field in ["Pre-Medical", "Pre-Engineering", "ICS"]:
            is_mismatch = True
            print("ACADEMIC ALERT: You selected Matric Arts, but your quiz results indicate a high interest in Science/Tech.")
            print("Note: In Pakistan, switching directly into core Pre-Medical/Pre-Engineering FSc tracks from Matric Arts is generally restricted.")
            print("Suggestion: You can still opt for specialized Arts, Humanities, or certain Commerce combinations.\n")
    
    elif current_level == "2":
        if actual_background in ["Pre-Engineering", "ICS"] and field == "Pre-Medical":
            is_mismatch = True
            print("ACADEMIC ALERT: Your FSc background lacks Biology, but your quiz shows Pre-Medical interest.")
            print("Note: You cannot apply for core medical degrees like MBBS/BDS without passing FSc Pre-Medical or Additional Biology.")
            print("Cross-Disciplinary Route: Look into Bioinformatics, Biomedical Engineering, or Health Informatics!\n")
        elif actual_background == "Pre-Medical" and field in ["Pre-Engineering", "ICS"]:
            print("CROSS-DISCIPLINARY NOTE: Moving from Pre-Medical to Computing/Engineering fields is highly popular!")
            print("Note: Ensure you check university criteria for basic Mathematics entry test requirements.\n")

    if not is_mismatch:
        print("Your background aligns well with your discovered career interest fields.")

    if current_level == "1":
        print("\n[RECOMMENDED CAREERS]")
        for career in career_data[field]["fsc_careers"][:3]:
            print("-", career)

        print("\n[RECOMMENDED BACHELOR PROGRAMS]")
        for prog in career_data[field]["bachelor_programs"]:
            print("-", prog)
    else:
        print("\n[RECOMMENDED MS / M.PHIL PROGRAMS]")
        for program in career_data[field]["ms_programs"]:
            print("-", program)

    print("\n====================================")
    print("PAKISTAN UNIVERSITIES")
    print("====================================")
    for uni in career_data[field]["pak_unis"]:
        print("-", uni, "( Pakistan )")

    print("\n====================================")
    print("GLOBAL UNIVERSITIES & SCHOLARSHIPS")
    print("====================================")

    countries = {
        "Harvard Medical School": "USA", "Oxford University": "UK", "Johns Hopkins University": "USA",
        "MIT": "USA", "Stanford University": "USA", "ETH Zurich": "Switzerland",
        "University of Toronto": "Canada", "LSE": "UK", "INSEAD": "France",
        "Wharton": "USA", "UCLA": "USA", "University of Melbourne": "Australia",
        "Carnegie Mellon": "USA", "Waterloo": "Canada"
    }

    is_eligible = (current_level == "1" and score_metric >= 60) or (current_level == "2" and score_metric >= 3.0)

    if is_eligible:
        print("Eligible Global Universities:")
        for target_uni in career_data[field]["global_unis"]:
            print(f"- {target_uni} ({countries.get(target_uni, 'Unknown')})")
        
        print("\nAvailable Scholarships:")
        for scholarship in set(career_data[field]["scholarships"]):
            print("-", scholarship)
    else:
        print("Not Currently Eligible for Top Tier International Placement.")
        if current_level == "1":
            print("Reason: FSc Percentage is below 60%. Look to improve metrics or clear entries.")
        else:
            print("Reason: CGPA is below 3.0. HEC minimum requirement for MS programs often leans higher.")

def start_assessment_system():
    print("==================================================")
    print("     WELCOME TO THE NEXT-UP CAREER PATHWAY SYSTEM")
    print("==================================================")
    
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        print("Name cannot be left blank!")

    while True:
        age = input("Enter your age: ").strip()
        if age:
            break
        print("Age cannot be left blank!")
    
    print(f"\nHello {name} ({age} years old)!")
    
    while True:
        print("Select your current educational status:")
        print("1 - FSc / Intermediate Student (Looking for Bachelor Programs)")
        print("2 - Bachelor Student (Looking for Master's/MS Programs)")
        level_choice = input("Enter option (1 or 2): ").strip()
        if level_choice in ["1", "2"]:
            break
        print("Invalid entry selection. Please input 1 or 2.\n")

    if level_choice == "1":
        while True:
            print("\nSelect your Matric Specialization Field:")
            print("1 - Matric Science (With Biology or Computer Science)")
            print("2 - Matric Arts / Humanities")
            matric_bg = input("Enter option (1 or 2): ").strip()
            if matric_bg in ["1", "2"]:
                break
            print("Invalid entry selection. Please input 1 or 2.")

        print("\n========== FSc Academic Profile ==========")
        while True:
            marks_input = input("Enter your current/expected FSc marks (out of 1100): ").strip()
            if not marks_input:
                print("Marks field cannot be empty.")
                continue
            try:
                marks = int(marks_input)
                if 0 <= marks <= 1100:
                    break
                print("Total FSc marks must realistically scale between 0 and 1100.")
            except ValueError:
                print("Invalid format! Please input numeric integer digits only.")

        percentage = (marks / 1100) * 100
        print(f"Calculated Percentage: {round(percentage, 2)}%")
        
        field = personality_quiz()
        show_path(name, level_choice, field, percentage, matric_bg)

    elif level_choice == "2":
        while True:
            print("\nSelect your Intermediate (FSc/ICS/I.Com) Academic Field:")
            print("1 - Pre-Medical")
            print("2 - Pre-Engineering")
            print("3 - ICS (Computer Science)")
            print("4 - Commerce (I.Com) / Arts")
            fsc_selection = input("Enter option (1-4): ").strip()
            
            bg_map = {"1": "Pre-Medical", "2": "Pre-Engineering", "3": "ICS", "4": "Commerce"}
            if fsc_selection in bg_map:
                fsc_bg = bg_map[fsc_selection]
                break
            print("Invalid field selection. Choose an option from 1 to 4.")

        print("\n========== Bachelor Academic Profile ==========")
        while True:
            cgpa_input = input("Enter your current CGPA (0.00 - 4.00): ").strip()
            if not cgpa_input:
                print("CGPA cannot be empty.")
                continue
            try:
                cgpa = float(cgpa_input)
                if 0.0 <= cgpa <= 4.0:
                    break
                print("Your CGPA must belong between the 0.0 to 4.0 scale boundaries.")
            except ValueError:
                print("Invalid format! Please input a fractional/decimal value (e.g., 3.4).")
        
        field = personality_quiz()
        show_path(name, level_choice, field, cgpa, fsc_bg)

if __name__ == "__main__":
    start_assessment_system()