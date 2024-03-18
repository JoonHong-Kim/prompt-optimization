GenerationPrompt = """
I gave a friend an instruction.
Based on the instruction they produced the following input-output pairs:

{train_data}

The instruction was to:
"""

ResamplePrompt = """
Generate a variation of the following instruction while keeping the semantic meaning.

Input: {instruction}

Output: {output}
"""
