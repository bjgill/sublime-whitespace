import sublime
import sublime_plugin


class InsertWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # Separate out regions to cope with multiple selections.
        for region in self.view.sel():

            # Update selection to include whole lines.
            region = self.view.line(region)

            # Extract individial lines.
            lines = self.view.substr(region).split("\n")
            new_lines = []

            for line in lines:
                new_line = line

                if len(line) < 79:

                    # If a line is shorter than 79 characters, append spaces.
                    new_line += " " * (79 - len(line))

                new_lines.append(new_line)

            # Replace old selection with new version with extra spaces.
            self.view.replace(edit, region, "\n".join(new_lines))
