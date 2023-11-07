# ===== LIST ===== #

# [0] * 4 creates a list with four zeros: [0, 0, 0, 0].
# Wrapping that in another list and multiplying by four, [[0, 0, 0, 0]] * 4,
# creates a list containing four references to that same list.
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print([[0] * 4] * 4)
