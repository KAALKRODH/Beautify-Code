class CodeBeautifier:
    def __init__(self):
        self.indentation_size = 4

    def beautify(self, code):
        # Split code into lines
        lines = code.split("\n")

        # Remove leading and trailing whitespace from each line
        lines = [line.strip() for line in lines]

        # Remove empty lines
        lines = [line for line in lines if line]

        # Initialize indentation level and other variables
        indentation_level = 0
        beautified_code = ""
        changes = []

        # Build the beautified code
        for line_number, line in enumerate(lines, start=1):
            original_line = line
            original_indentation = self.get_indentation(indentation_level)

            if line.endswith("{"):
                # Increase indentation level for lines ending with "{"
                indentation_level += 1
                line = original_indentation + line
                changes.append(
                    f"Added indentation at line {line_number}: {original_line} -> {line}")
            elif line.endswith("}"):
                # Decrease indentation level for lines ending with "}"
                indentation_level -= 1
                line = original_indentation + line
                changes.append(
                    f"Added indentation at line {line_number}: {original_line} -> {line}")
            else:
                # Maintain the current indentation level for other lines
                if not line.startswith(self.get_indentation(indentation_level)):
                    line = original_indentation + line
                    changes.append(
                        f"Added indentation at line {line_number}: {original_line} -> {line}")

            beautified_code += line + "\n"

        return beautified_code, changes

    def get_indentation(self, indentation_level):
        return " " * (self.indentation_size * indentation_level)


# Example usage
beautifier = CodeBeautifier()

# Paste your code below to beautify it
code = """
public class HelloWorld {
    public static void main(String[] args) {
    int x = 5;
    if (x > 0) {
    System.out.println("Positive");
    } else if (x < 0) {
    System.out.println("Negative");
    } else {
    System.out.println("Zero");
    }
    }
}
"""

beautified_code, changes = beautifier.beautify(code)
print("Beautified Code:")
print(beautified_code)
print("\nChanges:")
for change in changes:
    print(change)
