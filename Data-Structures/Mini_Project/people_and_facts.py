people_and_facts = {
	"Jeff": "Is afraid of dogs.",
	"David": "Plays the piano.",
	"Jason": "Can fly an airplane.",
}


def display_facts(facts):
	for person, fact in facts.items():
		print(f"{person}: {fact}")


display_facts(people_and_facts)
print()

people_and_facts["Jeff"] = "Is afraid of heights."
people_and_facts["Jill"] = "Can hula dance."

display_facts(people_and_facts)