from lnn import And, Implies, Or,  Equivalent, Fact, Proposition, Model

# Knowledge
A = Proposition("A")
B = Proposition("B")
C = Proposition("C")
D = Proposition("D")
E = Proposition("E")
A_implies_B = Implies(A, B)
C_and_D = And(C, D)
C_and_D_equivalent_E = Equivalent(C_and_D, E)
root = And(A_implies_B, C_and_D_equivalent_E)

BDE_disjunction = Or(B, D, E)

# Data
root.add_data(Fact.TRUE)
C.add_data(Fact.TRUE)
E.add_data((0.3, 0.7))
A.add_data((0.2, 0.0))


model = Model()
model.add_knowledge(root)

# root.print()

# Reasoning
model.infer()
# root.downward()
print("A implies B")
A_implies_B.downward()
B.print()


print("C and D")
C_and_D.downward()
D.print()

BDE_disjunction.upward()

query = BDE_disjunction

def format_result(node):
    round_off = lambda my_list: [float(f"{_:.1f}") for _ in my_list]
    return f"{node.state().name}: {tuple(round_off(node.get_data().tolist()))}"


print(format_result(query))
