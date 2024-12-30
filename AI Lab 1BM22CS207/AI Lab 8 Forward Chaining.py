class ForwardReasoning:
    def __init__(self, rules, facts):
        """
        Initializes the ForwardReasoning system.
        Parameters:
        rules (list): List of rules as tuples (condition, result),
                      where 'condition' is a set of facts.
        facts (set): Set of initial known facts.
        """
        self.rules = rules  # List of rules (condition -> result)
        self.facts = set(facts)  # Known facts

    def infer(self, query):
        """
        Applies forward reasoning to infer new facts based on rules and initial facts.
        Parameters:
        query (str): The fact to verify if it can be inferred.
        Returns:
        bool: True if the query can be inferred, False otherwise.
        """
        while True:
            new_facts = set()
            for condition, result in self.rules:
                # If the rule's condition is satisfied and the result is not in known facts
                if condition.issubset(self.facts) and result not in self.facts:
                    new_facts.add(result)
                    print(f"Applied rule: {condition} -> {result}")
            # If no new facts are inferred, break the loop
            if not new_facts:
                break
            # Add new facts to the known facts
            self.facts.update(new_facts)
        # Check if the query is in the facts
        return query in self.facts


# Define the Knowledge Base (KB) with rules as (condition, result)
rules = [
    ({"American(Robert)"}, "Sells(Robert, m1, CountryA)"),  # Rule 1
    (
        {"Sells(Robert, m1, CountryA)", "American(Robert)", "Hostile(CountryA)"},
        "Criminal(Robert)",
    ),  # Rule 2
]

# Define initial facts
facts = {
    "American(Robert)",
    "Hostile(CountryA)",
    "Missile(m1)",
    "Owns(CountryA, m1)",
}

# Query
alpha = "Criminal(Robert)"

# Initialize and run forward reasoning
reasoner = ForwardReasoning(rules, facts)
result = reasoner.infer(alpha)

# Display results
print("\nFinal facts:")
print(reasoner.facts)
print(f"\nQuery '{alpha}' inferred: {result}")
