"""
Problem Definitions for Cognitive Bias Study
=============================================
Stimuli replicated from:
  - Li & Feldman (2025): Mental Accounting (Problems 1-3)
  - Zhu & Feldman (2025): Psychology of Waste (Problem 18, Tent Project)

Original paradigms by Tversky & Kahneman (1981, 1986), Thaler (1980), Arkes (1996).
"""

SYSTEM_PROMPT = (
    "You are a participant in a decision-making study. "
    "Read the scenario carefully and respond with only the letter "
    "of your chosen option: A or B. "
    "Do not provide any explanation, reasoning, or additional text."
)

PROBLEMS = {

    "problem_1_risk_attitudes": {
        "source": "Li & Feldman (2025), originally Tversky & Kahneman (1986)",
        "conditions": {
            "condition_1_gain": (
                "Assume yourself richer by $300 than you are today. "
                "You are offered a choice between:\n\n"
                "A) A sure gain of $100\n"
                "B) A 50% chance to gain $200 and a 50% chance to gain $0\n\n"
                "Which do you choose?"
            ),
            "condition_2_loss": (
                "Assume yourself richer by $500 than you are today. "
                "You are offered a choice between:\n\n"
                "A) A sure loss of $100\n"
                "B) A 50% chance to lose $200 and a 50% chance to lose $0\n\n"
                "Which do you choose?"
            ),
        },
    },

    "problem_2_calculator_jacket": {
        "source": "Li & Feldman (2025), originally Tversky & Kahneman (1981)",
        "conditions": {
            "condition_1_cheap_calculator": (
                "Imagine that you are about to purchase a jacket for $125, "
                "and a calculator for $15. The calculator salesman informs you "
                "that the calculator you wish to buy is on sale for $10 at the "
                "other branch of the store, located 20 minutes drive away. "
                "Would you make the trip to the other store?\n\n"
                "A) Yes\n"
                "B) No"
            ),
            "condition_2_expensive_calculator": (
                "Imagine that you are about to purchase a jacket for $15, "
                "and a calculator for $125. The calculator salesman informs you "
                "that the calculator you wish to buy is on sale for $120 at the "
                "other branch of the store, located 20 minutes drive away. "
                "Would you make the trip to the other store?\n\n"
                "A) Yes\n"
                "B) No"
            ),
        },
    },

    "problem_3_theater_ticket": {
        "source": "Li & Feldman (2025), originally Tversky & Kahneman (1981)",
        "conditions": {
            "condition_1_lost_bill": (
                "Imagine that you have decided to see a play where admission "
                "is $10 per ticket. As you enter the theater you discover that "
                "you have lost a $10 bill.\n\n"
                "Would you still pay $10 for a ticket for the play?\n\n"
                "A) Yes\n"
                "B) No"
            ),
            "condition_2_lost_ticket": (
                "Imagine that you have decided to see a play and paid the "
                "admission price of $10 per ticket. As you enter the theater "
                "you discover that you have lost the ticket. The seat was not "
                "marked and the ticket cannot be recovered.\n\n"
                "Would you pay $10 for another ticket?\n\n"
                "A) Yes\n"
                "B) No"
            ),
        },
    },

    "problem_18_basketball_sunk_cost": {
        "source": "Zhu & Feldman (2025), originally Thaler (1980)",
        "conditions": {
            "condition_1_paid_ticket": (
                "Imagine that there is a basketball game to be played 60 miles "
                "from your home. Your family gave you a ticket. On the day of "
                "the game there is a snowstorm.\n\n"
                "Given the snowstorm, what would you choose to do if your "
                "family paid $40 for your ticket?\n\n"
                "A) Go to the game anyway\n"
                "B) Stay home"
            ),
            "condition_2_free_ticket": (
                "Imagine that there is a basketball game to be played 60 miles "
                "from your home. Your family gave you a ticket. On the day of "
                "the game there is a snowstorm.\n\n"
                "Given the snowstorm, what would you choose to do if the "
                "ticket was given to your family for free?\n\n"
                "A) Go to the game anyway\n"
                "B) Stay home"
            ),
        },
    },

    "tent_project_wastefulness": {
        "source": "Zhu & Feldman (2025), originally Arkes (1996)",
        "conditions": {
            "no_waste": (
                "As the owner of your own company, you have used $80,000 of your "
                "company's research funds to develop a type of plastic cloth which "
                "would be used to manufacture camping tents. This material is very "
                "light, so backpackers would find it easy to carry from one campsite "
                "to another. Furthermore it is completely waterproof, so it could "
                "keep campers dry, no matter how hard it was raining. The best part "
                "is that the cloth cannot be punctured. It is so durable that campers "
                "could use it without fear of accidentally damaging the tent.\n\n"
                "When the project is 90% completed, another firm begins marketing a "
                "waterproof tent that is made of material that is more durable than "
                "the material you have developed. It is also apparent that their tent "
                "is much cheaper than the tent you are building, and furthermore, it "
                "is much lighter. The question is: should you invest the last 10% of "
                "your research funds to finish your tent, or should you just abandon "
                "the project?\n\n"
                "If you abandon the project, a roofer said that he'd buy all the "
                "cloth you've developed so far for $10,000. He wants to sew all the "
                "tent-sized pieces together into one big tarp. He said this would "
                "come in handy as a waterproof tarp to place over roofs after he's "
                "taken old shingles off. If it rains before he gets the new shingles "
                "on, the exposed wood on the roof would be protected by the big tarp. "
                "Unfortunately you can't manufacture the cloth in this large size, "
                "and nobody wants a tarp of tent-sized pieces sewn together. The "
                "roofer can really use the cloth you've manufactured so far, however.\n\n"
                "Which option do you prefer?\n\n"
                "A) Invest the last 10% of your research funds to finish your tent "
                "(you have invested $80,000)\n"
                "B) Abandon the project and sell the tent material to the roofer "
                "for $10,000"
            ),
            "waste": (
                "As the owner of your own company, you have used $80,000 of your "
                "company's research funds to develop a type of plastic cloth which "
                "would be used to manufacture camping tents. This material is very "
                "light, so backpackers would find it easy to carry from one campsite "
                "to another. Furthermore it is completely waterproof, so it could "
                "keep campers dry, no matter how hard it was raining. The best part "
                "is that the cloth cannot be punctured. It is so durable that campers "
                "could use it without fear of accidentally damaging the tent.\n\n"
                "When the project is 90% completed, another firm begins marketing a "
                "waterproof tent that is made of material that is more durable than "
                "the material you have developed. It is also apparent that their tent "
                "is much cheaper than the tent you are building, and furthermore, it "
                "is much lighter. The question is: should you invest the last 10% of "
                "your research funds to finish your tent, or should you just abandon "
                "the project?\n\n"
                "If you abandon the project, you could sell all the cloth you've "
                "developed for its scrap value, which is $10,000.\n\n"
                "Which option do you prefer?\n\n"
                "A) Invest the last 10% of your research funds to finish your tent "
                "(you have invested $80,000)\n"
                "B) Abandon the project and sell for its scrap value of $10,000"
            ),
        },
    },
}
