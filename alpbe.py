import math

def alpha_beta(node, depth, alpha, beta, maximizing):
    # Terminal node: return its value
    if not isinstance(node, list):
        return node

    if maximizing:
        best = -math.inf

        for i, child in enumerate(node):
            val = alpha_beta(child, depth + 1,
                             alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)

            # Prune remaining branches
            if alpha >= beta:
                print("Pruning remaining branch at depth", depth)
                break

        return best

    else:
        best = math.inf

        for i, child in enumerate(node):
            val = alpha_beta(child, depth + 1,
                             alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)

            # Prune remaining branches
            if alpha >= beta:
                print("Pruning remaining branch at depth", depth)
                break

        return best


# Game tree from the given diagram
tree = [
    [ # N2: Minimizer
        [1, 4], # N4: Maximizer
        [7, 2] # N5: Maximizer
    ],
    [ # N3: Minimizer
        [3, 0], # N6: Maximizer
        [6, 5] # N7: Maximizer
    ]
]

result = alpha_beta(
    tree,
    0,
    -math.inf,
    math.inf,
    True
)

print("Optimal value at root N1:", result)


