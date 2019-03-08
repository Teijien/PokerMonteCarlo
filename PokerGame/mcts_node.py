class MCTSNode:

    def __init__(self, parent=None, parent_action=None, action_list=[]):
        self.parent = parent
        self.parent_action = parent_action

        self.child_nodes = {}
        self.untried_actions = action_list

        self.wins = 0
        self.visits = 0

    def __repr__(self):
        return ' '.join(["[", str(self.parent_action),
                         "Win rate:", "{0:.0f}%".format(100 * self.wins / self.visits),
                         "Visits:", str(self.visits),  "]"])

    def tree_to_string(self, horizon=1, indent=0):
        string = ''.join(['| ' for i in range(indent)]) + str(self) + '\n'
        if horizon > 0:
            for child in self.child_nodes.values():
                string += child.tree_to_string(horizon - 1, indent + 1)
        return string