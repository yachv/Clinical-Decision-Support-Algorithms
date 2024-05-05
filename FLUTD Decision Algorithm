import graphviz

def decision_making():
    print("Welcome to the FLUTD Decision-Making Algorithm")

    # Ask questions
    answers = {}
    questions = [
        "Has the cat been diagnosed with FIC following thorough diagnostic work-up ruling out other causes? (Y/N)",
        "Is the cat overweight? (Y/N)",
        "Is the cat male? (Y/N)",
        "Is the cat in a multi-cat household? (Y/N)",
        "Is the cat predominantly indoors? (Y/N)",
        "Does the cat exhibit behavioral abnormalities such as increased startle responses or excessive attachment to owners? (Y/N)",
        "Is the cat's litter box management optimal according to AAFP and ISFM guidelines? (Y/N)",
        "Has the cat been prescribed analgesics for pain management? (Y/N)",
        "Has the cat been prescribed alpha antagonists for obstructive FIC? (Y/N)",
        "Has the cat been provided with environmental modifications as part of MEMo therapy? (Y/N)",
        "Has the cat been prescribed a canned diet for FIC management? (Y/N)",
        "Has the cat been prescribed antibiotics for UTI based on positive urine culture? (Y/N)",
        "Are TCAs or SSRIs being considered for the cat's treatment? (Y/N)",
        "Is amitriptyline being considered for long-term treatment in severe, recurrent cases? (Y/N)",
        "Is fluoxetine being considered for managing house-soiling? (Y/N)"
    ]

    recommendations = {  # Define recommendations based on questions
        "Has the cat been diagnosed with FIC following thorough diagnostic work-up ruling out other causes? (Y/N)":
            "Implement management strategies for FIC as outlined in the guidelines.",
        "Is the cat overweight? (Y/N)":
            "Consider weight management strategies as part of overall FIC management.",
        "Is the cat male? (Y/N)":
            "Consider alpha antagonists for management, especially if obstructive FIC is present.",
        "Is the cat in a multi-cat household? (Y/N)":
            "Ensure multiple environmental resources are available to reduce competition and stress.",
        "Is the cat predominantly indoors? (Y/N)":
            "Focus on environmental enrichment to alleviate stress associated with indoor confinement.",
        "Does the cat exhibit behavioral abnormalities such as increased startle responses or excessive attachment to owners? (Y/N)":
            "Address behavioral abnormalities as part of a holistic FIC management approach.",
        "Is the cat's litter box management optimal according to AAFP and ISFM guidelines? (Y/N)":
            "Continue optimal litter box management practices.",
        "Has the cat been prescribed analgesics for pain management? (Y/N)":
            "Follow prescribed analgesic regimen for pain management in FIC.",
        "Has the cat been prescribed alpha antagonists for obstructive FIC? (Y/N)":
            "Consider prescribing alpha antagonists for obstructive FIC if present.",
        "Has the cat been provided with environmental modifications as part of MEMo therapy? (Y/N)":
            "Continue MEMo therapy to decrease clinical signs and improve disease-free intervals.",
        "Has the cat been prescribed a canned diet for FIC management? (Y/N)":
            "Continue with canned diet which may be helpful for some cats with FIC.",
        "Has the cat been prescribed antibiotics for UTI based on positive urine culture? (Y/N)":
            "Avoid prescribing antibiotics unless a positive urine culture is obtained, especially in cats with previous urinary catheterizations.",
        "Are TCAs or SSRIs being considered for the cat's treatment? (Y/N)":
            "Consider TCAs or SSRIs for severe, recurrent cases of FIC where other therapies have failed.",
        "Is amitriptyline being considered for long-term treatment in severe, recurrent cases? (Y/N)":
            "Consider amitriptyline for long-term treatment in severe, recurrent cases of FIC.",
        "Is fluoxetine being considered for managing house-soiling? (Y/N)":
            "Consider fluoxetine for managing house-soiling behavior in the cat."
    }

    for question in questions:
        answer = input(question + " ").upper()
        while answer not in ('Y', 'N'):
            print("Please enter 'Y' or 'N'")
            answer = input(question + " ").upper()
        answers[question] = answer

    # Provide recommendations
    selected_recommendations = {}  # Recommendations selected by the user
    for question, answer in answers.items():
        if answer == 'Y':
            selected_recommendations[question] = recommendations[question]

    print("\nRecommended Actions:")
    for recommendation in selected_recommendations.values():
        print(recommendation)

    # Generate Graphviz code
    dot = generate_graphviz_code(selected_recommendations)
    
    # Render and display the flowchart
    render_flowchart(dot)


def generate_graphviz_code(recommendations):
    dot = graphviz.Digraph()

    categories = {
        "treatment": "Treatment Recommendations\nfor FIC",
        "management": "Managemental Recommendations\nfor FIC"
    }

    for question, recommendation in recommendations.items():
        category = "treatment" if "treatment" in question.lower() else "management"
        # Split recommendation into multiple lines with a maximum width of 30 characters
        recommendation_lines = []
        current_line = ''
        for word in recommendation.split():
            if len(current_line) + len(word) + 1 <= 30:  # Check if adding the word exceeds the maximum width
                if current_line:  # If the current line is not empty, add a space before adding the word
                    current_line += ' '
                current_line += word
            else:
                recommendation_lines.append(current_line)
                current_line = word
        if current_line:  # Add the remaining words to the last line
            recommendation_lines.append(current_line)
        recommendation = '\\n'.join(recommendation_lines)
        if "Avoid prescribing antibiotics" in recommendation:
            dot.node(recommendation, recommendation, shape='rectangle', style='filled', fillcolor='red', fontcolor='white')
        else:
            dot.node(recommendation, recommendation, shape='rectangle')
        dot.edge(categories[category], recommendation)

    dot.node(categories["treatment"], categories["treatment"], shape='rectangle', style='filled', fillcolor='yellow')
    dot.node(categories["management"], categories["management"], shape='rectangle', style='filled', fillcolor='yellow')

    return dot


def render_flowchart(dot):
    # Set layout to 'dot' for vertical arrangement
    dot.attr(layout='dot')
    dot.render('flowchart', format='png', cleanup=True)
    dot.view()


# Run the decision-making algorithm
decision_making()
